var captchaRes = '';
var sibErrMsg;
var gCaptchaSibWidget;
var ajax_sib_front_object;
var sibVerifyCallback = function (response) {
    captchaRes = response;
    var formIdInvisible = sessionStorage.getItem("formIdRecapcha");
    if (captchaRes) {
        var validationErr = 0;
        jQuery.each(jQuery(formIdInvisible).find('input[required=required]'), function () {
            if (jQuery(this).val().trim() == '' || (jQuery(this).attr('type') == "checkbox" && jQuery(this).prop("checked") == false)) {
                validationErr++;
                var form = jQuery(this).closest('form');
                var requiredField = jQuery(this).closest('form').find('input[name="sib_form_alert_notice"]').val();
                if (requiredField !== undefined) {
                    sibErrMsg.requiredField = requiredField;
                }
                form.find('.sib_msg_disp').html('<p class="sib-alert-message sib-alert-message-warning ">' + sibErrMsg.requiredField + '</p>').show();
                return;
            }
        });
    }
    if (validationErr == 0) {
        jQuery(formIdInvisible).trigger('submit');
    }
};

jQuery(document).ready(function(){
    jQuery('.sib_signup_form').find('input[required=required]').on("invalid", function () {
        if(jQuery(this).val().trim() == '')
        {
            var alert_msg = jQuery(this).closest('form').find('input[name="sib_form_alert_notice"]').val();
            this.setCustomValidity(alert_msg);
        }
        else {
            this.setCustomValidity('');
        }
    });
    // run MA script identify() when submit on any forms with email field
    jQuery(document).on('submit', 'form', function(e){
        var invalidEmail = jQuery(this).closest('form').find('input[name="sib_form_invalid_email_notice"]').val();
        var requiredField = jQuery(this).closest('form').find('input[name="sib_form_alert_notice"]').val();
        if (invalidEmail !== undefined) {
            sibErrMsg.invalidMail = invalidEmail;
        }
        if (requiredField !== undefined) {
            sibErrMsg.requiredField = requiredField;
        }

        if(!jQuery(this).hasClass('sib_signup_form')) {
            var email = jQuery(this).find('input[type=email]').val();
            var emailPattern = /^([a-zA-Z0-9_.+-])+\@(([a-zA-Z0-9-])+\.)+([a-zA-Z0-9]{2,4})+$/;
            if (typeof sendinblue != 'undefined' && email != null && emailPattern.test(email)) {
                var postData = jQuery('input[type!=password]',this).serializeObject();
                sendinblue.identify(email, postData);
            }
        }
        else
        {
            e.preventDefault();
            var form = jQuery(this).closest('form');
            // for sms field
            jQuery.each(form.find('.sib-sms'), function () {
                var sms = jQuery(this).val();
                var sms_prefix = jQuery(this).closest('.sib-sms-field').find('input[name="sib_SMS_prefix"]').val();
                if ( sms == sms_prefix && !jQuery(this).prop('required')) {
                    jQuery(this).val('');
                }
            });

            /**
             * For safari
             * Not support required attribute
             */

            var required_fileds = [];
            var err_index = 0;

            var multi_lists = form.find(jQuery('.sib-multi-lists'));
            if( multi_lists != undefined && multi_lists.data('require') == 'required' )
            {
                if ( multi_lists.find('input:checked').length == 0 )
                {
                    err_index++;
                    multi_lists.addClass('sib_error');
                }
            }
            if(err_index > 0)
            {
                form.find('.sib_msg_disp').html('<p class="sib-alert-message sib-alert-message-warning ">' + sibErrMsg.requiredField + '</p>').show();
                return;
            }
            err_index=0;
            jQuery.each(form.find('input[type="email"]'), function(){
                var Email = /^([a-zA-Z0-9_.+-])+@(([a-zA-Z0-9-])+\.)+([a-zA-Z0-9]{2,4})+$/i;
                if (!Email.test(jQuery(this).val()))
                {
                    err_index++;
                }
            });
            if(err_index > 0)
            {
                form.find('.sib_msg_disp').html('<p class="sib-alert-message sib-alert-message-warning ">' + sibErrMsg.invalidMail + '</p>').show();
                return;
            }

            // Check sms validation
            err_index = 0;
            jQuery.each(form.find('.sib-sms'), function () {
                var sms = jQuery(this).val();
                if ( is_valid_sms(sms) == false && sms != '' ) {
                    err_index ++;
                }
            });
            if(err_index > 0)
            {
                form.find('.sib_msg_disp').html('<p class="sib-alert-message sib-alert-message-warning ">' + sibErrMsg.invalidSMSFormat + '</p>').show();
                return;
            }

            jQuery(".sib-default-btn").attr("disabled", true);
            form.find('.sib_loader').show();
            jQuery('.sib_msg_disp').hide();
            var postData = form.serializeArray();
            if( captchaRes != '' )
            {
                postData.push({"name": "g-recaptcha-response", "value": captchaRes});
            }
            captchaRes = '';
            if( jQuery('.sib-multi-lists').length )
            {
                var interesting_lists = [];
                jQuery('.sib-interesting-lists').each(function () {
                    postData.push({"name":"interestingLists[]", "value": jQuery(this).val()})
                });
            }
            var formURL = form.attr("action");
            form.addClass('sib_processing');

            postData.push({ "name": "security", "value": ajax_sib_front_object.ajax_nonce });
            jQuery.ajax({
                url: formURL,
                type: "POST",
                dataType: "json",
                data: postData,
                success: function (data, textStatus, jqXHR) {
                    jQuery(".sib-default-btn").attr("disabled", false);
                    jQuery('.sib_loader').hide();
                    if( jQuery('.sib-multi-lists').length )
                    {
                        jQuery('.sib-multi-lists').removeClass('sib_error');
                    }
                    if (data.status === 'success' || data.status === 'update') {
                        var cdata = '<p class="sib-alert-message sib-alert-message-success ">' + data.msg.successMsg + '</p>';
                        form.find('.sib_msg_disp').html(cdata).show();
                    } else if (data.status === 'failure') {
                        var cdata = '<p class="sib-alert-message sib-alert-message-error ">' + data.msg.errorMsg + '</p>';
                        form.find('.sib_msg_disp').html(cdata).show();
                    } else if (data.status === 'already_exist') {
                        var cdata = '<p class="sib-alert-message sib-alert-message-warning ">' + data.msg.existMsg + '</p>';
                        form.find('.sib_msg_disp').html(cdata).show();
                    } else if (data.status === 'invalid') {
                        var cdata = '<p class="sib-alert-message sib-alert-message-error ">' + data.msg.invalidMsg + '</p>';
                        form.find('.sib_msg_disp').html(cdata).show();
                    } else if (data.status === 'gcaptchaEmpty') {
                        var cdata = '<p class="sib-alert-message sib-alert-message-error ">' + data.msg + '</p>';
                        form.find('.sib_msg_disp').html(cdata).show();
                    } else if (data.status === 'gcaptchaFail') {
                        var cdata = '<p class="sib-alert-message sib-alert-message-error ">' + data.msg + '</p>';
                        form.find('.sib_msg_disp').html(cdata).show();
                    }
                    form[0].reset();
                    if (data.redirect && (data.status === 'success' || data.status === 'update')) {
                        window.location.href = data.redirect;
                    }

                    //Render the cloudflare captcha again
                    if (typeof data.turnstileCaptcha !== 'undefined' && data.turnstileCaptcha) {
                        jQuery.each(form.find('.cf-turnstile'), function () {
                            var siteKey = jQuery(this).data("sitekey");
                            var cfResponse = jQuery('input[name="cf-turnstile-response"]').val();
                            if (cfResponse) {
                                var idToBeRendered = "#cf-turnstile-"+siteKey;
                                turnstile.render(idToBeRendered, {
                                    sitekey: siteKey,
                                    callback: function(token) {
                                        console.log("Challenge Success");
                                    },
                                });
                            }
                        });
                    }
                    var previous_code = form.find('.sib-cflags').data('dial-code');
                    if ( previous_code )
                    {
                        form.find('.sib-sms').val('+' + previous_code);
                        form.find('input[name="sib_SMS_prefix"]').val('+' + previous_code);
                    }

                    // run MA script identify() when subscribe on SIB forms
                    if (typeof sendinblue != 'undefined') {
                        var email = form.find('input[name=email]').val();
                        var postData = form.serializeObject();
                        if (data.status === 'success' || data.status === 'update' || data.status === 'already_exist') {
                            sendinblue.identify(email, postData);
                        }
                    }
                    jQuery(".sib-alert-message").delay(5000).hide('slow');
                    form.removeClass('sib_processing');
                    if (typeof grecaptcha != 'undefined')
                    {
                        grecaptcha.reset(gCaptchaSibWidget);
                    }
                },
                error: function (jqXHR, textStatus, errorThrown) {
                    form.find('.sib_msg_disp').html(jqXHR).show();
                    jQuery(".sib-default-btn").attr("disabled", false);
                    if (typeof grecaptcha != 'undefined')
                    {
                        grecaptcha.reset(gCaptchaSibWidget);
                    }
                }
            });
        }
    });
    jQuery('.sib-country-block').on('click', function () {
       jQuery('.sib-country-list').toggle();
    });
    if (jQuery('.sib-country-list').length > 0)
    {
        jQuery('.sib-country-list').ready( function () {
            var data = {
                action : 'sib_get_country_prefix',
                security: ajax_sib_front_object.ajax_nonce,
            };
            jQuery.post( ajax_sib_front_object.ajax_url, data, function (respond) {
                jQuery('.sib-country-list').html(respond);
            });
        });
    }

    jQuery('body').on('click', function(e){
        if ( jQuery('.sib-sms-field .sib-country-list').length > 0 && !jQuery('.sib-sms-field .sib-country-list').is(e.target) && jQuery('.sib-sms-field .sib-country-list').has(e.target).length === 0 && jQuery('.sib-sms-field .sib-country-block').has(e.target).length === 0 ) {
            jQuery('.sib-sms-field .sib-country-list').hide();
        }
    });

    jQuery('.sib-country-list').on( 'click', 'li' , function () {
        var country_code = jQuery(this).data('country-code').toLowerCase();
        var dial_code = jQuery(this).data('dial-code');
        jQuery(this).closest('.sib-sms-field').find('.sib-sms').val('+' + dial_code );
        jQuery(this).closest('.sib-sms-field').find('input[name="sib_SMS_prefix"]').val('+' + dial_code );
        jQuery(this).closest('.sib-sms-field').find('.sib-cflags').css('background-image', 'url(' + ajax_sib_front_object.flag_url + country_code + '.png)');
        jQuery(this).closest('.sib-sms-field').find('.sib-cflags').data('dial-code', dial_code);
        jQuery(this).closest('.sib-country-list').hide();
    });
    jQuery(".sib-sms").on('keypress', function (event){
        validateInteger(event, 'sms');
    });

    // allow to input 0-9 and - only for date field
    jQuery(".sib-date").on('keypress', function(event) {
        validateInteger(event, 'date');
    });
    function is_valid_sms( sms ) {
        sms = sms.replace(/\b(0(?!\b))+/g, "");

        var tempSms = sms.replace(/( |\(|\)|\.|\-)/g, '');

        if (tempSms.length > 19  || tempSms.length < 6 || tempSms.charAt(0) != '+'){
            return false;
        }
        return true;
    }
    function validateInteger(evt,type) {
        var theEvent = evt || window.event;
        var key = theEvent.charCode || theEvent.which;

        key = String.fromCharCode( key );
        // 0-9, +/-, space, brackets
        var regex = /[ +0-9()-]/;
        var smsLength = 0;
        if( type == 'date' ) {
            regex = /[ 0-9-/]/;
        }
        if( !regex.test(key)) {
            theEvent.returnValue = false;
            key = theEvent.keyCode;
            // ignore input for del,tab, back, left, right, home amd end
            if(theEvent.preventDefault && key != 9 && key != 8 ) theEvent.preventDefault();
        }
    }


});
// get serialized data form subscribe form
jQuery.fn.serializeObject = function()
{
    var o = {};
    var a = this.serializeArray();
    jQuery.each(a, function() {
        if(this.name == 'sib_form_action' || this.name == 'sib_form_id' || this.name == 'email')
            return true; // continue
        if (o[this.name] !== undefined) {
            if (!o[this.name].push) {
                o[this.name] = [o[this.name]];
            }
            o[this.name].push(this.value || '');
        } else {
            o[this.name] = this.value || '';
        }
    });
    return o;
};
// get form id
jQuery(document).ready(function () {
    jQuery(".sib-default-btn").on("click", function () {
        var row = jQuery(this).closest(".sib_signup_form");
        sessionStorage.setItem("formIdRecapcha", "#" + jQuery(row).attr('id'));
    })
})

function errorCallbackForTurnstileErrors(){
}
