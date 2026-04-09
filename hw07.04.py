# Завдання 1
# Створіть клас Recipe з атрибутами
#  name – назва страви
#  ingredients – список продуктів
#  text – текст рецепту
#  time – час приготування
# методи:
#  __str__(self) – повертає назву страви
#  __contains__(self, item) – перевіряє чи є інгредієнт в
# рецепті
#  __gt__(self, other) – перевіряє чи є час приготування self
# більшим за other
#  display_info(self) – виводить всю інформацію про рецепт
# Створіть декілька рецептів та добавте їх у список.
# Виведіть назви тих рецептів, які містять інгредієнт томат
# Виведіть повну інформацію рецепта з найменшим часом
# приготування, скористайтесь функцією min
# Приклад рецептів:
# Recipe("Піца",
#  ["борошно", "вода", "дріжджі", "томат", "сир"],
#  "Готуємо тісто, додаємо інгредієнти та запікаємо",
#  30)
#
#  Recipe("Салат",
#  ["томат", "огірок", "зелень", "олія"],
#  "Нарізаємо овочі, додаємо зелень та поливаємо
# олією",
#  10)
#
#  Recipe("Суп",
#  ["вода", "картопля", "морква", "м'ясо"],
#  "Варимо всі інгредієнти до готовності",
#  45)


class Recipe:
    def __init__(self, name: str, ingredients: list, text: str, time: int):
        self._name = name
        self._ingredients = ingredients
        self._text = text
        self._time = time

    def __str__(self):
        return self._name

    def __contains__(self, item):
        return item in self._ingredients

    def __gt__(self, other):
        return self._time > other._time

    def display_info(self):
        print(f"Назва: {self._name}")
        print(f"Інгредієнти: {', '.join(self._ingredients)}")
        print(f"Рецепт: {self._text}")
        print(f"Час приготування: {self._time} хв")


recipes = [
    Recipe(
        "Піца",
        ["борошно", "вода", "дріжджі", "томат", "сир"],
        "Готуємо тісто, додаємо інгредієнти та запікаємо",
        30,
    ),
    Recipe(
        "Салат",
        ["томат", "огірок", "зелень", "олія"],
        "Нарізаємо овочі, додаємо зелень та поливаємо олією",
        10,
    ),
    Recipe(
        "Суп",
        ["вода", "картопля", "морква", "м'ясо"],
        "Варимо всі інгредієнти до готовності",
        45,
    ),
]


print("Рецепти з інгредієнтом 'томат':")
for recipe in recipes:
    if "томат" in recipe:
        print(recipe)


fastest_recipe = min(recipes, key=lambda r: r._time)

print("\nРецепт з найменшим часом приготування:")
fastest_recipe.display_info()
