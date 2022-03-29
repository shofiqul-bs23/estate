from odoo import fields, models


class EstatePropertyTag(models.Model):
    _name = 'estate.property.tag'
    _description = 'Contains tag for properties.'
    _order = 'name'

    name = fields.Char(required=True)
    Color = fields.Integer()

    _sql_constraints = [
        ('check_unique_tag', "unique (name)", "Property tag must be unique.")
    ]