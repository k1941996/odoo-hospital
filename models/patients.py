# -*- coding: utf-8 -*-

from odoo import models, fields, api
from datetime import date
import random

def calculateAge(birthDate):
    today = date.today()
    age = today.year - birthDate.year - ((today.month, today.day) < (birthDate.month, birthDate.day))
    return age

def AllotRoom():
    x = random.randint(1,100)
    return x


class hospital(models.Model):
    _name = 'hospital.hospital'
    _description = 'RedCross.Hospital'

    name = fields.Char("Patient Name",required=True)
    gender = fields.Selection([('male',"Male"),('female','Female'),('other','Other')],required=True,default="male")
    dateOfBirth = fields.Date("Date of Birth", required=True,default=date.today())
    disease = fields.Char("Disease")
    dateOfVisit = fields.Datetime("Date of Visit",required=True)
    contactNumber = fields.Char("Contact Details",required=True)
    assignedDoctor = fields.Many2one('hospital.doctors',ondelete='set null',string='Assigned Doctor',index=True)
    notes = fields.Text("Additional Notes")
    age = fields.Integer("Age")
    isAdmitted = fields.Boolean("Is Admitted")
    AllotedRoomNo = fields.Integer("Ward Number")

    @api.onchange('isAdmitted')
    def _assignWard(self):
        if self.isAdmitted:
            self.AllotedRoomNo = AllotRoom()
        else:
            self.AllotedRoomNo = None
    @api.model
    def create(self, value_list):
        print(value_list)
        # {'name': 'a', 'disease': 'Stomach Infection', 'dateOfVisit': '2021-03-12 12:49:45', 'assignedDoctor': 1,
        # 'isAdmitted': True, 'notes': 'asd', 'gender': 'male',
        # 'dateOfBirth': '2021-03-12', 'contactNumber': '9874563210'}
        dob = value_list["dateOfBirth"]
        a = dob.split('-')
        value_list['age'] = int(calculateAge(date(int(a[0]),int(a[1]),int(a[2]))))
        # print(value_list)
        new_values = super(hospital,self).create(value_list)
        return new_values