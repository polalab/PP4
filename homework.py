from info import Students

#Apply the binary search algorithm to the bday problem. In order to have a sorted list use the method ```sort_bday``` that will return a sorted birthday property
whose_birthday = Students()
search_bday = whose_birthday.birthday

sorted_bday = whose_birthday.sort_bday()
print(sorted_bday)

#my plan
#data - is my data the whole list with tuples? probably because we need the names as well - self?
#val - the value is only the date we want -> date[1][5::]?
#low - the first "date[1][5::]" for the first tuple or the whole tuple?
#high - the last "date[1][5::]" for the last tuple or the whole last tuple?
#mid - the "date[1][5::]" for (low + high) // 2 or the whole mid tuple?
#while low<=high and middle != the value
#assign mid to the middle date[[1][5::]
# if the date we are looking for is smaller than mid
# the high changes to mid-1
#else low changes to mid+1
# if the date we are looking for is equal to the mid
#we return a string, etc name[0]
#if there isnt anyone with a birthday we are looking for, return no one

def binary_search_for_bday(list, their_birthday):
    low = 0
    high = len(list) - 1
    #mid = int(high / 2)
    while low <= high:
        mid = (low + high) // 2
        midm = list[mid][1][5::]
        if their_birthday == midm:
            return list[mid][0]
        if their_birthday > midm:
            low = mid + 1
        else:
            high = mid - 1
    return "no one"

print(binary_search_for_bday(sorted_bday, "02-23"))