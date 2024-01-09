# Sprint_5

Проект тестирования для сайта заказа бургеров Stellar Burgers


# Тесты:


# Регистрация успешная / не успешная

Успешная регистрация. Поле «Имя» должно быть не пустым; в поле Email введён email в формате логин@домен: например, 123@ya.ru. Минимальный пароль — шесть символов.
test_registration_correct

Ошибка для некорректного пароля.
test_registration_error_pass

# переход в личный кабинет

test_go_to_personal_account
Переход в личный кабинет

# Вход в профиль

test_personal_area_log_in
вход по кнопке «Войти в аккаунт» на главной,

test_sign_to_personal_area
вход через кнопку «Личный кабинет»,

test_sign_in_after_registration
вход через кнопку в форме регистрации,

test_log_in_by_password_recovery_button
вход через кнопку в форме восстановления пароля.

# Выход из профиля

test_logout
Выход из аккаунта

# Переход из личного кабинета в конструктор 

test_constructor_btn
переход по клику на «Конструктор»

test_logo_btn
преход по логотипу Stellar Burgers

# Раздел «Конструктор» переходы к разделам:

test_go_to_buns
«Булки»,

test_go_to_sauce
«Соусы»,

test_go_to_fillings
«Начинки».