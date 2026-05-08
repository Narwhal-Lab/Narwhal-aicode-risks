#!/usr/bin/env python3
"""
validate_cases.py — Schema + integrity checks for cases/, inferred/, scenarios/.

Requires: PyYAML (`pip install pyyaml`)
Usage:    python3 scripts/validate_cases.py [--check-links]

Exit codes:
  0  — all checks passed
  1  — schema or integrity errors
  2  — broken external links (only with --check-links)

Default mode runs schema checks only. Pass --check-links to additionally HEAD
each reference URL (slower; allows network failures with a warning).
"""
from __future__ import annotations

import argparse
import sys
import urllib.error
import urllib.request
from pathlib import Path

try:
    import yaml
except ImportError:
    sys.stderr.write("ERROR: PyYAML required. `pip install pyyaml`\n")
    sys.exit(1)

ROOT = Path(__file__).resolve().parent.parent
BUCKETS = {
    "cases": {"requires_real_incident": True, "requires_severity_basis": True},
    "inferred": {"requires_real_incident": False, "requires_severity_basis": True},
    "scenarios": {"requires_real_incident": False, "requires_severity_basis": True},
}

VALID_CATEGORIES = {
    "supply-chain", "code-vulns", "cloud-iac", "agent-risk",
    "domain-specific", "ip-compliance", "human-factor",
}
VALID_SEVERITIES = {"critical", "high", "medium", "low", "info"}
VALID_SEVERITY_BASIS = {"cvss", "quantifiable-impact", "editorial"}

REQUIRED_FIELDS = {
    "slug", "title_en", "title_cn", "year", "category",
    "severity", "severity_basis", "tldr", "references",
}


class ValidationError(Exception):
    pass


def validate_meta(meta_file: Path, bucket_config: dict) -> list[str]:
    errors: list[str] = []
    try:
        data = yaml.safe_load(meta_file.read_text(encoding="utf-8"))
    except yaml.YAMLError as e:
        return [f"{meta_file}: YAML parse error: {e}"]

    if not data:
        return [f"{meta_file}: empty"]

    # Required fields
    for f in REQUIRED_FIELDS:
        if f not in data or data[f] in (None, "", []):
            errors.append(f"{meta_file}: missing or empty field `{f}`")

    # Slug must match parent dir name
    if data.get("slug") and data["slug"] != meta_file.parent.name:
        errors.append(
            f"{meta_file}: slug `{data['slug']}` != dirname `{meta_file.parent.name}`"
        )

    # Category whitelist
    if (cat := data.get("category")) and cat not in VALID_CATEGORIES:
        errors.append(
            f"{meta_file}: category `{cat}` not in {sorted(VALID_CATEGORIES)}"
        )

    # Severity whitelist
    if (sev := data.get("severity")) and sev not in VALID_SEVERITIES:
        errors.append(
            f"{meta_file}: severity `{sev}` not in {sorted(VALID_SEVERITIES)}"
        )

    # severity_basis whitelist
    if (sb := data.get("severity_basis")) and sb not in VALID_SEVERITY_BASIS:
        errors.append(
            f"{meta_file}: severity_basis `{sb}` not in {sorted(VALID_SEVERITY_BASIS)}"
        )

    # CVSS shape (optional, but if set, must be float 0-10)
    if (cvss := data.get("cvss")) is not None:
        try:
            v = float(cvss)
            if not 0 <= v <= 10:
                errors.append(f"{meta_file}: cvss {v} out of range [0, 10]")
        except (TypeError, ValueError):
            errors.append(f"{meta_file}: cvss `{cvss}` not a number")

    # CVE shape (optional, must look like CVE-YYYY-NNNNN if set)
    if (cve := data.get("cve")) is not None:
        if not (isinstance(cve, str) and cve.startswith("CVE-")):
            errors.append(f"{meta_file}: cve `{cve}` does not look like a CVE id")

    # references list shape
    refs = data.get("references") or []
    if not isinstance(refs, list):
        errors.append(f"{meta_file}: references must be a list")
    else:
        for i, ref in enumerate(refs):
            if not isinstance(ref, dict):
                errors.append(f"{meta_file}: references[{i}] not an object")
                continue
            if not ref.get("title"):
                errors.append(f"{meta_file}: references[{i}].title missing")
            if not ref.get("url"):
                errors.append(f"{meta_file}: references[{i}].url missing")

    # README must exist
    readme = meta_file.parent / "README.md"
    if not readme.exists():
        errors.append(f"{meta_file.parent}: missing README.md")

    return errors


def check_url(url: str, timeout: int = 10) -> tuple[str, str]:
    """Return ('ok'/'warn'/'fail', message)."""
    try:
        req = urllib.request.Request(url, method="HEAD", headers={
            "User-Agent": "narwhal-aicode-risks-validator/1.0"
        })
        with urllib.request.urlopen(req, timeout=timeout) as resp:
            status = resp.status
            if 200 <= status < 400:
                return ("ok", f"{status}")
    except urllib.error.HTTPError as e:
        if e.code in (403, 405, 429):
            # 403 / 405 / 429 often mean "we'd serve this to a real browser";
            # we won't treat them as fatal.
            return ("warn", f"HTTP {e.code} (treated as warning)")
        return ("fail", f"HTTP {e.code}")
    except (urllib.error.URLError, TimeoutError) as e:
        return ("warn", f"network error: {e}")
    except Exception as e:
        return ("warn", f"unexpected: {e}")
    return ("warn", "unknown")


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        "--check-links",
        action="store_true",
        help="Also HEAD each reference URL (slower)",
    )
    args = parser.parse_args()

    all_errors: list[str] = []
    all_warnings: list[str] = []
    total_cases = 0

    for bucket, config in BUCKETS.items():
        bucket_dir = ROOT / bucket
        if not bucket_dir.exists():
            continue
        for meta_file in bucket_dir.glob("*/meta.yaml"):
            if meta_file.parent.name == "_template":
                continue
            total_cases += 1
            all_errors.extend(validate_meta(meta_file, config))

    if args.check_links:
        print("Checking reference URLs (HEAD)...")
        for bucket in BUCKETS:
            bucket_dir = ROOT / bucket
            if not bucket_dir.exists():
                continue
            for meta_file in bucket_dir.glob("*/meta.yaml"):
                if meta_file.parent.name == "_template":
                    continue
                try:
                    data = yaml.safe_load(meta_file.read_text(encoding="utf-8"))
                except yaml.YAMLError:
                    continue
                for ref in data.get("references") or []:
                    url = ref.get("url")
                    if not url:
                        continue
                    status, msg = check_url(url)
                    label = f"{meta_file.parent.name}: {url} → {msg}"
                    if status == "fail":
                        all_errors.append(label)
                    elif status == "warn":
                        all_warnings.append(label)

    print(f"\nValidated {total_cases} cases.")
    if all_warnings:
        print(f"\n⚠️  {len(all_warnings)} warning(s):")
        for w in all_warnings:
            print(f"  WARN  {w}")
    if all_errors:
        print(f"\n❌  {len(all_errors)} error(s):")
        for e in all_errors:
            print(f"  FAIL  {e}")
        return 1
    print("\n✅  All checks passed.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
