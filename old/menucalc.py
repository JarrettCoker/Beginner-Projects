# Menu Calculator
# Python 3.5.10
# Written by rsz

# check for amount of items
def print_order(user_order):
    for i in range (1, 10):
        if user_order.count(str(i)) > 0:
            print(str(menulist[i - 1]) + ':' +  str(user_order.count(str(i))))


def print_menu(menu_list, menu_dic):
    print()
    orderNum = 1
    for i in menu_list:
        print(str(orderNum) + '. ' + i + ' - ' +  '$' + str(menu_dic[i]))
        orderNum += 1


# create dictionary
menu = {'Chicken Strips': 3.50, 'French Fries': 2.50, 'Hamburger': 4.00,
        'Hotdog': 3.50, 'Large Drink': 1.75, 'Medium Drink': 1.50,
        'Milk Shake': 2.25, 'Salad': 3.75, 'Small Drink': 1.25}

# list to call dictionary values
menulist = ['Chicken Strips','French Fries', 'Hamburger', 'Hotdog',
            'Large Drink' ,'Medium Drink' ,'Milk Shake', 'Salad', 'Small Drink']

print_menu(menulist, menu)

# main loop
while True:

    # ensure valid user input by requesting integer input before converting to a string
    while True:
        try:
            order = int(input('\nEnter your order: (0 to quit) '))
        except ValueError:
            print("Please enter numbers only.")
        else:
            break

    if order == 0:
        print("Goodbye!")
        break

    # convert user's int input into a string
    order = str(order)

    # print user's order
    print_order(order)

    # calculate total
    total = 0
    for num in order:
        total += float(menu[menulist[int(num) - 1]])

    print('\nThe total is: $', total)
