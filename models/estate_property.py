import odoo.odoo.fields
from odoo import fields, models
#from odoo.odoo import fields
from dateutil.relativedelta import relativedelta

class EstateProperty(models.Model):
    _name = 'estate.property'
    _description = 'This is the basic model to hold information about the property.'

    name = fields.Char(required = True)
    description = fields.Text()
    postcode = fields.Char()
    # date_availability = fields.Date(copy=False,default= fields.Date(default=lambda record: fields.Date.today() + relativedelta(days=30)))
    date_availability = fields.Date(default=lambda record: fields.Date.today() + relativedelta(months=3))
    expected_price = fields.Float(required = True)
    selling_price = fields.Float(readonly=True, copy=False)
    bedrooms = fields.Integer(default=2)
    living_area = fields.Integer()
    facades = fields.Integer()
    garage = fields.Boolean()
    garden = fields.Boolean()
    garden_area = fields.Integer()
    garden_orientation = fields.Selection(
        selection=[("north",'North'),('south',"South"),('east','East'),('west','West')]
    )
    active = fields.Boolean(default=True)
    state = fields.Selection(
        required = True,
        selection = [
            ('new',"New"),('offer_received',"Offer Received"),('offer_accepted','Offer Accepted'),
            ('sold','Sold'),('canceled','Canceled')
        ]
    )

