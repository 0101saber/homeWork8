import conf.connect
import sys
from conf.models import Quotes, Author


def find_author_by_name(fullname):
    result = Author.objects(fullname=fullname).first()
    return result


def search_by_author(author):
    quotes = Quotes.objects(author=find_author_by_name(author).id)
    return [quote.quote for quote in quotes]


def search_by_tag(tag):
    quotes = Quotes.objects(tags=tag)
    return [quote.quote for quote in quotes]


def search_by_tags(tags):
    tags_list = tags.split(',')
    quotes = Quotes.objects(tags__in=tags_list)
    return [quote.quote for quote in quotes]


def main():
    print("Enter commands in the format: name:<author>, tag:<tag>, tags:<tag1,tag2>, or 'exit' to quit.")

    while True:
        command_input = input("Enter command: ").strip()

        if command_input == "exit":
            print("Exiting the script.")
            break

        try:
            if command_input.startswith("name:"):
                author = command_input.split("name:", 1)[1].strip()
                results = search_by_author(author)
            elif command_input.startswith("tag:"):
                tag = command_input.split("tag:", 1)[1].strip()
                results = search_by_tag(tag)
            elif command_input.startswith("tags:"):
                tags = command_input.split("tags:", 1)[1].strip()
                results = search_by_tags(tags)
            else:
                print("Invalid command. Please use 'name:', 'tag:', 'tags:', or 'exit'.")
                continue

            for result in results:
                print(result.encode('utf-8').decode('utf-8'))

        except Exception as e:
            print(f"An error occurred: {e}", file=sys.stderr)


if __name__ == "__main__":
    main()
