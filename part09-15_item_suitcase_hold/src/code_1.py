class Item :
    def __init__(self, name: str, weight: int):
        self.__name = name
        self.__weight = weight
    
    def name(self):
        return self.__name
    
    def weight(self):
        return self.__weight

    def __str__(self):
        return f"{self.__name} ({self.__weight} kg)"

class Suitcase:
    def __init__(self, max_weight: int):
        self.max_weight = max_weight
        self.in_suitcase = []
        self.suitcase_weight = 0

    def add_item(self, item: "Item"):
        if self.suitcase_weight + item.weight() <= self.max_weight:
            self.in_suitcase.append(item)
            self.suitcase_weight += item.weight()


    def __str__(self):
        if len(self.in_suitcase) == 1 :
            return f"{len(self.in_suitcase)} item ({self.suitcase_weight} kg)"
        else:    
            return f"{len(self.in_suitcase)} items ({self.suitcase_weight} kg)"

    def print_items(self):
        for item in self.in_suitcase:
            print(item)

    def weight(self):
        return self.suitcase_weight
    
    def heaviest_item(self):
        heaviest = self.in_suitcase[0]
        if self.in_suitcase == []:
            return None
        else :
            for item in self.in_suitcase:
                if item.weight() >= heaviest.weight():
                    heaviest = item
            return heaviest
        
class CargoHold:
    def __init__(self, max_weight: int):
        self.max_weight = max_weight
        self.in_cargo = []
        self.cargo_weight = 0

    def add_suitcase(self, suitcase: "Suitcase"):
        if self.cargo_weight + suitcase.weight() <= self.max_weight:
            self.in_cargo.append(suitcase)
            self.cargo_weight += suitcase.weight()


    def __str__(self):
        space = self.max_weight - self.cargo_weight
        if len(self.in_cargo) == 1 :
            return f"{len(self.in_cargo)} suitcase, space for {space} kg"
        else:    
            return f"{len(self.in_cargo)} suitcases, space for {space} kg"

    def print_items(self):
        for suitcase in self.in_cargo:
            suitcase.print_items()
            
if __name__ == "__main__":
    
    book = Item("ABC Book", 2)
    phone = Item("Nokia 3210", 1)
    brick = Item("Brick", 4)

    adas_suitcase = Suitcase(10)
    adas_suitcase.add_item(book)
    adas_suitcase.add_item(phone)

    peters_suitcase = Suitcase(10)
    peters_suitcase.add_item(brick)

    cargo_hold = CargoHold(1000)
    cargo_hold.add_suitcase(adas_suitcase)
    cargo_hold.add_suitcase(peters_suitcase)

    print("The suitcases in the cargo hold contain the following items:")
    cargo_hold.print_items()