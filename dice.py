import random 
response = input("Do you want to roll again? If so, press y, if not press n")
response = "y"
while response == 'y':
    no = random.randint(1,6)
    if no == 1:
        print('Number on dice is 1')
    if no == 2:
        print('Number on dice is 2')
    if no == 3:
        print('Number on dice is 3')
    if no == 4:
        print('Number on dice is 4')
    if no == 5:
        print('Number on dice is 5')
    if no == 6:
        print('Number on dice is 6')
    print('\n')