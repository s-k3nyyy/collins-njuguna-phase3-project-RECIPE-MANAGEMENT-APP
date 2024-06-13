import click
from database.db_manager import DBManager

DBManager.db_name = 'recipe_manager.db'
db = DBManager()

def main_menu():
    while True:
        click.secho("\nWelcome to the Recipe Manager CLI!", fg="green", bold=True)
        click.secho("Please choose an option:", fg="cyan")
        click.secho("1. Add User", fg="yellow")
        click.secho("2. Change Password", fg="yellow")
        click.secho("3. List Users", fg="yellow")
        click.secho("4. Delete User", fg="yellow")
        click.secho("5. Update User Email", fg="yellow")
        click.secho("6. Add Recipe", fg="yellow")
        click.secho("7. List Recipes", fg="yellow")
        click.secho("8. Delete Recipe", fg="yellow")
        click.secho("9. Add Favorite Recipe", fg="yellow")
        click.secho("10. List Favorite Recipes", fg="yellow")
        click.secho("11. Delete Favorite Recipe", fg="yellow")
        click.secho("12. Search ingredients by recipe name", fg="yellow")
        click.secho("13. List Reviews", fg="yellow")
        click.secho("14. Add Review", fg="yellow")
        click.secho("15. Delete Review", fg="yellow")
        click.secho("0. Exit", fg="red")
        
        choice = click.prompt(click.style("Enter your choice", fg="blue"), type=int)

        if choice == 1:
            add_user()
        elif choice == 2:
            change_password()
        elif choice == 3:
            list_users()
        elif choice == 4:
            delete_user()
        elif choice == 5:
            update_user()
        elif choice == 6:
            add_recipe()
        elif choice == 7:
            list_recipes()
        elif choice == 8:
            delete_recipe()
        elif choice == 9:
            add_favorite()
        elif choice == 10:
            list_favorites()
        elif choice == 11:
            delete_favorite()
        elif choice == 12:
            search_recipes()
        elif choice == 13:
            list_reviews()
        elif choice == 14:
            add_review()
        elif choice == 15:
            delete_review()
        elif choice == 0:
            click.secho("Exiting...", fg="red")
            break
        else:
            click.secho("Invalid choice. Please try again.", fg="red")

def add_user():
    """Add a new user to the system."""
    username = click.prompt(click.style("Enter username", fg="blue"))
    email = click.prompt(click.style("Enter email", fg="blue"))
    password = click.prompt(click.style("Enter password", fg="blue"), hide_input=True)
    query = "INSERT INTO users (username, email, password) VALUES (?, ?, ?)"
    db.execute_query(query, (username, email, password))
    click.secho(f'Success! User "{username}" has been added.', fg="green")

def change_password():
    """Change user's password."""
    username = click.prompt(click.style("Enter username", fg="blue"))
    old_password = click.prompt(click.style("Enter old password", fg="blue"), hide_input=True)
    new_password = click.prompt(click.style("Enter new password", fg="blue"), hide_input=True)
    query = "SELECT password FROM users WHERE username = ?"
    result = db.fetch_all(query, (username,))

    if result:
        current_password = result[0][0]

        if old_password == current_password:
            update_query = "UPDATE users SET password = ? WHERE username = ?"
            db.execute_query(update_query, (new_password, username))
            click.secho(f"Password for user '{username}' successfully updated.", fg="green")
        else:
            click.secho("Old password does not match the current password.", fg="red")
    else:
        click.secho(f"User '{username}' not found.", fg="red")

def list_users():
    """List all users in the system."""
    query = "SELECT * FROM users"
    users = db.fetch_all(query)
    if users:
        click.secho("Here are all the users:", fg="cyan")
        for user in users:
            click.secho(f'User ID {user[0]}: {user[1]} - {user[2]}', fg="yellow")
    else:
        click.secho("No users found.", fg="red")

def delete_user():
    """Delete a user from the system."""
    username = click.prompt(click.style("Enter username", fg="blue"))
    query = "DELETE FROM users WHERE username = ?"
    db.execute_query(query, (username,))
    click.secho(f'User "{username}" has been deleted.', fg="green")

def update_user():
    """Update a user's email."""
    username = click.prompt(click.style("Enter username", fg="blue"))
    new_email = click.prompt(click.style("Enter new email", fg="blue"))
    query = "UPDATE users SET email = ? WHERE username = ?"
    db.execute_query(query, (new_email, username))
    click.secho(f'Email updated for user "{username}".', fg="green")

def add_recipe():
    """Add a new recipe to the collection."""
    recipe_name = click.prompt(click.style("Enter recipe name", fg="blue"))
    ingredients = click.prompt(click.style("Enter ingredients (comma-separated)", fg="blue"))
    query = "INSERT INTO recipes (recipe_name, ingredients) VALUES (?, ?)"
    db.execute_query(query, (recipe_name, ingredients))
    click.secho(f'Success! Recipe "{recipe_name}" has been added.', fg="green")

def list_recipes():
    """List all recipes in the collection."""
    query = "SELECT * FROM recipes"
    recipes = db.fetch_all(query)
    if recipes:
        click.secho("Here are all the recipes:", fg="cyan")
        for recipe in recipes:
            click.secho(f'Recipe ID {recipe[0]}: {recipe[1]}', fg="yellow")
    else:
        click.secho("No recipes found.", fg="red")

def delete_recipe():
    """Delete a recipe from the collection."""
    recipe_id = click.prompt(click.style("Enter recipe ID", fg="blue"), type=int)
    query = "DELETE FROM recipes WHERE recipe_id = ?"
    db.execute_query(query, (recipe_id,))
    click.secho(f"Recipe ID {recipe_id} deleted from the collection.", fg="green")

def add_favorite():
    """Add a recipe to favorites using recipe name and username."""
    recipe_name = click.prompt(click.style("Enter recipe name", fg="blue")).strip()
    username = click.prompt(click.style("Enter username", fg="blue")).strip()

    query_recipe = "SELECT recipe_id FROM recipes WHERE recipe_name = ?"
    recipe = db.fetch_all(query_recipe, (recipe_name,))
    
    if not recipe:
        click.secho(f'No recipe found with the name "{recipe_name}".', fg="red")
        return
    
    recipe_id = recipe[0][0]


    query_user = "SELECT user_id FROM users WHERE username = ?"
    user = db.fetch_all(query_user, (username,))
    
    if not user:
        click.secho(f'No user found with the username "{username}".', fg="red")
        return
    
    user_id = user[0][0]

    # Adds to favorites
    query_favorite = "INSERT INTO favorites (user_id, recipe_id) VALUES (?, ?)"
    db.execute_query(query_favorite, (user_id, recipe_id))

    click.secho(f'Recipe "{recipe_name}" added to favorites for user "{username}" successfully.', fg="green")

def list_favorites():
    """List all favorite recipes for a user."""
    user_id = click.prompt(click.style("Enter user ID", fg="blue"), type=int)
    query = """
        SELECT r.recipe_id, r.recipe_name, r.ingredients 
        FROM recipes r 
        JOIN favorites f ON r.recipe_id = f.recipe_id 
        WHERE f.user_id = ?
    """
    favorites = db.fetch_all(query, (user_id,))
    if favorites:
        click.secho(f"Favorite recipes for User ID {user_id}:", fg="cyan")
        for favorite in favorites:
            click.secho(f"Recipe ID {favorite[0]}: {favorite[1]}", fg="yellow")
            click.secho(f"Ingredients: {favorite[2]}", fg="yellow")
    else:
        click.secho("No favorite recipes found.", fg="red")

def delete_favorite():
    """Delete a recipe from favorites for a user."""
    user_id = click.prompt(click.style("Enter user ID", fg="blue"), type=int)
    recipe_id = click.prompt(click.style("Enter recipe ID", fg="blue"), type=int)
    query = "DELETE FROM favorites WHERE user_id = ? AND recipe_id = ?"
    db.execute_query(query, (user_id, recipe_id))
    click.secho(f"Recipe ID {recipe_id} deleted from favorites for User ID {user_id}.", fg="green")

def search_recipes():
    """Search ingredients by recipe name."""
    search_term = click.prompt(click.style("Enter recipe name", fg="blue")).strip()
    query = "SELECT recipe_name, ingredients FROM recipes WHERE recipe_name LIKE ? COLLATE NOCASE"
    recipes = db.fetch_all(query, ('%' + search_term +    '%',))
    
    if recipes:
        click.secho(f"Recipes matching '{search_term}':", fg="cyan")
        for recipe in recipes:
            click.secho(f"Recipe: {recipe[0]}", fg="yellow")
            click.secho(f"Ingredients: {recipe[1]}", fg="yellow")
    else:
        click.secho(f"No recipes found matching '{search_term}'.", fg="red")

def list_reviews():
    """List all reviews in the system."""
    query = "SELECT * FROM reviews"
    reviews = db.fetch_all(query)
    if reviews:
        click.secho("Here are all the reviews:", fg="cyan")
        for review in reviews:
            click.secho(f'Review ID {review[0]}: User ID {review[1]}, Recipe ID {review[2]}, Rating {review[3]}, Comment: {review[4]}', fg="yellow")
    else:
        click.secho("No reviews found.", fg="red")

def add_review():
    """Add a review for a recipe."""
    user_id = click.prompt(click.style("Enter user ID", fg="blue"), type=int)
    recipe_id = click.prompt(click.style("Enter recipe ID", fg="blue"), type=int)
    rating = click.prompt(click.style("Enter rating (1-5)", fg="blue"), type=int, default=5)
    comment = click.prompt(click.style("Enter comment", fg="blue"), default="")
    query = "INSERT INTO reviews (user_id, recipe_id, rating, comment) VALUES (?, ?, ?, ?)"
    db.execute_query(query, (user_id, recipe_id, rating, comment))
    click.secho('Review added successfully.', fg="green")

def delete_review():
    """Delete a review from the system."""
    review_id = click.prompt(click.style("Enter review ID", fg="blue"), type=int)
    query = "DELETE FROM reviews WHERE review_id = ?"
    db.execute_query(query, (review_id,))
    click.secho(f"Review ID {review_id} deleted from the system.", fg="green")

if __name__ == '__main__':
    main_menu()
