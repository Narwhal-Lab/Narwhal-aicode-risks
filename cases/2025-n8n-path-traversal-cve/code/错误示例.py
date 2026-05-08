#Vulnerable Code Location:
#The insecure path concatenation occurs in the download_workflow function within api_server.py, specifically at:

#file_path = os.path.join("workflows", filename)

import os
def download_workflow(filename: str) -> str:
    file_path = os.path.join("workflows", filename)  # ❌ 未校验
    return open(file_path, "r", encoding="utf-8").read()