# -*- coding: utf-8 -*-
###############################################################################
#
#    OpenEduCat Inc
#    Copyright (C) 2009-TODAY OpenEduCat Inc(<https://www.openeducat.org>).
#
#    This program is free software: you can redistribute it and/or modify
#    it under the terms of the GNU Lesser General Public License as
#    published by the Free Software Foundation, either version 3 of the
#    License, or (at your option) any later version.
#
#    This program is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU Lesser General Public License for more details.
#
#    You should have received a copy of the GNU Lesser General Public License
#    along with this program.  If not, see <http://www.gnu.org/licenses/>.
#
###############################################################################

from odoo import models, fields, api,_


class OpFaculty(models.Model):
    _inherit = 'op.faculty'

    session_ids = fields.Many2many(
        'op.session', compute='_compute_session_ids', string='Sessions')

    session_count = fields.Integer(
        string='Session Count', compute='_compute_session_count')

    def _compute_session_ids(self):
        for faculty in self:
            # Search for sessions where the faculty is part of faculty_ids
            faculty.session_ids = self.env['op.session'].search([('faculty_ids', 'in', faculty.id)])

    def _compute_session_count(self):
        for faculty in self:
            # Count the number of sessions related to the faculty
            faculty.session_count = len(faculty.session_ids)

    def count_sessions_details(self):
        self.ensure_one()
        return {
            'type': 'ir.actions.act_window',
            'name': _('Sessions'),
            'res_model': 'op.session',
            'view_mode': 'tree,form',
            'domain': [('faculty_ids', 'in', self.id)],
            'context': dict(self.env.context, default_faculty_ids=[self.id]),
            'target': 'current',
        }



