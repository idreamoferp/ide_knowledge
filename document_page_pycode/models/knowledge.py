from odoo import api, fields, models
class DocumentPage(models.Model):
    _inherit = "document.page"
    
    doc_type = fields.Selection([('html', 'HTML'), ('pycode', 'PyCode')],' Document Type', default="html")
    
    
    def _create_history(self, vals):
        self.ensure_one()
        history = self.env['document.page.history']
        vals['doc_type'] = self.doc_type
        if vals['doc_type'] == 'pycode':
            vals['content'] = vals['content'].replace('<p>',"").replace("</p>","")
        return super(DocumentPage, self)._create_history(vals)

    
class DocumentPageHistory(models.Model):

    _inherit = "document.page.history"
    doc_type = fields.Selection([('html', 'HTML'), ('pycode', 'PyCode')],' Document Type', default="html")