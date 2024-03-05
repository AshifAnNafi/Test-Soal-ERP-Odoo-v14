# -*- coding: utf-8 -*-
from odoo import http, _, exceptions
from odoo.http import request
import json
import  werkzeug.wrappers
import base64
import io
from PIL import Image
from base64 import b64encode, b64decode
import xmlrpc, xmlrpc.client
import logging
_logger = logging.getLogger(__name__)


class ApiDataProduct(http.Controller):
    @http.route(['/api/product'], csrf=False, type='json', auth='public', methods=['POST'], cors='*')        
    def create_product(self, **params):
        name = params.get("name")
        price = params.get("price")
        description = params.get("description")

        vals = {
            'name': name,
            'price': price,
            'description': description
        }
        
        create_product = http.request.env['data.product'].sudo().create(vals)
        header = request.httprequest.headers
        data = {
            'message': 'success',
            'name': name
        }
        return data
    
    @http.route('/api/get_product/<int:product_id>',crsf=False,cors='*', type='http', auth='public', methods=['GET'])
    def get_product(self,product_id, **kwargs):
        product = request.env['data.product'].sudo().search([('product_id', '=', product_id)])
        if product: 
            product_data = []
            for record in product:
                product_data.append({
                    'name': record.name,
                    'price': record.price,
                    'description': record.description
                })
            return request.make_response(json.dumps(product_data), headers={'Content-Type': 'application/json'})
        else:
            return request.make_response(json.dumps({'error': 'Product not found'}), headers={'Content-Type': 'application/json'}, status=404)
        
    @http.route('/api/update_product/<int:product_id>', crsf=False, cors='*', type='http', auth='public', methods=['PUT'])
    def update_product(self, product_id, **kwargs):
        product = request.env['data.product'].sudo().search([('product_id', '=', product_id)])
        if product:
            data = json.loads(request.httprequest.data)
            product.write({
                'name': data.get('name', product.name),
                'price': data.get('price', product.price),
                'description': data.get('description', product.description)
            })
            return request.make_response(json.dumps({'success': 'Product updated successfully'}), headers={'Content-Type': 'application/json'})
        else:
            return request.make_response(json.dumps({'error': 'Product not found'}), headers={'Content-Type': 'application/json'}, status=404)

    
    @http.route('/api/delete_product/<int:product_id>',crsf=False,cors='*', type='http', auth='public', methods=['GET'])
    def delete_product(self,product_id, **kwargs):
        product = request.env['data.product'].sudo().search([('product_id', '=', product_id)])
        if product: 
            product.unlink()
            return request.make_response(json.dumps({'success': 'Product deleted successfully'}), headers={'Content-Type': 'application/json'})
        else:
            return request.make_response(json.dumps({'error': 'Product not found'}), headers={'Content-Type': 'application/json'}, status=404)
