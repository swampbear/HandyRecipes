import streamlit as st
from models.Recipe import Recipe
from app_pages.recipe_page import RecipePage
from service.RecipeService import RecipeService

def fetch_recipes():
    recipe_service = RecipeService("database/recipes.json")
    return recipe_service.load_recipes_from_database()

def recipes_page():
    recipes = fetch_recipes()

    # Header section with centered text
    html = """\
        <div style="
        padding: 5px 10px; 
        text-align: center; 
        max-width: 50%; 
        margin: 0 auto 20px auto;
        border-radius: 22px;
        background-color: {};
        ">
        <h1>Browse Recipes</h1>
        <p>Choose a recipe you like from the list below:</p>
        </div>
    """.format(st.get_option("theme.secondaryBackgroundColor"))

    st.markdown(html, unsafe_allow_html=True)

    # Initialize session state for selected recipe
    if "selected_recipe" not in st.session_state:
        st.session_state.selected_recipe = None

    num_columns = 10
    columns = st.columns(num_columns)

    # Display recipe options in columns
    for index, recipe in enumerate(recipes):
        col = columns[index+3]  # Cycle through columns for each recipe

        with col:
            # Center the button within the column and limit the width
            if st.button(recipe.title, key=index, help="Click to view this recipe"):
                st.session_state.selected_recipe = recipe  # Set the selected recipe in session state

    # Display the selected recipe using RecipePage
    if st.session_state.selected_recipe:
        page = RecipePage(st.session_state.selected_recipe)
        page.display_recipe()

if __name__ == "__main__":
    recipes_page()
