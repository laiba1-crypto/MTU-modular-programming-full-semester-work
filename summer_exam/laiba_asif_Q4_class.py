#Name: LAIBA ASIF
#StudentID: R00201303
class ice_cream:
    def __init__(self, flavour, cost, cal):
        self.flavour = flavour
        self.cost_per_scoop = cost
        self.calories_per_scoop = cal

    def __str__(self):
        return (f"{self.flavour} ice cream, cost: €{str(self.cost_per_scoop)}, and have {self.calories_per_scoop:}cal per scoop")

    def describe_cal_per_scoop(self):
        cal = self.calories_per_scoop
        if 0 <= cal <=100:
            return "Light"
        elif 101 <= cal <= 400:
            return "Medium"
        else:
            return "Calorific"