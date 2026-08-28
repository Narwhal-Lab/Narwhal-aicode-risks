
function parseJqError(jqXHR) {
    if (jqXHR && jqXHR.responseJSON) return jqXHR.responseJSON;
    if (jqXHR && jqXHR.responseText) {
        try { return JSON.parse(jqXHR.responseText); } catch (e) {}
    }
    return null;
}

function getCaptchaSiteKey(result) {
    return result &&
    result.assessment &&
    result.assessment.captchaDetails &&
    result.assessment.captchaDetails.siteKey
        ? result.assessment.captchaDetails.siteKey
        : '';
}

function getCaptchaRequestId(result) {
    return result &&
    result.assessment &&
    result.assessment.requestId
        ? result.assessment.requestId
        : '';
}

function isCaptchaRequired(result) {
    return !!getCaptchaSiteKey(result);
}

function isCaptchaError(result) {
    if (!result) return false;

    if (result.code && String(result.code).toLowerCase().includes('captcha')) return true;
    if (result.error && String(result.error).toLowerCase().includes('captcha')) return true;

    if (Array.isArray(result.errors)) {
        return result.errors.some(function (e) {
            if (typeof e === 'string') return e.toLowerCase().includes('captcha');
            if (e && typeof e === 'object') {
                return (String(e.field || '').toLowerCase().includes('captcha') ||
                    String(e.code || '').toLowerCase().includes('captcha') ||
                    String(e.message || '').toLowerCase().includes('captcha'));
            }
            return false;
        });
    }

    if (result.message && String(result.message).toLowerCase().includes('captcha')) return true;

    return false;
}

function showCaptchaError(form, text) {
    form.find('.captcha-error-message').remove();
    var msg = jQuery('<div class="captcha-error-message" style="color:red; margin-top:10px;"></div>');
    msg.text(text || (window.jbFormsCfg && jbFormsCfg.captchaErrorMessage) || 'Captcha verification failed.');
    form.find('.form-subscribe__group-input').after(msg);
}

function showEmailError(form, emailInput, text) {
    form.find('.email-error-message').remove();
    emailInput.css('border-color', 'red');

    var msg = jQuery('<div class="email-error-message" style="color: red; margin-top: -15px;"></div>');
    msg.text(text || (window.loadmore_params && loadmore_params.email_error_message) || 'Invalid email');
    form.find('.form-subscribe__group-input').after(msg);

    setTimeout(function () {
        emailInput.attr('style', '');
        msg.fadeOut(300, function () { jQuery(this).remove(); });
    }, 2000);
}

var jbRecaptchaLoadedKey = null;
var jbRecaptchaLoadingPromise = null;

function loadRecaptchaScript(siteKey, locale) {
    if (!siteKey) return Promise.reject(new Error('Missing reCAPTCHA site key'));

    if (window.grecaptcha && window.grecaptcha.execute && jbRecaptchaLoadedKey === siteKey) {
        return Promise.resolve();
    }

    if (jbRecaptchaLoadingPromise) return jbRecaptchaLoadingPromise;

    jbRecaptchaLoadingPromise = new Promise(function (resolve, reject) {
        var existing = document.getElementById('jb-recaptcha-v3');
        if (existing) existing.remove();

        var script = document.createElement('script');
        script.id = 'jb-recaptcha-v3';
        script.async = true;
        script.defer = true;

        script.src = 'https://www.google.com/recaptcha/api.js?render=' + encodeURIComponent(siteKey) +
            (locale ? '&hl=' + encodeURIComponent(locale) : '');

        script.onload = function () {
            jbRecaptchaLoadedKey = siteKey;
            jbRecaptchaLoadingPromise = null;

            if (window.grecaptcha && window.grecaptcha.ready) {
                window.grecaptcha.ready(function () { resolve(); });
            } else {
                reject(new Error('grecaptcha not available after script load'));
            }
        };

        script.onerror = function () {
            jbRecaptchaLoadingPromise = null;
            reject(new Error('reCAPTCHA script load error'));
        };

        document.head.appendChild(script);
    });

    return jbRecaptchaLoadingPromise;
}

function getRecaptchaToken(siteKey) {
    if (!window.grecaptcha || !window.grecaptcha.execute) {
        return Promise.reject(new Error('grecaptcha not available'));
    }
    return window.grecaptcha.execute(siteKey, { action: 'submit' });
}

function getAssessmentUrl(marketoUrl) {
    try {
        var u = new URL(marketoUrl);
        return u.origin + '/assessment';
    } catch (e) {
        return marketoUrl.replace(/\/marketo\/?$/, '') + '/assessment';
    }
}

function sendAssessment(marketoUrl, requestId, token) {
    return jQuery.ajax({
        url: getAssessmentUrl(marketoUrl),
        type: 'POST',
        contentType: 'application/json',
        data: JSON.stringify({
            requestId: requestId,
            assessmentResponse: {
                token: token,
                type: 'reCaptcha v3'
            }
        })
    });
}
