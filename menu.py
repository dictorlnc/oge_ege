from telebot import types
import sqlite3


# Меню
def multi_menu(obj, type_obj):
    conn = sqlite3.connect("base.sqlite")
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM {}'.format(obj))
    row = cursor.fetchone()

    if type_obj == 'type2':
        menu = types.InlineKeyboardMarkup(row_width=1)
    else:
        menu = types.InlineKeyboardMarkup(row_width=3)

    buttons = []

    while row is not None:
        buttons.append(types.InlineKeyboardButton(text=row[0], callback_data=row[0]))
        row = cursor.fetchone()

    try:
        for i in range(int(len(buttons))):
            menu.add(buttons[0], buttons[1], buttons[2])

            del buttons[2]
            del buttons[1]
            del buttons[0]
    except IndexError:
        if len(buttons) == 2:
            menu.add(buttons[0], buttons[1])
        if len(buttons) == 1:
            menu.add(buttons[0])

    menu.add(types.InlineKeyboardButton(text='Вернуться к выбору страны и города',
                                        callback_data='Вернуться к выбору страны и города'))

    if type_obj == 'type2':
        menu.add(types.InlineKeyboardButton(text='Вернуться к выбору предмета',
                                            callback_data='Вернуться к выбору предмета'))

    del buttons

    return menu


# Меню после выбора региона
menu_num2 = types.InlineKeyboardMarkup(row_width=2)
menu_num2_btn = types.InlineKeyboardButton(text='Предметы', callback_data='catalog_predmetov')
menu_num2_btn_2 = types.InlineKeyboardButton(text='Реферальная система', callback_data='referral_system')
menu_num2.add(menu_num2_btn, menu_num2_btn_2)

# Реферальное меню
referral_menu = types.InlineKeyboardMarkup(row_width=2)
referral_menu_btn = types.InlineKeyboardButton(text='Назад в меню', callback_data='back_to_menu')
referral_menu.add(referral_menu_btn)

# Проверить оплату & отменить покупку   чекает оплату киви
check_buy = types.InlineKeyboardMarkup(row_width=1)
check_buy_btn = types.InlineKeyboardButton(text='🔄 Проверить оплату', callback_data='check_payment')
check_buy_btn2 = types.InlineKeyboardButton(text='❌ Отменить заказ', callback_data='cancel_payment')
check_buy.add(check_buy_btn, check_buy_btn2)

# Подтвердить
ch = types.InlineKeyboardMarkup()
ch.add(types.InlineKeyboardButton(text='Подтвердить', callback_data='Подтвердить'))

# Перейги к выбору предмета
go_to_catalog = types.InlineKeyboardMarkup(row_width=1)
go_to_catalog.add(types.InlineKeyboardButton(text='Перейти к каталогу', callback_data='catalog_predmetov'))
go_to_catalog.add(types.InlineKeyboardButton(text='Вернуться к выбору экзамена',
                                             callback_data='Вернуться к выбору экзамена и региона'))

# Родитель/ребенок
ageChoice = types.InlineKeyboardMarkup(row_width=2)
ageChoiceBTN = types.InlineKeyboardButton(text='Я родитель', callback_data='Я родитель')
ageChoiceBTN2 = types.InlineKeyboardButton(text='Я ребенок', callback_data='Я ребенок')
ageChoice.add(ageChoiceBTN, ageChoiceBTN2)

# Кнопка назад
back = types.InlineKeyboardMarkup()
back_btn = types.InlineKeyboardButton(text='🔙BACK', callback_data='🔙BACK')
back.add(back_btn)

# Выбор экзамена
exams = types.InlineKeyboardMarkup(row_width=1)
exams1 = types.InlineKeyboardButton(text='📖 ОГЭ 9-й класс', callback_data='oge_list')
exams2 = types.InlineKeyboardButton(text='📚 ЕГЭ 11-й класс', callback_data='ege_list')
exams.add(exams1, exams2)

# Админ меню
adminMenu = types.InlineKeyboardMarkup(row_width=1)
adminMenu.add(types.InlineKeyboardButton(text='Полная информация',
                                         callback_data='full_info')),
adminMenu.add(types.InlineKeyboardButton(text='Информация о пользователе',
                                         callback_data='user_info')),
adminMenu.add(types.InlineKeyboardButton(text='Топ 5 пользователей по приглашениям',
                                         callback_data='top_user')),
adminMenu.add(types.InlineKeyboardButton(text='Выйти из админского меню',
                                         callback_data='exit_admin_menu'))

# Обратно в админ меню
back_to_admin_menu = types.InlineKeyboardMarkup(row_width=3)
back_to_admin_menu.add(types.InlineKeyboardButton(text='Обратно в админ меню', callback_data='back_to_admin_menu'))

