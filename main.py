from logging import basicConfig, error, INFO
from pathlib import Path
from os import environ
from dotenv import load_dotenv
from time import sleep
from random import choice

from telebot import TeleBot, types


BOT_TOKEN: str
AVATAR_URL: str


def set_up() -> bool:

    global BOT_TOKEN, AVATAR_URL

    # Logging:
    basicConfig(level=INFO)

    # Environment variables:

    dotenv_path = Path(__file__).resolve().parent / '.env'

    load_dotenv(dotenv_path)

    BOT_TOKEN = environ.get('BOT_TOKEN', default=None)

    if not BOT_TOKEN:

        error('BOT_TOKEN environment variable is not set!')

        return False

    AVATAR_URL = environ.get('AVATAR_URL', default=None)

    if not AVATAR_URL:

        error('AVATAR_URL environment variable is not set!')

        return False

    return True


def run_bot() -> None:

    bot = TeleBot(BOT_TOKEN)

    main_markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)

    main_markup.add(types.KeyboardButton(text='/help'))
    main_markup.add(types.KeyboardButton(text='/info'))
    main_markup.add(types.KeyboardButton(text='/random_fact'))
    main_markup.add(types.KeyboardButton(text='/get_avatar'))

    @bot.message_handler(commands=['start'])
    def start_handler(message: types.Message):

        reply_text = 'Привет, я - бот-визитка\nМогу делать некоторые штуки, пиши /help, чтобы узнать подробнее'

        bot.reply_to(message, reply_text, reply_markup=main_markup)

    @bot.message_handler(commands=['help'])
    def help_handler(message: types.Message):

        reply_message = (
            '/help - список всех команд (ты уже тут)\n'
            '/info - информация о загадочном (нет) <span class="tg-spoiler">LaGGgggg</span>\n'
            '/random_fact - случайный факт обо мне\n'
            '/get_avatar - получить мою крутую аватарку'
        )

        bot.reply_to(message, reply_message, reply_markup=main_markup, parse_mode='HTML')

    @bot.message_handler(commands=['info'])
    def info_handler(message: types.Message):

        reply_message_first = (
            'Привет, ну смотри, я же не просто так на'
            ' <a href="https://github.com/LaGGgggg">GitHub-е своём</a> всё расписал? Ну вот и читай себе спокойно'
        )

        bot.reply_to(message, reply_message_first, reply_markup=main_markup, parse_mode='HTML')

        sleep(5)

        reply_message_second = (
            'Ну ладно, это шутка)) (не обижайся пожалуйста)\n'
            'Я являюсь senior python developer с 7 годами опыта. <span class="tg-spoiler">Повёлся?))</span>\n'
            'Ок, дальше только правда и серьёзность.'
            ' Меня зовут Никита <span class="tg-spoiler">(хотя кому это интересно вообще)</span>, уже больше двух лет'
            ' я занимаюсь разработкой на python и js (а ещё HTML, CSS, даже PHP, был грешок) и многом другом).'
            ' За это время я создал около сотни более-менее крупных проектов, но не все из них добрались до GitHub и уж'
            ' тем более не все из них в открытом доступе (если что, на GitHub у меня сейчас всего 24 репозитория).'
            ' Я обожаю web и всё что с ним связано. Делал сайты, парсеры различных конфигураций и API.'
            ' Помимо этой сферы творил и приложения для windows, телеграм ботов и даже игры.'
            ' Кстати, у меня уже почти 1000 часов code-time, полтора миллиона написанных строк кода,'
            ' а также 834 коммита за всё время (410 за неполный 2023 год),'
            ' вот <a href="https://wakatime.com/@LaGGgggg">пруфы</a>. А вообще, если честно, я просто пересказываю'
            ' тебе информацию из моего <a href="https://github.com/LaGGgggg">GitHub</a>, да, активно рекламирую его.'
            ' Давай расскажу что-то из интересных фактов? А вот нет, пиши /random_fact и смотри, надо же мне'
            ' хоть какой-то функционал в этого бота вставить.\n\n'
            'Псссс, если что, я открыт для найма, ну вдруг был такой вопрос))'
        )

        bot.reply_to(message, reply_message_second, reply_markup=main_markup, parse_mode='HTML')

    @bot.message_handler(commands=['random_fact'])
    def random_fact_handler(message: types.Message):

        facts = (
            '20. Я перфекционист и при этом ещё и гиперответственный и нервный'
            ' (волнуюсь, всё ли хорошо и безопасно работает). Весь этот букет даёт мне повышение качества конечных'
            ' продуктов, но заставляет много работать (хотя почему "но", "и заставляет много работать")',
            '21. Я зависим от программирования, в том плане, что отдыхать для меня далеко не просто, особенно, если'
            ' я ещё всё не сделал (и да, через пару дней без кода меня сильно тянет обратно)',
            '22. Помимо программистской жизни я много лет занимаюсь спортом (спортивный туризм), а ещё однажды'
            ' я бежал четыре километра по лесу/городу с велосипедом в -12'
            ' (колесо проколол в самой дальней точке маршрута)',
            '23. В 2023 Новый год я до 16:00 занимался парсингом (а начал я за день до этого'
            ' и, естественно, программа работала ночью, а я переодически вставал её проверять)',
            '24. Я в 11 классе и, естественно, писал итоговое сочинение (это экзамен, допуск к ЕГЭ). На работу'
            ' даётся 3 часа 55 минут, я сделал всё за 2 часа (ещё 30 минут я переписывал). Это был лучший экзамен,'
            ' я реально кайфовал на нём. Я даже написал текст песни "Король вечного сна" на черновике, настолько'
            ' я не торопился и получал удовольствие.',
            '25. Поделюсь лайфхаком: если биться головой о стенку, рано или поздно она рухнет',
            '26. Всем категорически рекомендую vim, но не сам редактор кода, а именно управление через горячие'
            ' клавиши всем на свете. Не бойтесь менять назначение клавиш, будет очень удобно',
            '27. Немного игр в студию, рекомендую RimWorld, у меня в совокупности чуть меньше 2000 часов',
            '28. Не пью чай в привычном понимании этого процесса, практикую только рассыпной чай, гайвань и пиалы',
            '29. Я тут чуток всех обманул с нумирацией фактов, их всего 10, но нумирация начинается с 20))',
            '30. Сейчас немного сложно будет, возможно, но смотри: есть код синхронный и асинхронный, тот, который'
            ' пишется по умолчанию, синхронный, он выполняется последовательно, строка за строкой, а асинхронный'
            ' может выполняться параллельно. В js, а конкретнее в расширениях для браузеров, чтобы написать по сути'
            ' синхронный код, нужно написать по факту асинхронный код. Теперь кивай и говори: ничего не понятно, но'
            ' очень интересно))',
        )

        bot.reply_to(message, choice(facts), reply_markup=main_markup)

    @bot.message_handler(commands=['get_avatar'])
    def text_handler(message: types.Message):
        bot.send_photo(message.chat.id, photo=AVATAR_URL, caption='лучшая аватарка в мире', reply_markup=main_markup)

    @bot.message_handler(content_types=['text'])
    def text_handler(message: types.Message):

        replies = (
            'О, круто!',
            'Верно подмечено!',
            'Как с языка снял',
            'Какой ты всё-таки умный',
            'По-любому что-то умное написал',
            'Как лаконично то!',
        )

        bot.reply_to(message, choice(replies), reply_markup=main_markup)

    bot.infinity_polling()


def main():

    if set_up():
        run_bot()

    else:
        error('Setup cannot be completed, some errors occurred')


if __name__ == '__main__':
    main()
