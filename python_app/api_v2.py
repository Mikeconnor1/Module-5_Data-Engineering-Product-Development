import requests

book_titles = [
    'Catcher in the Rye', 'lord of the rings the two towers', 'Lord of the rings the return of the king',
    'The hobbit', 'Dune', 'Little Women', 'IT', 'Misery', 'Catch 22', 'Animal Farm',
    '1984', 'East of Eden', 'America Is in the Heart', 'Wuthering Heights',
    'Dark Tales', 'Les Miserables', 'Dracula', 'Frankenstein'
]

def search_book(title):
    url = f"https://openlibrary.org/search.json?title={title}"
    response = requests.get(url)
    data = response.json()
    if data['docs']:
        doc = data['docs'][0]  # Get first result
        return {
            'title': doc.get('title'),
            'olid': doc.get('edition_key', [None])[0],
            'author_key': doc.get('author_key', [None])[0]
        }
    return None

def get_book_metadata(olid):
    url = f"https://openlibrary.org/api/books?bibkeys=OLID:{olid}&format=json&jscmd=data"
    response = requests.get(url)
    return response.json().get(f'OLID:{olid}', {})

def get_cover_url(olid):
    return f"http://covers.openlibrary.org/b/OLID/{olid}-L.jpg"

def get_author_bio(author_key):
    url = f"https://openlibrary.org/authors/{author_key}.json"
    response = requests.get(url)
    data = response.json()
    return data.get('bio', 'No bio available')

# Main loop
for title in book_titles:
    print(f"\n📘 Title: {title}")
    result = search_book(title)

    if result and result['olid']:
        olid = result['olid']
        author_key = result['author_key']

        print(f"🔗 OLID: {olid}")

        metadata = get_book_metadata(olid)
        print(f"📝 Metadata: {metadata.get('title')} by {metadata.get('authors', [{'name': 'Unknown'}])[0]['name']}")
        
        cover_url = get_cover_url(olid)
        print(f"🖼 Cover URL: {cover_url}")

        if author_key:
            bio = get_author_bio(author_key)
            print(f"👤 Author Bio: {bio if isinstance(bio, str) else bio.get('value', 'No bio')}")
        else:
            print("👤 Author Bio: Not found")
    else:
        print("⚠️ Book not found in Open Library")
