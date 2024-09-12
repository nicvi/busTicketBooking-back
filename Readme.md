# Bus Ticket Booking App

## Overview
The Bus Ticket Booking App is designed to simplify the process of reserving bus tickets online, allowing users to choose from various routes, dates, and buses. The system enables smooth trip management, route scheduling, and user bookings, while ensuring a clean and maintainable codebase with a focus on scalability.

## Features
- **Bus Routes Management**: Select routes between multiple cities, with flexible scheduling.
- **User Bookings**: Easily search, book, and manage tickets for specific dates and buses.
- **Trip Scheduling**: Manage bus trips, routes, and available seats in real-time.
- **Amenity Selection**: Offer buses with specific amenities (e.g., WiFi, USB charging).

## Project Structure
This project follows **Clean Architecture** principles, aiming to keep the code modular, scalable, and easy to maintain.

- **Domain Layer**: Contains the core business logic and entities, such as `User`, `Bus`, `Trip`, and `Booking`. This layer is independent of frameworks and databases.
- **Application Layer**: Responsible for handling use cases and defining input/output contracts between the Domain and other layers.
- **Interface Layer**: Contains the web framework integration ([FastAPI](https://fastapi.tiangolo.com/)), and DTOs to facilitate communication between the UI and business logic.
- **Infrastructure Layer**: Includes implementations like repositories, database models, and third-party integrations (e.g., PostgreSQL, Docker).

## Technologies
- **Backend**: [FastAPI](https://fastapi.tiangolo.com/)
- **Database**: PostgreSQL (with Docker for containerized environments)
- **ORM**: SQLAlchemy for database interactions, Alembic for migrations
- **Frontend**: (Optional) React for UI (if applicable)
- **Testing**: Pytest for unit testing
- **Others**: Uvicorn for running the application

## Getting Started

### Prerequisites
- Python 3.9+
- Docker (for running the database)

### Installation
1. Clone the repository:
   ```bash
   git clone <repository-url>
   cd bus-ticket-booking-app
    ```

2. Install dependencies:
   ```bash
   make install
    ```

3. Set up the PostgreSQL database:
   ```bash
   make create-db
    ```
4. Run database migrations:
   ```bash
   make run-migrations
    ```

5. Start the application:
   ```bash
   make run
    ```

6. Start the application:

    To run the database with Docker Compose:
   ```bash
   make run-db
    ```
