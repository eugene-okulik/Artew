

class Flower:
    def __init__(self, name, color, price, lifespan, stem_length):
        self.name = name
        self.color = color
        self.price = price
        self.lifespan = lifespan
        self.stem_length = stem_length

    def __str__(self):
        result_str = f'Название: {self.name}, Цвет: {self.color},' \
                     f'Цена: {self.price} руб, Время жизни: {self.lifespan} дней,' \
                     f' Длина стебля: {self.stem_length} см'
        return result_str


class Rose(Flower):
    def __init__(self, color, price, stem_length):
        super().__init__('Роза', color, price, lifespan=10, stem_length=stem_length)


class Gladiolus(Flower):
    def __init__(self, color, price, stem_length):
        super().__init__('Гладиолус', color, price, lifespan=15, stem_length=stem_length)


class Tulip(Flower):
    def __init__(self, color, price, stem_length):
        super().__init__('Тюльпан', color, price, lifespan=20, stem_length=stem_length)


class Daisy(Flower):
    def __init__(self, color, price, stem_length):
        super().__init__('Ромашка', color, price, lifespan=25, stem_length=stem_length)


class Bouquet:
    def __init__(self):
        self.flowers = []

    def add_flower(self, flower):  # Добавляет цветок в букет
        self.flowers.append(flower)

    def average_lifespan(self):  # среднее время жизни всех цветов в букете
        if not self.flowers:
            return 0
        total_lifespan = sum(flower.lifespan for flower in self.flowers)  # Cум.времени жизни всех цветов
        avg_lifespan = total_lifespan / len(self.flowers)
        return avg_lifespan

    def total_price(self):  # Общая стоимость букета
        total = sum(flower.price for flower in self.flowers)
        return total

    def sort_flowers(self, key_function):
        self.flowers.sort(key=key_function)

    def sort_by_fresh(self, flower):
        return flower.lifespan

    def sort_by_color(self, flower):
        return flower.color

    def sort_by_stem_length(self, flower):
        return flower.stem_length

    def sort_by_price(self, flower):
        return flower.price


    def __str__(self):
        flower_details = '\n'.join(str(flower) for flower in self.flowers)
        return (f'Букет состоит из {len(self.flowers)} цветов:\n'
               f'{flower_details}\n'
               f'Общая стоимость букета = {self.total_price()} руб\n'
               f'Среднее время жизни букета {self.average_lifespan():.0f} дней')

# Создание цветов
rose1 = Flower('Роза', 'Красный', 100, 11, 120)
rose2 = Flower('Роза', 'Белый', 200, 2, 230)
gladiolus1 = Flower('Гладиолус','Розовый', 52, 6, 40)
gladiolus2 = Flower('Гладиолус','Синий', 50, 5, 39)
tuple1 = Flower('Тюльпан','Желтый', 71, 3, 60)
tuple2 = Flower('Тюльпан','Белый', 70, 1, 70)
daisy = Flower('Ромашка','Белый', 93, 7, 180)

# Создание букета
my_bouquet = Bouquet()

# Добавление цветов в букет
my_bouquet.add_flower(rose1)
my_bouquet.add_flower(rose2)
my_bouquet.add_flower(gladiolus1)
my_bouquet.add_flower(gladiolus2)
my_bouquet.add_flower(tuple1)
my_bouquet.add_flower(tuple2)
my_bouquet.add_flower(daisy)

# Сортировка по свежести
# my_bouquet.sort_flowers(my_bouquet.sort_by_fresh)

# Сортировка по цвету
#my_bouquet.sort_flowers(my_bouquet.sort_by_color)

# Сортировка по длине стебля
my_bouquet.sort_flowers(my_bouquet.sort_by_stem_length)

# Сортировка по стоимости
#my_bouquet.sort_flowers(my_bouquet.sort_by_price)

print(my_bouquet)
