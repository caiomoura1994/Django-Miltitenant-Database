## Test Talk Project (Backend)
- It is a simple project to teach, how to create tests using Django Rest

# Runing the project
  - Add the file `core/firebase-credentials.json` to use googleStorage config
  - To Up the containers use docker and run `docker-compose up -d`
  - Your project should be running at `http://0.0.0.0:8080/`

# Access conntainer
  - To run any code in container use `docker-compose exec web bash`

# Run Tests
  - To run tests use `docker-compose exec web pythonn manage.py test -v 2`
