# В google colab добавить: !pip install pyTelegramBotAPI
# Чтобы добавить новое слово — нужно его прописать в объект DEFINITOINS на 13 строчке
# Важно все новые аббривиатуры в коде писать только с маленьких букв
# Пользователь в телеграм может писать и с большой и с маленькой — код всегда приводит к строчным

from telebot import TeleBot, types

bot = TeleBot(token='токен', parse_mode='html') # создание бота

# словарь с определениями и аббревиатурами, которые знает бот
# в формате:
# 'слово': 'артикль, перевод, комментарий, род'
DEFINITOINS = {
    'Tür': 'Die, женский род',
    'Junge': 'Der. Мальчик мужского рода',
    'Polizist': 'Der. Полицейский мужского рода',
    'Polizistin':'Die. Сотрудница полиции женского рода',
    'Lehrer': 'Der. Учитель мужского рода',
    'Lehrerin': 'Die. Учительница женского рода',
    'Arzt': 'Der. Врач мужского рода',
    'Bär': 'Der. Медведь мужского рода',
    'Hund': 'Der. Собака мужского рода',
    'Norden': 'Der. Север, как и другие стороны света, мужского рода',
    'Süden': 'Der. Юг, как и другие стороны света, мужского рода',
    'Westen ': 'Der. Запад, как и другие стороны света, мужского рода',
    'Osten': 'Der. Восток, как и другие стороны света, мужского рода',
    'Winter': 'Der. Зима, как и другие времена года, мужского рода',
    'Sommer': 'Der. Лето, как и другие времена года, мужского рода',
    'Frühling': 'Der. Весна, как и другие времена года, мужского рода',
    'Herbst': 'Der. Осень, как и другие времена года, мужского рода',
    'Januar': 'Der. Январь, как и другие месяцы, мужского рода',
    'Februar': 'Der. Февраль, как и другие месяцы, мужского рода',
    'März': 'Der. Март, как и другие месяцы, мужского рода',
    'April': 'Der. Апрель, как и другие месяцы, мужского рода',
    'Mai': 'Der. Май, как и другие месяцы, мужского рода',
    'Juni': 'Der. Июнь, как и другие месяцы, мужского рода',
    'Juli': 'Der. Июль, как и другие месяцы, мужского рода',
    'August': 'Der. Август, как и другие месяцы, мужского рода',
    'September': 'Der. Сентябрь, как и другие месяцы, мужского рода',
    'Oktober': 'Der. Октябрь, как и другие месяцы, мужского рода',
    'November': 'Der. Ноябрь, как и другие месяцы, мужского рода',
    'Dezember': 'Der. Декабрь, как и другие месяцы, мужского рода',
    'Montag': 'Der. Понедельник, как и другие дни недели, мужского рода',
    'Dienstag': 'Der. Вторник, как и другие дни недели, мужского рода',
    'Mittwoch': 'Der. Среда, как и другие дни недели, мужского рода',
    'Donnerstag': 'Der. Четверг, как и другие дни недели, мужского рода',
    'Freitag': 'Der. Пятница, как и другие дни недели, мужского рода',
    'Samstag': 'Der. Суббота, как и другие дни недели, мужского рода',
    'Sonntag': 'Der. Воскресенье, как и другие дни недели, мужского рода',
    'Morgen':'Der. Утро, как и другие времена суток, мужского рода',
    'Tag':'Der. День, как и другие времена суток, мужского рода',
    'Abend':'Der. Вечер, как и другие времена суток, мужского рода',
    'Nacht':'Die. Ночь, исключительное время суток, женского рода',
    'Regen':'Der. Дождь, как и другие погодные состояния, мужского рода',
    'Schnee':'Der. Снег, как и другие погодные состояния, мужского рода',
    'Granit':'Der. Гранит, как и другие камни и минералы, мужского рода',
    'Diamant':'Der. Алмаз, как и другие камни и минералы, мужского рода',
    'Baikal':'Der. Байкал, как и другие названия гор и озер, мужского рода',
    'Bier':'Das. Пиво, исключительный напиток, среднего рода',
    'Wodka':'Der. Водка, как и другие алкогольные напитки, мужского рода',
    'Wein':'Der. Вино, как и другие алкогольные напитки, мужского рода',
    'Euro':'Der. Евро, как и другие валюты, мужского рода',
    'Dollar':'Der. Доллар, как и другие валюты, мужского рода',
    'Rubel':'Der. Рубль, как и другие валюты, мужского рода',
    'Kopeke':'Die. Копейка, исключительная валюта, женского рода',
    'Krone':'Die. Крона, исключительная валюта, женского рода',
    'Mark':'Die. Марка, исключительная валюта, женского рода',
    'Mond':'Der. Луна, как и другие небесные тела, мужского рода',
    'Erde':'Der. Земля, как и другие небесные тела, мужского рода',
    'Mars':'Der. Марс, как и другие небесные тела, мужского рода',
    'Venus':'Die. Венера, исключительное небесное тело, женского рода',
    'Sonne':'Die. Солнце, исключительное небесное тело, женского рода',
    'Gang':'Der. Прогулка, как и большинство односложных слов, мужского рода',
    'Gruß':'Der. Приветствие, как и большинство односложных слов, мужского рода',
    'Sprang':'Der. Прыжок, как и большинство односложных слов, мужского рода',
    'Ruf':'Der. Призыв, как и большинство односложных слов, мужского рода',
    'Satz':'Der. Предложение, как и большинство односложных слов, мужского рода',
    'Spieler':'Der. Игрок мужского рода',
    'Sportler':'Der. Спортсмен мужского рода',
    'Rentner':'Der. Пенсионер мужского рода',
    'Schmetterling':'Der. Бабочка мужского рода',
    'Wuchs':'Der. Рост мужского рода',
    'Präsident':'Der. Президент мужского рода',
    'Laborant':'Der. Лаборант мужского рода',
    'Publizist':'Der. Публицист мужского рода',
    'Poet':'Der. Поэт мужского рода',
    'Pilot':'Der. Пилот мужского рода',
    'Kandidat':'Der. Кандидат мужского рода',
    'Philosoph':'Der. Философ мужского рода',
    'Astronom':'Der. Астроном мужского рода',
    'Photograph':'Der. Фотограф мужского рода',
    'Ingenieur':'Der. Инженер мужского рода',
    'Pionier':'Der. Пионер мужского рода',
    'Jubilar':'Der. Юбилей мужского рода',
    'Sekretär':'Der. Секретарь мужского рода',
    'Doktor':'Der. Доктор мужского рода',
    'Mann':'Der. Мужчина мужского рода',
    'Frau':'Die. Женщина женского рода',
    'Mädchen':'Das. Девочка среднего рода 😂',
    'Kuh':'Die. Корова, как и другие животные женского пола, женского рода',
    'Katze':'Die. Кошка, как и другие животные женского пола, женского рода',
    'Huhn':'Das. Курица среднего рода',
    'Schaf':'Das. Овца среднего рода',
    'Birke':'Die. Береза, как и другие деревья, женского рода',
    'Ahorn':'Das. Клен среднего рода',
    'Rose':'Die. Роза, как и другие цветы, женского рода',
    'Mohn':'Der. Мак, цветок исключение, мужского рода',
    'Kaktus':'Das. Кактус, цветок исключение, среднего рода',
    'Himbeere':'Die. Малина, как и другие ягоды, женского рода',
    'Erdbeere':'Die. Клубника, как и другие ягоды, женского рода',
    'Birne':'Die. Груша, как и другие фрукты и овощи, женского рода',
    'Apfel':'Der. Яблоко, фрукт исключение, мужского рода',
    'Pfirsich':'Der. Персик, фрукт исключение, мужского рода',
    'Kohl':'Der. Капуста, овощ исключение, мужского рода',
    'Kürbis':'Der. Тыква, овощ исключение, мужского рода',
    'Einigkeit':'Die. Единство женского рода',
    'Umarmung':'Die. Объятье женского рода',
    'Freiheit':'Die. Свобода женского рода',
    'Mannschaft':'Die. Команда женского рода',
    'Bäckerei':'Die. Пекарня женского рода',
    'Chemie':'Die. Химия женского рода',
    'Qualität':'Die. Качество женского рода',
    'Information':'Die. Информация женского рода',
    'Kultur':'Die. Культура женского рода',
    'Physik':'Die. Физика женского рода',
    'Passage':'Die. Прохождение женского рода',
    'Fassade':'Die. Фасад женского рода',
    'Ambulanz':'Die. Скорая помощь женского рода',
    'Existenz':'Die. Существование женского рода',
    'Liebe':'Die. Любовь женского рода',
    'Hilfe':'Die. Помощь женского рода', 
    'Siege':'Die. Победа женского рода',
    'Kollege':'Der. Коллега мужского рода',
    'Name':'Der. Имя мужского рода',
    'Gedanke':'Der. Мысль мужского рода',
    'Käse':'Der. Сыр мужского рода',
    'Ende':'Der. Конец мужского рода',
    'Interesse':'Der. Интерес мужского рода',
    'Auge':'Der. Глаз мужского рода',
    'Hündchen':'Das. Собачка среднего рода',
    'Tischlein':'Das. Столик среднего рода',
    'Viertel':'Das. Квартал среднего рода',
    'Eigentum':'Das. Владение среднего рода',
    'Reichtum':'Der. Богатство мужского рода',
    'Irrtum':'Der. Ошибка мужского рода',
    'Verhältnis':'Das. Отношение среднего рода',
    'Kenntnis':'Die. Знание женского рода',
    'Erlaubnis':'Die. Разрешение женского рода',
    'Kabinett':'Das. Кабинет среднего рода',
    'Dokument':'Das. Документ среднего рода',
    'Drama':'Das. Драма среднего рода',
    'Kino':'Das. Кино среднего рода',
    'Gefühl':'Das. Чувство среднего рода',
    'Gehirn':'Das. Мозг среднего рода',
    'Geheim':'Das. Секрет среднего рода',
    'Essen':'Das. Еда среднего рода',
    'Lernen':'Das. Обучение среднего рода',
    'See':'DAS или DER. Озеро среднего рода, а море - мужского',
    'Messer':'DAS или DER. Нож среднего рода, а измерительный прибор - мужского',
    'Bauer':'DAS или DER. Клетка среднего рода, а крестьянин - мужского',
}

# обработчик команды '/start'
@bot.message_handler(commands=['start'])
def start_command_handler(message: types.Message):
    # отправляем ответ на команду '/start'
    bot.send_message(
        chat_id=message.chat.id, # id чата, в который необходимо направить сообщение
        text='Привет! Я помогу тебе вспомнить род немецкого слова 🤓\nВведи слово, например, Tür', # текст сообщения
    )

@bot.message_handler(commands=['rulesdie'])
def rules_die_command_handler(message: types.Message):
    # отправляем ответ на команду '/start'
    bot.send_message(
        chat_id=message.chat.id, # id чата, в который необходимо направить сообщение
        text='''Самая простая категория слов, относящаяся к женскому роду — лица женского пола и феминитивы:

die Frau (женщина), die Polizistin (сотрудница полиции) НО das Mädchen (девочка)
Другие слова женского рода:

животные женского пола: die Kuh (корова), die Katze (кошка) НО das Huhn (курица), das Schaf (овца)
деревья — die Birke (берёза), НО der Ahorn (клён)
цветы — die Rose (роза), НО der Mohn (мак), der Kaktus (кактус)
ягоды — die Himbeere (малина), die Erdbeere (клубника)
фрукты и овощи — die Birne (груша), НО der Apfel (яблоко), der Pfirsich (персик), der Kohl (капуста), der Kürbis (тыква)
большинство рек в Германии и Австрии — die Elbe, die Oder, die Spree, но der Rhein, der Main, der Neckar
Так же, как и с мужским родом, существуют суффиксы, автоматические “ставящие” существительное в женский род:
-ung — die Umarmung (объятье)
-heit — die Freiheit (свобода)
-keit — die Einigkeit (единство)
-schaft —die Mannschaft (команда)
-ei — die Bäckerei (пекарня)

Заимствованные слова. Отдельно отметим, что на эти суффиксы падает ударение:
-ie — die Chemie (химия)
-tät — die Qualität (качество)
-tion — die Information (информация)
-ur — die Kultur (культура)
-ik — die Physik (физика)
-age — die Passage (прохождение)
-ade — die Fassade (фасад)
-anz — die Ambulanz (скорая помощь)
-enz — die Existenz (существование)

Большинство слов с суффиксом -e:
die Liebe (любовь), die Hilfe (помощь), die Siege (победа)

Важный момент, не все слова с этим суффиксом на конце автоматически принимают женский род. В случае, если слово обозначает некую деятельность, национальность или просто было заимствовано, то род слова будет другим: der Kollege (коллега), der Russe (русский), der Junge (мальчик), der Name (имя), der Gedanke (мысль), der Käse (сыр), das Ende (конец), das Interesse (интерес), das Auge (глаз)

Отглагольные существительные с суффиксом -t на конце:
die Fahrt (поездка), die Kunst (искусство), die Macht (сила)''', # текст сообщения
    )

@bot.message_handler(commands=['rulesder'])
def rules_der_command_handler(message: types.Message):
    # отправляем ответ на команду '/start'
    bot.send_message(
        chat_id=message.chat.id, # id чата, в который необходимо направить сообщение
        text='''Самое очевидное - к мужском роду относятся все лица мужского пола и представители профессий-мужчины:

der Mann (мужчина), der Junge (мальчик)
der Polizist (полицейский), der Lehrer (учитель), der Arzt (врач)
То же самое касается животных-самцов:

der Bär (медведь), der Hund (собака), der Affe (обезьяна)
Остальные слова, относящиеся к мужскому роду по факту значения:

Стороны света: der Norden (север), der Süden (юг), der Westen (запад), der Osten (восток)
Времена года: der Winter (зима), der Sommer (лето), der Frühling (весна), der Herbst (осень)
Названия месяцев: der Januar (январь), der Februar (февраль), der Mai (май), der August (август) и т.д.
Дни недели: der Montag (понедельник), der Mittwoch (среда), der Freitag (пятница), der Sonntag (воскресенье) и т.д.
Времена суток: der Morgen (утро), der Tag (день), der Abend (вечер), НО die Nacht (ночь)
Погодные состояния: der Regen (дождь), der Schnee (снег)
Минералы и камни: der Granit (гранит), der Diamant (алмаз)
Названия гор и озёр: der Harz, der Baikal
Спиртные напитки: der Wodka (водка), der Wein (вино), НО das Bier (пиво)
Валюты: der Euro, der Dollar, der Rubel, НО die Kopeke, die Krone, die Mark
Небесные тела: der Mond (луна), der Erde (Земля), der Mars (Марс), НО die Venus (венера), die Sonne (солнце)
Автомобильные бренды: der Lada, der Mercedes-Benz, der BMW
В остальных случаях мужской род определяется по внешнему виду слова:

Большинство односложных (т.е. состоящих из одного слога) и отглагольных существительных:
- der Gang (прогулка), der Gruß (приветствие), der Sprang (прыжок), der
Ruf (призыв), der Satz (предложение)
Большинство существительных с суффиксами:
-er — der Spieler (игрок)
-ler — der Sportler (спортсмен)
-ner — der Rentner (пенсионер)
-ling — der Schmetterling (бабочка)
-s — der Wuchs (рост)
Большинство заимствованных слов с суффиксами:
-ent — der Präsident (президент)
-ant — der Laborant (лаборант)
-ist — der Publizist (публицист)
-et — der Poet (поэт)
-ot — der Pilot (пилот)
-at — der Kandidat (кандидат)
-soph — der Philosoph (философ)
-nom — der Astronom (астроном)
-graph — der Photograph (фотограф)
-eur — der Ingenieur (инженер)
-ier — der Pionier (пионер)
-ar — der Jubilar (юбилей)
-är — der Sekretär (секретарь)
-or — der Doktor (доктор)''', # текст сообщения
    )

@bot.message_handler(commands=['rulesdas'])
def rules_das_command_handler(message: types.Message):
    # отправляем ответ на команду '/start'
    bot.send_message(
        chat_id=message.chat.id, # id чата, в который необходимо направить сообщение
        text='''В отличие от других родов, слово редко принимает средний род по значению. К словам среднего рода относят существительные с суффиксами:
-chen — das Mädchen (девочка), das Hündchen (собачка)
-lein — das Tischlein (столик)
-(s)tel — das Viertel (квартал)
-tum — das Eigentum (владение), НО der Reichtum (богатство), der Irrtum (ошибка)
-nis — das Verhältnis (отношение), НО die Kenntnis (знание), die Erlaubnis (разрешение)
-ett — das Kabinett (кабинет)
-ment — das Dokument (документ)
-ma — das Drama (драма)
-o — das Kino (кино)

Самое главное — средний род автоматически принимают слова с приставкой Ge-:
das Gefühl (чувство), das Gehirn (мозг), das Geheim (секрет)

Другая особенность — когда глагол становится существительным и никак не меняется внешне, получившееся слово автоматически принимает на себя средний род:
- das Essen (еда) — essen (еда)
- das Lernen  (обучение) — lernen (учиться)

Этот обширный список богат на исключения, частные случаи и двусмысленности — у некоторых слов род меняется в зависимости от значения:
- das See (озеро) — der See (море)
- der Messer (измерительный прибор) — das Messer (нож)
- der Bauer (крестьянин) — das Bauer (клетка)''', # текст сообщения
    )

# обработчик всех остальных сообщений
@bot.message_handler()
def message_handler(message: types.Message):
    # пробуем найти ключевую фразу в словаре
    definition = DEFINITOINS.get(
        message.text.strip().lower().capitalize(), # приводим текст сообщения к слову начинающемуся с заглавной буквы
    )
    # если фразы нет в словаре, то переменная definition будет иметь значение None
    # проверяем это условие
    if definition is None:
        # если ключевая фраза не была найдена в словаре
        # отправляем ответ
        bot.send_message(
            chat_id=message.chat.id,
            text='😋 Для меня это слово еще гендерно-нейтрально',
        )
        # выходим из функции
        return
    
    # если ключевая фраза была найдена, формируем текст сообщения и отправляем его
    # если перед строкой поставить букву f, то в фигурных скобках {} можно использовать переменные :)
    bot.send_message(
        chat_id=message.chat.id,
        text=f'Артикль:\n<code>{definition}</code>',
    )

    bot.send_message(
        chat_id=message.chat.id,
        text=f'Жду новое слово',
    )


# главная функция программы
def main():
    # запускаем нашего бота
    bot.infinity_polling()


if __name__ == '__main__':
    main()
