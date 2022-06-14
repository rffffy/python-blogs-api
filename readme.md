# Python API development with FastAPI

### Description
A simple REST Api for blog posts.

### Gettinng Started
Start server, run on command line: 
`uvicorn app.main:app --reload`

To view api documentations: [server-address/docs](http://localhost:8000/docs)

### Features

1. CRUD operations with GET, POST, DELETE and PUT methods for:

   - **Posts**:
     - Create Posts
     - Get a Post filtered by id
     - Delete a Post filtered by id
     - Update a Post filtered by id

   - **Users**:
     - Create a User
     - Get a User filtered by id

2. Object Relational Mapping with **SQLAlchemy**

3. Authorization and Authentication with JWT