# bot.py
from telebot import TeleBot, types

TOKEN = "5197676792:AAGtJYcNfjVF2gl9NHPc3TcYumEv-utkryM"  # o'zingizning tokeningizni qo'ying

bot = TeleBot(TOKEN, parse_mode="HTML")


@bot.message_handler(commands=['start'])
def start(message):
    kb = types.ReplyKeyboardMarkup(
        resize_keyboard=True      # tugmalar ekranga moslashadi
        # one_time_keyboard=False # default o'zi False, klaviatura yashirilmaydi
    )

    # 1-qator: faqat WebApp tugmasi -> kattaroq ko'rinadi
    web_app_btn = types.KeyboardButton(
        "📚💻 Ona tili Pro kursiga  kirish ",
        web_app=types.WebAppInfo(
            url="https://shahboz793.github.io/telegram/"  # sizning saytingiz
        )
    )
    kb.add(web_app_btn)

    # 2-qator: ikki dona oddiy tugma
    info_courses = types.KeyboardButton("📚 Kurslar haqida")
    info_center = types.KeyboardButton("🏫 O‘quv markazi haqida")
    kb.add(info_courses, info_center)

    # 3-qator: bitta tugma
    contact_btn = types.KeyboardButton("📞 Admin bilan aloqa")
    kb.add(contact_btn)

    text = (
        "Assalomu alaykum!\n\n"
        "<b>Ona tili Pro</b> onlayn o‘quv kursi botiga xush kelibsiz. 👋\n\n"
        "Pastdagi <b>“📚💻 Ona tili Pro kursiga  kirish”</b> tugmasini bosing va kurslar platformasiga kiring.\n\n"
        "Qolgan tugmalar orqali esa kurslar va markaz haqida ma’lumot olishingiz mumkin."
    )

    bot.send_message(message.chat.id, text, reply_markup=kb)


@bot.message_handler(func=lambda m: True)
def menu_handler(message):
    txt = message.text

    if txt == "📚 Kurslar haqida":
        bot.send_message(
            message.chat.id,
            "Bu yerda Ona tili va adabiyot bo‘yicha onlayn kurslar, video darslar va testlar jamlangan. "
            "Web app ichida har bir kursni alohida ko‘ra olasiz."
        )

    elif txt == "🏫 O‘quv markazi haqida":
        bot.send_message(
            message.chat.id,
            "“Ona tili Pro” — ona tili va adabiyot fanidan onlayn tayyorlov kursi. "
            "Darslar video shaklida, qulay interfeys va avtomatik quiz tizimi bilan."
        )

    elif txt == "📞 Admin bilan aloqa":
        bot.send_message(
            message.chat.id,
            "Admin: @onatili_premium\nSavollar, takliflar va hamkorlik uchun yozishingiz mumkin."
        )

    elif txt == "📚💻 Ona tili Pro kursiga  kirish":
        # WebApp tugmasi bosilganda Telegram o'zi saytingizni ochadi,
        # shu sababli bu yerda alohida kod bo'lishi shart emas.
        bot.send_message(
            message.chat.id,
            "Agar Web App ochilmagan bo‘lsa, yuqoridagi '📚💻 Ona tili Pro kursiga  kirish' tugmasini yana bir marta bosing."
        )

    else:
        bot.send_message(
            message.chat.id,
            "Menuni pastdagi tugmalar orqali ishlating 🙂"
        )


if __name__ == "__main__":
    print("Bot ishga tushdi...")
    bot.infinity_polling()
