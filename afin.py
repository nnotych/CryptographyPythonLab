def affine_cipher(text, a, b):
  """
  Шифрує текст афінним шифром.

  Аргументи:
    text: Текст, який потрібно зашифрувати.
    a: Коефіцієнт лінійного перетворення.
    b: Додаток до лінійного перетворення.

  Повертає:
    Шифрований текст.
  """

  ciphertext = ""
  for char in text:
    ciphertext += chr(a * ord(char) + b)

  return ciphertext


def affine_decipher(ciphertext, a, b):
  """
  Дешифрує текст афінним шифром.

  Аргументи:
    ciphertext: Шифрований текст.
    a: Коефіцієнт лінійного перетворення.
    b: Додаток до лінійного перетворення.

  Повертає:
    Дешифрований текст.
  """

  plaintext = ""
  for char in ciphertext:
    plaintext += chr((ord(char) - b) // a)

  return plaintext


if __name__ == "__main__":
  #  використання шифра.

  text = "Hello, Nikita!"
  a = 3
  b = 2

  ciphertext = affine_cipher(text, a, b)
  print("Зашифрований текст:", ciphertext)

  plaintext = affine_decipher(ciphertext, a, b)
  print("Дешифрований текст:", plaintext)
