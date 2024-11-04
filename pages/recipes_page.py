import streamlit as st
from models.Recipe import Recipe
from pages.recipe_page import RecipePage
from service.RecipeService import RecipeService

def fetch_recipes():
    recipe_service = RecipeService("database/recipes.json")
    return recipe_service.load_recipes_from_database()

def recipes_page():
    recipes = fetch_recipes()

    st.title("Browse Recipes")
    st.write("Choose a recipe you like from the list below:")

    # Initialize session state for selected recipe
    if "selected_recipe" not in st.session_state:
        st.session_state.selected_recipe = None

    # Define the number of columns per row
    num_columns = 5  # Adjust based on your layout preference
    columns = st.columns(num_columns)

    # Display recipe options in columns
    for index, recipe in enumerate(recipes):
        col = columns[index % num_columns]  # Cycle through columns for each recipe

        with col:
            if st.button(recipe.title, key=index):
                st.session_state.selected_recipe = recipe  # Set the selected recipe in session state

    # Display the selected recipe using RecipePage
    if st.session_state.selected_recipe:
        page = RecipePage(st.session_state.selected_recipe)
        page.display_recipe()

        if st.button("Go Back"):
            st.session_state.selected_recipe = None

if __name__ == "__main__":
    recipes_page()