'''
Created on 02.06.2018

@author: miw
'''

from odoo import models, fields, api
import logging
LOG = logging.getLogger(__name__)

from odoo.tools.translate import _
from odoo.exceptions import ValidationError


class HomeDeviceDiscoveryItem(models.TransientModel):
    _name = 'home.device.discovery.item'
    _description = "Home Device Discovery Item"
    _order = "name"
    
    name  = fields.Char()
    mac = fields.Char()
    lease_ends_iso = fields.Char()
    ip = fields.Char()
    
    discovery = fields.Many2one('home.device.discovery')



class HomeDeviceDiscovery(models.TransientModel):
    _name = 'home.device.discovery'
    _description = "Home Device Discovery"
    _order = "name"
    
    name  = fields.Char()
    description  = fields.Text()
    state = fields.Selection([('draft','Draft'),
                              ('discovered','Discovered'),], default="draft")

    items = fields.One2many('home.device.discovery.item', 'discovery', 'Discovered Items')


    def save_to_home_devices(self):
        LOG.info("Saving %d items to home devices ..."%(len(self.items or[])))
        
        for item in self.items:
            # TODO create for un-matched items
            pass
        
            # TODO update for matched items
            pass
        
    def discover(self):
        LOG.info("Start discovery ...")
        
        import requests
        l = requests.get('http://router3/opt/cgi-bin/leases.py')
        
        if l.ok:
            for lease in l.json():
                lease['discovery'] = self.id
                self.env['home.device.discovery.item'].create(lease)
                
                # TODO: match using mac
                
        
        self.state = 'discovered'
        LOG.info("Discovery done.")

        return {
            'type': 'ir.actions.act_window',
            'res_model': self._name,
            'view_type': 'form',
            'view_mode': 'form',
            'target': 'new',
            'key2': "client_action_multi",
            'res_id': self.id,
        }
