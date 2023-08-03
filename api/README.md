# Mashgin - Restaurant App

## About

The app is done by incorporating a few practices from Domain-Driven Design (DDD) and Repository Pattern on the server side, while utilizing the React framework on the client side.

> Server App with DDD, Repository Pattern:
>
> - The server app architecture follows Domain-Driven Design principles, which organizes the codebase around the core business logic and domain entities.
> - The Repository Pattern is used to separate data access concerns from the domain logic.

- Domain Layer: The Domain Layer forms the core of the application and contains domain entities, aggregates, and value objects. 
- Infrastructure layer: The Infrastructure layer is responsable for defining the basics of the infra in the application. Example, the postgres database
- Models: Defines The Models layers is a strucutre of the models that will be used as datamodels by the entities.
- Repository Layer: The Repository Layer abstracts the data access logic from the rest of the application. Applying an abstraction from the SqlAlchemy.
- Service Layer: The Service Layer provides services that don't fit directly into the domain entities or use cases but are still relevant to the application.

> Client Side with Vue.js:
>
> - The client-side of the "Restaurant App" is built using the Vue.js framework, known for its simplicity, reactivity, and component-based architecture.

## API Documentation	

### Entrypoint
```shell
http://localhost:8000/docs
```

![api_documentation](/resources/api_documentation.png)

Discover the FastAPI app documentation at {$URL}:8000/docs. FastAPI offers interactive auto-generated documentation, allowing you to explore API endpoints, input parameters, and responses. Test the API directly from the documentation and experiment with different inputs. It's basically  a swagger UI.

## Running the Application

```shell
docker-compose up -d --build backend
```

It will run the back-end application.

## Populating the database

In Docker Compose, volumes are used to persist data and share files between containers and the host machine. They provide a way to store data outside the container's writable layer, making it independent of the container's lifecycle. This allows data to be preserved even if the container is stopped, restarted, or replaced.

### First Solution

On Ubuntu or Debian-based systems, you can install `make` using the package manager `apt`. Open a terminal and run:

```shell
sudo apt update
sudo apt install make
```

Once `make` is installed, you can use it by calling make `make help` to see the existing command available. But, for this scenario, run:

```shell
make run-populate-database
```

### Second Solution


1. ```shell
   chmod +x resources/populate_database.sh
   ```

2. ```shell
   sh resources/populate_database.sh
   ```

A CURL call will be performed to insert the data in the database through the application. I chose to use it to follow the concept of "dog food", using the same entrance door ("food") as the customer.

## Executing tests

Pytest is a simple, scalable testing framework in Python. It encourages writing readable tests without complex classes or fancy constructs, making them easy to maintain. Just run:

```shell
make run-backend-tests
```

## Improvement points

Points that I consider to be improved for the future and some decisions that were taken:

- I didn't add many constraints to the database because I was not sure how the application might evolve in future stages. For this reason, the database ended up being more open to new ideas.
- Apply dependency injection to some service layers and the repository. I did it in a simpler way to avoid the need for abstract classes or any additional complexity.
- Increase test coverage and fix the bugs that were found.
- Include CI/CD routines in the code.
- Improving the payment flow and its structure, I ended up putting a very basic payment flow because we would not have an information being processed. I ended up adding some parts to accept more than one payment method per order, but this is also an evolution for the future.
