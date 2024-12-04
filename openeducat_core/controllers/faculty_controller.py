# -*- coding: utf-8 -*-
from odoo import http
from odoo.http import request


class FacultyController(http.Controller):

    @http.route(['/faculty/join'], type='http', auth="public", website=True)
    def faculty_join_form(self, **post):
        # Render the form template
        return request.render("openeducat_core.template_faculty_form")

    @http.route(['/faculty/submit'], type='http', auth="public", website=True, methods=['POST'])
    def faculty_form_submit(self, **post):
        title_id = post.get('title')

        first_name = post.get('first_name')
        middle_name = post.get('middle_name')
        last_name = post.get('last_name')
        blood_group = post.get('blood_group')
        nationality = post.get('nationality')
        birth_date = post.get('birth_date')
        gender = post.get('gender')

        street = post.get('street')
        street2 = post.get('street2')
        city = post.get('city')
        state_id = post.get('state_id')  # Assuming you have state logic
        zip = post.get('zip')
        country_id = post.get('country_id')
        phone = post.get('phone')
        email = post.get('email')

        partner_vals = {
            'name': f"{first_name} {middle_name} {last_name}",
            'title': title_id,
            'email': email,
            'phone': phone,
            'street': street,
            'street2': street2,
            'city': city,
            'zip': zip,
            'country_id': country_id,
            'state_id': state_id,  # You may need to adjust this to use a record ID
        }

        partner = request.env['res.partner'].sudo().create(partner_vals)

        faculty_vals = {
            'first_name':first_name,
            'middle_name':middle_name,
            'name': f"{first_name} {middle_name} {last_name}",
            'birth_date': birth_date,
            'gender': gender,
            'blood_group': blood_group,
            'nationality': nationality,
            'partner_id': partner.id,  # Link faculty record to the partner
            'last_name': last_name,  # Ensure last_name is included here
        }
        request.env['op.faculty'].sudo().create(faculty_vals)

        # Redirect to thank you page
        return request.render('openeducat_core.faculty_thank_you')
