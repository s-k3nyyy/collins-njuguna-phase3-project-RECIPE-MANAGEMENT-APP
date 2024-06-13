# Recipe Manager CLI

The Recipe Manager CLI is a powerful command-line tool for managing recipes, users, and reviews. It allows you to perform various actions related to your recipe collection directly from the terminal.

## Installation

1. Clone the repository to your local machine:
   ```bash
   git clone <repository_url>
   ```

### Navigate to the project directory:

cd recipe_manager

## Create and activate a virtual environment using Pipenv (Python 3.8):

pipenv --python 3.8
pipenv shell
Install dependencies:

pipenv install click

### Initialize the database:

python cli.py
Usage

### User Management

Add a new user:

python cli.py add-user "username" "email" "password"

### List all users:

python cli.py list-users

### Delete a user:

python cli.py delete-user "username"

### Update a user’s email:

python cli.py update-user "username" "new_email"

### Recipe Management

Add a new recipe:

bash
Copy code
python cli.py add-recipe "recipe_name" "ingredients"

### List all recipes:

python cli.py list-recipes

### Search for recipes containing a specified item:

python cli.py search-recipes "search_term"

### Delete a recipe from the collection:

python cli.py delete-recipe recipe_id
Review Management

### Add a review for a recipe:

python cli.py add-review user_id recipe_id --rating 4 --comment "Delicious recipe!"

### List all reviews:

python cli.py list-reviews

### Delete a review from the system:

python cli.py delete-review review_id

### Favorites Management

Add a recipe to favorites:

python cli.py add-favorite recipe_id user_id

### List all favorite recipes for a user:

python cli.py list-favorites user_id

### Delete a recipe from favorites for a user:

python cli.py delete-favorite user_id recipe_id

### Change Password

Change a user’s password:
python cli.py change-password username old_password new_password

## Features

-Robust User Management: Easily add, list, delete, and update user accounts.
-Efficient Recipe Management: Add new recipes, list existing recipes, and search by ingredients.
-Comprehensive Review System: Add and list reviews, and delete individual reviews.
-Convenient Favorites Management: Add, list, and delete favorite recipes.
-Secure Password Change: Change a user’s password with old password verification.

This README provides an overview of the Recipe Manager CLI, its installation, usage, and features. For more detailed instructions and information, please refer to the command-specific help options available in the CLI.
