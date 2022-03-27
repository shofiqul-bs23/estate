from odoo import fields, models, api
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


