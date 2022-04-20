from odoo import fields, models, api
import odoo
from dateutil.relativedelta import relativedelta


class EstatePropertyOffer(models.Model):
    _name = 'estate.property.offer'
    _description = 'Contain the offers that has been given to property'
    _order = 'price desc'
    price = fields.Float()
    status = fields.Selection(copy=False,
                              selection=[("accepted", 'Accepted'), ('refused', "Refused")]
                              )
    partner_id = fields.Many2one('res.partner', required=True)
    property_id = fields.Many2one('estate.property', required=True)

    validity = fields.Integer(default=7)
    date_deadline = fields.Date(compute='_calculate_date_deadline', inverse='_inverse_date_deadline')
    property_type_id = fields.Many2one(related='property_id.property_type_id',
                                       store=True)

    _sql_constraints = [
        ('check_offer_price', 'CHECK(price > 0)', 'Offer price must be strictly positive.')
    ]

    @api.depends('validity', 'create_date')
    def _calculate_date_deadline(self):
        for record in self:
            if record.create_date:
                record.date_deadline = fields.Date.add(record.create_date, days=record.validity)
            else:
                record.date_deadline = fields.Date.add(fields.Datetime.now(), days=record.validity)

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
            if record.status != 'refused' and record.property_id.state in ['new',
                                                                           'offer_received','offer_accepted'] and record.property_id.num_accepted_property < record.property_type_id.num_can_accept:
                record.property_id.num_accepted_property += 1
                record.status = "accepted"
                record.property_id.selling_price = record.price
                record.property_id.buyer_id = record.partner_id
                record.property_id.state = 'offer_accepted'

                # record.property_id.offer_id_accepted.create([{
                #     'price': record.price,
                #     'status' : record.status,
                #     'partner_id': record.partner_id.id,
                #     'property_id': record.property_id.id,
                #     'validity': record.validity,
                #     'date_deadline': record.date_deadline,
                #     'property_type_id': record.property_type_id.id
                # }])

                temp = self.env['estate.property.offer'].create([{
                    'price': record.price,
                    'status' : record.status,
                    'partner_id': record.partner_id.id,
                    # 'property_id': record.property_id.id,
                    'property_id': 16,
                    'validity': record.validity,
                    'date_deadline': record.date_deadline,
                    'property_type_id': record.property_type_id.id
                }])

                current_ids = []
                current_ids = record.property_id.offer_id_accepted.ids
                current_ids = current_ids+temp.ids
                current_ids
                record.property_id.offer_id_accepted = [(6,0,current_ids)]
                1
                # t = record.property_id.offer_id_accepted.create([{
                #
                #         'price': record.price,
                #         'status' : record.status,
                #         'partner_id': record.partner_id.id,
                #         'property_id': record.property_id.id,
                #         'validity': record.validity,
                #         'date_deadline': record.date_deadline,
                #         'property_type_id': record.property_type_id.id
                # }])
                # temp.write({
                #     'price': 1212
                # })

                # record.property_id.offer_id_accepted.add(t)
                # self.unlink()
                # t.unlink()



            else:
                raise odoo.exceptions.UserError(
                    "The offer has been rejected before or The Property is no longer available.")
        return True

    def offer_reject(self):
        for record in self:
            if record.status != 'accepted':
                record.status = "refused"
            else:
                raise odoo.exceptions.UserError("The offer has already been accepted!")
        return True

    @api.model
    def create(self, vals):
        p_id = vals['property_id']

        if p_id != 16:
            property = self.env['estate.property'].browse(p_id)
            property.state = 'offer_received'


            if vals['price'] < self.env['estate.property'].browse(p_id).best_offer:
                raise odoo.exceptions.UserError("Offers can not be lower than the Current Best offer!")
            return super(EstatePropertyOffer, self).create(vals)
        else:
            return super(EstatePropertyOffer, self).create(vals)
