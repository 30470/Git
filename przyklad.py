import math
# print("Welcome")
# # program hello world
# # komentarz
# # dalszy
# # komentarz

# print("""
# hello
# world
# program
# """)

# nowy komentarz

print("siema")
print('siema')
print('"siema"')
print("'siema'")
print('\"siema \'')


i = 10
j = -3
r = 3.5
y = 9//2 #dzielenie calkowitoliczbowe

print(f"Zmienna i ma wartosc: {i}.")
print(f"Zmienna i w systemie szesnastkowym ma wartosc: {i:x}.")
print(f"Zmienna i w systemie binarnym ma wartosc: {i:b}.")
print(f"Zmienna j ma wartosc: {j}.")
print(f"Zmienna r ma wartosc: {r:2.3f}.") #wymusza wyswietlanie okreslonej ilosci cyfr przed/po przecinku
print(f"Zmienna y ma wartosc: {y}")

#pole kola
r = 5
pole = math.pi * r * r
#print(pole)
print("%.2f" %pole)