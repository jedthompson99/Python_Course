html = [',h1>', 'Some content', 'more', 'even more', '</h1>']

def remove_first_and_last(list_to_clean):
    for elements in list_to_clean:
        _, *content, _, _ = list_to_clean
        return content


print(remove_first_and_last(html))