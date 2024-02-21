# **User Service**

**The User Service provides endpoints for user authentication and management, including user signup, login, password update, and deletion.
Built using Flask, a Python web framework, the service offers a RESTful API for seamless interaction with user-related data.**

## APIs:

### Signup API (POST /signup):

#### Description:

The signup route handles POST requests to register new users. It receives JSON data containing the user's email, password, and role.
It checks if the email already exists in the database and then creates a new User object with a hashed password. It returns a success message 
if the user is registered successfully.

#### URL: /signup

    Method: POST

    Request Body: 
    {
      "email": "string",
      "password": "string",
      "role": "string"
    }
    Response:
    Status Code: 201 Created
    Content: 
    {
     "message": "User registered successfully"
    }

### Login API (POST /login):

#### Description:

The login route handles POST requests for user authentication. It receives JSON data containing the user's email and password.
It validates the credentials against the stored hashed password and returns a JWT access token if authentication is successful.

#### URL: /login

    Method: POST

    Request Body: 
    {
      "email": "string",
      "password": "string"
    }
    Response:
    Status Code: 200 OK
    Content:
    {
      "token": "string"
    }
    Error: Returns an appropriate error message if the request fails.

### Update Password API (POST /update_password):

#### Description:

The update_password route handles POST requests to update a user's password. It receives JSON data containing the user's 
new password and verifies that it is different from the current password. If the new password is valid, it updates the 
password in the database and returns a success message.

#### URL: /update_password

    Method: POST
    Authentication: Required

    Request Body
    {
      "new_password": "string"
    }
    Response
    Status Code: 200 OK
     Content:
    {
      "message": "Password updated successfully"
    }

    Error: Returns an appropriate error message if the request fails.

### Delete User API (DELETE /delete_user):

#### Description:

The delete_user route handles DELETE requests to delete a user account. It deletes the user from the database and returns a success message.

#### URL: /delete_user

    Method: DELETE
    Authentication: Required
    
    Response:
    Status Code: 200 OK
    Content:
    {
      "message": "User deleted successfully"
    }
    Error: Returns an appropriate error message if the request fails.