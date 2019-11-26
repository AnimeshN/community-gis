map = L.map('map', {
    center:[19.8480, 74.1090], 
    zoom:12,
    zoomControl:false, 
    attributionControl:false,
    messagebox: true,
    contextmenu: true,
    measureControl: true
  });
map.messagebox.options.timeout = 5000;
map.messagebox.setPosition("bottomright");
lyrOSM = L.tileLayer.provider('OpenStreetMap.Mapnik');
lyrOSM2 = L.tileLayer.provider('OpenStreetMap.Mapnik');
lyrImagery = L.tileLayer.provider('Esri.WorldImagery');
map.addLayer(lyrOSM);
objBasemaps = {
  "Open Street Maps": lyrOSM,
  "Imagery":lyrImagery
};
objOverlays = {
};
var ctlLayers = L.control.layers(objBasemaps, objOverlays).addTo(map);
// var ctlPan = L.control.pan().addTo(map);
// var ctlZoomslider = L.control.zoomslider({position:'topright'}).addTo(map);
ctlAttribute = L.control.attribution({position:'bottomright'}).addTo(map);
ctlAttribute.addAttribution('&copy; <a href="http://www.makerghat.org">makerGHAT</a>');
var miniMap = new L.Control.MiniMap(lyrOSM2, { toggleDisplay: true }).addTo(map);
