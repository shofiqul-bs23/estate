import odoo
from odoo import fields, models, api


class ResUsers(models.Model):
    _inherit = 'res.users'

    # salesperson_id
    property_ids = fields.One2many("estate.property", "salesperson_id")
    test = fields.Char(default="TESTING TESTING TESTING")
