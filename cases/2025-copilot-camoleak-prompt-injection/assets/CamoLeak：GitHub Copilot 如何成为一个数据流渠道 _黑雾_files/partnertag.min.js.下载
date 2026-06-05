(() => {

function $parcel$defineInteropFlag(a) {
  Object.defineProperty(a, '__esModule', {value: true, configurable: true});
}

function $parcel$export(e, n, v, s) {
  Object.defineProperty(e, n, {get: v, set: s, enumerable: true, configurable: true});
}

      var $parcel$global = globalThis;
    
var $parcel$modules = {};
var $parcel$inits = {};

var parcelRequire = $parcel$global["parcelRequire6ac2"];

if (parcelRequire == null) {
  parcelRequire = function(id) {
    if (id in $parcel$modules) {
      return $parcel$modules[id].exports;
    }
    if (id in $parcel$inits) {
      var init = $parcel$inits[id];
      delete $parcel$inits[id];
      var module = {id: id, exports: {}};
      $parcel$modules[id] = module;
      init.call(module.exports, module, module.exports);
      return module.exports;
    }
    var err = new Error("Cannot find module '" + id + "'");
    err.code = 'MODULE_NOT_FOUND';
    throw err;
  };

  parcelRequire.register = function register(id, init) {
    $parcel$inits[id] = init;
  };

  $parcel$global["parcelRequire6ac2"] = parcelRequire;
}

var parcelRegister = parcelRequire.register;
parcelRegister("g4dDw", function(module, exports) {

$parcel$defineInteropFlag(module.exports);

$parcel$export(module.exports, "Logging", () => $b4042044759f709c$export$f13b02179817fff);
$parcel$export(module.exports, "default", () => $b4042044759f709c$export$2e2bcd8739ae039);

var $iOx9P = parcelRequire("iOx9P");

var $7inJL = parcelRequire("7inJL");

var $31U67 = parcelRequire("31U67");
class $b4042044759f709c$export$f13b02179817fff {
    constructor(){
        // Logging
        /**
   * Enables logging connector activity in the browser console.
   * @memberOf Demandbase.utils
   * @type {Boolean}
   */ this.logging = false;
        /**
   * Enables alerts for thrown errors.
   * @memberOf Demandbase.utils
   * @type {Boolean}
   */ this.debug = false;
        this.logging = window.Demandbase && window.Demandbase.Config && window.Demandbase.Config.logging;
    }
    /**
   * Displays a JS alert with the string/message passed when debug mode is enabled.
   * Used throughout modules in catch statements to show errors.
   * @function
   * @todo refactor to use log function
   * @param  {String} err The error message to display in the alert.
   */ alert(message) {
        this.log(message);
    }
    /**
   * Wrapper around console.log, takes message string as argument.
   * @memberOf Demandbase.utils
   * @function
   * @param  {String} message Text to be logged to console
   * @return [No return value]
   */ log(message) {
        if (this.logging || (0, $31U67.default).getQueryParam((0, $iOx9P.default).QS_ENABLE_LOG) === "true") (0, $7inJL.default).console.log(`DB: ${message}`);
    }
}
const $b4042044759f709c$var$logger = new $b4042044759f709c$export$f13b02179817fff();
var $b4042044759f709c$export$2e2bcd8739ae039 = $b4042044759f709c$var$logger;

});
parcelRegister("iOx9P", function(module, exports) {

$parcel$export(module.exports, "default", () => $0d891f552b1ae0b0$export$2e2bcd8739ae039);
// TODO: Refactor stuff in Config. to use Config.tokens or Config.Constants
// TODO: Move Domain API stuff into domainApi.ts
class $0d891f552b1ae0b0$var$Constants {
    static{
        this.PROTOCOL = "https://";
    }
    static{
        this.URL_COMPANY_TARGET_DOMAIN = "company-target.com";
    }
    static{
        this.QS_USE_TEST_DOMAIN = "db_useTestDomain";
    }
    static{
        this.QS_QUERY_DOMAIN = "db_domain";
    }
    static{
        this.QS_ENABLE_LOG = "db_logging";
    }
    static{
        this.QS_PREVIEW_TOKEN = "db_preview_token";
    }
    static{
        this.DFLT_NON_COMPANY = "(Non-Company Visitor)";
    }
    static{
        this.DFLT_AW_EMPTY = "(AccountWatch Empty)" // When AW company but no value is set aka "Value Not Provided"
        ;
    }
    static{
        this.DFLT_NON_AW = "(Non-AccountWatch Visitor)" // Default for companies not in AW
        ;
    }
    static{
        this.DFLT_EVENT_TYPE = "click";
    }
    static{
        this.URL_IP_API = `api.${this.URL_COMPANY_TARGET_DOMAIN}/api/v3/ip.json` // Note: This is only a fallback. Source of truth in IpApiModule
        ;
    }
    static{
        this.URL_DOMAIN_API = "api.company-target.com/api/v3/domain.json";
    }
    static get URL_BW_AD_PIXEL() {
        return window.Demandbase.Config.tokens?.URL_BW_AD_PIXEL || "match.prod.bidr.io/cookie-sync/demandbase";
    }
    static get URL_LR_AD_PIXEL() {
        return window.Demandbase.Config.tokens?.URL_LR_AD_PIXEL || "id.rlcdn.com/464526.gif";
    }
    static get URL_SMART_PIXEL() {
        return window.Demandbase.Config.ads?.smarPixelURL || `https://s.${this.URL_COMPANY_TARGET_DOMAIN}/s/sync`;
    }
    static{
        this.MODIFICATION_ERROR = "SCModificationError";
    }
    static{
        //mas integrations
        this.PARDOT_VISITOR_COOKIE_REGEX = /^visitor_id[\d]+$/;
    }
    static{
        this.NON_HUMAN_DEVICES = [
            /adsbot-google/i,
            /googlebot/i
        ];
    }
    static{
        this.URL_CURRENT = function() {
            //TODO: use in api calls.
            let pg = document.URL;
            if (window.Demandbase?.Config?.isInIFrame) pg = document.referrer;
            pg = encodeURIComponent(pg);
            return pg;
        }();
    }
    static{
        this.URL_EVENT_API = `et.${this.URL_COMPANY_TARGET_DOMAIN}`;
    }
    static{
        this.EVENT_TYPES = {
            EXPERIENCE_FIRED: "experience_fired",
            EXPERIENCE_CLICKED: "experience_clicked"
        };
    }
}
var $0d891f552b1ae0b0$export$2e2bcd8739ae039 = $0d891f552b1ae0b0$var$Constants;

});

parcelRegister("7inJL", function(module, exports) {

$parcel$export(module.exports, "default", () => $a2ab75eb652422d6$export$2e2bcd8739ae039);
/* eslint-disable no-underscore-dangle, no-self-compare, no-void, no-bitwise */ const $a2ab75eb652422d6$export$e896d9a1b4631fa1 = window.console || {
    log () {},
    debug () {}
};
const $a2ab75eb652422d6$export$eba5dfac2fe298 = window.JSON || {
    stringify () {},
    parse () {}
};
class $a2ab75eb652422d6$export$8c9c6d63b3d598b1 {
    constructor(){
        this.console = $a2ab75eb652422d6$export$e896d9a1b4631fa1;
        this.JSON = $a2ab75eb652422d6$export$eba5dfac2fe298;
    // if (!window.Demandbase && !window.Demandbase.Shims) {
    //   window.Demandbase = window.Demandbase || {};
    //   window.Demandbase.Shims = this;
    // }
    }
    indexOf(array, searchElement, fromIndex) {
        if (array === null || array === undefined) throw new TypeError("Array.indexOf called on null or undefined");
        if (array.indexOf) return array.indexOf(searchElement, fromIndex);
        return this._indexOfPolyfill(array, searchElement, fromIndex);
    }
    assign(...args) {
        if (Object.assign && typeof Object.assign === "function") return Object.assign.apply(null, args);
        if (args[0] === null || args[0] === undefined) throw new TypeError("Cannot convert undefined or null to object");
        return this._assignPolyfill(args);
    }
    startsWith(s, search, rawPos) {
        const pos = rawPos > 0 ? rawPos | 0 : 0;
        return s.substring(pos, pos + search.length) === search;
    }
    includes(search, start) {
        if (search instanceof RegExp) throw new TypeError("First argument must not be a RegExp");
        if (start === undefined) start = 0;
        return this.indexOf(search, start) !== -1;
    }
    keys(obj) {
        if (Object.keys) return Object.keys(obj);
        if (typeof obj !== "function" && (typeof obj !== "object" || obj === null)) throw new TypeError("Object.keys called on non-object");
        return this._keysPolyfill(obj);
    }
    // --- POLYFILLS ---
    _indexOfPolyfill(array, searchElement, fromIndex) {
        const len = array.length >>> 0;
        let i = Math.min(fromIndex | 0, len);
        if (i < 0) i = Math.max(0, len + i);
        else if (i >= len) return -1;
        if (searchElement === void 0) for(; i !== len; ++i){
            if (array[i] === void 0 && i in array) return i;
        } // undefined
        else if (searchElement !== searchElement) for(; i !== len; ++i){
            if (array[i] !== array[i]) return i;
        } // NaN
        else for(; i !== len; ++i){
            if (array[i] === searchElement) return i;
        } // all else
        return -1; // if the value was not found, then return -1
    }
    _assignPolyfill(args) {
        const to = Object(args[0]);
        for(let index = 1; index < args.length; index++){
            const nextSource = args[index];
            if (nextSource != null) {
                // Skip over if undefined or null
                for(const nextKey in nextSource)// Avoid bugs when hasOwnProperty is shadowed
                if (Object.prototype.hasOwnProperty.call(nextSource, nextKey)) to[nextKey] = nextSource[nextKey];
            }
        }
        return to;
    }
    _keysPolyfill(obj) {
        const { hasOwnProperty: hasOwnProperty } = Object.prototype;
        const hasDontEnumBug = !({
            toString: null
        }).propertyIsEnumerable("toString");
        const dontEnums = [
            "toString",
            "toLocaleString",
            "valueOf",
            "hasOwnProperty",
            "isPrototypeOf",
            "propertyIsEnumerable",
            "constructor"
        ];
        const dontEnumsLength = dontEnums.length;
        const result = [];
        let prop;
        let i;
        for(prop in obj)if (hasOwnProperty.call(obj, prop)) result.push(prop);
        if (hasDontEnumBug) {
            for(i = 0; i < dontEnumsLength; i++)if (hasOwnProperty.call(obj, dontEnums[i])) result.push(dontEnums[i]);
        }
        return result;
    }
}
const $a2ab75eb652422d6$var$defaultShims = new $a2ab75eb652422d6$export$8c9c6d63b3d598b1();
var $a2ab75eb652422d6$export$2e2bcd8739ae039 = $a2ab75eb652422d6$var$defaultShims;

});

parcelRegister("31U67", function(module, exports) {

$parcel$export(module.exports, "BaseUtilities", () => $4e0f4b85637db2c2$export$c133914a3af303df);
$parcel$export(module.exports, "default", () => $4e0f4b85637db2c2$export$2e2bcd8739ae039);

var $iOx9P = parcelRequire("iOx9P");

var $7inJL = parcelRequire("7inJL");
class $4e0f4b85637db2c2$export$c133914a3af303df {
    getCookiesByRegex(regex, _document) {
        const extractedCookies = {};
        _document.cookie.split(";").forEach((cookieString)=>{
            const cookie = cookieString.split("=");
            const cookieKey = cookie[0].trim();
            if (regex.test(cookieKey) && cookie.length > 1) extractedCookies[cookieKey] = cookie[1].trim();
        });
        return extractedCookies;
    }
    getElementByIdOrName(elementIdentifier) {
        return document.getElementById(elementIdentifier) || document.getElementsByName(elementIdentifier)[0] || null;
    }
    addEventListener(target, type, listener) {
        if (target.addEventListener) target.addEventListener(type, listener);
        else if (target.attachEvent) target.attachEvent(type, listener);
    }
    dig(target, ...keys) {
        let digged = target;
        for (const key of keys){
            if (typeof digged === "undefined") return undefined;
            if (typeof key === "function") digged = key(digged);
            else digged = digged[key];
        }
        return digged;
    }
    set(obj, path, value) {
        if (Object(obj) !== obj) return obj; // When obj is not an object
        // If not yet an array, get the keys from the string-path
        if (!Array.isArray(path)) path = path.toString().match(/[^.[\]]+/g) || [];
        path.slice(0, -1).reduce((a, c, i // Iterate all of them except the last one
        )=>Object(a[c]) === a[c] // Does the key exist and is its value an object?
             ? a[c] : a[c] = Math.abs(path[i + 1]) >> 0 === +path[i + 1] ? [] // Yes: assign a new array object
             : {}, obj)[path[path.length - 1]] = value; // Finally assign the value to the last key
        return obj; // Return the top-level object to allow chaining
    }
    flatten(object) {
        if (!object || typeof object !== "object") return object;
        for(const key in object){
            const value = object[key];
            if (typeof value !== "object" || value === null || !object.hasOwnProperty(key)) continue;
            // NB Current expected behavior is to flatten 1 level deep, may be revisted.
            // value = flattenData(value) // Add for recursive flattening
            for(const nestedKey in value)object[`${key}_${nestedKey}`] = value[nestedKey];
            delete object[key];
        }
        return object;
    }
    getAttributeValue(data, attrName) {
        if (data[attrName] === false) return "false";
        const registryMap = {
            city: "registry_city",
            state: "registry_state",
            zip: "registry_zip_code",
            country: "registry_country_code",
            country_name: "registry_country",
            latitude: "registry_latitude",
            longitude: "registry_longitude"
        };
        const dflt = window.Demandbase.Config.nonCompanyDefault || (0, $iOx9P.default).DFLT_NON_COMPANY;
        let awDflt = window.Demandbase.Config.emptyWatchDefault || (0, $iOx9P.default).DFLT_AW_EMPTY;
        const regName = registryMap[attrName] || "";
        let attrValue = data[attrName] || data[regName] || this.dig(data, "custom_fields", attrName) || dflt;
        const isCompany = (data.company_name || dflt) !== dflt;
        const dataKeys = (0, $7inJL.default).keys(data);
        let isAcctWatch = false;
        for(let i = 0; i < dataKeys.length; i++)if ((0, $7inJL.default).indexOf(dataKeys[i], "watch_list_") === 0) {
            isAcctWatch = true;
            break;
        }
        if ((0, $7inJL.default).indexOf(attrName, "watch_list_") !== -1 && isCompany) {
            // TAG-109: since AW object exists here, default should show that
            if (!isAcctWatch) awDflt = window.Demandbase.Config.nonWatchDefault || (0, $iOx9P.default).DFLT_NON_AW;
            attrValue = data[attrName] || awDflt;
        }
        return attrValue;
    }
    /**
     * Takes a string--the name of a query string parameter, and retrieves the value of a parameter
     * from the pages URL query string.
     * Note: supported parameters are defined in {@link Demandbase.utils.tokens}.
     * Supported parameters are: <br/>
     * Booleans:<br/>
     * {@link db_useTestIp} - required to use {@link db_ip} <br/>
     * {@link db_useTestDomain} - required to use {@link db_domain} <br/>
     * {@link db_logging} - Enable verbose console logging <br/>
     * {@link db_debug} - Enable alert messages for errors. <br/>
     * Override values: <br/>
     * {@link db_ip}, {@link db_domain} <br/>
     * @memberof Demandbase.utils
     * @type {Function}
     * @function getQueryParam
     * @param    {String} param Exact parameter name to grab from URL query string.
     * @param    {String} window object to use, will use the global window object if not specified
     * @return   {String} Value of named parameter in query string or empty string if not present.
     */ // TODO: Refactor into engine wide cached tool, to prevent reparsing
    getQueryParam(param, _window) {
        var _window = _window || window || {
            location: {
                search: "",
                hash: ""
            }
        };
        const params = {};
        const qs = _window.location.search.substring(1) || _window.location.hash && _window.location.hash.split("?")[1];
        if (!qs) return "";
        const pairs = qs.split("&");
        // get query string, remove the leading '?'
        for(let i = 0; i < pairs.length; i++){
            const nvArray = pairs[i].split("=");
            const name = nvArray[0];
            const value = nvArray[1];
            params[name] = value;
        }
        return params[param] || "";
    }
    // TODO reevaluate the runtime dom insert implications
    insertScript(url, id, srcPrefix = "https://") {
        if (!url) return;
        // NB This was a patch to prevent the multiloading of forms in certain cases.
        //    Which might be dude to multiple markto related loadFormModule calls
        // TODO reevaluate the underlaying cause and need for this, possibly refactor
        window.Demandbase._loadedScripts = window.Demandbase._loadedScripts || {};
        if (window.Demandbase._loadedScripts[url]) return;
        window.Demandbase._loadedScripts[url] = true;
        const element = document.createElement("script");
        const firstScript = document.getElementsByTagName("script")[0];
        element.async = true;
        element.id = id || "";
        element.src = `${srcPrefix}${url.replace(/(^\/\/)|(^http:\/\/)|(^https:\/\/)/, "")}`;
        if (firstScript && firstScript.parentNode) firstScript.parentNode.insertBefore(element, firstScript);
    }
    /**
     * Returns true if the browser is IE10 or prior.
     *
     * Example User Agents:
     *  IE10: 'Mozilla/5.0 (compatible; MSIE 10.0; Windows NT 6.2; Trident/6.0)';
     *  IE11: 'Mozilla/5.0 (Windows NT 6.3; Trident/7.0; rv:11.0) like Gecko';
     */ isOldBrowserOrUserAgentUnavailable() {
        try {
            return (0, $7inJL.default).indexOf(window.navigator.userAgent, "MSIE ") > 0;
        } catch (error) {
            // userAgent is not readable in some private browsing scenarios, if
            // that happens, assume the worsts
            return true;
        }
    }
    b64EncodeUnicode(str) {
        return btoa(encodeURIComponent(str).replace(/%([0-9A-F]{2})/g, function toSolidBytes(match, p1) {
            return String.fromCharCode(parseInt(`0x${p1}`, 16));
        }));
    }
    /**
     * Generates a friendly deprecation message that can be raised in errors
     * @method generateDeprecationMessage
     * @param  name    name of deprecated function or variable
     * @param  version version that it was deprecated in
     * @return         message
     */ generateDeprecationMessage(name, version) {
        return `${name} has been deprecated since version ${version}`;
    }
    /**
     * Finds the first non-empty object from the provided arguments.
     *
     * @param {...object} items - The list of objects to check.
     * @returns {object | null} - The first non-empty object, or null if none found.
     */ getFirstNonEmptyObject(...items) {
        for (const item of items){
            if (item && Object.keys(item).length > 0) return item;
        }
        return null;
    }
}
const $4e0f4b85637db2c2$var$baseUtilities = new $4e0f4b85637db2c2$export$c133914a3af303df();
var $4e0f4b85637db2c2$export$2e2bcd8739ae039 = $4e0f4b85637db2c2$var$baseUtilities;

});


parcelRegister("7VWOe", function(module, exports) {

$parcel$defineInteropFlag(module.exports);

$parcel$export(module.exports, "EmailDomainReporterModule", () => $4f5b31f03b96a79e$export$a26ba7a1d97c0115);
$parcel$export(module.exports, "default", () => $4f5b31f03b96a79e$export$2e2bcd8739ae039);
/* eslint-disable no-useless-catch */ 
var $brhsV = parcelRequire("brhsV");

var $31U67 = parcelRequire("31U67");

var $4w27I = parcelRequire("4w27I");
class $4f5b31f03b96a79e$export$a26ba7a1d97c0115 extends (0, $brhsV.BaseModule) {
    constructor(config){
        super();
        this.DEFAULT_CONFIGURATION = {
            enabled: true,
            fireOnLoad: false,
            formInputSelectors: [
                'input[type="text"]',
                'input[type="email"]'
            ],
            inputSearchTerms: [
                "email",
                "user",
                "login"
            ]
        };
        this.configuration = {};
        this.baseUrl = "https://segments.company-target.com";
        this.activeSetTimeout = 0;
        this._setup = ()=>{
            super.mergeConfigs(this.DEFAULT_CONFIGURATION, config);
            return this;
        };
        this._setup();
    }
    initialize() {
        super.initialize();
        // Skip this for now as it is causing too much noise for
        // Predefined test emails on legit websites
        if (this.configuration.fireOnLoad) this.sendDataIfAlreadyPresent();
        this.attachListenersIfDocumentReady();
    }
    sendDataIfAlreadyPresent() {
        const emailInputs = this.suspectedEmailInputs();
        if (emailInputs.length < 1) return;
        emailInputs.forEach((input)=>{
            const { value: value } = input;
            if (!(0, $4w27I.default).isValidEmail(value)) return;
            // grab domain and send to Mariposa API
            const domain = value.split("@")[1].toLowerCase();
            this.send(domain);
        });
    }
    attachListenersIfDocumentReady() {
        if ((0, $4w27I.default).getDocumentReadyState() === "loading") {
            document.addEventListener("DOMContentLoaded", this.attachListenersIfDocumentReady.bind(this));
            return;
        }
        // TODO: If this.suspectedEmailInputs().length === 0, let's add a
        // mutation observer to attach handlers to the inputs added later (or
        // just set a timer to keep running this.attachListenersIfDocumentReady)
        //
        // For now, we only support forms that exist when Tag loads - let's see
        // how much data we miss
        //@TODO_REWORK This part seems to fail in jest testing
        this.suspectedEmailInputs().forEach((input)=>{
            input.addEventListener("input", ()=>{
                const { value: value } = input;
                if (!(0, $4w27I.default).isValidEmail(value)) return;
                // grab domain and send to Mariposa API
                const domain = value.split("@")[1].toLowerCase();
                // Don't send immediately on input, allow multiple changes to
                // input before sending. The active timeout is stored in
                // this.activeSetTimeout so that we can clear it if the input
                // value changes before 400ms
                window.clearTimeout(this.activeSetTimeout);
                this.activeSetTimeout = window.setTimeout(()=>{
                    this.send(domain);
                }, 400);
            });
        });
    }
    suspectedEmailInputs() {
        // grab all form input elements that match our rules and convert to array
        const allInputsOnPage = (0, $4w27I.default).nodeListToArray(document.querySelectorAll(this.configuration.formInputSelectors.join(","))).map((element)=>element);
        const suspectedEmailInputs = allInputsOnPage.filter((inputElement)=>{
            const name = inputElement.name.toLowerCase();
            const id = inputElement.id.toLowerCase();
            const searchTerms = this.configuration.inputSearchTerms;
            if ((0, $4w27I.default).includesAny(name, searchTerms)) return true;
            if ((0, $4w27I.default).includesAny(id, searchTerms)) return true;
            return false;
        });
        return suspectedEmailInputs;
    }
    getNewRequest() {
        let xhttp;
        if (window.XMLHttpRequest) xhttp = new XMLHttpRequest();
        else if (window.ActiveXObject) xhttp = new ActiveXObject("Microsoft.XMLHTTP");
        return xhttp;
    }
    send(domain) {
        let xhttp = this.getNewRequest();
        const token = (0, $4w27I.default).getApiAuthToken();
        const qsB64 = (0, $31U67.default).b64EncodeUnicode(`vendor=mariposa&p1=${domain}&token=${token}`);
        const url = `${this.baseUrl}/l/${qsB64}`;
        try {
            xhttp.open("GET", url);
            xhttp.withCredentials = true;
            xhttp.setRequestHeader("Content-type", "application/json");
            xhttp.send();
        } catch (requestError) {
            // May want to handle status 0, if we see lots of these
            throw requestError;
        }
    }
    responseHandler(request) {
    // This does nothing other than allow Jasmine to properly spy on AJAX
    // method for .send() above...
    }
}
var $4f5b31f03b96a79e$export$2e2bcd8739ae039 = $4f5b31f03b96a79e$export$a26ba7a1d97c0115;

});
parcelRegister("brhsV", function(module, exports) {

$parcel$export(module.exports, "BaseModule", () => $c67fa303a599c3f7$export$adea4f5921a64958);

var $7inJL = parcelRequire("7inJL");
class $c67fa303a599c3f7$export$adea4f5921a64958 {
    constructor(config){
        this.DEFAULT_CONFIGURATION = {};
        this.configuration = {};
        this._setup = ()=>{
            this.mergeConfigs(this.DEFAULT_CONFIGURATION, config || window.Demandbase?.Config?.[this.constructor.name]);
            return this;
        };
        this._setup();
    }
    isEnabled() {
        return this.configuration.enabled || false;
    }
    mergeConfigs(...configs) {
        for(let i = 0; i < configs.length; i++)this.configuration = (0, $7inJL.default).assign(this.configuration, configs[i]);
    }
    initialize() {
        this._setup();
    }
}

});

parcelRegister("4w27I", function(module, exports) {

$parcel$export(module.exports, "default", () => $aa6dde14f53f2697$export$2e2bcd8739ae039);
/* eslint-disable no-inner-declarations */ 
var $iOx9P = parcelRequire("iOx9P");

var $g4dDw = parcelRequire("g4dDw");

var $7inJL = parcelRequire("7inJL");

var $31U67 = parcelRequire("31U67");
class $aa6dde14f53f2697$export$58ce12eb22e52a3f extends (0, $31U67.BaseUtilities) {
    detectIFrame() {
        return window.top !== window.self;
    }
    getDocumentReadyState() {
        return document.readyState;
    }
    isCookieEnabled() {
        try {
            if (window.navigator.cookieEnabled) {
                document.cookie = "COOKIE_TEST=TEST";
                if ((0, $7inJL.default).indexOf(document.cookie, "COOKIE_TEST=TEST") !== -1) {
                    document.cookie = "COOKIE_TEST=PASSED_TEST";
                    return true;
                }
            }
            return false;
        } catch (error) {
            return false;
        }
    }
    /*
     * Wraps up all the logic for determining what the current URL is.
     * */ getCurrentUrl(currUrl) {
        let currentUrl = document.location.href;
        // TODO: First, think about if this has implications....
        // TODO Refactor this to use Constants.URL_CURRENT
        if (window.Demandbase.Config.isInIFrame) currentUrl = document.referrer;
        if (currUrl) currentUrl = currUrl;
        return currentUrl;
    }
    /**
     * Pass it a URL  (with or without query string, sub domain, or tailing slashes)
     * Returns true if the URL passed matches the current {@link document.loction.href};
     *
     * <em>This is not a simple string comparison.  The structure of the test URL dictates which parts
     * of the current page are examined.  If the test URL does not have query string parameters or
     * a hash, then the query string and hash on the current url are ignored.  Trailing slashes and
     * hash signs are also generally ignored.  Protocol and 'www.' are also ignored.  Other
     * subdomains, such as www2 or www-qa are not ignored.</em>
     * @todo  possibly support array of urls as first param
     * @todo re-write this crap
     * @param  {String}  testUrl The url to compare against the current page
     * @param  {String}  currentUrl Optional - test against this URL, rather than the current page, if passed
     * @return {Boolean}     true if the url matches the current document or second parameter
     */ isCurrentPage(testUrl, currUrl) {
        const qm = "?";
        const pound = "#";
        let { hash: hash } = document.location;
        let { search: search } = document.location;
        let currentUrl = this.getCurrentUrl(currUrl);
        if (currUrl) {
            let searchEnd = (0, $7inJL.default).indexOf(currUrl, pound);
            if (searchEnd === -1) searchEnd = currUrl.length;
            hash = currUrl.substring((0, $7inJL.default).indexOf(currUrl, pound), currUrl.length);
            search = currUrl.substring((0, $7inJL.default).indexOf(currUrl, qm), searchEnd);
            currentUrl = currUrl;
        }
        //TODO - possibly chain these functions together so they can be called as one
        //strip [ptcl]:// and //
        function stripProtocol(str) {
            const doubleSlash = "//";
            if ((0, $7inJL.default).indexOf(str, doubleSlash) === 0) //remove double slash if it starts with that
            return str.substring(doubleSlash.length, str.length);
            //otherwise remove entire protocol
            return str.replace(/^.*?:\/\//g, "");
        }
        //remove 'www.' from url
        function stripWww(str) {
            return str.replace(/^(www\.)/g, "");
        }
        //remove trailiing '/' or '#'
        function stripTail(str) {
            const slash = "/";
            if ((0, $7inJL.default).indexOf(str, pound, str.length - pound.length) !== -1) str = str.substring(0, str.length - 1);
            if ((0, $7inJL.default).indexOf(str, slash, str.length - slash.length) !== -1) {
                str = str.substring(0, str.length - 1);
                if ((0, $7inJL.default).indexOf(str, slash, str.length - slash.length) !== -1) return stripTail(str);
            }
            return str;
        }
        testUrl = stripProtocol(testUrl);
        testUrl = stripWww(testUrl);
        testUrl = stripTail(testUrl);
        currentUrl = stripProtocol(currentUrl);
        currentUrl = stripWww(currentUrl);
        currentUrl = stripTail(currentUrl);
        if ((0, $7inJL.default).indexOf(testUrl, pound) === -1 && (0, $7inJL.default).indexOf(currentUrl, pound) !== -1) //hash !== ''
        //if testUrl does not have hash defined
        //and the current page does,
        //then
        //strip the hash off the current url
        //otherwise, evaluate the current url using the anchor on the current page
        currentUrl = currentUrl.substring(0, currentUrl.length - hash.length);
        if ((0, $7inJL.default).indexOf(testUrl, qm) === -1 && (0, $7inJL.default).indexOf(currentUrl, qm) !== -1) //if testUrl does NOT have query string parameters,
        //and current URL does
        //then
        //strip the qs params off the current url (document.location.href)
        //otherwise, evaluate the testUrl using the qs parameters on the current page
        currentUrl = currentUrl.substring(0, currentUrl.length - search.length);
        //do this again after qs/hash is stripped
        currentUrl = stripTail(currentUrl);
        const result = currentUrl === testUrl;
        (0, $g4dDw.default).log("utilities.isCurrentPage(): Page check resulted in: " + result);
        return result;
    }
    isCurrentPageRegex(testRegex, currUrl) {
        if (!testRegex) return false;
        if (testRegex.length <= 0) return false;
        if (testRegex[0] !== "^") testRegex = `^${testRegex}`;
        const end = testRegex.length - 1;
        if (testRegex[end] !== "$") testRegex += "$";
        const currentUrl = this.getCurrentUrl(currUrl);
        return new RegExp(testRegex).test(currentUrl);
    }
    /**
     * Can be extended to support sessionStorage.
     * @see https://gist.github.com/paulirish/5558557
     */ isStorageEnabled(type) {
        try {
            const storage = window[type.toString()];
            storage.setItem("STORAGE_CHECK", "STORAGE_CHECK");
            const test = storage.getItem("STORAGE_CHECK");
            storage.removeItem("STORAGE_CHECK");
            return true;
        } catch (error) {
            return false;
        }
    }
    // TODO Potential only used in forms/autocomplete possible refactor into
    jqid(id) {
        return !id ? null : `#${id.replace(/(:|\.|\[|\]|,|\s)/g, "\\$1")}`;
    }
    /**
     * Checks if the provided string is a valid email address as best as
     * a regexp can
     *
     * @param  {string} str [description]
     * @return {boolean}    [description]
     */ includesAny(haystack, needles) {
        for(let i = 0; i < needles.length; i++){
            if (this.includes(haystack, needles[i])) return true;
        }
        return false;
    }
    /**
     * Checks if the provided string is a valid email address as best as
     * a regexp can
     *
     * @param  {string} str [description]
     * @return {boolean}    [description]
     */ isValidEmail(str) {
        const regexp = /^(([^<>()\[\]\\.,;:\s@"]+(\.[^<>()\[\]\\.,;:\s@"]+)*)|(".+"))@((\[[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}])|(([a-zA-Z\-0-9]+\.)+[a-zA-Z]{2,}))$/;
        return regexp.test(str);
    }
    /**
     * escapes a string for use in a regular expression
     * */ escapeRegExp(str) {
        return str.replace(/[.*+?^${}()|[\]\\\/]/g, "\\$&");
    }
    /**
     * Converts a NodeList (structure returned by document.querySelectorAll)
     * to a normal array that can be iterated over and operated on like an
     * array
     * @param  {NodeListOf<Element>}     nodeList [description]
     * @return {Array<HTMLElement>}          [description]
     */ nodeListToArray(nodeList) {
        const output = [];
        for(let i = 0; i < nodeList.length; i++)output.push(nodeList[i]);
        return output;
    }
    includes(str, search) {
        if (!search) return false;
        if (search.length > str.length) return false;
        return (0, $7inJL.default).indexOf(str, search) !== -1;
    }
    /**
     * Generates a version 4 UUID.
     *
     * A version 4 UUID is a universally unique identifier that is generated using random numbers.
     * The UUID generated by this function is in the form of 'xxxxxxxx-xxxx-4xxx-yxxx-xxxxxxxxxxxx',
     * where the x's are any hexadecimal digits and the y is a hexadecimal digit from the set [8, 9, a, or b].
     *
     * @returns {string} A version 4 UUID in the form of 'xxxxxxxx-xxxx-4xxx-yxxx-xxxxxxxxxxxx'.
     * @ref https://stackoverflow.com/a/2117523
     */ generateUuid() {
        try {
            return "10000000-1000-4000-8000-100000000000".replace(/[018]/g, (c)=>(+c ^ crypto.getRandomValues(new Uint8Array(1))[0] & 15 >> +c / 4).toString(16));
        } catch (error) {
            console.error("Failed to generate UUID:", error);
            // return a fallback random ID
            return "id-" + Date.now() + "-" + Math.floor(Math.random() * Number.MAX_SAFE_INTEGER);
        }
    }
    /**
     * Retrieves the authentication token for making calls to the Demandbase API.
     * It tries to find the token in several places within the Demandbase configuration object.
     * If it can't find a valid token, it returns the string 'ERR_NO_AUTH_KEY'.
     *
     * @returns {string} The authentication token, or 'ERR_NO_AUTH_KEY' if no valid token is found.
     */ getApiAuthToken() {
        return this.dig(window.Demandbase, "Config", "key") || this.dig(window.Demandbase, "Config", "analytics", "key") || this.dig(window.Demandbase, "Config", "ads", "key") || this.dig(window.Demandbase, "Config", "forms", "key") || this.DEFAULT_NO_TOKEN_VALUE;
    }
    /**
     * Sets the protocol as HTTPS for the given URL.
     *
     * @param url - The URL to modify.
     * @returns The modified URL with the HTTPS protocol.
     */ setHttpsProtocol(url) {
        return url.replace(/^([^:]+:\/\/)?/, (0, $iOx9P.default).PROTOCOL);
    }
    constructor(...args){
        super(...args);
        this.DEFAULT_NO_TOKEN_VALUE = "ERR_NO_AUTH_KEY";
    }
}
const $aa6dde14f53f2697$var$defaultUtils = new $aa6dde14f53f2697$export$58ce12eb22e52a3f();
var $aa6dde14f53f2697$export$2e2bcd8739ae039 = $aa6dde14f53f2697$var$defaultUtils;

});


parcelRegister("a3Qp1", function(module, exports) {

$parcel$defineInteropFlag(module.exports);

$parcel$export(module.exports, "AdvertisingModule", () => $db5313ea8b48677f$export$c7746fc6fa0e7608);
$parcel$export(module.exports, "default", () => $db5313ea8b48677f$export$2e2bcd8739ae039);

var $31U67 = parcelRequire("31U67");

var $brhsV = parcelRequire("brhsV");

var $g4dDw = parcelRequire("g4dDw");

var $iOx9P = parcelRequire("iOx9P");
class $db5313ea8b48677f$export$c7746fc6fa0e7608 extends (0, $brhsV.BaseModule) {
    constructor(config){
        super(config);
        this.ADVERTISING_PIXEL_ID = "ad";
        this.CONVERSION_PIXEL_ID = "cn";
        this.RETARGETING_PIXEL_ID = "rt";
        this.SMART_PIXEL_ID = "db-sync";
        this.PIXEL_ID_IX = "ix";
        this.PIXEL_ID_MCTV = "mctv";
        /**
     * The pixel id for Magnite_DV ("rp")
     */ this.PIXEL_ID_MAGNITE_DV = "rp";
        this.PIXEL_ID_LR = "lr";
        this.DEFAULT_CONFIGURATION = {
            enabled: true,
            key: undefined,
            reportingOnly: false,
            enableBW: false,
            enableLR: true,
            enableIX: true,
            enableMCTV: true,
            enableRP: true,
            enableSmartPixel: true
        };
        this.configuration = {};
        // NB: Backwards Compatibility Shims - 3/31/2017 /////////////////////////////
        this.trackConversion = this.trackConversionListener;
        this.load = this.initialize;
        this.loadPixels = this.insertPixels;
        this._loadPixel = this.insertPixel;
        this._setCampaign = this.loadCampaign;
        this._setEvents = this.registerEvents;
        this._setup = ()=>{
            super.mergeConfigs(this.DEFAULT_CONFIGURATION, config);
            // NB: Backwards Compatibility Shim - 3/21/2017 ////////////////////////////
            super.mergeConfigs(config);
            ////////////////////////////////////////////////////////////////////////////
            return this;
        };
        this._setup();
    }
    //////////////////////////////////////////////////////////////////////////////
    initialize(configOverride) {
        super.initialize();
        if (configOverride) super.mergeConfigs(configOverride);
        this.insertPixels();
    }
    /**
     * @deprecated since 8.0.0 - removal of IPONWEB
     * @method isConversionPage
     */ isConversionPage() {
        throw new Error((0, $31U67.default).generateDeprecationMessage("AdvertisingModule.isConversionPage", "8.0.0"));
    }
    fireIpApiReporting() {
        // TODO: Unquieness of key/call should be a concern IP module, as Ads shouldnt need to know about IP config
        // TODO: Not sure if this needs to reference Demandbase.Config
        if (this.configuration.reportingOnly === true && this.configuration.key && window.Demandbase.Config.key) window.Demandbase.IpApiReportingOnly.get(this.configuration.key, false);
    }
    insertPixels() {
        // Check if we should load the smart pixel iframe
        if (this.configuration.enableSmartPixel) this.insertSmartPixel();
        if (this.configuration.enableBW) (0, $g4dDw.default).log("BW pixel is deprecated and will not load.");
        if (this.configuration.enableLR) {
            (0, $g4dDw.default).log("LR pixel enabled");
            this.insertLRPixel(this.ADVERTISING_PIXEL_ID);
        }
    }
    createAndAppendPixel(id, src) {
        const element = document.getElementsByTagName("body")[0] || document.getElementsByTagName("head")[0];
        const pixelElm = document.createElement("img");
        // Set styles with cssText instead of setAttribute to avoid CSP issues for clients
        pixelElm.style.cssText = "display: none;";
        pixelElm.setAttribute("alt", "");
        pixelElm.setAttribute("aria-hidden", "true");
        pixelElm.setAttribute("width", "0");
        pixelElm.setAttribute("height", "0");
        pixelElm.id = id;
        pixelElm.src = src;
        element.appendChild(pixelElm);
    }
    createAndAppendIFrame(id, src) {
        const element = document.getElementsByTagName("body")[0] || document.getElementsByTagName("head")[0];
        const pixelElm = document.createElement("iframe");
        // Set styles with cssText instead of setAttribute to avoid CSP issues for clients
        pixelElm.style.cssText = "display: none; border: 0px;";
        pixelElm.setAttribute("alt", "");
        pixelElm.setAttribute("aria-hidden", "true");
        pixelElm.setAttribute("width", "0");
        pixelElm.setAttribute("height", "0");
        pixelElm.setAttribute("sandbox", "");
        pixelElm.id = id;
        pixelElm.src = src;
        element.appendChild(pixelElm);
        return pixelElm;
    }
    insertSmartPixel() {
        (0, $g4dDw.default).log("insertSmartPixel(): Smart pixel loading");
        const smartPixelUrl = this.configuration.smarPixelURL || (0, $iOx9P.default).URL_SMART_PIXEL;
        const params = this.buildSmartPixelParameters();
        const src = `${smartPixelUrl}?${params}`;
        const iframeElement = this.createAndAppendIFrame(this.SMART_PIXEL_ID, src);
        return iframeElement;
    }
    buildSmartPixelParameters() {
        const paramsToExcludeArray = [];
        paramsToExcludeArray.push(this.PIXEL_ID_LR);
        if (!this.configuration.enableIX) paramsToExcludeArray.push(this.PIXEL_ID_IX);
        if (!this.configuration.enableMCTV) paramsToExcludeArray.push(this.PIXEL_ID_MCTV);
        if (!this.configuration.enableRP) paramsToExcludeArray.push(this.PIXEL_ID_MAGNITE_DV);
        let params = "";
        if (paramsToExcludeArray.length > 0) params = `exc=${paramsToExcludeArray.join(",")}`;
        return params;
    }
    /**
     * Create a Live Ramp pixel
     * Ultimately looks like:
     * <iframe name="_rlcdn" width=0 height=0 frameborder=0
     * src="https://idsync.rlcdn.com/710927.html?partner_uid=[partner_cookie]"></iframe>
     * @param name the name/identifier for this pixel
     */ insertLRPixel(name) {
        const id = `db_lr_pixel_${name}`;
        const src = this.configuration.lrAdPixelURL || (0, $iOx9P.default).PROTOCOL + (0, $iOx9P.default).URL_LR_AD_PIXEL;
        this.createAndAppendPixel(id, src);
    }
    /**
     * @deprecated since 8.0.0 - removal of IPONWEB
     * @method insertPixel
     */ insertPixel(name) {
        throw new Error((0, $31U67.default).generateDeprecationMessage("AdvertisingModule.insertPixel", "8.0.0"));
    }
    /**
     * @deprecated since 8.0.0 - removal of IPONWEB
     * @method loadCampaign
     */ loadCampaign() {
        throw new Error((0, $31U67.default).generateDeprecationMessage("AdvertisingModule.loadCampaign", "8.0.0"));
    }
    /**
     * @deprecated since 8.0.0 - removal of IPONWEB
     * @method registerEvents
     */ registerEvents() {
        throw new Error((0, $31U67.default).generateDeprecationMessage("AdvertisingModule.registerEvents", "8.0.0"));
    }
    /**
     * @deprecated since 8.0.0 - removal of IPONWEB
     * @method trackConversionListener
     */ trackConversionListener() {
        throw new Error((0, $31U67.default).generateDeprecationMessage("AdvertisingModule.trackConversionListener", "8.0.0"));
    }
    /**
     * @deprecated since 8.0.0 - removal of IPONWEB
     * @method virtualPageViewListener
     */ virtualPageViewListener() {
        throw new Error((0, $31U67.default).generateDeprecationMessage("AdvertisingModule.virtualPageViewListener", "8.0.0"));
    }
}
var $db5313ea8b48677f$export$2e2bcd8739ae039 = $db5313ea8b48677f$export$c7746fc6fa0e7608;

});

parcelRegister("46JbE", function(module, exports) {

$parcel$defineInteropFlag(module.exports);

$parcel$export(module.exports, "IpApiUtilities", () => $8e2bd7f50f8abdfb$export$dcc23046e728e382);
$parcel$export(module.exports, "default", () => $8e2bd7f50f8abdfb$export$2e2bcd8739ae039);

var $g4dDw = parcelRequire("g4dDw");
class $8e2bd7f50f8abdfb$export$dcc23046e728e382 {
    /**
   * Async function to get the Chrome third party cookie deprecation label, if available.
   */ static async getThirdPartyOptInLabel() {
        try {
            if (typeof window.navigator !== "undefined" && typeof window.navigator.cookieDeprecationLabel !== "undefined" && typeof window.navigator.cookieDeprecationLabel.getValue === "function") {
                const label = await window.navigator.cookieDeprecationLabel.getValue();
                return label;
            }
            return "";
        } catch (e) {
            (0, $g4dDw.default).log("Error getting third party opt in" + e + " stack: " + e.stack);
            return "";
        }
    }
    /**
   * Creates a new XMLHttpRequest object or an ActiveXObject for making HTTP requests.
   * @returns The created XMLHttpRequest object or ActiveXObject.
   */ static getNewRequest() {
        let request;
        if (window.XMLHttpRequest) request = new XMLHttpRequest();
        else if (window.ActiveXObject) request = new ActiveXObject("Microsoft.XMLHTTP");
        return request;
    }
    /**
   * Fires an IP API request with the provided arguments.
   *
   * @param request - The XMLHttpRequest or ActiveXObject instance
   * @param url - The full URL to send the request to
   * @param params - The request body (object to be stringified)
   * @param responseHandler - callback to handle the response (request: XMLHttpRequest) => void
   * @param isIgnorableDevice - function to check if device is ignorable (returns boolean)
   */ static async fireRequest({ request: request, url: url, params: params, responseHandler: responseHandler, isIgnorableDevice: isIgnorableDevice, triggerCallback: triggerCallback = true }) {
        if (triggerCallback) request.onreadystatechange = ()=>{
            responseHandler(request);
        };
        try {
            request.open("POST", url);
            // Get chrome third party cookie label
            const thirdPartyCookieLabel = await $8e2bd7f50f8abdfb$export$dcc23046e728e382.getThirdPartyOptInLabel();
            if (thirdPartyCookieLabel) params["cookie_deprecation_label"] = thirdPartyCookieLabel;
            // Support IE9 and ActiveXObject
            if (typeof request.withCredentials !== "undefined") request.withCredentials = true;
            request.send(JSON.stringify(params));
        } catch (error) {
            if (request.status === 0) {
                if (!isIgnorableDevice()) throw new Error("IP API Request Blocked");
            } else throw error;
        }
    }
}
var $8e2bd7f50f8abdfb$export$2e2bcd8739ae039 = $8e2bd7f50f8abdfb$export$dcc23046e728e382;

});

var $548914322ea4771d$exports = {};
// Add global type declarations for UMD and custom properties
// Fixes: Cannot find name 'define', and global property errors
/* eslint-disable no-empty, consistent-return */ 
var $brhsV = parcelRequire("brhsV");

var $31U67 = parcelRequire("31U67");

var $g4dDw = parcelRequire("g4dDw");
/* eslint-disable no-underscore-dangle, no-var, vars-on-top */ // https://raw.githubusercontent.com/stacktracejs/error-stack-parser/4ea1f3f0c81bda847d175318f35144c93bb2bb2b/dist/error-stack-parser.js

var $7inJL = parcelRequire("7inJL");
class $d9b9ae09465e9a88$export$7ebf908d4310f9e3 {
    static{
        this.FIREFOX_SAFARI_STACK_REGEXP = /(^|@)\S+\:\d+/;
    }
    static{
        this.CHROME_IE_STACK_REGEXP = /^\s*at .*(\S+\:\d+|\(native\))/m;
    }
    static{
        this.SAFARI_NATIVE_CODE_REGEXP = /^(eval@)?(\[native code\])?$/;
    }
    parse(error) {
        if (typeof error.stacktrace !== "undefined" || typeof error["opera#sourceloc"] !== "undefined") return this.parseOpera(error);
        if (error.stack && error.stack.match($d9b9ae09465e9a88$export$7ebf908d4310f9e3.CHROME_IE_STACK_REGEXP)) return this.parseV8OrIE(error);
        if (error.stack) return this.parseFFOrSafari(error);
        return undefined;
    }
    extractLocation(urlLike) {
        // Fail-fast but return locations like "(native)"
        if ((0, $7inJL.default).indexOf(urlLike, ":") === -1) return [
            urlLike
        ];
        const regExp = /(.+?)(?:\:(\d+))?(?:\:(\d+))?$/;
        const parts = regExp.exec(urlLike.replace(/[\(\)]/g, ""));
        return [
            parts[1],
            parts[2] || undefined,
            parts[3] || undefined
        ];
    }
    _parseInt(string, radix = 10) {
        if (!string) return undefined;
        return parseInt(string, radix);
    }
    parseV8OrIE(error) {
        const filtered = error.stack.split("\n").filter(function(line) {
            return !!line.match($d9b9ae09465e9a88$export$7ebf908d4310f9e3.CHROME_IE_STACK_REGEXP);
        }, this);
        return filtered.map(function(line) {
            if ((0, $7inJL.default).indexOf(line, "(eval ") > -1) // Throw away eval information until we implement stacktrace.js/stackframe#8
            line = line.replace(/eval code/g, "eval").replace(/(\(eval at [^\()]*)|(\)\,.*$)/g, "");
            const tokens = line.replace(/^\s+/, "").replace(/\(eval code/g, "(").split(/\s+/).slice(1);
            const locationParts = this.extractLocation(tokens.pop());
            const functionName = tokens.join(" ") || undefined;
            const fileName = (0, $7inJL.default).indexOf([
                "eval",
                "<anonymous>"
            ], locationParts[0]) > -1 ? undefined : locationParts[0];
            return {
                function: functionName,
                file: fileName,
                line: this._parseInt(locationParts[1]),
                column: this._parseInt(locationParts[2])
            };
        }, this);
    }
    parseFFOrSafari(error) {
        const filtered = error.stack.split("\n").filter(function(line) {
            return !line.match($d9b9ae09465e9a88$export$7ebf908d4310f9e3.SAFARI_NATIVE_CODE_REGEXP);
        }, this);
        return filtered.map(function(line) {
            // Throw away eval information until we implement stacktrace.js/stackframe#8
            if ((0, $7inJL.default).indexOf(line, " > eval") > -1) line = line.replace(/ line (\d+)(?: > eval line \d+)* > eval\:\d+\:\d+/g, ":$1");
            if ((0, $7inJL.default).indexOf(line, "@") === -1 && (0, $7inJL.default).indexOf(line, ":") === -1) // Safari eval frames only have function names and nothing else
            return {
                function: line
            };
            const tokens = line.split("@");
            const locationParts = this.extractLocation(tokens.pop());
            const functionName = tokens.join("@") || undefined;
            return {
                function: functionName,
                file: locationParts[0],
                line: this._parseInt(locationParts[1]),
                column: this._parseInt(locationParts[2])
            };
        }, this);
    }
    parseOpera(e) {
        if (!e.stacktrace || (0, $7inJL.default).indexOf(e.message, "\n") > -1 && e.message.split("\n").length > e.stacktrace.split("\n").length) return this.parseOpera9(e);
        if (!e.stack) return this.parseOpera10(e);
        return this.parseOpera11(e);
    }
    parseOpera9(e) {
        const lineRE = /Line (\d+).*script (?:in )?(\S+)/i;
        const lines = e.message.split("\n");
        const result = [];
        for(let i = 2, len = lines.length; i < len; i += 2){
            const match = lineRE.exec(lines[i]);
            if (match) result.push({
                file: match[2],
                line: this._parseInt(match[1])
            });
        }
        return result;
    }
    parseOpera10(e) {
        const lineRE = /Line (\d+).*script (?:in )?(\S+)(?:: In function (\S+))?$/i;
        const lines = e.stacktrace.split("\n");
        const result = [];
        for(let i = 0, len = lines.length; i < len; i += 2){
            const match = lineRE.exec(lines[i]);
            if (match) result.push({
                function: match[3] || undefined,
                file: match[2],
                line: this._parseInt(match[1])
            });
        }
        return result;
    }
    // Opera 10.65+ Error.stack very similar to FF/Safari
    parseOpera11(error) {
        const filtered = error.stack.split("\n").filter(function(line) {
            return !!line.match($d9b9ae09465e9a88$export$7ebf908d4310f9e3.FIREFOX_SAFARI_STACK_REGEXP) && !line.match(/^Error created at/);
        }, this);
        return filtered.map(function(line) {
            const tokens = line.split("@");
            const locationParts = this.extractLocation(tokens.pop());
            const functionCall = tokens.shift() || "";
            const functionName = functionCall.replace(/<anonymous function(: (\w+))?>/, "$2").replace(/\([^\)]*\)/g, "") || undefined;
            let argsRaw;
            if (functionCall.match(/\(([^\)]*)\)/)) argsRaw = functionCall.replace(/^[^\(]+\(([^\)]*)\)$/, "$1");
            const args = argsRaw === undefined || argsRaw === "[arguments not available]" ? undefined : argsRaw.split(",");
            return {
                function: functionName,
                file: locationParts[0],
                line: this._parseInt(locationParts[1]),
                column: this._parseInt(locationParts[2])
            };
        }, this);
    }
}
const $d9b9ae09465e9a88$var$defaultErrorParser = new $d9b9ae09465e9a88$export$7ebf908d4310f9e3();
var $d9b9ae09465e9a88$export$2e2bcd8739ae039 = $d9b9ae09465e9a88$var$defaultErrorParser;



var $7inJL = parcelRequire("7inJL");
class $e7c0969cc278f22d$export$87308137e53d8862 extends (0, $brhsV.BaseModule) {
    constructor(config){
        super(config);
        this.VERSION = "0.0.0";
        this.PROJECT_ID = "141580";
        this.PROJECT_KEY = "9a0a3519e930259f5886a7af53b0ccaa";
        this.SENTRY_PROJECT_ID = "1190150";
        this.SENTRY_PUBLIC_KEY = "3c9d467f8a9d4295b0f8320ae852091d";
        this.DEFAULT_CONFIGURATION = {
            environment: "production",
            ignorableErrors: []
        };
        this.configuration = {};
        this.additionalErrorDetails = {};
        this._setup = ()=>{
            super.mergeConfigs(this.DEFAULT_CONFIGURATION, config || window.Demandbase?.Config?.ErrorReporter);
            return this;
        };
        this._setup();
    }
    initialize() {
        super.initialize();
    }
    getNewRequest() {
        let sentryXhttp;
        if (window.XMLHttpRequest) sentryXhttp = new XMLHttpRequest();
        else if (window.ActiveXObject) sentryXhttp = new ActiveXObject("Microsoft.XMLHTTP");
        return sentryXhttp;
    }
    send(error, additionalExtraInfo = {}) {
        // to ignore errors, the ignorableErrors string must exactly match the
        // error name or message
        if ((0, $7inJL.default).indexOf(this.configuration.ignorableErrors, error.name) > -1 || (0, $7inJL.default).indexOf(this.configuration.ignorableErrors, error.message) > -1) return;
        let sentryXhttp = this.getNewRequest();
        const sentryUrl = `https://sentry.io/api/${this.SENTRY_PROJECT_ID}/store/?sentry_version=7&sentry_key=${this.SENTRY_PUBLIC_KEY}`;
        // report to Sentry
        try {
            sentryXhttp.open("POST", sentryUrl, true);
            sentryXhttp.setRequestHeader("Content-type", "text/plain;charset=UTF-8");
            sentryXhttp.send(this.formatMessage(error, true, additionalExtraInfo));
        } catch (requestError) {}
    }
    wrap(method) {
        if (typeof method !== "function") throw new Error(`Invalid Function: ${method}`);
        return (...parameters)=>{
            try {
                // TODO: Temporary fix to silence apply errors until we introduce
                // Raven
                if (typeof method !== "undefined" && typeof method.apply === "function") return method.apply(this, parameters);
            } catch (error) {
                this.send(error);
                (0, $g4dDw.default).alert(`Error: ${error}\n${error.stack}`);
            }
        };
    }
    formatMessage(error, forSentry = false, additionalExtra) {
        const errorDetails = this.parseError(error);
        const context = this.parseContext();
        const environment = this.parseEnviroment();
        const session = this.parseSession();
        const params = this.parseParams();
        const { additionalErrorDetails: additionalErrorDetails } = this;
        if (forSentry) {
            const sentryFormattedError = this.formatErrorForSentry(errorDetails);
            return (0, $7inJL.default).JSON.stringify({
                logger: context.notifier.name,
                platform: "javascript",
                release: context.version,
                environment: context.environment,
                request: {
                    url: context.url
                },
                contexts: {
                    browser: {
                        userAgent: context.userAgent
                    }
                },
                tags: {
                    clientId: environment.config.clientId
                },
                extra: (0, $7inJL.default).assign({}, {
                    readyState: context.readyState,
                    config: environment.config,
                    companyProfile: session,
                    additionalErrorDetails: additionalErrorDetails
                }, additionalExtra),
                exception: {
                    values: [
                        sentryFormattedError
                    ]
                }
            });
        }
        return (0, $7inJL.default).JSON.stringify({
            errors: [
                errorDetails
            ],
            context: context,
            environment: environment,
            session: session,
            params: params
        });
    }
    formatErrorForSentry(errorDetails) {
        const stacktrace = [];
        for (const frame of errorDetails.backtrace)stacktrace.push({
            function: frame.function,
            filename: frame.file,
            lineno: frame.line,
            colno: frame.column
        });
        return {
            type: errorDetails.type,
            value: errorDetails.message,
            stacktrace: {
                frames: stacktrace
            }
        };
    }
    parseError(error) {
        return {
            type: error.name,
            message: error.message,
            backtrace: (0, $d9b9ae09465e9a88$export$2e2bcd8739ae039).parse(error)
        };
    }
    parseContext() {
        return {
            notifier: {
                name: "ErrorReporterModule",
                version: this.VERSION
            },
            environment: this.configuration.environment,
            version: window.Demandbase.version,
            url: window.location.href,
            userAgent: navigator.userAgent,
            rootDirectory: window.location.origin,
            readyState: document.readyState
        };
    }
    // TODO: Functions in Config get parsed out
    parseEnviroment() {
        return {
            config: (0, $31U67.default).dig(window.Demandbase, "Config")
        };
    }
    parseSession() {
        return {
            companyProfile: (0, $31U67.default).dig(window.Demandbase, "IP", "CompanyProfile")
        };
    }
    parseParams() {
        return {};
    }
    // --- STATIC METHODS FOR PARTNER TAG (NO window.Demandbase DEPENDENCY) ---
    /**
   * Send an error to Sentry without referencing window.Demandbase. All context must be provided.
   * @param error The error object to report
   * @param context An object with context fields: { environment, version, url, userAgent, rootDirectory, readyState, [any other fields] }
   * @param extra Optional extra info to include in the Sentry payload
   */ static sendErrorToSentry(error, context, extra = {}) {
        let sentryXhttp;
        if (typeof window !== "undefined" && window.XMLHttpRequest) sentryXhttp = new XMLHttpRequest();
        else if (typeof window !== "undefined" && window.ActiveXObject) sentryXhttp = new ActiveXObject("Microsoft.XMLHTTP");
        else // Not in a browser environment, do nothing
        return;
        const SENTRY_PROJECT_ID = "1190150";
        const SENTRY_PUBLIC_KEY = "3c9d467f8a9d4295b0f8320ae852091d";
        const sentryUrl = `https://sentry.io/api/${SENTRY_PROJECT_ID}/store/?sentry_version=7&sentry_key=${SENTRY_PUBLIC_KEY}`;
        try {
            sentryXhttp.open("POST", sentryUrl, true);
            sentryXhttp.setRequestHeader("Content-type", "text/plain;charset=UTF-8");
            sentryXhttp.send($e7c0969cc278f22d$export$87308137e53d8862.formatErrorForSentryStatic(error, context, extra));
        } catch (requestError) {}
    }
    /**
   * Format an error for Sentry (static, no window.Demandbase dependency)
   * @param error The error object
   * @param context Context object (see sendErrorToSentry)
   * @param extra Optional extra info
   */ static formatErrorForSentryStatic(error, context, extra = {}) {
        // Use ErrorStackParser if available, else fallback
        let backtrace = [];
        try {
            backtrace = (0, $d9b9ae09465e9a88$export$2e2bcd8739ae039).parse(error);
        } catch (e) {
            // fallback: minimal frame
            backtrace = [
                {
                    function: error.name,
                    file: "",
                    line: 0,
                    column: 0
                }
            ];
        }
        const stacktrace = backtrace.map((frame)=>({
                function: frame.function,
                filename: frame.file,
                lineno: frame.line,
                colno: frame.column
            }));
        const sentryFormattedError = {
            type: error.name,
            value: error.message,
            stacktrace: {
                frames: stacktrace
            }
        };
        return (0, $7inJL.default).JSON.stringify({
            logger: "PartnerTag",
            platform: "javascript",
            release: context.version,
            environment: context.environment,
            request: {
                url: context.url
            },
            contexts: {
                browser: {
                    userAgent: context.userAgent
                }
            },
            tags: context.tags || {},
            exception: {
                values: [
                    sentryFormattedError
                ]
            }
        });
    }
    /**
   * Wrap a function so that any errors are reported to Sentry using the static method.
   * @param fn The function to wrap
   * @param context The context object to pass to Sentry
   * @param extra Optional extra info to include in the Sentry payload
   */ static wrapForSentry(fn, context, extra = {}) {
        return function(...args) {
            try {
                const result = fn.apply(this, args);
                if (result && typeof result.then === "function") // It's a Promise, attach a catch handler for async errors
                return result.catch((error)=>{
                    $e7c0969cc278f22d$export$87308137e53d8862.sendErrorToSentry(error, context, extra);
                    throw error; // rethrow so caller can handle if needed
                });
                return result;
            } catch (error) {
                $e7c0969cc278f22d$export$87308137e53d8862.sendErrorToSentry(error, context, extra);
            }
        };
    }
}
const $e7c0969cc278f22d$var$defaultErrorReporterModule = new $e7c0969cc278f22d$export$87308137e53d8862();
var $e7c0969cc278f22d$export$2e2bcd8739ae039 = $e7c0969cc278f22d$var$defaultErrorReporterModule;






(function(global, factory) {
    if (!global.DemandbasePartnerTag) global.DemandbasePartnerTag = {};
    $548914322ea4771d$exports = factory((parcelRequire("g4dDw")), (parcelRequire("7VWOe")), (parcelRequire("a3Qp1")), (parcelRequire("46JbE")));
})(typeof self !== "undefined" ? self : undefined, function(logger, EmailDomainReporterModule, AdvertisingModule, IpApiUtilities) {
    logger = logger && logger.default || logger;
    EmailDomainReporterModule = EmailDomainReporterModule && EmailDomainReporterModule.default || EmailDomainReporterModule;
    AdvertisingModule = AdvertisingModule && AdvertisingModule.default || AdvertisingModule;
    IpApiUtilities = IpApiUtilities && IpApiUtilities.default || IpApiUtilities;
    const DEFAULT_CONFIG = {
        advertising: {
            enableBW: true,
            enableLR: true,
            enableIX: true,
            enableMCTV: true,
            enableRP: true,
            enableSmartPixel: true,
            smarPixelURL: `https://s.company-target.com/s/sync`,
            lrAdPixelURL: "https://id.rlcdn.com/464526.gif"
        },
        emailDomainReporter: {
            enableEmailDomainReporter: true
        }
    };
    class DemandbasePartnerTagModule {
        constructor(config = {}, auth){
            this.hasFired = false;
            this.version = "0.0.2";
            if (!auth) throw new Error("DemandbasePartnerTagModule: 'auth' key is required for instantiation.");
            this.auth = auth;
            this.initializeModules(this.normalizeConfig(config));
        }
        normalizeConfig(config) {
            const normalizedConfig = JSON.parse(JSON.stringify(DEFAULT_CONFIG));
            function buildFlatToNestedMap(obj, path = []) {
                let map = {};
                Object.keys(obj).forEach((key)=>{
                    if (typeof obj[key] === "object" && obj[key] !== null && !Array.isArray(obj[key])) Object.assign(map, buildFlatToNestedMap(obj[key], path.concat(key)));
                    else {
                        // Only map booleans and primitive config keys
                        const flatKey = (path.length ? path[path.length - 1] : "") + key.charAt(0).toUpperCase() + key.slice(1);
                        map[key.toLowerCase()] = [
                            path[path.length - 1] || "",
                            key
                        ];
                        // Also support enable-style keys (e.g., enableBW)
                        if (key.startsWith("enable")) map[key.toLowerCase()] = [
                            path[path.length - 1] || "",
                            key
                        ];
                    }
                });
                return map;
            }
            // Build the map from DEFAULT_CONFIG
            const flatToNestedMap = buildFlatToNestedMap(DEFAULT_CONFIG);
            const adKeys = Object.keys(DEFAULT_CONFIG.advertising).filter((k)=>k.startsWith("enable") && k !== "enableSmartPixel");
            if (typeof config === "object") {
                // Check if SmartPixel is explicitly set to false
                const smartPixelExplicitlyOff = Object.keys(config).some((k)=>k.toLowerCase() === "enablesmartpixel" && config[k] === false);
                if (smartPixelExplicitlyOff) // If SmartPixel is off, all ad configs are off
                Object.keys(normalizedConfig.advertising).forEach((key)=>{
                    if (typeof normalizedConfig.advertising[key] === "boolean") normalizedConfig.advertising[key] = false;
                });
                else {
                    // If any ad config (except SmartPixel) is provided, set all others to false
                    const providedAdKeys = adKeys.filter((key)=>Object.keys(config).map((k)=>k.toLowerCase()).includes(key.toLowerCase()));
                    if (providedAdKeys.length > 0) adKeys.forEach((key)=>{
                        normalizedConfig.advertising[key] = false;
                    });
                }
                // Apply explicit config values
                Object.keys(config).forEach((key)=>{
                    const lowerKey = key.toLowerCase();
                    if (flatToNestedMap[lowerKey]) {
                        const [section, nestedKey] = flatToNestedMap[lowerKey];
                        // If SmartPixel is off, all ad configs must remain false
                        if (section === "advertising" && smartPixelExplicitlyOff) normalizedConfig[section][nestedKey] = false;
                        else normalizedConfig[section][nestedKey] = config[key];
                    }
                });
                // SmartPixel and emailDomainReporter are always on unless explicitly set to false
                if (!smartPixelExplicitlyOff) normalizedConfig.advertising.enableSmartPixel = true;
                if (!Object.keys(config).some((k)=>k.toLowerCase() === "enableemaildomainreporter" && config[k] === false)) normalizedConfig.emailDomainReporter.enableEmailDomainReporter = true;
            }
            return normalizedConfig;
        }
        initializeModules(config) {
            this.config = config;
            // Initialize modules with normalized config
            this.Advertising = new AdvertisingModule(config.advertising);
            if (config.emailDomainReporter.enableEmailDomainReporter) this.EmailDomainReporter = new EmailDomainReporterModule(config.emailDomainReporter);
        }
        async fire() {
            logger.log("Firing PartnerTag");
            // TEST: Throw an error to verify Sentry error reporting
            if (!this.hasFired) {
                this.Advertising._setup();
                this.Advertising.initialize();
                if (this.EmailDomainReporter) {
                    logger.log("EmailDomainReporterModule initializing");
                    this.EmailDomainReporter._setup();
                    this.EmailDomainReporter.initialize();
                    logger.log("EmailDomainReporterModule initialized");
                }
                this.hasFired = true;
            } else logger.log("PartnerTag already initialized, skipping module setup.");
            const request = IpApiUtilities.getNewRequest();
            const url = "https://api.company-target.com/api/v3/ip.json";
            // Use auth from private variable if present, otherwise default to 'n/a'
            const params = {
                src: "partner-tag",
                auth: this.auth
            };
            return new Promise((resolve, reject)=>{
                IpApiUtilities.fireRequest({
                    request: request,
                    url: url,
                    params: params,
                    responseHandler: (req)=>{
                        logger.log("IP API response: " + req?.status);
                        try {
                            if (req && req.readyState === 4 && req.status === 200 && req.responseText) {
                                const data = JSON.parse(req.responseText);
                                resolve(data);
                            } else if (req && req.readyState === 4) // Request finished but not 200, resolve with null or error info
                            resolve(null);
                        // Otherwise, do nothing (wait for readyState 4)
                        } catch (e) {
                            reject(e);
                        }
                    },
                    isIgnorableDevice: ()=>false,
                    triggerCallback: true
                });
            });
        }
        // Static method to get configuration from script tag
        static getScriptConfig() {
            const config = {};
            // Try to find our script tag - handle both regular and module scripts
            let scriptElement = null;
            // First try using currentScript (works for regular scripts during loading)
            if (document.currentScript) scriptElement = document.currentScript;
            if (scriptElement) {
                // Extract all data attributes
                const attributes = scriptElement.attributes;
                // Dynamically get all enable* keys from DEFAULT_CONFIG (in original case)
                const enableKeys = Object.keys(DEFAULT_CONFIG.advertising).filter((k)=>k.startsWith("enable")).concat(Object.keys(DEFAULT_CONFIG.emailDomainReporter).filter((k)=>k.startsWith("enable")));
                // Build a map of lower-case enable keys to their canonical form
                const enableKeyMap = {};
                enableKeys.forEach((k)=>{
                    enableKeyMap[k.toLowerCase()] = k;
                });
                for(let i = 0; i < attributes.length; i++){
                    const attr = attributes[i];
                    if (attr.name.startsWith("data-")) {
                        // Convert data-enable-bw to enableBW (preserve correct casing)
                        const rawKey = attr.name.substring(5).replace(/-([a-z])/g, (g)=>g[1].toUpperCase());
                        const canonicalKey = enableKeyMap[rawKey.toLowerCase()];
                        if (canonicalKey) config[canonicalKey] = attr.value === "true";
                    } else if (enableKeyMap[attr.name.toLowerCase()]) // Also support direct attribute names (legacy)
                    config[enableKeyMap[attr.name.toLowerCase()]] = attr.value === "true";
                }
            }
            return config;
        }
    }
    // Auto-initialization for browser globals
    if (typeof document !== "undefined") {
        // Setup the global namespace if needed
        if (!window.DemandbasePartnerTag) window.DemandbasePartnerTag = {};
        // Get configuration from multiple sources with priority:
        // 1. Existing window.DemandbasePartnerTag.config (pre-configured)
        // 2. Script tag attributes
        // 3. Auth from window.DemandbasePartnerTag.auth (not from config)
        const partnerTagGlobal = window.DemandbasePartnerTag;
        const existingConfig = partnerTagGlobal.config || {};
        const scriptConfig = DemandbasePartnerTagModule.getScriptConfig();
        // Merge configs (script tag attributes lowest priority)
        const mergedConfig = {
            ...scriptConfig,
            ...existingConfig
        };
        // Ingest auth ONLY from window.DemandbasePartnerTag.auth (not from config or script tag attributes)
        const auth = typeof partnerTagGlobal.auth !== "undefined" ? partnerTagGlobal.auth : undefined;
        // Store the config
        window.DemandbasePartnerTag.config = mergedConfig;
        // Create and initialize the instance, passing auth separately
        const instance = new DemandbasePartnerTagModule(mergedConfig, auth);
        window.DemandbasePartnerTag.version = instance.version;
        // Build the context for Sentry reporting
        const sentryContext = {
            environment: mergedConfig.environment || "production",
            version: instance.version,
            url: window.location.href,
            userAgent: navigator.userAgent,
            rootDirectory: window.location.origin,
            readyState: document.readyState
        };
        // Wrap the fire method with error reporting (no global, no require)
        window.DemandbasePartnerTag.fire = (0, $e7c0969cc278f22d$export$87308137e53d8862).wrapForSentry(instance.fire.bind(instance), sentryContext);
    }
    // Return the class definition
    return DemandbasePartnerTagModule;
});

})();
//# sourceMappingURL=partnerTag.js.map
