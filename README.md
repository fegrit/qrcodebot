#чат-бот

в этом проекте используются возможности языка Python, стандартной библиотеки для создания чат-ботов в Telegram telebot, библиотеки pyqrcode для реализации работы чат-бота.

#запуск бота

1. клонируйте репозиторий: https://github.com/fegrit/qrcodebot
2. перейдите в исходную папку
3. откройте командную строку и установите (pip install 'name') все необходимые библиотеки из файла requirements.txt
4. в строке инициализации токена вставьте свой токен чат-бота
5. запустите файл bot.py
6. готово!

#результаты

1. для начала отправляем боту стандартную команду /start
![](https://github.com/fegrit/qrcodebot/blob/main/results/start.png)

2. после его приветствия нажимаем на кнопку "🔑Получить QR-code"
![](https://github.com/fegrit/qrcodebot/blob/main/results/click_button.png)

3. затем он попросит нас прислать ему ссылку для создания qr-кода в виде документа формата png
4. бот отправляет нам qr-код!
![](https://github.com/fegrit/qrcodebot/blob/main/results/link_n_result.png)
5. в случае, если написать боту какой-либо текст, вместо нажатия на кнопку
![](https://github.com/fegrit/qrcodebot/blob/main/results/unknown_command.png)
