# **Order Service**

**The Order Service allows users to create, retrieve, update, and delete orders, providing essential functionality for managing transactions.
Built using Flask, a Python web framework, the service offers a RESTful API for seamless interaction with order-related data.**

## APIs:

### Create Order API (POST /order):

#### Description:
The create order route handles POST requests to create new orders. It receives JSON data containing the user 
ID and a list of products with their quantities. For each product in the request, it calculates the total order amount using a 
get_total function from the app.service module. It then creates a new Orders object in the database, along with associated OrderedProducts, and returns a success message.

#### URL: /order

    Method: POST
    Authentication: Required

    Request Body: 
    {
        "user_id": "string",
         "products": [
            {
               "product_id": "string",
               "qty": integer
           },
           ...
        ]
    }
    Response:
    Status Code: 200 OK
    Content: 
    {
       "message": "Order created successfully"
    }

### Read Orders API (GET /orders):

#### Description: 

The get orders route handles GET requests to retrieve all orders from the database.
It queries the Orders table and constructs a JSON response containing order details, including
associated products and their quantities.

#### URL: /orders

    Method: GET
    Authentication: Required

    Response
    Status Code: 200 OK
    Content:
    [
      {
        "id": integer,
        "order_id": "string",
        "user_id": "string",
        "date_of_purchase": "datetime",
        "status": "string",
        "products": [
            {
                "product_id": "string",
                "qty": integer
            },
            ...
        ],
        "total": float
    },
    ...
    ]
    Error: Returns an appropriate error message if the request fails.


### Update Order API (PUT /order):

#### Description: 

The update_order route handles PUT requests to update existing orders.
It receives JSON data containing the order ID and a list of products with updated quantities.
It retrieves the order from the database, recalculates the total amount for the order, and 
updates the order's total. It then updates the quantities of ordered products accordingly and 
returns a success message.

#### URL: /order

    Method: PUT
    Authentication: Required

    Request Body
    {
       "order_id": "string",
       "products": [
         {
             "product_id": "string",
             "qty": integer
         },
         ...
     ]
    }
    Response
    Status Code: 200 OK
    Content:
    {
       "message": "Order products updated successfully"
    }

    Error: Returns an appropriate error message if the request fails.


### Delete Order API (DELETE /order/<order_id>):

#### Description: 

This API endpoint allows users to delete existing orders by providing the order ID.

    URL: /order/<order_id>
    Method: DELETE
    Authentication: Required

    URL Parameters:
    order_id: The ID of the order to delete (string)

    Response:
    Status Code: 200 OK
    Content:
    {
      "message": "Order deleted successfully"
    }

    Error: Returns an appropriate error message if the request fails.
