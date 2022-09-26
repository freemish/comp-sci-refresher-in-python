from typing import List
from urllib.request import urlopen

DEFAULT_FILENAME = "other/english.txt"
ENGLISH_WORDLIST_URL = "https://raw.githubusercontent.com/meetDeveloper/freeDictionaryAPI/master/meta/wordList/english.txt"


def get_english_word_list_contents() -> str:
    with urlopen(ENGLISH_WORDLIST_URL) as data:
        return data.read().decode("utf-8")


def write_to_file(s: str, filename=DEFAULT_FILENAME) -> None:
    with open(filename, 'w') as f:
        f.write(s)


def read_from_file(filename=DEFAULT_FILENAME) -> str:
    with open(filename, 'r') as f:
        return f.read()


def filter_compound_words_and_phrases(wordlist: List[str]) -> List[str]:
    flist = []

    for w in wordlist:
        if w.isalpha():
            flist.append(w)

    return flist


def main() -> None:
    try:
        read_from_file()
        print("file exists")
    except OSError:
        print("requesting from internet")
        text = "\n".join(
            filter_compound_words_and_phrases(
                get_english_word_list_contents().split('\n')
            )
        )
        write_to_file(text)
        print('done')


if __name__ == '__main__':
    main()
