list1 = [1,2,3,4,5,6,7,8,9,10]
print(list1)
even_num = (x for x in list1 if x%2 ==0)
for num in even_num:
    print(num,end=" ")

items = ["apple", "banana", "cherry","grapes","Kiwi","oranges","honey"]
prices = [0.5, 0.3, 0.2]
my_dict = {key:value for key,value in zip(items,prices)}
print(my_dict)

scores = {"math": 80, "science": 90, "english": 75}
passed = {k:v for k,v in scores.items() if v>=80}
print(passed)


list2 =[]
for x in [1,2]:
    for y in [3,4]:
        list2.append((x,y))
print(list2)     


def get_numbers():
    for i in range(5):
        yield i


for num in get_numbers():
    print(num)        
   
def read_lines(filepath):
    with open(filepath) as file:
        for line in file:
            yield line.strip().lower()


for line in read_lines(aiojidihohs):
    print(line)            
