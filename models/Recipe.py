class Recipe():
    def __init__(self, title="title", description="description", estimated_time="20-30 min", difficulty="hard",portions=1,recipe_components={}, steps={}):
        self.title = title
        self.description = description
        self.estimated_time = estimated_time
        self.difficulty = difficulty
        self.portions = portions
        self.recipe_components = recipe_components
        self.steps = steps

    def __repr__(self):
        return f"<Recipe(title='{self.title}', description='{self.description}')>"
