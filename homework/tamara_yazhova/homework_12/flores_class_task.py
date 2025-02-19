import random


class Flower:
    def __init__(self, name, color, freshness, stem_length, lifetime, price):
        self.name = name
        self.color = color
        self.freshness = freshness
        self.stem_length = stem_length
        self.lifetime = lifetime
        self.price = price

    def __str__(self):
        return (
            f"{self.name}, цвет: {self.color}, свежесть: {self.freshness}, "
            f"длина стебля: {self.stem_length} см, время жизни: {self.lifetime} дней, цена: {self.price}$"
        )


class Rose(Flower):
    def __init__(self, name, color, freshness, stem_length):
        super().__init__(name, color, freshness, stem_length, lifetime=random.randint(5, 12), price=3)


class Tulip(Flower):
    def __init__(self, name, color, freshness, stem_length):
        super().__init__(name, color, freshness, stem_length, lifetime=random.randint(7, 14), price=6)


class Lavender(Flower):
    def __init__(self, name, color, freshness, stem_length):
        super().__init__(name, color, freshness, stem_length, lifetime=random.randint(7, 14), price=4)


class Lily(Flower):
    def __init__(self, name, color, freshness, stem_length):
        super().__init__(name, color, freshness, stem_length, lifetime=random.randint(7, 15), price=5)


class Bouquet:
    def __init__(self):
        self.flowers = []

    def make_bouquet(self, flower):
        self.flowers.append(flower)

    def calculate_price(self):
        return sum(flower.price for flower in self.flowers)

    def average_lifetime(self):
        return sum(flower.lifetime for flower in self.flowers) / len(self.flowers)

    def find_flowers(self, key, value):
        return [flower for flower in self.flowers if getattr(flower, key) >= value]

    def sort_flowers(self, key):
        self.flowers.sort(key=lambda flower: getattr(flower, key))

    def __str__(self):
        result = []
        for flower in self.flowers:
            result.append(str(flower))
        return "\n".join(result)


rosa_1 = Rose('White Roses', 'white', 2, 30)
tulip_1 = Tulip("Parrit Tulip", "red", 3, 27)
lavender_1 = Lavender("French Lavender", "violet", 1, 23)
lily_1 = Lily("Tiger Lily", "yellow", 4, 34)
rosa_2 = Rose("Red rose", "red", 3, 29)
tulip_2 = Tulip("Yellow Tulip", "yellow", 2, 25)

print(rosa_1)
print(tulip_1)
print(lavender_1)

bouquet_1 = Bouquet()
bouquet_1.make_bouquet(rosa_1)
bouquet_1.make_bouquet(tulip_1)
bouquet_1.make_bouquet(tulip_2)

print("\nБукет:")
print(bouquet_1)
print(f"Цена букета: {bouquet_1.calculate_price()}$")
print(f"\nУвядяет в среднем через {round(bouquet_1.average_lifetime(), 2)} дней")

expensive_flowers = bouquet_1.find_flowers("price", 5)
print("\nЦветы дороже 5$")
for flower in expensive_flowers:
    print(flower)

resistant_flowers = bouquet_1.find_flowers("lifetime", 10)
print("\nЦветы, которые не вянут более 10 дней:")
for flower in resistant_flowers:
    print(flower)

print("\nБукет отсортирован по цене:")
bouquet_1.sort_flowers("price")
print(bouquet_1)

print("\nБукет отсортирован по свежести:")
bouquet_1.sort_flowers("freshness")
print(bouquet_1)
