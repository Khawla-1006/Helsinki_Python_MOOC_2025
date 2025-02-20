# write your solution here
def matrix_read(file : str) :
    f =[]
    with open(file) as matrix_file :
        for line in matrix_file :
            line = line.replace("\n", "")
            new_line = line.split(",")
            f.append(new_line)
    print(f)
    return f

def matrix_sum() :
    sum_up = 0
    all = 0
    list = matrix_read("matrix.txt")
    for r in list :
        for s in r :
            sum_up += int(s)
    all += sum_up
    return all

def matrix_max():
    my_list = matrix_read("matrix.txt")
    m = []
    for line in my_list :
        mx = max(line)
        m.append(mx)
    max_list = max(m)
    return int(max_list)

def row_sums():
    sum_list = []
    my_l = matrix_read("matrix.txt")
    for row in my_l :
        l = []
        for r in row:
            s = int(r)
            l.append(s)
        sum_list.append(sum(l))
    return sum_list

if __name__ == "__main__":
    matrix_max()
    matrix_sum()
    row_sums()
