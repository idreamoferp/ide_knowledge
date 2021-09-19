from odoo import api, fields, models
class DocumentPage(models.Model):
    _inherit = "document.page"
    
    doc_type = fields.Selection([('html', 'HTML')],' Document Type', default="html")
    
    def _create_history(self, vals):
        self.ensure_one()
        vals['doc_type'] = self.doc_type
        return super(DocumentPage, self)._create_history(vals)
    
class DocumentPageHistory(models.Model):
    _inherit = "document.page.history"
    
    doc_type = fields.Selection([('html', 'HTML')],' Document Type', default="html")