# HandyRecipes

A recipe webapp containing tasty recipes and a gesture based step treversal feature. By simply showing your indexfinger to the camera you can move trough the different recipe steps. Never get fat, flour and other ingridients spilled over your device ever again, wile keeping your hands free from devices full of bacteria!

## LINK TO DEMONSTRATION OF THE APPLICATION
[![Watch the video](https://img.youtube.com/vi/BjRyf9MhWf4/0.jpg)](https://www.youtube.com/watch?v=BjRyf9MhWf4)

## Imports used and handrecognition class
### OpenCV
Used to access camera from device
### Mediapipe
Mediapipe is used together with open cv to create functions for fingerUp find position and so on described in the mediumarticle below. The most important for us in this project is tp utilize the fingerUp method and connecting it to events suiting our usecases
### Class for drawing nodes and edges, and register fingers, or combination of fingers
The class in the hand_estimation.py is retrieved from the following Medium article: [Hand Detection Tracking in Python using OpenCV and MediaPipe](https://gautamaditee.medium.com/hand-recognition-using-opencv-a7b109941c88)

## Features

### Honorable mention to chatGPT for creating these great bulletpoints

- **Recipe Database**: Recipes are stored in a structured JSON file format, making it easy to add, update, or delete recipes.
- **Recipe Components**: Each recipe consists of components (e.g., "Sauce," "Base") that break down ingredients by portion size.
- **Recipe Steps**: Detailed step-by-step instructions are available for each recipe, allowing for easy replication of the dishes.
- **Streamlit Interface**: A user-friendly interface for browsing and selecting recipes, displaying components, ingredients, and steps.
- **JSON Parsing and Service Layer**: Recipes are dynamically fetched from JSON and converted into custom Python objects, thanks to a dedicated service layer for efficient data handling.
- **Hand Gestures for Scrolling**: Use hand gestures to scroll through recipe pages. This feature uses a hand detection system to recognize gestures like swiping up or down, allowing users to navigate the recipe content without touching their device.

## Project Structure

```
project-root/
├── database/
│   └── recipes.json             # JSON file storing all recipe data
├── models/
│   ├── Recipe.py                # Recipe model with components and ingredients
│   ├── RecipeComponents.py      # RecipeComponents model to represent components of a recipe
│   ├── Ingridient.py            # Ingredient model for individual ingredients
│   └── Steps.py                 # Step model containing step number and description
├── pages/
│   ├── home_page.py             # Streamlit page to display the home page
│   ├── recepies_page.py         # Streamlit page where you can choose what dish you want to displays
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
   git clone https://github.com/your-username/HandyRecipes.git
   cd HandyRecipes
   ```
2. Create and activate viritual environtment
   ```bash
   python3 -m venv <myenvname>
   ```
3. Activate environtment
   ```bash
   source myvenvname/bin/activate
   ```
   
5. **Install Dependencies**:
   - Ensure you have Python 3.7+ and install required libraries:
   ```bash
   pip install -r requirements.txt
   ```

6. **Run the Streamlit Application**:
   ```bash
   streamlit run app.py
   ```

## Usage

- **Browse Recipes**: When entering the recipes page you see all the available recipes that can be browsed
- **View Recipe Details**: Click on a recipe to see detailed components, ingredients, and steps to make the dish.
- **Hand Gesture Navigation**: Use hand gestures to scroll through recipe steps, providing a touch-free navigation experience.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

