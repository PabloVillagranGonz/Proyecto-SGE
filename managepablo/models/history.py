# -*- coding: utf-8 -*-
from odoo import models, fields

class History(models.Model):
    _name = 'managepablo.history'
    _description = 'managepablo.history'
    
    name = fields.Char(string="Nombre", required=True, help="Introduzca el nombre")
    description = fields.Text(string="Descripción")

   
    # Muchas historias tienen un proyecto
    project_id = fields.Many2one("managepablo.project", string="Project", required=True, ondelete="cascade")
    
    # Una historia tiene muchas tareas
    task_id = fields.One2many(string="Tasks", comodel_name="managepablo.task", inverse_name="history_id")

    used_technologies = fields.Many2many("managepablo.technology", compute = "_get_used_technologies")

    def _get_used_technologies(self):
        for history in self:
            technologies = None
            for task in history.task_id:
                if not technologies:
                    technologies = task.technologies
                else:
                    technologies = technologies + task.technologies
            history.used_technologies = technologies
