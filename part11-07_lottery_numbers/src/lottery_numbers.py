class LotteryNumbers:
    def __init__(self, week_number: int, week_lottery: list):
        self.week_number = week_number
        self.__correct_lottery_numbers = week_lottery
    
    def number_of_hits(self, numbers: list):
        return len([number for number in numbers if number in self.__correct_lottery_numbers])

    def hits_in_place(self, numbers: list):
        return [number if number in self.__correct_lottery_numbers else -1 for number in numbers]

if __name__ == "__main__":
    week5 = LotteryNumbers(5, [1,2,3,4,5,6,7])
    my_numbers = [1,4,7,11,13,19,24]

    print(week5.number_of_hits(my_numbers))

    week8 = LotteryNumbers(8, [1,2,3,10,20,30,33])
    my_numbers = [1,4,7,10,11,20,30]

    print(week8.hits_in_place(my_numbers))