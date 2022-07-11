def generate_bin(M, prefix=""):
    if M == 0:
        print(prefix)
        return
    generate_bin(M - 1, prefix+"0")
    generate_bin(M - 1, prefix+"1")

def generate_number(N, M, prefix = None):
    prefix = prefix or []
    if M == 0:
        print(prefix)
        return
    for digit in range(N):
        prefix.append(digit)
        generate_number(N, M - 1, prefix)
        prefix.pop()

#generate_bin(3)
generate_number(10, 2)