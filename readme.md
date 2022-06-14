# Python API development with FastAPI

### Description
A simple REST Api for blog posts.

### Gettinng Started
Start server, run on command line: 
`uvicorn app.main:app --reload`

To view api documentations(after server is running): [{HOST_ADDRESS}/docs](http://localhost:8000/docs)

### Features

1. CRUD operations with GET, POST, DELETE and PUT methods for:

   - **Posts**:
     - Create Posts
     - Get all Posts of the logged in User
     - Get a Post, of the logged in User, filtered by id
     - Delete a Post filtered by id
     - Update a Post filtered by id

   - **Users**:
     - Create a User
     - Get a User filtered by id

2. Object Relational Mapping with **SQLAlchemy**

3. Authorization and Authentication with JWT