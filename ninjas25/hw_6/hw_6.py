"""
Домашнее задание (занятие 6)

1 Модуль.
- Перенесите ваши функции из прошлого домашнего задания в отдельный
файл и импортируйте их в основной (исполняемый) файл.
- Запустите каждую вашу функцию по 1 или более раз в исполняемом файле.

2Анонимная функция

- Создайте анонимную функцию pow, которая принимает 2 аргумента x и y.
Функция должна возвращать x, возведенное в степень y.

3 Змея.

- Создайте функцию snake_talk, которая принимает 1 аргумент text (строка).
- Функция должна создать новую строку, где все гласные буквы
aeiouyAEIOUY в строке text дублируются.
- Например, такой вызовы функции snake_talk(“Harry”) должен вернуть
строку “Haaryy”.

Повторение прошлого материала.

Ответьте на следующие вопросы:
• Что такое изменяемый и неизменяемый объект?
• Как НЕЛЬЗЯ называть переменную?
• Зачем нужна строка документации в функции?
"""
# ---------------- Задача из повторения ---------------- from Sasha
# import functions as func

# def test_get_all_bookings():
#     response = func.get_all_bookings()
#
#     assert response.status_code == 200, "Код статуса не равен 200!"
#
#
# def test_create_booking():
#     data = {
#         "firstname": "Jack",
#         "lastname": "London",
#         "totalprice": 90,
#         "depositpaid": False,
#         "bookingdates": {
#             "checkin": "2025-01-01",
#             "checkout": "2025-02-02"
#         },
#         "additionalneeds": "Breakfast"
#     }
#
#     # Создаем бронирование и получаем его id из ответа
#     created_booking = func.create_booking(data)
#     id_ = created_booking.json()["bookingid"]
#
#     # Получаем наше бронирование по его id
#     response = func.get_booking_by_id(id_)
#     response_data = response.json()
#
#     assert response_data["firstname"] == data["firstname"]
#     assert response_data["lastname"] == data["lastname"]
#
#
# def test_create_and_update_booking_via_patch():
#     data = {
#         "firstname": "Jules",
#         "lastname": "Verne",
#         "totalprice": 200,
#         "depositpaid": True,
#         "bookingdates": {
#             "checkin": "2025-03-03",
#             "checkout": "2025-04-04"
#         },
#         "additionalneeds": "Breakfast"
#     }
#
#     created_booking = func.create_booking(data)
#     id_ = created_booking.json()["bookingid"]
#
#     # Изменили имя и фамилию в нашем бронировании
#     headers = {
#         "Cookie": f"token={func.get_token()}"
#     }
#     new_data = {
#         "firstname": "Mike",
#         "lastname": "Wazowski"
#     }
#     func.patch_booking_by_id(new_data, headers, id_)
#
#     # Получили наше бронирование по его id
#     patched_booking = func.get_booking_by_id(id_)
#     response_data = patched_booking.json()
#
#     assert response_data["firstname"] == new_data["firstname"]
#     assert response_data["lastname"] == new_data["lastname"]
#
#
# def test_delete_booking():
#     data = {
#         "firstname": "Jules",
#         "lastname": "Verne",
#         "totalprice": 200,
#         "depositpaid": True,
#         "bookingdates": {
#             "checkin": "2025-03-03",
#             "checkout": "2025-04-04"
#         },
#         "additionalneeds": "Breakfast"
#     }
#
#     created_booking = func.create_booking(data)
#     id_ = created_booking.json()["bookingid"]
#
#     # Удаляем наше бронирование
#     headers = {
#         "Cookie": f"token={func.get_token()}"
#     }
#     func.delete_booking_by_id(headers, id_)
#
#     # Пробуем получить наше удаленное бронирование
#     booking = func.get_booking_by_id(id_)
#
#     assert booking.status_code == 404 # 404 - ресурс не найден

