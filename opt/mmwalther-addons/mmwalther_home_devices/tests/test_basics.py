from odoo.tests import common

class TestHomeDevice(common.TransactionCase):
    
    def test_homedevice_defaultstate(self):
        record = self.env['home.device'].create({'name': 'Test1'})

        self.assertEqual(record.state,'discxxxxovered')