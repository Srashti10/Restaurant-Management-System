import json
import pprint

def get_rating(reviews):
    rating = 5
    if reviews: #[3,4,5,1,4,5]
        rating = sum(reviews)//len(reviews)
    return '⭐'*rating


with open('menu.json', 'r') as f:
    data = json.load(f)


items = data.get('items', [])
while True:
    print('-'*40)
    print('Motilal Cafe and Restaurant')
    print('-'*40)
    print('1. Show Menu')
    print('2. Order Items')
    print('3. Add Item')
    print('4. Add Rating')
    print('5. Exit')
    print('-'*40)

    choice = int(input())

    if choice == 1:
        print('-'*40)
        print('ID\tName\t\tPrice\tRating')
        print('-'*40)
        for item in items:
            print(f'{item.get("id")}\t{item.get("name")}\t{item.get("price")}\t{get_rating(item.get("reviews", []))}')
        print('-'*40)


    elif choice == 2:
        ordered_items = {}
        order_items = list(map(int, input('What you want to try today? ').split(',')))
        print('-'*40)
        print('ID\tName\t\tPrice')
        print('-'*40)
        total_bill = 0
        for order_item in order_items:
            for item in items:
                if item['id'] == order_item:
                    print(f'{item.get("id")}\t{item.get("name")}\t{item.get("price")}')
                    total_bill = total_bill + int(item.get('price', 10))
                break
        print('-'*40)
        print(f'\t Total Amount: {total_bill}')
        print('-'*40)


    elif choice == 3:
        name = input('Enter item name: ')
        item_price = int(input('Enter the price: '))
        item_type = input('veg or non-veg')
        items.append({
            'id': len(items) + 1,
            'name': name,
            'item_price': item_price,
            'item_type': True if item_type == 'veg' else False,
            'reviews': []
        })
        data['items'] = items
        with open('menu.json', 'w') as f:
            json.dump(data, f)
        print('Item is added')

        
    elif choice == 4:
        item_id = int(input('Enter the item id:'))
        rating = int(input('Give your rating(1-5): '))
        for i,item in enumerate(items):
            if item['id'] == item_id:
                items[i]['reviews'].append(rating)
                break
        print('Thank You for your review. Your response is recorded.')



    else:
        data['items'] = items
        with open('menu.json', 'w') as f:
            json.dump(data, f)
        print('Thanku')
        break