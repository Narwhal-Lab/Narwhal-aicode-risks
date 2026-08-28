if (typeof ui === 'undefined') {
  var ui = {};
}

ui.gmaps = {

  isInited: false,

  mapStyles: [
    {
      featureType: "all",
      "stylers": [
        { "visibility": "on" },
        { "hue": "#0044ff" },
        { "saturation": -80 }
      ]
    },
    {
      "featureType": "road.arterial",
      "stylers": [
        { "visibility": "on" },
        { "color": "#ffffff" }
      ]
    },
    {
      "featureType": "water",
      "stylers": [
        {"color": "#d1dbe1"},
        {"visibility": "on"}
      ]
    },
    {
      "featureType": "water",
      "elementType": "labels.text.fill",
      "stylers": [
        { "color": "#456184" }
      ]
    },
    {
      "featureType": "water",
      "elementType": "labels.text.stroke",
      "stylers": [
        { "weight": 2 }
      ]
    }
  ],

  _callback: function() {
    var map,
      mapNodes = document.querySelectorAll('.map'),
      mapNode = null,
      mapOptions,
      center, coordsFromNode,
      zoom,
      markersNodes, markerNode, marker;

    for (var i = 0; i < mapNodes.length; i++) {
      mapNode = mapNodes[i];
      markersNodes = mapNode.querySelectorAll('.map-marker');
      mapOptions = {};

      // Center
      mapOptions.coords = mapNode.getAttribute('data-coords')
        ? mapNode.getAttribute('data-coords').split(',')
        : null;

      // Zoom
      mapOptions.zoom = Number(mapNode.getAttribute('data-zoom'));

      map = ui.gmaps.createMap(mapNode, mapOptions);

      // Markers
      if (markersNodes.length > 0) {
        for (var j = 0; j < markersNodes.length; j++) {
          markerNode = markersNodes[j];
          marker = {};

          // Coordinates
          marker.coords = markerNode.getAttribute('data-coords')
            ? markerNode.getAttribute('data-coords').split(',')
            : mapOptions.coords;

          marker.text = markerNode.getAttribute('data-text')
            ? markerNode.getAttribute('data-text')
            : null;

          ui.gmaps.createMapMarker(map, marker);
        }
      }
    }
  },

  init: function(opts) {
    var that = this,
      key = opts.apiKey,
      sensor = (typeof opts.sensor !== 'undefined') ? opts.sensor : false,
      callback = (typeof opts.callback !== 'undefined') ? opts.callback : this._callback,
      callbackName,
      callbackWrapper,
      scriptSrc;

    callbackName = '__gMapInit_';
    scriptSrc = '//maps.googleapis.com/maps/api/js?key='+ key +'&sensor=' + (sensor).toString();
    scriptSrc += '&callback=' + callbackName;

    callbackWrapper = function() {
      that.isInited = true;
      if (callback !== null) {
        callback.call(this);
      }
    };

    window[callbackName] = callbackWrapper;

    // Load script
    var script = document.createElement('script');
    script.type = 'text/javascript';
    script.src = scriptSrc;
    document.body.appendChild(script);
  },

  createMap: function(node, options) {
    var map,
      gmaps = google.maps,
      mapOptions,
      mapStyles = this.mapStyles,
      coords = options.coords;

    if (coords === null) {
      coords = [];
    }

    mapOptions = {
      center: new gmaps.LatLng(coords[0], coords[1]),
      zoom: options.zoom,
      mapTypeId: gmaps.MapTypeId.ROADMAP,
      scrollwheel: false,
      disableDefaultUI: true,
      zoomControl: true
    };

    map = new gmaps.Map(node, mapOptions);
    map.setOptions({styles: mapStyles});

    return map;
  },

  createMapMarker: function(map, options) {
    var infoWindow = null,
      marker = null,
      gmaps = gmaps = google.maps;

    infoWindow = new gmaps.InfoWindow();

    marker = new gmaps.Marker({
      map: map,
      position: new gmaps.LatLng(options.coords[0], options.coords[1])
      //icon: options.markerImages
    });

    if (options.text) {
      gmaps.event.addListener(marker, 'click', function() {
        var balloonText = '';
        balloonText += '<div class="map-marker-info-window">';
        balloonText += '<div class="text">' + options.text + '</div>';
        balloonText += '</div>';
        infoWindow.setContent(balloonText);
        infoWindow.open(map, marker);
      });

      /*
      gmaps.event.addListener(marker, 'mouseover', function() {
          marker.setIcon(options.markerImageHover);
      });

      gmaps.event.addListener(marker, 'mouseout', function() {
          marker.setIcon(options.markerImage);
      });
      */
    }
  }
};