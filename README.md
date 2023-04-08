# Restaurant API

This api is used to manage restaurants and their menus.
Used techonolgies are: Python, Flask, POSTGRESQL

## Getting Started
- Clone the repository
- Install the requirements and Python 3.11.1
- Activate the virtual environment
- Install PostgreSQL and create a database with the name 'challenge' and a user with the name 'challenge' and password '123456'
- Finally run the index.py file

## Features

- Create a restaurant
- Login to a restaurant
- Update a restaurant
- List all restaurants
- List only one restaurant
- Delete a restaurant

- Create a dish
- List all dishes
- Add a dish to a restaurant
- List dishes from a restaurant
- Update a dish
- Delete a dish
- Add a dish to buy to a restaurant
- Finally buy

## Endpoints
- GET /restaurants - List all restaurants
- POST /register - Create a restaurant
- GET /restaurants/<int:id> - List only one restaurant
- DELETE /restaurants/<int:id> - Delete a restaurant
- POST /login - Login to a restaurant
- POST /logout - Logout to a restaurant
- PATCH /restaurants/<int:id> - Update a restaurant

- GET /dishes - List all dishes
- GET /dishes/<int:id> - List only one dish
- POST /dishes - Create a dish
- GET /dishes/<int:restaurant_id> - List dishes from a restaurant
- PUT /dishes/<restaurant_id>/<int:dish_id> - Update a dish
- DELETE /dishes/<restaurant_id>/<int:dish_id> - Delete a dish
- POST /dishes/<int:restaurant_id>/<int:dish_id>/buy - Add a dish to buy to a restaurant
- GET /dish/buy - Finally buy