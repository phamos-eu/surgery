// Copyright (c) 2019, tüit GmbH and contributors
// For license information, please see license.txt

frappe.ui.form.on('Surgery Report', {
	refresh: function(frm) {
		// filter for diagnosis based on side data- and surgery body part link-field
		cur_frm.fields_dict['diagnosis'].get_query = function(doc) {
			 return {
				 filters: {
					 "side": cur_frm.doc.side,
					 "body_part": cur_frm.doc.body_part
				 }
			 }
		}
	}
});