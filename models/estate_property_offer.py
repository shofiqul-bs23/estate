from odoo import fields, models


class EstatePropertyType(models.Model):
    _name = 'estate.property.offer'
    _description = 'Contain the offers that has been given to property'

    price = fields.Float()
    status = fields.Selection(copy=False,
                              selection=[("accepted",'Accepted'),('refused',"Refused")]
                              )
    partner_id = fields.Many2one('res.partner', required = True)
    property_id = fields.Many2one('estate.property', required = True)
