# Интернет-магазин SkyStore 🛍️

Проект интернет-магазина, разработанный в рамках курса по Django.

## Описание проекта
Данный проект представляет собой базовую реализацию интернет-магазина с каталогом товаров, возможностью просмотра деталей продукта и формой обратной связи для взаимодействия с клиентами.

## ✨ Ключевые особенности
-   **Каталог товаров**: Отображение списка доступных товаров с их описанием и ценой.
-   **Детали продукта**: Просмотр подробной информации о каждом товаре.
-   **Форма обратной связи**: Добавление контактов для возможности сообщения администрации магазина.
-   **Административная панель Django**: Управление товарами и категориями через стандартный интерфейс администратора Django.

## 🛠️ Технологии
Проект разработан с использованием следующих технологий:
-   Python 3.13
-   Django 5.2
-   PostgreSQL (в качестве основной базы данных)
-   `psycopg2` (для установки пакета с драйвером PostgreSQL)
-   `python-dotenv` (для переменных окружения)
-   Bootstrap 5 (для стилизации фронтенда)


## ▶️ Установка и запуск
=======
*   Python 3.13
*   Django 5.2 
*   PostgreSQL (в качестве основной базы данных)
*   python-dotenv (для управления переменными окружения)
*   Bootstrap 5 (для стилизации фронтенда)

## Установка и запуск


Для установки и запуска проекта выполните следующие шаги:

1.  **Клонируйте репозиторий**:
    ```bash
    git clone <URL вашего репозитория> # Замените <URL вашего репозитория> на фактический URL вашего репозитория на GitHub
    cd Doczadrot-DjangoHomeWork # Замените на имя вашей папки, если оно другое
    ```

2.  **Создайте виртуальное окружение (рекомендуется)**:
    ```bash
    python -m venv venv
    ```

3.  **Активируйте виртуальное окружение**:
    * **Для Windows**:
        ```bash
        .\venv\Scripts\activate
        ```
    * **Для macOS и Linux**:
        ```bash
        source venv/bin/activate
        ```

4.  **Установите зависимости**:
    ```bash
    pip install -r requirements.txt
    ```

5.  **Настройте базу данных PostgreSQL**:
    * Убедитесь, что у вас установлен и запущен сервер PostgreSQL.
    * Создайте базу данных для проекта (например, `skystore_db`).
    * Создайте файл `.env` в корневой директории проекта (он не включен в репозиторий) со следующими переменными:
        ```dotenv
        DEBUG=True
        SECRET_KEY='ваш_секретный_ключ' # Сгенерируйте свой уникальный ключ!
        DB_NAME=skystore_db
        DB_USER=ваш_пользователь_pg
        DB_PASSWORD=ваш_пароль_pg
        DB_HOST=localhost
        DB_PORT=5432
        ```
        *Если у вас другие названия переменных для Django, используйте их.*

6.  **Выполните миграции Django**:
    ```bash
    python manage.py makemigrations
    python manage.py migrate
    ```

7.  **Создайте суперпользователя (для доступа в админ-панель Django)**:
    ```bash
    python manage.py createsuperuser
    ```
    Следуйте инструкциям в консоли для создания логина и пароля.

8.  **Запустите сервер разработки Django**:
    ```bash
    python manage.py runserver
    ```
    Теперь вы можете открыть проект в браузере по адресу `http://127.0.0.1:8000/`. Административная панель будет доступна по адресу `http://127.0.0.1:8000/admin/`.


## ✍️ Автор
Проект разработан в рамках учебного задания.
=======
Проект будет доступен по адресу <mcurl name="http://127.0.0.1:8000/" url="http://127.0.0.1:8000/"></mcurl>.

## Структура проекта