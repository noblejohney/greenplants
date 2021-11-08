# -*- coding: utf-8 -*-
import logging
from odoo.exceptions import UserError, ValidationError
from odoo import api, fields, models, _
from datetime import datetime

_logger = logging.getLogger(__name__)

class BudgetPurchaseOrder(models.Model):
    _name = "budget.purchase.order"
    
    @api.model
    def create(self, vals):
        if not vals.get('name') or vals['name'] == _('New'):
            vals['name'] = self.env['ir.sequence'].next_by_code('budget_allocation.purchase_order') or _('New')
        return super(BudgetPurchaseOrder, self).create(vals)
    
    name = fields.Char("Purchase Order")
    partner_id = fields.Many2one('res.partner',"Vendor")
    order_date = fields.Date("Order Date")
    description = fields.Char("Description")
    amount = fields.Float("Amount")
    notes = fields.Text("Notes")
    budget_po_line_ids = fields.One2many('budget.purchase.order.line','budget_purchase_order_id',"Budget Head")
    
class BudgetPurchaseOrderLine(models.Model):
    _name = 'budget.purchase.order.line'
    
    project_budget_id = fields.Many2one('project.budget',"Project")
    budget_head_id = fields.Many2one('budget.head',"Budget Head")
    amount = fields.Float("Amount")
    budget_purchase_order_id = fields.Many2one('budget.purchase.order',"Purchase Order")

    
    