# Пользовательская документация

## 1. Введение

Программа "Анализатор изображений" предназначена для автоматической обработки изображений из указанной папки. Она позволяет получать информацию о размере изображений, их разрешении (DPI), глубине цвета и типе компрессии. Программа имеет графический интерфейс, отображающий результаты анализа в удобной таблице.

## 2. Системные требования

- **Операционная система**: Windows 7 и выше, Linux, macOS
- **Программное обеспечение**: Python 3.x
- **Библиотеки**:
  - `Pillow` (PIL)
  - `Tkinter` (входит в стандартную библиотеку Python)
- **Аппаратные требования**:
  - Минимум 512 МБ ОЗУ
  - 50 МБ свободного места на диске

## 3. Установка

### 3.1 Установка Python

1. Перейдите на официальный сайт Python: [python.org](https://www.python.org/).
2. Скачайте последнюю версию Python 3.x.
3. При установке отметьте опцию **Add Python to PATH**.
4. Убедитесь, что Python установлен, введя в командной строке:
   ```
   python --version
   ```

### 3.2 Установка библиотек

Установите библиотеку `Pillow`, если она отсутствует. В командной строке выполните:
```
pip install pillow
```

### 3.3 Скачивание программы

1. Скачайте файл программы `image_analyzer.py` из репозитория (или другого источника).
2. Убедитесь, что файл сохранен в отдельной папке.

### 3.4 Запуск программы

1. Откройте командную строку.
2. Перейдите в папку с файлом программы:
   ```
   cd путь/к/папке
   ```
3. Запустите программу:
   ```
   python image_analyzer.py
   ```

## 4. Использование приложения

### 4.1 Выбор папки с изображениями

1. После запуска программы появится окно выбора папки.
2. Укажите путь к папке, содержащей изображения.

### 4.2 Поддерживаемые форматы изображений

Программа поддерживает следующие форматы:
- **JPG/JPEG**
- **GIF**
- **TIFF**
- **BMP**
- **PNG**
- **PCX**

### 4.3 Анализ изображений

- После выбора папки программа автоматически обработает все изображения.
- Если изображения не обнаружены, появится сообщение об ошибке.

### 4.4 Отображение результатов

Результаты анализа отображаются в таблице с колонками:
- **File Name**: имя файла изображения.
- **Size (px)**: размер изображения в пикселях (ширина × высота).
- **Resolution (DPI)**: разрешение изображения.
- **Color Depth**: глубина цвета (бит).
- **Compression**: используемый тип компрессии (если указан).

### 4.5 Закрытие приложения

Для завершения работы закройте окно таблицы.

## 5. Пример использования

### Пример анализа папки

1. Создайте папку `images` и поместите в неё изображения:
   - `example1.jpg` (1920×1080, DPI: 72, 24-bit, JPEG)
   - `example2.png` (800×600, DPI: 96, 32-bit, PNG)
2. Запустите программу.
3. Укажите путь к папке `images`.
4. Программа выведет результаты анализа в таблице:
   ```
   File Name      Size (px)       Resolution (DPI)   Color Depth   Compression
   example1.jpg   1920x1080       72x72              24 bit        JPEG
   example2.png   800x600         96x96              32 bit        N/A
   ```

## 6. Обратная связь

Для вопросов и предложений обращайтесь на почту: **agadjangarlyev@gmail.com**.

## 7. Приложения

### Приложение 1. Возможности программы

1. Автоматический анализ изображений в папке.
2. Вывод информации о каждом файле:
   - Размер (ширина × высота в пикселях).
   - Разрешение (DPI).
   - Глубина цвета.
   - Тип компрессии.
3. Удобный графический интерфейс на основе Tkinter.

### Приложение 2. Описание функций

#### `get_image_info(file_path)`
- **Описание**: Получает информацию об изображении.
- **Входные данные**: Путь к файлу изображения.
- **Возвращает**: Имя файла, размер изображения, DPI, глубину цвета, тип компрессии.

#### `load_images_from_folder(folder)`
- **Описание**: Загружает все изображения из указанной папки.
- **Входные данные**: Путь к папке.
- **Возвращает**: Список информации об изображениях.

#### `display_results(data)`
- **Описание**: Отображает результаты анализа в виде таблицы.
- **Входные данные**: Список данных об изображениях.

#### `main()`
- **Описание**: Основная функция программы. Запускает интерфейс для выбора папки, анализирует изображения и отображает результаты.

### Приложение 3. Часто задаваемые вопросы

#### В: Почему некоторые изображения не отображаются в таблице?  
О: Проверьте, поддерживается ли формат файла (см. раздел 4.2).

#### В: Программа не открывается или выдает ошибку. Что делать?  
О: Убедитесь, что Python установлен корректно и библиотека `Pillow` установлена.

#### В: Можно ли анализировать изображения в подпапках?  
О: На данный момент программа работает только с файлами в указанной папке.

## Лицензия

Программа распространяется под лицензией MIT. Подробности смотрите в файле `LICENSE`.

## Дополнительные материалы

- Официальный сайт Python: [python.org](https://www.python.org/)
- Документация библиотеки Pillow: [pillow.readthedocs.io](https://pillow.readthedocs.io/)