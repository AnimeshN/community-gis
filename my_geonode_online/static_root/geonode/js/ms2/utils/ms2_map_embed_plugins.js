// needs base_plugins.js
var MS2_EMBED_PLUGINS = {
	"desktop": [ 
		// Map, BackgroundSelector, Identify from base
    {
		"name": "TOC",
		"cfg": {
			"activateQueryTool": false,
			"activateAddLayerButton": false,
            "activateMetedataTool": false,
            "activateSettingsTool": false,
            "activateRemoveLayer": false,
            "activateFilterLayer": false,
			"spatialOperations": [
				{ "id": "INTERSECTS", "name": "queryform.spatialfilter.operations.intersects" },
				{ "id": "BBOX", "name": "queryform.spatialfilter.operations.bbox" },
				{ "id": "CONTAINS", "name": "queryform.spatialfilter.operations.contains" },
				{ "id": "WITHIN", "name": "queryform.spatialfilter.operations.within" }
			],
			"spatialMethodOptions": [
				{ "id": "Viewport", "name": "queryform.spatialfilter.methods.viewport" },
				{ "id": "BBOX", "name": "queryform.spatialfilter.methods.box" },
				{ "id": "Circle", "name": "queryform.spatialfilter.methods.circle" },
				{ "id": "Polygon", "name": "queryform.spatialfilter.methods.poly" }
			]
		}

	},
		// Setting, Toolbar, MapLoading, DrawerMenu, Cookie, OmniBar, Expander,
		// Undo, Redo, BurgerMenu, MapFooter, Measure, Print
		// ZoomAll, ZoomIn, ZoomOut from base
	"Widgets", "Notifications"
	]
}
