# For 1

# k = 5
# n = int(input("N sonini kiriting: "))
# if n > 0:
#     for i in range(n):
#         print(k)
# else:
#     print("N 0 dan kichik qayta urinib ko'ring: ")


# For 2
# # Foydalanuvchidan a va b qiymatlarini kiritishni so'raymiz
# a = int(input("a sonini kiriting: "))
# b = int(input("b sonini kiriting: "))

# # Barcha butun sonlarni chiqarish uchun for tsiklidan foydalanamiz
# count = 0  # chiqarilgan sonlar sonini hisoblash uchun

# if a < b: # a soni b dan kichi ekanligini tekshiramiz
#     for i in range(a, b + 1):  # 'range' funksiyasi a dan b gacha bo'lgan sonlarni hosil qiladi, b ham qo'shiladi
#         print(i)  # har bir sonni ekranga chiqaramiz
#         count += 1  # chiqarilgan sonlar sonini bittaga oshiramiz
#     # Natijani chiqaramiz
#     print("Chiqarilgan sonlar soni:", count)
# else:
#     print("Kechirasi a soni b dan kichi qaytadan urinib ko'ring")

# # For 3
# # Foydalanuvchidan a va b qiymatlarini kiritishni so'raymiz
# a = int(input("a sonini kiriting: "))
# b = int(input("b sonini kiriting: "))

# # Barcha butun sonlarni kamayish tartibida chiqarish uchun for tsiklidan foydalanamiz
# count = 0  # chiqarilgan sonlar sonini hisoblash uchun

# for i in range(b - 1, a, -1):  # 'range' funksiyasi b-1 dan a+1 gacha kamayadi
#     print(i)  # har bir sonni ekranga chiqaramiz
#     count += 1  # chiqarilgan sonlar sonini bittaga oshiramiz

# # Natijani chiqaramiz
# print("Chiqarilgan sonlar soni:", count)


# # For 4
# # Foydalanuvchidan konfetning 1 kg uchun narxini so'raymiz
# price_per_kg = float(input("1 kg konfetning narxini kiriting: "))

# # 1 kg dan 10 kg gacha bo'lgan miqdorlar uchun narxlarni hisoblab chiqarish
# for kg in range(1, 11):  # 1 dan 10 gacha bo'lgan sonlarni olamiz
#     total_price = kg * price_per_kg  # har bir kg uchun umumiy narxni hisoblaymiz
#     print(f"{kg} kg konfet narxi: {total_price}")


# # For 5
# # Foydalanuvchidan konfetning 1 kg uchun narxini so'raymiz
# price_per_kg = float(input("1 kg konfetning narxini kiriting: "))

# # 0.1 kg dan 0.9 kg gacha bo'lgan miqdorlar uchun narxlarni hisoblab chiqarish
# for kg in range(1, 10):  # 1 dan 9 gacha bo'lgan sonlarni olamiz
#     weight = kg / 10  # 0.1, 0.2, ..., 0.9 kg miqdorlarini hosil qilamiz
#     total_price = weight * price_per_kg  # har bir miqdor uchun umumiy narxni hisoblaymiz
#     print(f"{weight} kg konfet narxi: {total_price}")


# # For 6
# # Foydalanuvchidan konfetning 1 kg uchun narxini so'raymiz
# price_per_kg = float(input("1 kg konfetning narxini kiriting: "))

# # 1.2 kg dan 2 kg gacha bo'lgan miqdorlar uchun narxlarni hisoblab chiqarish
# for kg in range(12, 21, 2):  # 12 dan 20 gacha 2 qadam bilan olamiz
#     weight = kg / 10  # 1.2, 1.4, ..., 2.0 kg miqdorlarini hosil qilamiz
#     total_price = weight * price_per_kg  # har bir miqdor uchun umumiy narxni hisoblaymiz
#     print(f"{weight} kg konfet narxi: {total_price}")


# # For 7 
# # Foydalanuvchidan a va b sonlarini kiritishni so'raymiz
# a = int(input("a sonini kiriting: "))
# b = int(input("b sonini kiriting (a dan katta bo'lishi kerak): "))

# # Yig'indini saqlash uchun o'zgaruvchi
# sum_result = 0

# # a dan b gacha bo'lgan barcha sonlarni qo'shamiz
# for num in range(a, b + 1):
#     sum_result += num

# # Natijani chiqaramiz
# print(f"{a} dan {b} gacha bo'lgan sonlar yig'indisi: {sum_result}")



# # For 8
# # Foydalanuvchidan a va b sonlarini kiritishni so'raymiz
# a = int(input("a sonini kiriting: "))
# b = int(input("b sonini kiriting (a dan katta bo'lishi kerak): "))

# # Ko'paytmani saqlash uchun o'zgaruvchi
# product_result = 1

# # a dan b gacha bo'lgan barcha sonlarni ko'paytiramiz
# for num in range(a, b + 1):
#     product_result *= num

# # Natijani chiqaramiz
# print(f"{a} dan {b} gacha bo'lgan sonlar ko'paytmasi: {product_result}")


# # For 9
# # Foydalanuvchidan a va b sonlarini kiritishni so'raymiz
# a = int(input("a sonini kiriting: "))
# b = int(input("b sonini kiriting (a dan katta bo'lishi kerak): "))

# # Kvadratlar yig'indisini saqlash uchun o'zgaruvchi
# sum_of_squares = 0

# # a dan b gacha bo'lgan barcha sonlarning kvadratlarini qo'shamiz
# for num in range(a, b + 1):
#     sum_of_squares += num ** 2

# # Natijani chiqaramiz
# print(f"{a} dan {b} gacha bo'lgan sonlar kvadratlari yig'indisi: {sum_of_squares}")



# # For 10
# # Foydalanuvchidan n sonini kiritishni so'raymiz
# n = int(input("n sonini kiriting (n > 0 bo'lishi kerak): "))

# # Yig'indini saqlash uchun o'zgaruvchi
# sum_result = 0

# # 1 dan n gacha bo'lgan teskari qiymatlarni yig'amiz
# for i in range(1, n + 1):
#     sum_result += 1 / i

# # Natijani chiqaramiz
# print(f"1 dan {n} gacha bo'lgan teskari qiymatlar yig'indisi: {sum_result}")
