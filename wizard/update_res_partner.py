from odoo import _, api, fields, models

class updateResPartner(models.TransientModel):
    _name = 'update.wizard'

    partner_id = fields.Many2one('res.partner', string='Partner')
    identification_number = fields.Char(string='Tipo de identificacion')
    vat = fields.Char(string='Numero de identificacion')
    name = fields.Char(string='Name')

    l10n_latam_identification_type_id = fields.Many2one('l10n_latam.identification.type',
                                                        string="Identification Type", index='btree_not_null',
                                                        auto_join=True,
                                                        default=lambda self: self.env.ref('l10n_latam_base.it_vat',
                                                                                          raise_if_not_found=False),
                                                        help="The type of identification")
    vat_update = fields.Char(string='Identification Number', help="Identification Number for selected type")

    def update_data(self):
        self.partner_id.vat = self.vat_update
        self.partner_id.l10n_latam_identification_type_id = self.l10n_latam_identification_type_id.id
        self.partner_id._doc_number_change()


