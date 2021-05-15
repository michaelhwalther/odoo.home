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
    ('discovered', 'Discovered'),
    ('active', 'Active'),
    ('unused', 'Not in use'),
]

TYPES = [
    ('desktop', 'Desktop Computer'),
    ('laptop', 'Laptop Computer'),
    ('tablet', 'Tablet'),
    ('cellphone', 'Cell Phone'),
    ('tv', 'TV'),
    ('router', 'Router'),
]


class HomeDevice(models.Model):
    _name = 'home.device'
    _description = "Home Device"
    _inherit = ['mail.thread']
    _order = "name"
    
    name  = fields.Char()
    description  = fields.Text()
    state = fields.Selection(STATES, default="discovered", required=True)
    type  = fields.Selection(TYPES, required=True)

    active = fields.Boolean(default=True)

