from __future__ import unicode_literals
from frappe import _

def get_data():
	return [
		{
			"label": _("Acquisition"),
			"items": [
				{
					"type": "doctype",
					"name": "Purchase Order",
				},
				{
					"type": "doctype",
					"name": "Supplier",
				},
			]
		},
		{
			"label": _("Supplychain Pipeline"),
			"items": [
				{
					"type": "doctype",
					"name": "Purchase of New Empty Cylinders",
				},
				{
					"type": "doctype",
					"name": "Gas Purchase Order",
				},
				{
					"type": "doctype",
					"name": "Cylinder Retrieval",
				},
				{
					"type": "doctype",
					"name": "Cylinder Sales",
				},
			]
		},
		{
			"label": _("Distribution"),
			"items": [
				{
					"type": "doctype",
					"name": "Sales Order"
				},
				{
					"type": "doctype",
					"name": "Customer"
				},
			]
		},
	]