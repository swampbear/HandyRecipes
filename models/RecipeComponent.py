class RecipeComponent:
    def __init__(self, name="Name",ingredients={}):
        self.name = name
        self.ingredients_per_portion = ingredients

    def __str__(self):
        return f"{self.name} - {self.ingredients_per_portion}"