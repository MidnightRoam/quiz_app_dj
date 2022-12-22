## Quiz app

## Описание работы веб-приложения:

### Начальная страница:
Страница со списком зарегестрированных в системе викторин. Чтобы начать викторину - Пользователь должен зарегестрироваться или войти в систему. 
Система авторизации взята из чистого Django, реализована обработка ошибок, если: пользователь с таким никнеймом уже существует и если введеные пароли при регестрации не совпадают.
Поиск релизован на native JavaScript, поиск осуществляется по любым данным группы.

### Персональная страница викторины:
Здесь расположена краткая информация об выбранной группе: количество вопросов в группе, описание тестовой группы, кнопка начала ответа на вопросы.

### Страница с вопросами группы:
Есть вопрос и ответы к нему, каждый вопрос на отдельной странице, при выборе варианта ответа - появляется кнопка "Submit", которая при нажатии переключает страницу на следующий вопрос.
Если вопросов не осталось - происходит редирект на страницу с результатами.

### Персональные возможности для администрации:
Если пользователь имеет права администратора, то на главной странице у него появляется кнопка добавления тестовой группы, на странице тестовой группы появляются кнопки 
создания вопросов и ответов на вопросы.

### Админ панель: 
В админ панеле зарегестрированы группы вопросов (викторины), из которых можно удалять вопросы/варианты ответов/изменение правильных решений при редактировании тестового набора,
создавать новые вопросы и ответы к ним. Такая возможность реализована при помощи TabularInline связей в admin.py с другими моделями. 

### UX & UI элементы:
1. На главной странице при наведении на блок "Availiable tests" выпадает окно с последними добавленными комнатами в обратном порядке, 
где первая группа в блоке является последней добавленной группой в базу данных.
2. При наведении на значок поиска на главной странице - он раскрывается.
3. При наведении на группу - меняется высота и границы группы, появляется эффект "раскрытия" блока. 

### Пользователи для тестирования:
Вы можете зарегестрировать своих собственных пользователей или использовать следующих:

Админ
Username: Midnight
Password: Momoru00
Обычный пользователь
Username: Nadin
Password: User12345

### Инструменты, задействованные при разработке:
Django - основной backend инструмент
JavaScript - реализация поиска карт на главной странице, включение показа кнопки при выборе ответа на вопрос и заполнения данных на странице регестрации пользователя
HTML/CSS - структура, внешний вид и анимации приложения
