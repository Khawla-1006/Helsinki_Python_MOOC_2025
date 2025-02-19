# Write your solution here
def create_tuple(x: int, y: int, z : int) :
    sum_up = (x,y,z)
    tupled = (min(x,y,z),max(x,y,z),sum(sum_up))
    return tupled


if __name__ == "__main__":
    print(create_tuple(5, 3, -1))
