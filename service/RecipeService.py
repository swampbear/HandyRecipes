# recipeservice.py
import json
from models.Recipe import Recipe
from models.RecipeComponent import RecipeComponent
from models.Step import Step
from models.Ingredient import Ingredient

class RecipeService:
    def __init__(self, file_path):
        self.file_path = file_path

    def load_recipes_from_database(self):
        """Load and parse recipes from a JSON file."""
        with open(self.file_path, 'r') as file:
            data = json.load(file)
            
        recipes = []
        for recipe_data in data['recipes']:
            # Parse components and ingredients
            components = [
                RecipeComponent(
                    name=component_data['name'],
                    ingredients=[
                        Ingredient(
                            name=ingredient_data['name'],
                            measurement_type=ingredient_data['measurement_type'],
                            amount_per_portion=ingredient_data['amount_per_portion']
                        )
                        for ingredient_data in component_data['ingredients_per_portion']
                    ]
                )
                for component_data in recipe_data['recipe_components']
            ]
            
            # Parse steps
            steps = [
                Step(
                    number=step_data['number'],
                    description=step_data['description']
                )
                for step_data in recipe_data['steps']
            ]
            
            # Create Recipe instance
            recipe = Recipe(
                title=recipe_data['title'],
                description=recipe_data['description'],
                estimated_time=recipe_data['estimated_time'],
                difficulty=recipe_data['difficulty'],
                recipe_components=components,
                steps=steps,
                portions=recipe_data['portions']
            )
            
            recipes.append(recipe)
            
        return recipes