### Сервис проведения тендеров

### Проблема:
Авито — большая компания, в рамках которой пользователи не только продают/покупают товары и услуги, но и предоставляют помощь крупному бизнесу и предприятиям.
Поэтому ребята из Авито решили сделать сервис, который позволит бизнесу создать тендер на оказание каких-либо услуг. А пользователи/другие бизнесы будут предлагать свои выгодные условия для получения данного тендера.
Помогите ребятам из Авито реализовать новое HTTP API!

### Как запустить проект:
Клонировать репозиторий и перейти в него в командной строке:

```
git clone git@github.com:progmat64/tender_service.git
```


Cоздать, активировать виртуальное окружение и обновить менеджер пакетов:

* Если у вас Linux/macOS:

    ```
    python3 -m venv venv
    source venv/bin/activate
    python3 -m pip install --upgrade pip
    ```

* Если у вас windows:

    ```
    python -m venv venv
    source venv/scripts/activate
    python -m pip install --upgrade pip
    ```


Установить зависимости из файла requirements.txt:

```
pip install -r requirements.txt
```

Выполнить миграции:

```
cd tender_service
```

* Если у вас Linux/macOS:

    ```
    python3 manage.py migrate
    ```

* Если у вас windows:

    ```
    python manage.py migrate
    ```


Запустить проект:


* Если у вас Linux/macOS:

    ```
    python3 manage.py runserver
    ```

* Если у вас windows:

    ```
    python manage.py runserver
    ```

### API

```
GET /api/ping/
GET /api/tenders/
POST /api/tenders/new
GET /api/tenders/my?username=user1
PATCH /api/tenders/1/edit
PUT /api/tenders/1/rollback/2
POST /api/bids/new
GET /api/bids/my?username=user1
PUT /api/bids/1/rollback/2
GET /api/bids/1/reviews?authorUsername=user2&organizationId=1
```

### Примеры работы с API
-   Пользователь отправляет GET-запрос, чтобы проверить, готов ли сервер принимать запросы.

-   Пользователь отправляет POST-запрос на добавление тендера на эндпоинт POST /api/tenders/new.

```json
{
    "creator": "example",
    "name":  "example",
    "description": "example",
    "service_type": "example",
    "organization": 1
}
```

Проект реализован в рамках тестового задания.
