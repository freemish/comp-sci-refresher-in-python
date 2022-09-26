import random
from typing import List, Optional

DEFAULT_FILENAME = "other/english.txt"


def get_random_words(wordlist: List[str], wordcount: int = 4) -> str:
    return random.choices(wordlist, k=wordcount)


def get_english_word_list(filename: str = DEFAULT_FILENAME) -> List[str]:
    with open(filename, 'r') as f:
        text = f.read()
        return text.splitlines()


def generate_password(joined_str: str = ".", word_list: Optional[List[str]] = None, wordcount: int = 4) -> str:
    if not word_list:
        word_list = get_english_word_list()
    random_words = get_random_words(wordlist=word_list, wordcount=wordcount)
    return joined_str.join(random_words)


def main() -> None:
    try:
        print(generate_password())
    except OSError:
        import get_english_word_list as gewl
        gewl.main()
        print(generate_password())


if __name__ == '__main__':
    main()
