def is_palindrome(word):
    word = word.replace(' ', '').lower()
    if word == word[::-1]:
        return True
    else:
        return False


def run():
    word = input('Introduce la palabra que quieres probar: ')
    if is_palindrome(word):
        print('Es palíndromo')
    else:
        print('No es palíndromo')
