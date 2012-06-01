# -*- coding: utf-8 -*-
#########################################################################
#                                                                       #
# Copyright (C) 2012 Factor Libre SL                                    #
#                                                                       #
#This program is free software: you can redistribute it and/or modify   #
#it under the terms of the GNU General Public License as published by   #
#the Free Software Foundation, either version 3 of the License, or      #
#(at your option) any later version.                                    #
#                                                                       #
#This program is distributed in the hope that it will be useful,        #
#but WITHOUT ANY WARRANTY; without even the implied warranty of         #
#MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the          #
#GNU General Public License for more details.                           #
#                                                                       #
#You should have received a copy of the GNU General Public License      #
#along with this program.  If not, see <http://www.gnu.org/licenses/>.  #
#########################################################################

from osv import osv
from osv import fields

class res_partner(osv.osv):
    _inherit = 'res.partner'
    _columns = {
        'address': fields.one2many('res.partner.address', 'partner_id',
            'Contacts', domain=[('active','=',True)]),
        'historic_address': fields.one2many('res.partner.address', 'partner_id',
            'Historic Addresses', domain=[('active','=',False)]),
    }
res_partner()

class res_partner_address(osv.osv):
    _inherit = 'res.partner.address'
    
    _columns = {
        #'historic': fields.boolean('Historic?'),
        'locked': fields.boolean('Locked'),
    }
    
    def set_editable_address(self, cr, uid, ids, context=None):
       return {'value': {'locked': False}}
    
    def _remove_invoice_type_address(self, cr, uid, ids, context=None):
        """
        Este método mantiene una unica dirección de facturación para el cliente
        quitando el tipo de dirección a la dirección de facturación anterior.
        """
        addr_id = ids[0]
        addr_obj = self.browse(cr, uid, addr_id)
        partner_id = addr_obj.partner_id and addr_obj.partner_id.id
        if partner_id:
            inv_addr_ids = self.search(cr,uid,[('partner_id','=',partner_id),('type','=','invoice')])
            if addr_id and addr_id in inv_addr_ids:
                inv_addr_ids.pop(inv_addr_ids.index(addr_id))
        
            self.write(cr, uid, inv_addr_ids, {'type':None})
        return True
    
    def write(self, cr, uid, ids, vals, context=None, update=True):
        """
        Este método modifica el comportamiento del método de escritura del objeto res.partner.address
        bloqueando la edición de la dirección, eliminando el tipo de la misma si pasa a ser historica 
        y llamando al método _remove_invoice_type_address para mantener una única dirección de facturación
        """
        if type(ids) == int:
            ids = [ids]
        if not context:
            context = []
        ####
        #vals['historic'] = True
        ####
        if 'update' not in context or context['update']:
            vals['locked'] = True
            
        if 'active' in vals and not vals['active']:
            vals['type'] = None
            
        if 'type' in vals and vals['type'] == 'invoice':            
            self._remove_invoice_type_address(cr, uid, ids, context=context)
            
        res = super(res_partner_address, self).write(cr, uid, ids, vals, context=context)        
        return res
       
        
    
    def create(self, cr, uid, vals, context=None):
        """
        Este método modifica el comportamiento del método de creación del objeto res.partner.address
        bloqueando la edición de la dirección, eliminando el tipo de la misma si pasa a ser historica 
        y llamando al método _remove_invoice_type_address para mantener una única dirección de facturación
        """
        if not context:
            context = []
        if 'active' in vals and not vals['active']:
            vals['type'] = None
        vals['locked'] = True
        res = super(res_partner_address, self).create(cr, uid, vals, context=context)
        if 'type' in vals and vals['type'] == 'invoice':
            self._remove_invoice_type_address(cr, uid, [res], context=context)
        return res
        
res_partner_address()
