class Body:
    def __init__(self, mass, heat_capacity, temperature):
        if mass <= 0:
            mass = 0.01
        if heat_capacity <= 0:
            heat_capacity = 0.01
        if temperature < 0:
            temperature = 0.0

        self.mass = mass
        self.heat_capacity = heat_capacity
        self.temperature = temperature

    def add_heat(self, heat_joules):
        delta_t = heat_joules / (self.mass * self.heat_capacity)
        self.temperature += delta_t
        return self.temperature


if __name__ == "__main__":
    test_body = Body(100, 0.15, 200)
    print(test_body.add_heat(20))
    print(test_body.add_heat(-40))