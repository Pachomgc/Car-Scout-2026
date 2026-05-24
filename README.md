# Car Scout

Car Scout is a browser-based car management application built with Python, NiceGUI and SQLAlchemy.

---

# Project Goals

The goal of this project was to develop a modern browser application for managing cars using a clean software architecture with frontend, backend and database layers.

The application allows users to:

- Add cars
- Browse all cars
- Search cars by brand or model
- View car details
- Edit cars
- Delete cars

---

# User Stories

- As a user, I want to add a car so that I can manage my vehicles.
- As a user, I want to browse all cars so that I can view stored vehicles.
- As a user, I want to search for cars so that I can quickly find a specific vehicle.
- As a user, I want to edit cars so that I can update information.
- As a user, I want to delete cars so that I can remove outdated entries.

---

# Use Cases

## Add Car
The user enters car information into a form and saves it into the database.

## Search Cars
The user searches for a car by entering a brand or model name.

## Edit Car
The user updates existing car information using the edit page.

## Delete Car
The user deletes a selected car from the application.

---

# Features

- Browser-based UI
- CRUD operations
- Search functionality
- Form validation
- Responsive layout
- SQLite database
- ORM with SQLAlchemy

---

# Technologies

- Python
- NiceGUI
- SQLAlchemy
- SQLite

---

# Architecture

The project follows a layered architecture.

## Presentation Layer

Located in:

ui/

Contains all frontend pages and NiceGUI components.

## Application Logic Layer

Located in:

services/

Contains business logic and validation.

## Persistence Layer

Located in:

data_access/

Handles database communication and ORM operations.

## Domain Layer

Located in:

domain/

Contains the car model.

---

# Database Model

## Car

| Field | Type |
|---|---|
| id | Integer |
| brand | String |
| model | String |
| year | Integer |
| km | Integer |
| trans | String |
| price | Float |

---

# Validation

The application validates:

- Empty fields
- Invalid years
- Invalid kilometre values
- Invalid prices

---

# Project Structure

ui/                -> frontend pages

services/          -> business logic

data_access/       -> database access

domain/            -> models

---

# Installation

Install requirements:

pip install -r requirements.txt

Run the application:

python app.py

---

# Team Distribution

## Michael

- Backend logic
- CRUD implementation
- Search functionality
- Edit functionality
- Validation logic
- Database integration

## Francisco

- UI improvements
- Layout styling
- Navigation bar
- README and documentation
- Frontend polishing

---

# Challenges

Some challenges during development included:

- Structuring the project into layers
- Connecting NiceGUI with the database
- Implementing edit and delete functionality
- Creating responsive UI layouts
- Handling validation correctly

---

# Future Improvements

Possible future improvements:

- User authentication
- Image upload for cars
- Advanced filters
- Sorting functionality
- REST API integration

---

# GitHub

GitHub repository:

https://github.com/Pachomgc/Car-Scout-2026