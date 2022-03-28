from odoo import fields, models, api
import odoo
from dateutil.relativedelta import relativedelta


class EstatePropertyOffer(models.Model):
    _name = 'estate.property.offer'
    _description = 'Contain the offers that has been given to property'

    price = fields.Float()
    status = fields.Selection(copy=False,
                              selection=[("accepted",'Accepted'),('refused',"Refused")]
                              )
    partner_id = fields.Many2one('res.partner', required = True)
    property_id = fields.Many2one('estate.property', required = True)

    validity = fields.Integer(default = 7)
    date_deadline = fields.Date(compute = '_calculate_date_deadline', inverse = '_inverse_date_deadline')

    _sql_constraints = [
        ('check_offer_price','CHECK(price > 0)','Offer price must be strictly positive.')
    ]


    @api.depends('validity','create_date')
    def _calculate_date_deadline(self):
        for record in self:
            if record.create_date:
                record.date_deadline = fields.Date.add(record.create_date, days=record.validity)
            else:
                record.date_deadline = fields.Date.add(fields.Datetime.now(),days=record.validity)

    def _inverse_date_deadline(self):
        for record in self:
            date_deadline_datetime = record.date_deadline
            # date_str = date_deadline_datetime.strftime("%m/%d/%Y")
            # print(date_str)
            create_date_datetime = record.create_date.date()
            # date_str = create_date_datetime.strftime("%m/%d/%Y")
            # print(date_str)
            delta = date_deadline_datetime - create_date_datetime

            record.validity = delta.days

    def offer_accept(self):
        for record in self:
            if record.status != 'refused' and record.property_id.state in ['new','offer_received']:
                record.status = "accepted"
                record.property_id.selling_price = record.price
                record.property_id.buyer_id = record.partner_id
                record.property_id.state = 'offer_accepted'
            else:
                raise odoo.exceptions.UserError("The offer has been rejected before or The Property is no longer available.")
        return True

    def offer_reject(self):
        for record in self:
            if record.status != 'accepted':
                record.status = "refused"
            else:
                raise odoo.exceptions.UserError("The offer has already been accepted!")
        return True


