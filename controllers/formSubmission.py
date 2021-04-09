from odoo import http
from odoo.http import request

class Hospital(http.Controller):
    @http.route('/patient_web',type="http",auth="public",website=True)
    def patient_web(self,**kwargs):
        return http.request.render('hospital.cart_template',{})

    @http.route('/patient-thank-you',type="http",auth="public",website=True)
    def patientThanks(self,**kwargs):
        print(kwargs)
        data={
            'name':kwargs['patient_name'],
            'gender':kwargs['gender'],
            'dateOfVisit':kwargs['DateOfVisit'],
            'dateOfBirth':kwargs['dateOfBirth'],
            'contactNumber':kwargs['ContactNumber']
        }
        request.env['hospital.hospital'].sudo().create(data)
        return http.request.render('hospital.patient_thanks',{})

    # @http.route('/shop/previous_purchase_product',type='json', auth='public', website=True)
    # def previous_purchase_product(self):
    #

