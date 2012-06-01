partner_historic_address
========================

By default, OpenERP have a many2one relationship in most of the objects where an address is required: sales, purchases, shipping, invoices... This is great, because you can edit those address from there when needed. But, it can be also a problem because sometimes a user can edit an address record already used or in use. 

Obviously, they have to be allowed to change the value of some fields due to an error, but they have to be informed that if the information is a complete new address (a new invoice or shipping address for example) they have to insert a new address instead of editing an existing one, because the edited information would replace the previous one in all the records related to it. 

So, this module blocks by default the edition of address, adding a new button to unblock it and showing a warning message to the user.