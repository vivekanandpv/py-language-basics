book = {
    'title': 'War and Peace',
    'author': 'Leo Tolstoy',
    'original_language': 'Russian',
    'category': 'Novel'
}

# accessing by keys
print(f'original title: {book["title"]}')
# also, book.get('title')

# mutation
book['title'] = 'Anna Karenina'
print(f'modified title: {book.get("title")}')

# iterator gives keys by default
# use for val in book.values() for values
# use for item in book.items() for set-like object for key and value

# existence: if 'title' in book

# adding new pair
book['year'] = 1878

print(f'book after adding year {book.get("year")}')

# removing: book.pop('key') or del book['key']

book.pop('category')
print(f'book after pop() for category {book}')

# update: if key exists, value is changed
# if key doesn't exist, new pair is created
book.update({'title': 'War and Peace'})
print(f'book after update {book}')
