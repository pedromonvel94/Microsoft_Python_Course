import pandas as pd
import os 

file_name = 'grocery_list.csv'
items_needed = True
items_to_add = ['Kiwis', 'Raspberries']

if os.path.exists(file_name):
    # Load the grocery list from the CSV file
    grocery_list_df = pd.read_csv(file_name)

    # Extract the items from the DataFrame and store them in a list
    grocery_list = grocery_list_df['item'].tolist()

    # Print the grocery list and inspect the output
    print(grocery_list)
else:
    print(f"Error: The file '{file_name}' was not found in the current directory.")
    print("Please ensure you have followed the instructions on the Coursera site to extract the files from the zip archive.")

while items_needed:
    ask_user = input('Do you want to add an item to your grocery list? (yes/no): ')
    
    if ask_user.lower() == 'yes':
        user_items = input('Enter an item you want to add to your grocery list: ')

        items_to_add.append(user_items)

        for item in items_to_add:
            grocery_list.append(item)
    elif ask_user.lower() == 'no':
        remove_option = input('Do you want to remove an item from your grocery list? (yes/no): ')
        
        if remove_option.lower() == 'yes':
            item_to_remove = input('Enter the item you want to remove from your grocery list: ')
            
            if item_to_remove.lower() in grocery_list.lower():
                grocery_list.remove(item_to_remove)
            else:
                print(f"Item '{item_to_remove}' not found in the grocery list.")
        elif remove_option.lower() == 'no':
            print('No items were added or removed from your grocery list.')
            items_needed = False

    else:
        print("Please answer with 'yes' or 'no'.")

print('Your updated list is: ', grocery_list) 