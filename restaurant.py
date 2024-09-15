import json
import pprint

with open('menu.json', 'r') as f:
    data = json.load(f)


items = data.get('items', [])
while True:
    print('-'*40)
    print('Motilal Cafe and Restaurant')
    print('-'*40)
    print('1. Show Menu')
    print('2. Order Items')
    print('3. Update Menu')
    print('4. Add Review')
    print('5. Exit')
    print('-'*40)

    choice = int(input())

    if choice == 1:
        print('-'*40)
        print('ID\tName\t\tPrice')
        print('-'*40)
        for item in items:
            print(f'{item.get("id")}\t{item.get("name")}\t{item.get("price")}')
        print('-'*40)
    elif choice == 2:
        order_items = list(map(int, input('What you want to try today? ').split(',')))
        print('-'*40)
        print('ID\tName\t\tPrice')
        print('-'*40)
        total_bill = 0

        for order_item in order_items:
            for item in items:
                if item['id'] == order_item:
                    print(f'{item.get("id")}\t{item.get("name")}\t{item.get("price")}')
                    total_bill = total_bill + int(item.get('price', 50))
                    break
        print('-'*40)
        print(f'\t Total Amount: {total_bill}')0
        print('-'*40)
    elif choice == 3:
        print('Update Menu')
    elif choice == 4:
        print('Add review')
    else:
        print('Thanku')
        break