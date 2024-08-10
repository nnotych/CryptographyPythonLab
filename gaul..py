def multiply_GF2_8(byte, factor):
    # Множення в полі Галуа GF(2^8) за модулем m(x) = x^8 + x^4 + x^3 + x + 1

    result = 0

    # Перевірка кожного біта фактору
    for _ in range(8):
        if factor & 1:
            result ^= byte  # XOR для додавання

        # Зсув байту вліво
        byte <<= 1

        # Якщо старший біт байту був 1, то відбувається віднімання за модулем m(x)
        if byte & 0x100:
            byte ^= 0x1b  # 0x1b - поліном m(x) = x^8 + x^4 + x^3 + x + 1

        # Зсув біта фактору вправо
        factor >>= 1

    return result


def mul02(byte):
    # Множення на 02
    return multiply_GF2_8(byte, 0x02)


def mul03(byte):
    # Множення на 03
    return multiply_GF2_8(byte, 0x03)


#Тестування
result1 = mul02(0xD4)
result2 = mul03(0xBF)

print(hex(result1))  # Очікуваний результат: 0xB3
print(hex(result2))  # Очікуваний результат: 0xDA
