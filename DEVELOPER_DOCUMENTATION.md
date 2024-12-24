# Документация разработчика

## Текст программы

### Наименование программы

**ImageInfoApp** — приложение для анализа изображений, извлечения и отображения их основных характеристик.

### Область применения

Программа предназначена для анализа изображений в выбранной папке. Она позволяет получить информацию о характеристиках изображений, таких как размер, разрешение, глубина цвета и метод сжатия. Это полезно для работы с большими наборами изображений, в том числе в области графического дизайна, обработки изображений и оценки качества.

### Назначение программы

- Сканирование указанной папки для поиска изображений.
- Извлечение и отображение информации об изображениях:
  - Имя файла.
  - Размер (в пикселях).
  - Разрешение (DPI).
  - Глубина цвета (бит).
  - Метод сжатия (если доступен).
- Демонстрация полученной информации в графическом интерфейсе.

### Функциональные возможности

- Поддержка популярных форматов изображений: `.jpg`, `.jpeg`, `.gif`, `.tif`, `.tiff`, `.bmp`, `.png`, `.pcx`.
- Автоматическое извлечение метаинформации об изображениях с использованием библиотеки PIL (Pillow).
- Отображение результатов в таблице с возможностью прокрутки.
- Возможность выбора папки с изображениями через графический интерфейс.

---

## Описание программы

### Структура программы

- **Функции**:
  - `get_image_info(file_path)`:
    - Извлекает информацию об изображении, включая имя файла, размер, разрешение, глубину цвета и метод сжатия.
    - Возвращает кортеж с этими данными.
  - `load_images_from_folder(folder)`:
    - Сканирует папку на наличие изображений поддерживаемых форматов.
    - Для каждого файла вызывает функцию `get_image_info`.
    - Возвращает список информации об изображениях.
  - `display_results(data)`:
    - Отображает таблицу с информацией об изображениях в графическом интерфейсе с использованием Tkinter.
    - Использует `ttk.Treeview` для создания таблицы.
  - `main()`:
    - Открывает диалог выбора папки с изображениями.
    - Вызывает функции для анализа и отображения данных.
- **Главный блок**:
  - Запускает программу с вызовом функции `main()`.

---

### Используемые библиотеки и модули

- **os**: для работы с файловой системой (чтение списка файлов в папке).
- **Pillow (PIL)**: для обработки изображений и извлечения их характеристик.
- **tkinter**: для создания графического интерфейса.
- **ttk**: для создания таблицы с информацией об изображениях.

---

### Логические структуры данных

- **Переменные**:
  - `supported_formats`: кортеж с поддерживаемыми форматами изображений.
  - `image_info_list`: список, содержащий информацию об изображениях в виде кортежей.
- **Возвращаемые значения**:
  - `get_image_info`: возвращает кортеж с характеристиками изображения.
  - `load_images_from_folder`: возвращает список кортежей с информацией об изображениях.
  - `main`: вызывает графический интерфейс для выбора папки и отображения данных.

---

### Взаимодействие с пользователем

1. **Выбор папки**:
   - Пользователь выбирает папку через графический интерфейс с помощью диалога `filedialog.askdirectory`.
2. **Сканирование папки**:
   - Программа анализирует содержимое папки, отбирая файлы поддерживаемых форматов.
3. **Отображение информации**:
   - Результаты анализа выводятся в таблице, где каждая строка соответствует отдельному изображению.
   - Таблица содержит следующие столбцы:
     - Имя файла.
     - Размер изображения (ширина x высота).
     - Разрешение (DPI).
     - Глубина цвета.
     - Метод сжатия.

---

## Инструкция по установке и запуску

### Требования к системе

- **Python** версии 3.6 и выше.
- Установленная библиотека Pillow.

### Установка

1. **Убедитесь, что установлен Python**:
   ```
   python --version
   ```

2. **Установите библиотеку Pillow**:
   ```
   pip install pillow
   ```

3. **Проверьте наличие tkinter**:
   - Для Ubuntu/Debian:
     ```
     sudo apt-get install python3-tk
     ```

### Запуск программы

1. Сохраните код программы в файл с расширением `.py`, например, `image_info_app.py`.

2. Запустите программу:
   ```
   python image_info_app.py
   ```

---

## Инструкция пользователя

1. **Запустите программу**.
2. **Выберите папку**:
   - В появившемся диалоговом окне выберите папку, содержащую изображения.
3. **Просмотрите результаты**:
   - После анализа изображений программа отобразит таблицу с информацией об изображениях.
   - В таблице можно прокручивать список вверх и вниз, чтобы изучить данные.

---

## Требования к техническим характеристикам

- **Процессор**: не менее 1 ГГц.
- **Оперативная память**: не менее 512 МБ.
- **Дисплей**: поддержка разрешения не менее 1024x768.

---

## Обработка ошибок

- **Некорректный файл**:
  - Если файл невозможно открыть как изображение, он пропускается.
- **Пустая папка**:
  - Если в выбранной папке нет поддерживаемых форматов изображений, программа выводит сообщение: "No valid image files found".
- **Необработанные ошибки**:
  - Исключения, возникающие при чтении файлов, выводятся в консоль.

---

## Дополнительные сведения

### Поддерживаемые форматы изображений

- `.jpg`, `.jpeg`
- `.gif`
- `.tif`, `.tiff`
- `.bmp`
- `.png`
- `.pcx`

### Извлекаемая информация

1. **Имя файла**: отображает имя изображения.
2. **Размер**: ширина и высота изображения в пикселях.
3. **Разрешение (DPI)**: разрешение изображения в точках на дюйм.
4. **Глубина цвета**: количество бит на пиксель (8, 16, 24 и т. д.).
5. **Метод сжатия**: информация о сжатии изображения (если доступна в метаданных).

---

## Сопровождение и развитие

- Код программы хорошо структурирован и снабжен комментариями.
- Для добавления новых функций (например, дополнительных характеристик изображений) необходимо модифицировать функцию `get_image_info`.
- Возможность сортировки данных в таблице или экспорта информации в файл может быть добавлена в будущем.

---

## Заключение

Программа **ImageInfoApp** предоставляет удобный инструмент для анализа характеристик изображений в выбранной папке. Она поддерживает популярные форматы изображений и отображает ключевую информацию в удобном графическом интерфейсе. Благодаря использованию библиотек Pillow и Tkinter, программа легко расширяется и сопровождается.

Чтобы создать .exe файл из Python-кода, используется библиотека pyinstaller. Вот пошаговая инструкция:
1. Установите библиотеку pyinstaller
Откройте терминал в PyCharm или командную строку и выполните:
Copy
pip install pyinstaller
2. Подготовьте ваш .py файл
Убедитесь, что ваш Python-скрипт работает корректно. Например, пусть у вас есть файл main.py, который вы хотите превратить в .exe.

3. Создайте .exe файл с помощью pyinstaller
В терминале PyCharm выполните следующую команду:
Copy
pyinstaller --onefile main.py
--onefile: объединяет все файлы в один .exe.
main.py: это ваш Python-скрипт.
После выполнения команды в папке проекта появятся новые директории, такие как build и dist.