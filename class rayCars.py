class RayCars:
    def __init__(self, name, amount_fuel, engine):
        self.name = name
        self.amount_fuel = amount_fuel
        self.engine = engine
      
RC = RayCars("RollsRoyce", 45, "Diesel")

print(RC.name)
print(RC.amount_fuel)
print(RC.engine)
