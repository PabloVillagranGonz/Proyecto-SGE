# -*- coding: utf-8 -*-
from odoo import models, fields

class Technology(models.Model):
    _name = 'managepablo.technology'
    _description = 'managepablo.technology'
    
    name = fields.Char(string="Nombre", required=True, help="Introduzca el nombre")
    description = fields.Text(string="Descripción")
    image = fields.Image(string="Imagen", max_width=1024, max_height=1024)

    tareas_id = fields.Many2many(
        string="Tareas",
        comodel_name="managepablo.task", 
        relation="tecnologias_tareas", 
        column1="tareas_ids", 
        column2="tecnologias_ids"
    )

    
    
