# -*- coding: utf-8 -*-
from odoo import models, fields

class Project(models.Model):
    _name = 'managepablo.project'
    _description = 'managepablo.project'
    
    name = fields.Char(string="Nombre", required=True, help="Introduzca el nombre")
    description = fields.Text(string="Descripción")


    # Un proyecto tiene varias historias
    history_id = fields.One2many(string="Histories", comodel_name="managepablo.history", inverse_name="project_id")

    # Un proyecto tiene muchas carreras
    sprint_id = fields.One2many( string="Sprints",comodel_name="managepablo.sprint", inverse_name= "project_id")
