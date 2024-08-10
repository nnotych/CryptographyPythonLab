#Реалізація одного раунду AES для повної реалізації слід реалізувати розширення ключа та повторювати раунди згідно з кількістю раундів, що використовується для конкретної версії AES

def sub_bytes(state):
    for i in range(4):
        for j in range(4):
            state[i][j] = s_box[state[i][j]]

def shift_rows(state):
    state[1] = state[1][1:] + state[1][:1]
    state[2] = state[2][2:] + state[2][:2]
    state[3] = state[3][3:] + state[3][:3]

def mix_columns(state):
    for i in range(4):
        s0 = gmul(0x02, state[0][i]) ^ gmul(0x03, state[1][i]) ^ state[2][i] ^ state[3][i]
        s1 = state[0][i] ^ gmul(0x02, state[1][i]) ^ gmul(0x03, state[2][i]) ^ state[3][i]
        s2 = state[0][i] ^ state[1][i] ^ gmul(0x02, state[2][i]) ^ gmul(0x03, state[3][i])
        s3 = gmul(0x03, state[0][i]) ^ state[1][i] ^ state[2][i] ^ gmul(0x02, state[3][i])

        state[0][i] = s0
        state[1][i] = s1
        state[2][i] = s2
        state[3][i] = s3

def add_round_key(state, round_key):
    for i in range(4):
        for j in range(4):
            state[i][j] ^= round_key[i][j]

def key_expansion(key, round_constant):
   
    pass

def aes_round(state, round_key):
    sub_bytes(state)
    shift_rows(state)
    mix_columns(state)
    add_round_key(state, round_key)

# Припустимо, що у нас є функція gmul для множення байтів у полі Галуа
def gmul(a, b):
    p = 0
    for _ in range(8):
        if b & 1:
            p ^= a
        hi_bit_set = a & 0x80
        a <<= 1
        if hi_bit_set:
            a ^= 0x1b
        b >>= 1
    return p

# Припустимо, що у нас є таблиця s_box
s_box = [
    [0x63, 0x7c, 0x77, 0x7b, 0xf2, 0x6b, 0x6f, 0xc5, 0x30, 0x01, 0x67, 0x2b, 0xfe, 0xd7, 0xab, 0x76],
    # ... інші значення таблиці s_box ...
]

# Припустимо, що у нас є початковий текст і ключ
plaintext = [[0x32, 0x43, 0xf6, 0xa8],
             [0x88, 0x5a, 0x30, 0x8d],
             [0x31, 0x31, 0x98, 0xa2],
             [0xe0, 0x37, 0x07, 0x34]]

key = [[0x2b, 0x7e, 0x15, 0x16],
       [0x28, 0xae, 0xd2, 0xa6],
       [0xab, 0xf7, 0x97, 0x75],
       [0x46, 0x03, 0x9a, 0x32]]




# Результат
print("Ciphertext:", plaintext)
