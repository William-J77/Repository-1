


def make_summary(title, author, pages):
    print(f"The book is {title} by {author}. It has {pages} pages.")
    

title = input("What is the book's title?\n").strip().title()
author = input("Who is the author of the book?\n").strip().title()
pages = int(input("How many pages does the book have?\n"))

make_summary(title, author, pages)
# Didn't actually need return!