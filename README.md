<div style="background-image: url('https://avatars.mds.yandex.net/i?id=3b33bbfad871af6b828e53200fb2ca2a95605319-10234623-images-thumbs&n=13');  padding: 20px;">

<div id="header" align="center">
  <img src="https://media.giphy.com/media/M9gbBd9nbDrOTu1Mqx/giphy.gif" width="100"/>
</div>

<div align="center" style="color: #000"> 

# Приложение на **Django** 
# для создания голосовых напоминаний и задач.

 </div>

<div style="color: #7d03fc">

## Содержание: 

<ol style="color: #000">


<li> 

### Обзор проекта   


<ul style="color: #000">

<li>

 #### Введение

</li>

<li>

 #### Цель проекта

</li>

<li>

 #### Описание функционала

</li>

<li>

 #### Заключение, или дополнительные идеи для реализации 

</li>

</ul>

</li>

<li>

### Структура проекта

<ul style="color: #000">

<li>

#### Домашняя страница

</li>

<li>

#### Страница регистрации / авторизации

</li>

</ul>

</li>

<li>

### Заключение

</li>

<li>

### Приложение 1. Пример файловой структуры проекта

</li>

<li>

### Приложение 2. Список необходимых библиотек

</li>

<li>

### Обязательно к прочтению. Настройка приложения для работы с телеграм

</li>

</ol>
<br>
<br>
<br>
<br>



## Обзор проекта:

<div id="header" align="center">
  <img src="https://media.giphy.com/media/zt8JjcyjwakSJ9mP56/giphy.gif?cid=ecf05e47l4ex9g2mrdbvx3d3991yuh25xrvvrh314i5rqy04&ep=v1_stickers_search&rid=giphy.gif&ct=s" width="150"/>
</div>

<div align="center" style="color: #000"> 

## Введение:

</div>

<p style="color: #000 ; font-size: 20px; "><strong><em>
В современном мире, где технологии становятся неотъемлемой частью повседневной жизни, возрастает потребность в инструментах, которые позволяют эффективно управлять временем и задачами. Одним из таких инструментов является веб-приложение, разработанное на платформе Django, которое интегрирует голосовое управление и систему напоминаний. Данный проект направлен на создание удобного и интуитивно понятного интерфейса для пользователей, позволяющего создавать задачи и напоминания с помощью голосовых команд, а также получать уведомления в удобной форме.

</strong></em></p>
<br>
<br>
<br>
<br>

<div id="header" align="center">
  <img src="https://media.giphy.com/media/aqY2D3963vIuaq2Cfv/giphy.gif?cid=ecf05e47idkpiw3sun3o5yol7m820aempxy76a7rubx61f75&ep=v1_stickers_search&rid=giphy.gif&ct=s" width="150"/>
</div>

<div align="center" style="color: #000"> 

## Цель проекта:

</div>

<p style="color: #000 ; font-size: 20px; "><strong><em>
Целью проекта является разработка веб-приложения на Django, которое позволяет авторизованным пользователям создавать задачи и напоминания с помощью голосовых команд. Приложение должно обеспечивать следующие функциональные возможности:
<br>
<br>
Голосовое управление: Пользователи могут записывать голосовые команды на домашней странице приложения, которые будут преобразованы в текстовые задачи и напоминания.
<br>
<br>
Напоминания: В назначенное время пользователь получает уведомление в виде всплывающего окна, содержащего текст напоминания и записанную голосовую заметку.
<br>
<br>
Интеграция с Telegram: Если пользователь не подтверждает получение напоминания, оно автоматически отправляется ему в Telegram.

</strong></em></p>
<br>
<br>
<br>
<br>

<div id="header" align="center">
  <img src="https://media.giphy.com/media/I1U6uOX07tI8D1Kcr4/giphy.gif?cid=ecf05e47gt8456s0u5izji2rzpl7ooxz2hxy2rxtktxhrb0b&ep=v1_stickers_search&rid=giphy.gif&ct=s" width="150"/>
</div>

<div align="center" style="color: #000"> 

## Описание функционала:

</div>

### Авторизация пользователя

<p style="color: #000 ; font-size: 20px; "><strong><em>
Приложение начинается с механизма авторизации пользователей. Только авторизованные пользователи имеют доступ к функционалу создания и управления задачами и напоминаниями. Это обеспечивает безопасность данных и персонализацию пользовательского опыта.

</strong></em></p>

### Голосовое управление

<p style="color: #000 ; font-size: 20px; "><strong><em>
На главной странице приложения пользователи находят кнопку микрофона, которая активирует функцию голосового управления. После нажатия на кнопку пользователь может произнести голосовую команду, которая будет записана и обработана. Приложение использует технологии распознавания речи для преобразования голосовой команды в текстовую задачу или напоминание.

</strong></em></p>

### Создание задач и напоминаний

<p style="color: #000 ; font-size: 20px; "><strong><em>
После распознавания голосовой команды приложение создает текстовую задачу или напоминание. Пользователь может указать время, когда ему нужно получить напоминание. Приложение сохраняет задачу или напоминание в базе данных и планирует уведомление на указанное время.

</strong></em></p>

### Уведомления

<p style="color: #000 ; font-size: 20px; "><strong><em>
В назначенное время пользователь получает уведомление в виде всплывающего окна на веб-странице. В окне отображается текст напоминания и кнопка для прослушивания записанной голосовой заметки. Пользователь может подтвердить получение напоминания, нажав на кнопку "ОК". Если пользователь не подтверждает получение напоминания, оно автоматически отправляется ему в Telegram.

</strong></em></p>

### Интеграция с Telegram

<p style="color: #000 ; font-size: 20px; "><strong><em>
Приложение интегрировано с мессенджером Telegram, что позволяет отправлять напоминания пользователям, которые не подтвердили их получение на веб-странице. Это обеспечивает надежность доставки напоминаний и гарантирует, что пользователь не пропустит важную информацию.

</strong></em></p>

### Заключение, или дополнительные идеи для реализации

<p style="color: #000 ; font-size: 20px; "><strong><em>
Разработанное веб-приложение на Django демонстрирует возможности интеграции голосового управления и системы напоминаний в веб-интерфейс. Проект направлен на улучшение пользовательского опыта за счет использования интуитивно понятных и удобных инструментов. Реализация голосового управления и интеграции с Telegram расширяет функциональные возможности приложения и делает его более универсальным и удобным в использовании.
<br>
<br>
Для дополнительной реализации можно создать команды в которой будут роли и возможность разбивать задачи по ролям и также совместное решение задач

</strong></em></p>

## Структура проекта:

<div id="header" align="center">
  <img src="https://media.giphy.com/media/RebuFPBBijsA4nlF9O/giphy.gif?cid=ecf05e47uq1mhvmssfwxrqgx6sq6034hs6as4xwk0a6kv5gl&ep=v1_stickers_search&rid=giphy.gif&ct=s" width="150"/>
</div>

<div align="center" style="color: #000"> 

## Домашняя страница:

</div>

<p style="color: #000 ; font-size: 20px; "><strong><em>
После авторизации пользователь попадает на домашнюю страницу где он может:
<br>
Нажать на кнопку записи после чего начнется запись? что будет видно по анимации кнопки и сработает счетчик записи. Для того чтобы остановить запись нужно нажать еще раз. После остановки запись проиграется автоматически и в правой части экрана появиться заметка, первая часть которой состоит из текста записанного голосом а вторая со временем выполнения заметки.
<br>
Если не обработчик аудио не распознал голос или не было обявленно о времени, то время ставиться текущее.
<br>
После достижении времени появиться окно с текстом заметки и начнет проигрываться голос если нажать ок то все остановиться, если проигнорировать то задание отправиться в телеграмм пользователя

</strong></em></p>
<br>
<br>![Снимок экрана 2024-11-06 в 18 39 49](https://github.com/user-attachments/assets/e1e13c28-fd73-43f8-ae27-c95b6d8fd48b)


<br>
<br>
<br>

<div id="header" align="center">
  <img src="https://media.giphy.com/media/CDFhZhEVBm2RcEL17H/giphy.gif?cid=ecf05e47ficbxhmemk52m732uc9b6oascnopsbbws36j07k4&ep=v1_stickers_search&rid=giphy.gif&ct=s" width="250"/>
</div>

<div align="center" style="color: #000"> 

## Страница регистрации / авторизации:

</div>

<p style="color: #000 ; font-size: 20px; "><strong><em>
Здесь представлена одна страница где пользователь может зарегистрироваться, Валидации особой нет и длина пароля не важна так как проект представлен как тестовый чтобы показать общий функционал
<br>
Снизу в форме есть кнопка переключив которую пользователь попадает на страницу авторизации

</strong></em></p>
<br>
<br>![Снимок экрана 2024-11-06 в 19 04 43](https://github.com/user-attachments/assets/456b32d1-7f2d-4556-abe8-dc96d4d873e0)

<br>
<br>

![Снимок экрана 2024-11-06 в 19 07 07](https://github.com/user-attachments/assets/6fdd0064-d04e-4560-b9d9-bc66185a399c)


## Заключение:

<p style="color: #000 ; font-size: 20px; "><strong><em>
Разработанное веб-приложение на Django демонстрирует возможности интеграции голосового управления и системы напоминаний в веб-интерфейс. Проект направлен на улучшение пользовательского опыта за счет использования интуитивно понятных и удобных инструментов. Реализация голосового управления и интеграции с Telegram расширяет функциональные возможности приложения и делает его более универсальным и удобным в использовании.
<br>
В ходе разработки проекта были реализованы следующие ключевые моменты:
<br>
<br>
**Авторизация пользователей:** 
<br>
Только авторизованные пользователи имеют доступ к функционалу создания и управления задачами и напоминаниями, что обеспечивает безопасность данных и персонализацию пользовательского опыта.
<br>
<br>
**Голосовое управление:** 
<br>
Пользователи могут записывать голосовые команды на домашней странице приложения, которые будут преобразованы в текстовые задачи и напоминания с использованием технологий распознавания речи.
<br>
<br>
**Создание задач и напоминаний:**
<br>
Приложение позволяет пользователям указывать время, когда им нужно получить напоминание, и сохраняет задачи или напоминания в базе данных с планированием уведомлений на указанное время.
<br>
<br>
**Уведомления:** 
<br>
В назначенное время пользователь получает уведомление в виде всплывающего окна на веб-странице, содержащего текст напоминания и записанную голосовую заметку.
<br>
<br>
**Интеграция с Telegram:**
<br>
Если пользователь не подтверждает получение напоминания, оно автоматически отправляется ему в Telegram, что обеспечивает надежность доставки напоминаний и гарантирует, что пользователь не пропустит важную информацию.
<br>
<br>
<br>
Проект успешно реализует поставленные задачи и демонстрирует практическую ценность использования голосового управления и интеграции с мессенджерами для улучшения пользовательского опыта в веб-приложениях. 
<br>
Для дальнейшего развития проекта можно рассмотреть следующие идеи:
<br>
<br>
* **Улучшение распознавания речи:** 
<br>
Использование более продвинутых моделей распознавания речи для повышения точности преобразования голосовых команд в текст.
<br>
<br>
* **Персонализация напоминаний:** 
<br>
Добавление возможности настройки напоминаний (например, повторение напоминаний, выбор способа уведомления).
<br>
<br>
* **Совместное использование задач:** 
<br>
Реализация функционала для совместного использования задач и напоминаний между пользователями.
<br>
<br>
* **Мобильное приложение:** 
<br>
Разработка мобильного приложения для доступа к задачам и напоминаниям на ходу.
В целом, разработанное веб-приложение на Django представляет собой интересный и перспективный проект, который может быть полезен для широкого круга пользователей, желающих эффективно управлять своим временем и задачами с помощью инновационных технологий.

</strong></em></p>
<br>
<br>
<div id="header" align="center">

### Приложение 1. Пример файловой структуры проекта

![Снимок экрана 2024-11-06 в 19 29 01](https://github.com/user-attachments/assets/f5e58774-db06-4a8e-8aaa-9adc886200ae)

  
</div>

<div id="header" align="center">

### Приложение 2. Список необходимых библиотек:
<ul style="color: #000 ; font-size: 20px; font-weight: bold; list-style: none">

<li>
- Django
</li>

<li>
- RestFramework
</li>

<li>
- HTTP
</li>
      
<li>
- Pydub
</li>   

<li>
- PyTelegramBotAPI 
</li>

<li>
- SpeechRecognition 
</li>

<li>
- Property-manager 
</li>

<li>
- Logging
</li>
        
       
       
       
      
</ul>
</div>

### Настройка приложения для работы с телеграм

Для начала создайте бота

</div>![Снимок экрана 2024-11-06 в 20 44 13](https://github.com/user-attachments/assets/37d91aea-561b-4ba5-b2cd-28b0e34b6802)

скопируйте и сохранити HTTP API  

![Снимок экрана 2024-11-06 в 20 49 09](https://github.com/user-attachments/assets/2ddf63fc-bb70-48c5-ad90-ff02bf999c45)

потом вам нужен чат-ид его тоже скопируйте и сохраните

![Снимок экрана 2024-11-06 в 20 46 51](https://github.com/user-attachments/assets/c6600359-39f0-46da-9afb-77c9004d5fac)


потом вам нано зайти в проект и вставить эти данные в переменные

![Снимок экрана 2024-11-06 в 20 52 25](https://github.com/user-attachments/assets/69f512f6-e1e5-42fc-a02a-e1a387969202)

теперь можно можно пользоваться 

Запустите сервер командой python manage.py runserver


</div>



