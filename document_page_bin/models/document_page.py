from odoo import api, fields, models
class DocumentPage(models.Model):
    _inherit = "document.page"
    
    doc_type = fields.Selection(selection_add=[('bin', 'Attachment')])
    attachment = fields.Binary(string='Document File', compute="_compute_attachment", inverse="_inverse_attachment")
    
    def _compute_attachment(self):
        for rec in self:
            rec.attachment = None
            if rec.doc_type == "bin":
                if rec.history_head.attachment :
                    rec.attachment = rec.history_head.attachment 

    def _inverse_attachment(self):
        for rec in self:
            if rec.doc_type == "bin":
                rec._create_history(
                    {
                        "page_id": rec.id,
                        "name": rec.draft_name,
                        "summary": rec.draft_summary,
                        "content": rec.content,
                        "attachment": rec.attachment
                    }
                )
                

    
class DocumentPageHistory(models.Model):

    _inherit = "document.page.history"
    doc_type = fields.Selection(selection_add=[('bin', 'Attachment')])
    attachment = fields.Binary(string='Document File', attachment=True)