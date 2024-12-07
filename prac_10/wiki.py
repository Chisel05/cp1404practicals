"""
The wiki.py program from prac 10.
"""
import wikipedia


def main():
    page_title = input("Enter page title: ")
    while page_title != '':
        try:
            wiki_page = wikipedia.page(page_title, auto_suggest=False)
        except wikipedia.exceptions.DisambiguationError as e:
            print(f"We need a more specific title. Try one of the following, or a new search:"
                  f"\n{e.options}")
        except wikipedia.exceptions.PageError:
            print(f'Page id "{page_title}" does not match any pages. Try another id!')
        else:
            print(wiki_page.title, wiki_page.summary, wiki_page.url, sep='\n')
        page_title = input("\nEnter page title: ")
    print("Thank you.")


main()
