from odoo import fields, models


class EstatePropertyType(models.Model):
    _name = 'estate.property.type'
    _description = 'Contain the type of the properties'
    _order = 'sequence, name'

    sequence = fields.Integer('Sequence', default=1, help="Used to order property type")

    name = fields.Char(required=True)
    property_ids = fields.One2many('estate.property','property_type_id')

    _sql_constraints = [
        ('check_unique_type',"unique (name)","Property type must be unique.")
    ]

