# -*- coding: utf-8 -*-
import logging
from odoo.exceptions import UserError, ValidationError
from odoo import api, fields, models, _
from datetime import datetime

_logger = logging.getLogger(__name__)

class BudgetHead(models.Model):
    _name = "budget.head"
    
    name = fields.Char("Name")
    description = fields.Char("Description")
    amount = fields.Float("Amount")
    notes = fields.Text("Notes")
    
    