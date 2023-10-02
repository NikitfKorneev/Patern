class Beverage:
    def cost(self):
        pass

    def description(self):
        pass

class Coffee(Beverage):
    def cost(self):
        return 5.0

    def description(self):
        return "Кофе"

class Tea(Beverage):
    def cost(self):
        return 4.0

    def description(self):
        return "Чай"

class Soda(Beverage):
    def cost(self):
        return 3.0

    def description(self):
        return "Газировка"

class MilkDecorator(Beverage):
    def __init__(self, beverage):
        self._beverage = beverage

    def cost(self):
        return self._beverage.cost() + 2.0

    def description(self):
        return self._beverage.description() + " с молоком"

class SugarDecorator(Beverage):
    def __init__(self, beverage):
        self._beverage = beverage

    def cost(self):
        return self._beverage.cost() + 1.0

    def description(self):
        return self._beverage.description() + " с сахаром"

if __name__ == "__main__":
    print("Выберите напиток:")
    print("1. Кофе")
    print("2. Чай")
    print("3. Газировка")
    choice = input("Введите номер выбранного напитка: ")

    if choice == "1":
        selected_beverage = Coffee()
    elif choice == "2":
        selected_beverage = Tea()
    elif choice == "3":
        selected_beverage = Soda()
    else:
        print("Выбор не распознан, заказ отменен.")
        exit()

    if isinstance(selected_beverage, Coffee) or isinstance(selected_beverage, Tea):
        add_milk = input("Добавить молоко? (y/n): ")
        if add_milk.lower() == "y":
            selected_beverage = MilkDecorator(selected_beverage)

        add_sugar = input("Добавить сахар? (y/n): ")
        if add_sugar.lower() == "y":
            selected_beverage = SugarDecorator(selected_beverage)

    print("Вы заказали:", selected_beverage.description())
    print("Стоимость:", selected_beverage.cost())
