# Test-Soal-ERP-Odoo-v14

1.
- Endpoints untuk Create: /api/product
  Request Body:
  {
      "name": "product_name",
      "price": product_price,
      "description": "product_description"
  }
  
- Endpoints untuk Read: /api/get_product/<int:product_id>
  
- Endpoints untuk Update: /api/update_product/<int:product_id>
  Request Body:
  {
    "name": "new_product_name",
    "price": new_product_price,
    "description": "new_description"
  }
  
- Endpoints untuk Delete: /api/delete_product/<int:product_id>
  
