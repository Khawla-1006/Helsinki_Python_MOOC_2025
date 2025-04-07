# Write your solution here!
class  NumberStats:
    def __init__(self):
        self.numbers = 0
        self.counter = 0
        self.sum = 0
        self.avg = 0

    def add_number(self, number:int):
        self.numbers = number
        self.counter += 1
        self.sum += number
        return self.numbers

    def count_numbers(self):
        return self.counter
    
    def get_sum(self):
        return self.sum
    
    def average(self):
        if self.counter != 0 :
            self.avg = self.sum / self.counter
        return self.avg
    
print("Please type in integer numbers:")
stats = NumberStats()
even  = NumberStats()
odd = NumberStats()

while True :
    user_input = int(input())
    if user_input == -1 :
        break
    stats.add_number(user_input)
    if user_input % 2 == 0 :
        even.add_number(user_input)
    else : 
        odd.add_number(user_input)

print("Numbers added:", stats.count_numbers())
print("Sum of numbers:", stats.get_sum())
print("Mean of numbers:", stats.average())
print("Sum of even numbers:", even.get_sum())
print("Sum of odd numbers:", odd.get_sum())
