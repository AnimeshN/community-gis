/** Base configuration for map and layer preview These are maps are shown embedded in geonode */
var MS2_BASE_PLUGINS = {
	"desktop": [
		{
			"name": "Map",
			"cfg": {
				"tools": ["locate", "measurement","draw"],
				"mapOptions": {
					"openlayers": {
						"interactions": {
							"pinchRotate": false,
							"altShiftDragRotate": false
						}
					},
					"leaflet": {
						"attribution": {
							"container": "#mapstore-map-footer-container"
						}
					}
				}
			}
		},
		{
			"name": "BackgroundSelector",
			"cfg": {
				"style": {
					"bottom": 0,
					"marginBottom": 25
				},
				"dimensions": {
					"side": 65,
					"sidePreview": 65,
					"frame": 3,
					"margin": 5,
					"label": false,
					"vertical": true,
				}
			}
		},
		
		{
			"name": "Identify",
			"cfg": {
				"showFullscreen": false,
				"dock": true,
				"position": "right",
				"size": 0.4,
				"fluid": true,
				"viewerOptions": {
					"container": "{context.ReactSwipe}"
				}
			},
			"override": {
				"Toolbar": {
					"position": 11,
					"alwaysVisible": false
				}
			}
		},
		{
			"name": "TOC",
			"cfg": {
				"activateMapTitle": false,
				"activateSettingsTool": false,
				"activateMetedataTool": false,
				"activateRemoveLayer": false
			}

		}, {
			"name": "Settings",
			"cfg": {
				"wrap": true
			}
		}, {
			"name": "Toolbar",
			"id": "NavigationBar",
			"cfg": {
				"id": "navigationBar",
				"layout": "horizontal"
			}
		}, {
			"name": "MapLoading",
			"override": {
				"Toolbar": {
					"alwaysVisible": true
				}
			}
		},
		"DrawerMenu", "Cookie", "OmniBar", "Expander", "Undo", "Redo",
        "BurgerMenu", "MapFooter", "Measure",
        {
			"name": "Print",
			"cfg": {
				"useFixedScales": true
			}
		},
		{
			"name": "ZoomAll",
			"override": {
				"Toolbar": {
					"alwaysVisible": false
				}
			}
		},
		{
			"name": "ZoomIn",
			"override": {
				"Toolbar": {
					"alwaysVisible": true
				}
			}
		},
		{
			"name": "ZoomOut",
			"override": {
				"Toolbar": {
					"alwaysVisible": true
				}
			}
		}, {
			"name":"Timeline",
			"cfg": {
				"style": {
						"marginBottom": 30,
						"marginLeft": 80,
						"marginRight": 45
					},
					"compact": true
				}
		}, "Playback"
	]
}
