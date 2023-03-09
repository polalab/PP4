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
def binary_search(list):
    # during the class
    pass

def binary_search_for_bday(list):
    # homework
    pass

print(linear_search_everyone(our_class_bday))