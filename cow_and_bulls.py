import random
random_number = random.randint(999, 10000)
random_number_list = [int(i) for i in str(random_number)]
print(random_number_list)


def cow_and_bulls():
    cow = 0
    bull = 0
    while cow != 4:
        user_number = str(input("Print your number for 4 symbols: "))
        user_number_list = [int(q) for q in str(user_number)]
        for x in random_number_list:
            for y in user_number_list:
                if x == y and random_number_list.index(x) == user_number_list.index(y):
                    cow += 1
                elif x == y and random_number_list.index(x) != user_number_list.index(y):
                    bull += 1
        print("cow: ", cow)
        print("bull: ", bull)
        return cow, bull


cow_and_bulls()