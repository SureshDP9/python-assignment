# Product Service

The Product Service is responsible for managing products. It provides functionalities to retrieve, add, update,
and delete products. Built using Flask, a Python web framework, the service offers a RESTful API for seamless 
interaction with product-related data.

## APIs:

### Get Products API (GET /products):

#### Description:

The Get Products API retrieves all products available in the database and returns a list of product details
including ID, product ID, product name, price per unit, and quantity.

#### URL: /products

    Method: GET
    Authentication: Required

    Response:
    Status Code: 200 OK
    Content:
     [
      {
        "id": integer,
         "product_id": "string",
         "product_name": "string",
         "price_per_unit": float,
         "qty": integer
     },
     ...
    ]
    Error: Returns an appropriate error message if the request fails.

### Get Product API (GET /product/<product_id>):

#### Description:

The Get Product API retrieves a specific product by its product ID from the database and returns its details 
including ID, product ID, product name, price per unit, and quantity.

#### URL: /product/<product_id>

    Method: GET
    Authentication: Required

    URL Parameters:
    product_id: The ID of the product to retrieve (string)

    Response:
    Status Code: 200 OK
    Content:
    {
       "id": integer,
       "product_id": "string",
       "product_name": "string",
       "price_per_unit": float,
       "qty": integer
    }
    Error: Returns an appropriate error message if the requested product is not found.

## Add Product API (POST /product):

#### Description:

The Add Product API allows administrators to add new products to the database. It generates a random UUID
as the product ID, accepts product details in the request body, and adds the product to the database.

#### URL: /product

    Method: POST
    Authentication: Required (Admin)

    Request Body:
    {
       "product_name": "string",
       "price_per_unit": float,
       "qty": integer
    }
    Response:
    Status Code: 201 Created
    Content:
    {
     "message": "Product added successfully"
    }

    Error: Returns an appropriate error message if the request fails or the user is not authorized.

### Update Product API (PUT /product):

#### Description:

The Update Product API allows administrators to update existing product details in the database. It receives 
updated product details in the request body and updates the corresponding product.

#### URL: /product

    Method: PUT
    Authentication: Required (Admin)

    Request Body:
    {
      "product_id": "string",
      "product_name": "string",
      "price_per_unit": float,
      "qty": integer
    }
    Response:
    Status Code: 200 OK
    Content:
    {
      "message": "Product updated successfully"
    }

    Error: Returns an appropriate error message if the request fails, the product is not found, or the user is not authorized.

### Delete Product API (DELETE /product/<product_id>):

#### Description:

The Delete Product API allows administrators to delete existing products from the database by providing 
the product ID.

#### URL: /product/<product_id>

    Method: DELETE
    Authentication: Required (Admin)

    URL Parameters:
    product_id: The ID of the product to delete (string)

    Response:
    Status Code: 200 OK
    Content:
    {
     "message": "Product deleted successfully"
    }

    Error: Returns an appropriate error message if the requested product is not found or the user is not authorized