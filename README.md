# Koshelek Project

## Description / Описание

**English:**
This is a test project for registration on the site koshelek.ru. The project includes automated tests for negative scenarios for the fields on the Registration page. The tests are written using Python and Playwright.

## Test Cases
- Sending empty input fields
- Sending fields with only spaces
- Sending incorrect data in input fields(for example, incorrect email)
- Sending correct data in input fields, but without agreement to the agreement
- Sending data with the maximum number of characters in input fields
- Sending data with the maximum number of characters in input fields and one more character
- Sending data with the character "-" in input fields
- Sending data with the maximum number of digits in input fields
- Sending data with Hebrew in input fields
- Sending data with cross-scripting in input fields
- Sending data with SQL injection in input fields


**Русский:**
Это тестовый проект для регистрации на сайте koshelek.ru. Проект включает автоматические тесты для негативных сценариев для полей на странице Регистрация. Тесты написаны с использованием Python и Playwright.

## Test Cases / Тест-кейсы
- Отправка пустых полей ввода
- Отправка полей ввода с только с пробелами
- Отправка некорректных данных в полях ввода(например, некорректный email)
- Отправка корректных данных в полях ввода, но без согласия на соглашение
- Отправка данных с максимальным количеством символов в полях ввода
- Отправка данных с максимальным количеством символов в полях ввода и одним символом больше
- Отправка данных с символом "-" в полях ввода
- Отправка данных с максимальным количеством цифр в полях ввода
- Отправка данных с ивритом в полях ввода
- Отправка данных с кросс-скриптингом в полях ввода
- Отправка данных с SQL-инъекцией в полях ввода


## Installation / Установка

**English:**
1. Clone the repository:
    ```sh
    git clone <repository_url>
    ```
2. Navigate to the project directory:
    ```sh
    cd koshelek-project
    ```
3. Install the dependencies:
    ```sh
    poetry install
    ```

**Русский:**
1. Клонируйте репозиторий:
    ```sh
    git clone <repository_url>
    ```
2. Перейдите в директорию проекта:
    ```sh
    cd koshelek-project
    ```
3. Установите зависимости:
    ```sh
    poetry install
    ```

## Running Tests / Запуск тестов

**English:**
To run the tests, use the following command:
```sh
pytest
```

In the project, you can configure the sizes of the browser window, as well as use the headless mode, base-url, and other parameters. To do this, use command-line parameters. For example:
Example of running tests with browser configuration:
```sh
pytest --size 1792,1120 --headed --base-url https://www.koshelek_v2.ru/
```
where:
- `--size 1792,1120` - browser window size(width, height, default 1920,1080)
- `--headed` - run the browser in headed mode
- `--base-url https://www.koshelek_v2.ru/` - base URL for tests(default https://www.koshelek.ru/)

or as an example:
```sh
pytest --device="iPhone 14 Plus" --browser-channel msedge -screenshot=off --video=off -n 2
```

where:
- `--device="iPhone 14 Plus"` - device to run the tests on(default desktop)
- `--browser-channel msedge` - local browser to run the tests(default chromium)
- `-screenshot=off` - disable taking screenshots when a test fails
- `--video=off` - disable recording video when a test fails
- `-n 2` - number of threads to run tests(default 5)


**Русский:**
Для запуска тестов используйте следующую команду:
```sh
pytest
```

В проекте можно конфигурировать размеры окна браузера, а также использовать headless-режим, base-url и другие параметры. Для этого используйте параметры командной строки. Например:
Пример запуска тестов с конфигурацией браузера:
```sh
pytest --size 1792,1120 --headed --base-url https://www.koshelek_v2.ru/
```
где:
- `--size 1792,1120` - размер окна браузера(ширина, высота, по умолчанию 1920,1080)
- `--headed` - запуск браузера в режиме с графическим интерфейсом
- `--base-url https://www.koshelek_v2.ru/` - базовый URL для тестов(по умолчанию https://www.koshelek.ru/)

или как пример:
```sh
pytest --device="iPhone 14 Plus" --browser-channel msedge -screenshot=off --video=off -n 2
```
где:
- `--device="iPhone 14 Plus"` - устройство для запуска тестов(по умолчанию desktop)
- `--browser-channel msedge` - локальный браузер для запуска тестов(по умолчанию chromium)
- `-screenshot=off` - отключение создания скриншотов при падении теста
- `--video=off` - отключение записи видео при падении теста
- `-n 2` - количество потоков для запуска тестов(по умолчанию 5)

В проекте также реализован CI/CD с использованием GitHub Actions. Тесты будут запускаться после каждого пуша в репозиторий, а также после каждого создания Pull Request и по расписанию в 00:00 UTC.
Результаты отображаются в виде отчетов в формате Allure. И будут отображены в GitHub Pages.

Пример отображения отчета Allure:

![Allure Report](./images/allure_report.png)