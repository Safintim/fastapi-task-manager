[![wemake-python-styleguide](https://img.shields.io/badge/style-wemake-000000.svg)](https://github.com/wemake-services/wemake-python-styleguide)

# Менеджер задач

API [менеджера задач](https://python-l4-task-manager.herokuapp.com/), разработанный на fastapi.


## Как установить

Для работы нужен python версии не ниже 3.9. В качестве менеджера зависимостей используется poetry.

```bash
make install # установить
make test # проверить код
make init-db # создание таблиц
```

## Переменные окружения

Создать файл _.env_ в корне проекта

 - SERVER_HOST
 - SERVER_PORT


### Статус

_В разработке_
