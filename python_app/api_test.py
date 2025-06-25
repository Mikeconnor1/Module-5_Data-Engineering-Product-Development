import requests

def search_books_by_title(title):
    url = f"https://openlibrary.org/search.json?title={title}"
    response = requests.get(url)

    if response.status_code == 200:
        books = response.json()['docs']
        print(f"Top {len(books[:10])} results for '{title}':")
        for book in books[:10]:  # Limit to 10 results
            print(f"- {book.get('title')} by {book.get('author_name', ['Unknown'])[0]}")
    else:
        print("Failed to retrieve data.")

search_books_by_title("lord of the rings")


book_titles = ['Catcher in the Rye', 'lord of the rings the two towers', 'Lord of the rings the return of the king', 'The hobbit', 'Dune ', 'Little Women', 'IT', 'Misery', 'Catch 22', 'Animal Farm', '1984', 'Little Women', 'East of Eden', 'America Is in the Heart', 'Wuthering Heights', 'Dark Tales', 'Les Miserables', 'Dracula', 'Frankenstein']

for title in book_titles:
    search_books_by_title(title)

