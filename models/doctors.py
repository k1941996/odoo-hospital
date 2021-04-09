from odoo import fields,models

class doctors(models.Model):
    _name = "hospital.doctors"
    _description = "Red Cross Hospital Doctors"

    name = fields.Char("Doctor's Name",required=True)
    dateOfBirth = fields.Date("Date of Birth",required=True)
    specialization = fields.Char("Specialization")
    patients = fields.One2many('hospital.hospital','assignedDoctor',string='Patients')
