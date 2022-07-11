def generate_bin(M, prefix=""):
    """ Генерирует все числа (с лидирующими незначущими нулями)
        в двоичной системе счисления длинны M
    """
    if M == 0:
        print(prefix)
        return
    generate_bin(M - 1, prefix+"0")
    generate_bin(M - 1, prefix+"1")

def generate_number(N, M, prefix = None):
    """ Генерирует все числа (с лидирующими незначущими нулями)
        в N-ричной системе счисления (N <= 10)длинны M
    """
    prefix = prefix or []
    if M == 0:
        print(prefix)
        return
    for digit in range(N):
        prefix.append(digit)
        generate_number(N, M - 1, prefix)
        prefix.pop()

#generate_bin(3)
generate_number(2, 3)