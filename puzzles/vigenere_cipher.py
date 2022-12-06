"""Demonstrates the vigenere cipher and how to crack it."""

import string


class VigenereTable:
    _numbered_letters: dict = {letter: ord(letter) - 65 for letter in string.ascii_uppercase}
    _lettered_numbers: dict = {v: k for k, v in _numbered_letters.items()}
    _calculated_letter_offsets_cache: dict = {}

    def get_number_of_letter(self, letter: str) -> int | None:
        return self._numbered_letters.get(letter.upper())

    def get_letter_of_number(self, num: int) -> str | None:
        return self._lettered_numbers.get(num)

    def get_alphabet_offset_for_letter(self, letter: str) -> str | None:
        letter_list = self._calculated_letter_offsets_cache.get(letter.upper())
        if letter_list is not None:
            return letter_list

        letter_num = self.get_number_of_letter(letter)
        letter_list = string.ascii_uppercase[letter_num:] + string.ascii_uppercase[:letter_num]

        self._calculated_letter_offsets_cache[letter.upper()] = letter_list
        return letter_list


def encipher_message(message: str, key: str, keep_nonalpha: bool = True) -> str:
    """
    Returns message enciphered with a message and a given key.
    """
    vigenere_table = VigenereTable()
    key = clean_nonalpha(key).upper()

    if not keep_nonalpha:
        message = clean_nonalpha(message)

    enciphered_message = ""
    for mi, mc in enumerate(message):
        mc_number = vigenere_table.get_number_of_letter(mc)
        if mc_number is None:
            enciphered_message += mc
            continue

        key_offset_array = vigenere_table.get_alphabet_offset_for_letter(key[mi % len(key)])
        enciphered_message += key_offset_array[mc_number]

    return enciphered_message


def decipher_message(enciphered_message: str, key: str) -> str:
    """Accepts an enciphered message with a key and outputs the original message."""
    vigenere_table = VigenereTable()
    key = clean_nonalpha(key).upper()

    deciphered_message = ""
    for ei, ec in enumerate(enciphered_message):
        ec_number = vigenere_table.get_number_of_letter(ec)
        if ec_number is None:
            deciphered_message += ec
            continue

        key_num = vigenere_table.get_number_of_letter(key[ei % len(key)])
        deciphered_message += vigenere_table.get_letter_of_number((ec_number - key_num) % 26)

    return deciphered_message


def clean_nonalpha(message: str) -> str:
    """Removes nonalpha characters from a given string."""
    new_message = ""
    for c in message:
        if c.isalpha():
            new_message += c

    return new_message


def main() -> None:
    test_message = "weneedmoresuppliesfast"
    test_key = "mec"
    test_result = "".join("I I P Q I F Y S T Q W W B T N U I U R E U F".split(" "))

    assert encipher_message(test_message, test_key) == test_result
    assert decipher_message(test_result, test_key) == test_message.upper()

    encryptme = "Hi. I need help. Please help me."
    key = "guns n roses"
    new_cipher = encipher_message(encryptme, key)
    print(new_cipher)
    print(decipher_message(new_cipher, key))


if __name__ == '__main__':
    main()
