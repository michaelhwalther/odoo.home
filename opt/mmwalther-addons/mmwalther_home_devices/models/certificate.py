'''
Created on 02.06.2018

@author: miw
'''

from odoo import models, fields, api
import logging
LOG = logging.getLogger(__name__)

from odoo.tools.translate import _
from odoo.exceptions import ValidationError


STATES = [
    ('draft', 'Draft'),
    ('active', 'Active'),
    ('unused', 'Not in use'),
]


class Certificate(models.Model):
    _name = 'home.certificate'
    _description = "Certificate"
    _inherit = ['mail.thread']
    _order = "name"
    
    name  = fields.Char()
    description  = fields.Text()
    state = fields.Selection(STATES, default="draft", required=True)

    active = fields.Boolean(default=True)

    public_key = fields.Text(string="Public Key")
    private_key = fields.Text(string="Private Key")

