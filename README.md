## Multi Tenant Django Project (Backend)
- It is a simple project to teach, how to create Multi tenant config

# Running the project
  - To Up the containers use docker and run `docker-compose up -d`
  - Your project should be running at `http://0.0.0.0:8080/`

# Access container
  - To run any code in container use `docker-compose exec web bash`

# Run Tests
  - To run tests use `docker-compose exec web python manage.py test -v 2`

# Handle with Migrations in schemas
  - To run Migrations in all schemas use `docker-compose exec web python manage.py migrate_schemas`
  - Use `--shared` to execute only in apps declared here -> `SHARED_APPS`
  - Create Super user in any tenant `docker-compose exec web python manage.py tenant_command createsuperuser`


