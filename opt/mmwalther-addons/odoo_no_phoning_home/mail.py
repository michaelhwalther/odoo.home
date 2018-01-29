# -*- coding: utf-8 -*-

from odoo.models import AbstractModel
from odoo import api
from odoo.tools import config

import logging
_logger = logging.getLogger(__name__)


config['publisher_warranty_url'] = ''


class publisher_warranty_contract(AbstractModel):
    _inherit = 'publisher_warranty.contract'

    @api.multi
    def update_notification(self, cron_mode=True):

        _logger.info("NO More Spying Stuff")

        return True


publisher_warranty_contract()

