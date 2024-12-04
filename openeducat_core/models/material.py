from odoo import fields,models


class OpMaterial(models.Model):
    _name = 'op.material'

    name = fields.Char('Material',required=True)



