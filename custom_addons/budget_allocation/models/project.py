# -*- coding: utf-8 -*-
import logging
from odoo.exceptions import UserError, ValidationError
from odoo import api, fields, models, _
from datetime import datetime

_logger = logging.getLogger(__name__)

class ProjectBudget(models.Model):
    _name = "project.budget"
    
    name = fields.Char("Name")
    description = fields.Char("Description")
    amount = fields.Float("Total Amount")
    project_budget_line_ids = fields.One2many('project.budget.line','project_id',"Project Budget Details")
    
class BudgetHeadLine(models.Model):
    _name = 'project.budget.line'
    
    budget_head_id = fields.Many2one('budget.head',"Budget Head")
    amount = fields.Float("Allocation Amount")
    project_id = fields.Many2one('project.budget',"Project")
    
    