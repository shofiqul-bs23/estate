import odoo.odoo.fields
from odoo import fields, models , api
#from odoo.odoo import fields
from dateutil.relativedelta import relativedelta
def getThreeMonthLaterDate():
    return fields.Date.today() + relativedelta(months=3)



class EstateProperty(models.Model):
    _name = 'estate.property'
    _description = 'This is the basic model to hold information about the property.'

    name = fields.Char(required = True)
    description = fields.Text()
    postcode = fields.Char()
    # date_availability = fields.Date(copy=False,default= fields.Date(default=lambda record: fields.Date.today() + relativedelta(days=30)))
    # date_availability = fields.Date(default=lambda record: fields.Date.today() + relativedelta(months=3))
    date_availability = fields.Date(default = getThreeMonthLaterDate())
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

    property_type_id = fields.Many2one('estate.property.type')
    # salesperson_id = fields.Many2one('')
    salesperson_id = fields.Many2one('res.users', string='Salesperson', index=True, tracking=True, default=lambda self: self.env.user)
    buyer_id = fields.Many2one('res.partner', string='Buyer', index=True, tracking=True)

    tag_ids = fields.Many2many('estate.property.tag')

    offer_ids = fields.One2many('estate.property.offer','property_id',string='Offers')

    total_area = fields.Float(compute = '_compute_total_area')

    best_offer = fields.Float(compute = '_compute_best_offer')


    @api.depends('living_area', 'garden_area')
    def _compute_total_area(self):
        for record in self:
            record.total_area = record.living_area + record.garden_area

    @api.depends('offer_ids')
    def _compute_best_offer(self):
        for record in self:
            if len(record.offer_ids.mapped('price')):
                record.best_offer = max(record.offer_ids.mapped('price'))
            else:
                record.best_offer = 0

    @api.onchange('garden')
    def _onchange_garden(self):
        if self.garden == True:
            self.garden_orientation='north'
            self.garden_area = 10
        else:
            self.garden_orientation = ''
            self.garden_area = 0



