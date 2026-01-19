class Distance:
    conversion_dict = {
        "cm": 0.01,
        "m": 1,
        "km": 1000,
    }

    def __init__(self, value, unit):
        self.value = value
        self.unit = unit

    def to_meters(self):
        factor = Distance.conversion_dict.get(self.unit)
        if factor is None:
            raise ValueError(f"Неизвестная единица измерения: {self.unit}")
        return self.value * factor

    def __str__(self):
        return f"{self.value} {self.unit}"

    def __add__(self, other):
        if not isinstance(other, Distance):
            return NotImplemented

        total_meters = self.to_meters() + other.to_meters()

        return Distance(total_meters / Distance.conversion_dict[self.unit], self.unit)


d1 = Distance(10, "m")
d2 = Distance(2, "km")
d3 = Distance(500, "cm")

print(d1)
print(d2)
print(d3)

# сложение
sum1 = d1 + d2
print(sum1)

sum2 = d2 + d3
print(sum2)
