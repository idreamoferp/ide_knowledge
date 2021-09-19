from odoo import api, fields, models
class DocumentPage(models.Model):
    _inherit = "document.page"
    
    doc_type = fields.Selection(selection_add=[('pycode', 'PyCode')])
    content_py = fields.Text("Content", compute="_compute_content_py", inverse="_inverse_content_py")
    
    def _compute_content_py(self):
        for rec in self:
            rec.content_py  = rec.content

    def _inverse_content_py(self):
        for rec in self:
            rec.content = rec.content_py

    def _create_history(self, vals):
        self.ensure_one()
        history = self.env['document.page.history']
        vals['doc_type'] = self.doc_type
        return super(DocumentPage, self)._create_history(vals)

    
class DocumentPageHistory(models.Model):

    _inherit = "document.page.history"
    doc_type = fields.Selection(selection_add=[('pycode', 'PyCode')])
    
    content_py = fields.Text("Content", compute="_compute_content_py")
    
    def _compute_content_py(self):
        for rec in self:
            rec.content_py  = rec.content