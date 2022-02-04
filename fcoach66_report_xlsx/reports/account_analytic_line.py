from odoo import models

class TimesheetXLS(models.AbstractModel):
    _name = 'report.fcoach66_report_xlsx.report_account_analytic_line_xls'
    _inherit = 'report.report_xlsx.abstract'

    def generate_xlsx_report(self, workbook, data, lines):
        sheet = workbook.add_worksheet('Sheet 1')
        sheet.set_column('A:A', 25)
        sheet.set_column('B:B', 12)
        sheet.set_column('C:C', 10)
        sheet.set_column('D:D', 40)
        count = 0
        for obj in lines:
            count = count+1
            date_obj = workbook.add_format({'num_format': 'dd/mm/yyyy'})
            sheet.write_string(count, 0, obj.employee_id.display_name)
            sheet.write(count, 1, obj.date, date_obj)
            sheet.write_number(count, 2, obj.unit_amount)
            sheet.write_string(count, 3, obj.name)