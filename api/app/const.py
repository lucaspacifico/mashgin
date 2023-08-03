APP_DESCRIPTION = """
The "Simple Checkout Order System" is done by incorporating a few practices from Domain-Driven Design (DDD) and Repository Pattern on the server side, 
while utilizing the Vue.js framework on the client side.

Server App with DDD, Repository Pattern:
The server app architecture follows Domain-Driven Design principles, which organizes the codebase around the core business logic and domain entities.
It also adopts the Repository Pattern to separate data access concerns from the domain logic.

Domain Layer: The Domain Layer forms the core of the application and contains domain entities, aggregates, and value objects. 
Infrastructure layer: The Infrastructure layer is responsable for defining the basics of the infra in the application. Example, the postgres database
Models: Defines The Models layers is a structure of the models that will be used as datamodels by the entities.
Repository Layer: The Repository Layer abstracts the data access logic from the rest of the application. Applying an abstraction from the SqlAlchemy.
Service Layer: The Service Layer provides services that don't fit directly into the domain entities or use cases but are still relevant to the application.

Client Side with Vue.js:
The client-side of the "Simple Checkout Order System" is built using the Vue.js framework, known for its simplicity, reactivity, and component-based architecture.

"""

MENU_GET_DESCRIPTION = (
    "If menu_id equals to 0 ( zero ) it will be returned the last created menu"
)

ORDER_GET_DESCRIPTION = (
    "If order_id equals to 0 ( zero ) it will be returned the last created order"
)

GET_ALL_ORDERS_DESCRIPTION = (
    "Return all created orders"
)
