from odoo import fields, models, api


class PropertyOfferXlsx(models.AbstractModel):
    _name = 'report.estate.report_property_offers_xlsx'
    _inherit = 'report.report_xlsx.abstract'
    _description = 'Test Excel Report'

    def generate_xlsx_report(self, workbook, data, partners):
        for obj in partners:
            row = 1
            col = 1

            report_name = obj.name
            # One sheet by partner
            sheet = workbook.add_worksheet(report_name[:31])
            sheet.set_column('B:C',20)
            sheet.set_column('D:F', 15)

            bold = workbook.add_format({'bold': True})
            sheet.write(row, col, obj.name, bold)

            row += 1
            sheet.write(row, col, "Salesman ", bold)
            col += 1
            sheet.write(row, col, obj.salesperson_id.name)

            row += 1
            col -= 1
            sheet.write(row, col, "Expected Price ", bold)
            col += 1
            sheet.write(row, col, obj.expected_price)
            row += 1
            col -= 1
            sheet.write(row, col, "Status ", bold)
            col += 1
            sheet.write(row, col, obj.state)

            row += 2
            col -= 1

            #Setting Offer Table Titles
            sheet.write(row, col, "Price", bold)
            sheet.write(row, col+1, "Partner", bold)
            sheet.write(row, col+2, "Validity (days)", bold)
            sheet.write(row, col + 3, "Deadline", bold)
            sheet.write(row, col + 4, "State", bold)


            #Populating The Sheet
            for offer in obj.offer_ids:
                row+=1
                sheet.write(row, col, offer.price)
                sheet.write(row, col + 1, offer.partner_id.name)
                sheet.write(row, col + 2, offer.validity)
                temp = fields.Date.from_string(
                    offer.date_deadline).strftime('%d/%m/%Y')
                sheet.write(row, col + 3, temp)
                sheet.write(row, col + 4, offer.status)
