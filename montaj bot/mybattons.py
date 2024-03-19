



from aiogram.types import InlineKeyboardMarkup,InlineKeyboardButton
from aiogram.utils.keyboard import InlineKeyboardBuilder

inline_menu = InlineKeyboardMarkup(
    inline_keyboard= [

    [InlineKeyboardButton(text="Bizning kurslar",callback_data="courses"),
    InlineKeyboardButton(text="Bizning manzil",callback_data="location"),],

    [InlineKeyboardButton(text="Bizning sayt",callback_data="about-us"),],

    [InlineKeyboardButton(text="Admin ",callback_data="contact-admin")],
    [InlineKeyboardButton(text="rasm yuborishingiz mumkun ",callback_data="delete")],

    ]
)


delete = InlineKeyboardMarkup(
    inline_keyboard= [
        [InlineKeyboardButton(text="Rasm yubor",callback_data="rasm yubor")],
    ]
)
sayt  = InlineKeyboardMarkup(
    inline_keyboard= [
        [InlineKeyboardButton(text="Sifat EDU",url="https://sifatedu.uz/")],
        [InlineKeyboardButton(text="ortga",callback_data="back")],
    ]
)

admin = InlineKeyboardMarkup(
    inline_keyboard=[
        [InlineKeyboardButton(text="Jurabekjon",url="https://t.me/Jur_bek_jon_123com")],
        [InlineKeyboardButton(text="ortga",callback_data="back")],
    ]
)

location = InlineKeyboardMarkup(
    inline_keyboard= [
    [InlineKeyboardButton(text="Sifat edu",url="https://www.google.com/maps/@40.1028381,65.3730178,16z?entry=ttu")],
    [InlineKeyboardButton(text="ortga",callback_data="back")],
    ]
)
courses_menu = InlineKeyboardMarkup(
    inline_keyboard= [

    [InlineKeyboardButton(text="Frontend",url="https://medium.com/@muhammadbobur99/front-end-nima-fc747f74f568"),
    InlineKeyboardButton(text="Backend",url="https://uzbekdevs.uz/wiki/backend"),],

    [InlineKeyboardButton(text="Online kurslar",url="https://www.youtube.com/@SIFATDEV"),],
    [InlineKeyboardButton(text="ortga",callback_data="back")],

    ]
)


ortga = InlineKeyboardMarkup(
    inline_keyboard=[
        [InlineKeyboardButton(text="ortga",callback_data="back-courses")],
    ]
)

colours_inline_button = InlineKeyboardMarkup(
    inline_keyboard=[
        [InlineKeyboardButton(text="black",callback_data="black"),
         InlineKeyboardButton(text="blue",callback_data="blue"),
         InlineKeyboardButton(text="yellow",callback_data="yellow")],
        [InlineKeyboardButton(text="green",callback_data="green"),
         InlineKeyboardButton(text="white",callback_data="white"),
         InlineKeyboardButton(text="orange",callback_data="orange")],
         [InlineKeyboardButton(text="brown",callback_data="brown")],
    ]
)




