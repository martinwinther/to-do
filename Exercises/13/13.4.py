def get_nr_items(user_input):
    items = user_input.split(',')
    return len(items)


names = input("Enter names separated by commas (no spaces): ")
nr_items = get_nr_items(names)
print(nr_items)