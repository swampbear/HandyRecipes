# HandyRecipes

A Python-based Recipe Management System designed to organize, display, and interact with recipes through a clean interface built with Streamlit. This project includes a structured JSON-based recipe database, dynamic loading and display of recipes, and customizable layouts for an intuitive browsing experience.

## Features

- **Recipe Database**: Recipes are stored in a structured JSON file format, making it easy to add, update, or delete recipes.
- **Recipe Components**: Each recipe consists of components (e.g., "Sauce," "Base") that break down ingredients by portion size.
- **Recipe Steps**: Detailed step-by-step instructions are available for each recipe, allowing for easy replication of the dishes.
- **Streamlit Interface**: A user-friendly interface for browsing and selecting recipes, displaying components, ingredients, and steps.
- **JSON Parsing and Service Layer**: Recipes are dynamically fetched from JSON and converted into custom Python objects, thanks to a dedicated service layer for efficient data handling.
- **Hand Gestures for altrenating trough steps**: Use hand gestures to manouver between recipe steps

## Project Structure

```
project-root/
├── database/
│   └── recipes.json             # JSON file storing all recipe data
├── models/
│   ├── Recipe.py                # Recipe model with components and ingredients
│   ├── RecipeComponents.py      # RecipeComponents model to represent components of a recipe
│   └── Ingredient.py            # Ingredient model for individual ingredients
│   └── Step.py                  # Step model with stepnumber and description
├── pages/
│   └── recipe_page.py           # Streamlit page to display recipe details
├── service/
│   └── RecipeService.py         # Service layer to fetch and parse JSON recipes
├── app.py                       # Main file to run the Streamlit app
├── .gitignore                   # Git ignore file, ignoring .pyc and __pycache__
└── README.md                    # Project README file
```

### JSON Recipe File (`recipes.json`)

The recipe data is stored in a structured JSON file format within the `database` directory. Each recipe contains:

- **Title and Description**: Basic information about the recipe.
- **Estimated Time** and **Difficulty Level**: Indicators for preparation time and difficulty.
- **Portions**: The serving size of the recipe.
- **Components**: Each recipe can have multiple components (e.g., "Sauce," "Base"), each with its own ingredients.
- **Steps**: A sequential list of steps to prepare the recipe.

### Example Recipe JSON Structure

```json
{
  "recipes": [
    {
      "title": "Spaghetti Carbonara",
      "description": "A classic Italian pasta dish made with eggs, cheese, pancetta, and pepper.",
      "estimated_time": "15-20 min",
      "difficulty": "medium",
      "portions": 2,
      "recipe_components": [
        {
          "name": "Pasta Base",
          "ingredients_per_portion": [
            {
              "name": "Spaghetti",
              "measurement_type": "grams",
              "amount_per_portion": 100
            },
            {
              "name": "Pancetta",
              "measurement_type": "grams",
              "amount_per_portion": 50
            }
          ]
        },
        {
          "name": "Sauce",
          "ingredients_per_portion": [
            {
              "name": "Eggs",
              "measurement_type": "units",
              "amount_per_portion": 1
            },
            {
              "name": "Pecorino Romano",
              "measurement_type": "grams",
              "amount_per_portion": 25
            },
            {
              "name": "Black Pepper",
              "measurement_type": "teaspoon",
              "amount_per_portion": 0.5
            }
          ]
        }
      ],
      "steps": [
        {
          "number": 1,
          "description": "Boil the spaghetti in salted water until al dente."
        },
        {
          "number": 2,
          "description": "In a separate pan, cook the pancetta until crispy."
        },
        {
          "number": 3,
          "description": "Whisk eggs and Pecorino Romano together."
        },
        {
          "number": 4,
          "description": "Combine pasta with pancetta and mix with egg mixture, stirring quickly."
        },
        {
          "number": 5,
          "description": "Serve immediately with extra Pecorino and black pepper."
        }
      ]
    }
  ]
}
```

## Installation

1. **Clone the Repository**:
   ```bash
   git clone https://github.com/your-username/HandyRecipea.git
   cd recipe-management-system
   ```

2. **Install Dependencies**:
   - Ensure you have Python 3.7+ and install required libraries:
   Had some bugs setting up the env with conda. So here you just ned to ran and pipinstall missing dependencies. Working to fix it.

3. **Run the Streamlit Application**:
   ```bash
   streamlit run app.py
   ```

## Usage

- **Browse Recipes**: When the app starts, it displays a home screen, with a nav bar that can be used to reach recepies, settings and about
- **View Recipe Details**: Click on a recipe to see detailed components, ingredients, and steps to make the dish.
- **Hand Gesture Navigation**: Use hand gestures to move trough recipes steps, providing a touch-free navigation experience.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

