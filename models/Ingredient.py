
class Ingredient:
    def __init__(self, name, measurement_type, amount_per_portion):
        self.name = name # Example: "Tomato"
        self.measurement_type = measurement_type # Example: "dl"
        self.amount_per_portion = amount_per_portion # Example: 2.5
    
    def calculate_amount(self, portions):
        return self.amount_per_portion * portions

    def __repr__(self):
        return f"Ingredient(name={self.name}, measurement_type={self.measurement_type}, amount_per_portion={self.amount_per_portion})"

    def __str__(self):
        return f"{self.name} - {self.amount_per_portion} {self.measurement_type}"