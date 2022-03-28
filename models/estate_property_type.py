from odoo import fields, models


class EstatePropertyType(models.Model):
    _name = 'estate.property.type'
    _description = 'Contain the type of the properties'

    name = fields.Char(required=True)

    _sql_constraints = [
        ('check_unique_type',"unique (name)","Property type must be unique.")
    ]

