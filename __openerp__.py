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

{
    "name" : "Partner Historic Address",
    "version" : "1.0",
    "author" : "Factor Libre SL",
    "category" : "General",
    "description": """By default, OpenERP have a many2one relationship in most of the objects where an address is required: sales, purchases, shipping, invoices... This is great, because you can edit those address from there when needed. But, it can be also a problem because sometimes a user can edit an address record already used or in use. 

Obviously, they have to be allowed to change the value of some fields due to an error, but they have to be informed that if the information is a complete new address (a new invoice or shipping address for example) they have to insert a new address instead of editing an existing one, because the edited information would replace the previous one in all the records related to it. 

So, this module blocks by default the edition of address, adding a new button to unblock it and showing a warning message to the user.""",
    "depends" : ["base"],
    "license" : "AGPL-3",
    "init_xml" : [],
    "demo_xml" : [],
    "update_xml" : [
        'wizard/unlock_address_wizard.xml',
        #'partner_view.xml',
        'partner_view_historic.xml',        
     ],
    "active": False,
    "installable": True
}
