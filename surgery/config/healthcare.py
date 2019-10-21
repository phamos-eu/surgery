from __future__ import unicode_literals
from frappe import _

def get_data():

	return [
		{
			"label": _("Surgery"),
			"icon": "icon-star",
			"items": [
				{
					"type": "doctype",
					"name": "Surgery Report",
					"label": _("Surgery Report"),
					"description": _("Surgery Report")
				},
				{
					"type": "doctype",
					"name": "Surgery Body Part",
					"label": _("Body Part"),
					"description": _("Surgery Body Part")
				},
				{
					"type": "doctype",
					"name": "Surgery",
					"label": _("Surgery"),
					"description": _("Surgery")
				},
				{
					"type": "doctype",
					"name": "Attitude",
					"label": _("Attitude"),
					"description": _("Attitude")
				}
			]
		}
	]
