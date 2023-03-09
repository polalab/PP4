from info import Students

our_class = Students()
our_class_bday = our_class.birthday
def linear_search(list):
    # during the class
    today = "03-09"
    for student in list:
        # 1st: student = ("Katrina", "2002-03-16")
        if today == student[1][5::]:
            return student[0]

# O(n)

def linear_search_everyone(list):
    # during the class
    today = "03-09"
    bday_ppl = []
    for student in list:
        # 1st: student = ("Katrina", "2002-03-16")
        if today == student[1][5::]:
            bday_ppl.append(student[0])
    return bday_ppl

# O(n)

def binary_search(data, val):
    # during the class
    low = 0
    high = len(data)-1
    mid = int(high/2)
    while low <= high and data[mid]!= val:
        mid = int((high+low)/2)
        if val < data[mid]:
            high = mid - 1
        else:
            low = mid + 1
    if data[mid] == val:
        return mid
    else:
        return -1

try_out = [3, 7, 8, 10, 13, 40, 69]
print(binary_search(try_out, 20))

def binary_search_for_bday(list):
    # homework
    pass


print(linear_search_everyone(our_class_bday))


