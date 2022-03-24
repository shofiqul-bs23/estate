from odoo import fields, models


class EstatePropertyTag(models.Model):
    _name = 'estate.property.tag'
    _description = 'Contains tag for properties.'

    name = fields.Char(required=True)
