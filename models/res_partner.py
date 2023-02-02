import requests
from odoo import fields, api, models, _
from odoo.exceptions import UserError

class ResPartner(models.Model):
    _inherit = 'res.partner'

    def update_document_wizard(self):
        contact_update = self.env['update.wizard'].create({
            'partner_id': self.id,
            'name': self.name,
            'identification_number': self.l10n_latam_identification_type_id.name,
            'vat': self.vat,
        })
        return {
            'name': _('Update Document'),
            'type': 'ir.actions.act_window',
            'res_model': 'update.wizard',
            'view_mode': 'form',
            'target': 'new',
            'res_id': contact_update.id,
            'context': self.env.context,
        }
    # def update_document(self):
    #     contact_update = self.env['update.wizard'].create({
    #         'name': self.name,
    #         'identification_number': self.l10n_latam_identification_type_id.name,
    #         'vat': self.vat,
    #     })
    #     return {
    #         'name': _('Update Document'),
    #         'type': 'ir.actions.act_window',
    #         'res_model': 'update.wizard',
    #         'view_mode': 'form',
    #         'target': 'new',
    #         'res_id': contact_update.id,
    #         'context': self.env.context,
    #     }
    #     # res = super(ResPartner, self).update_document()
    #     # a  =1
    #     # return res
