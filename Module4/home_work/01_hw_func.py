# Дан шестизначный номер билета. Определить, является ли билет счастливым.
# Решение реализовать в виде функции.
# Билет считается счастливым, если сумма его первых и последних цифр равны.

def lucky_ticket(ticket_number):
    s1 = 0
    s2 = 0
    for _ in range(3):
        s1 += ticket_number % 10
        ticket_number = ticket_number // 10
    for _ in range(3):
        s2 += ticket_number % 10
        ticket_number = ticket_number // 10
    return s1 == s2

# Тестируем функцию
print(lucky_ticket(123106))
print(lucky_ticket(123321))
print(lucky_ticket(436751))
