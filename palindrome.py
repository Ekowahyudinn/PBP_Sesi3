def palindrome(angka):
    teks = str(angka)
    return teks == teks[::-1]


def cari_palindrome(angka):
    angka += 1

    while not palindrome(angka):
        angka += 1

    return angka


print("====================================")
print("    PROGRAM PALINDROME BERIKUTNYA")
print("====================================")

data = [9, 100, 200, 1000, 2345]

for angka in data:
    hasil = cari_palindrome(angka)
    print("Input  :", angka)
    print("Output :", hasil)
    print("------------------------------------")