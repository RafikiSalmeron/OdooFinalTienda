from odoo import models, fields, api

class Ordenador(models.Model):
    _name = 'tienda.ordenador'
    codigo = fields.Integer('Codigo de identificacion', required = True)
    modelo = fields.Char('Modelo', required = True)
    precio = fields.Float('Precio', required = True)
    Procesador = fields.Many2one('tienda.procesador', 'Procesador')
    PlacaBase = fields.Many2one('tienda.placa', 'Placa Base')

    

    