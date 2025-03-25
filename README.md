# FastAPI Template

This repository serves as a template for building FastAPI applications. It provides a foundational structure and
necessary tools to help you kickstart your project efficiently.

## Features

- **FastAPI Framework**: A modern, fast (high-performance) web framework for building APIs with Python.
- **SQLAlchemy**: Used as the ORM (Object-Relational Mapper) for database interactions.
- **Alembic**: Handles database migrations easily with example migration.
- **Pytest**: Integrated testing framework for reliable and scalable test coverage.
- **Pre-configured Project Structure**: A scalable layout for managing larger FastAPI applications efficiently.

## Quick Start

1. Clone the repository:
   ```bash
   git clone <repository_url>
   ```
2. Navigate to the project directory:
   ```bash
   cd finance
   ```
3. Build the Docker images:
   ```bash
   docker compose build
   ```
4. Start the project:
   ```bash
   docker compose up -d
   ```
5. Create the database:
   ```bash
   docker compose exec postgres psql -U user -d postgres -c "CREATE DATABASE example_db;"
   ```
6. Apply database migrations:
   ```bash
   docker compose exec backend alembic upgrade head
   ```
   
Once all steps are completed, your project will be available at:  
[http://localhost:8000](http://localhost:8000)


## Running Tests

You can verify the functionality of the project by running the tests. There are two ways to do so:

1. **Inside the Docker container** (service should be running):
   ```bash
   docker compose exec backend pytest -n auto
   ```

2. **Locally (if you have Python installed)**:
   Ensure your virtual environment is activated, then run:
   ```bash
   pytest -n auto
   ```

## Notes

- Modify this template to fit the specific needs of your project.
- Use Alembic for managing database migrations (`alembic init` and subsequent commands).
- Expand or customize the structure as required.

## Contributing

Feel free to open issues or submit pull requests to enhance the template.

## License

This project is open-source and available under the [MIT License](LICENSE).
