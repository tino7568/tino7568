## Всем привет 👋
<div id="header" align="center"> 
  <img src="https://media2.giphy.com/media/v1.Y2lkPTZjMDliOTUyZjAwazQ3bHFwbWhnNW0ybzlkbXZ3anRqOHl5aGQ5dHNoOGxhenZuOCZlcD12MV9pbnRlcm5hbF9naWZfYnlfaWQmY3Q9Zw/kt8o8lrHgDlkI/giphy.gif" width="400"/>
</div>
<div align="center">
  <img src="https://img.shields.io/badge/%D0%B7%D0%B0%D0%B9%D1%87%D0%B8%D0%BA%20%D1%83%D1%81%D1%82%D0%B0%D0%BB-99%25-orange" alt="Зайчик устал на:"/>
</div>

## Это учебный гитхаб профиль 🚨

![GitHub Stats](https://github-readme-stats.vercel.app/api?username=tino7568&theme=radical)

## Канбан-проект: Дневник тренировок (Программа на Python) 🐍🏋️‍♂️

### Структура и компоненты программы 👥

<details>
<summary><b>📦 Модуль 1. Справочник упражнений</b></summary>
<blockquote>
<b>Файлы:</b> <code>models/exercise.py</code> / <code>services/catalog.py</code><br>
<b>Функционал:</b> Хранение списка упражнений, группировка по мышечным группам (грудь, спина, ноги и т.д.), добавление собственных упражнений пользователя.
</blockquote>
</details>

<details>
<summary><b>📦 Модуль 2. Журнал тренировочной сессии</b></summary>
<blockquote>
<b>Файлы:</b> <code>models/workout.py</code> / <code>schemas/set_entry.py</code><br>
<b>Функционал:</b> Создание новой тренировки (дата, название). Фиксация подходов внутри упражнения: порядковый номер подхода, рабочий вес, количество повторений.
</blockquote>
</details>

<details>
<summary><b>📦 Модуль 3. Анализ прогресса и Рекордов</b></summary>
<blockquote>
<b>Файлы:</b> <code>services/analytics.py</code><br>
<b>Функционал:</b> Поиск личного рекорда (максимальный вес), расчет суммарного тоннажа (общий поднятый вес), отслеживание роста рабочих весов от даты к дате.
</blockquote>
</details>

<details>
<summary><b>📦 Модуль 4. Профиль и Антропометрия</b></summary>
<blockquote>
<b>Файлы:</b> <code>models/user.py</code> / <code>schemas/metrics.py</code><br>
<b>Функционал:</b> Логирование веса тела, замеров (бицепс, талия и т.д.), расчет индекса массы тела (ИМТ) и установка целевых показателей для тренировочных циклов.
</blockquote>
</details>

<details>
<summary><b>📦 Модуль 5. История и Экспорт данных</b></summary>
<blockquote>
<b>Файлы:</b> <code>services/history.py</code> / <code>utils/export.py</code><br>
<b>Функционал:</b> Разбивка прошлых тренировок по страницам, фильтрация по календарю, сохранение всей истории в текстовый файл для резервной копии.
</blockquote>
</details>

---

### 🏄‍♂️ Канбан

| 📝 Что надо сделать | ⏳ В процессе | 💀 Тестирование | ✅ Всё готово |
| :--- | :--- | :--- | :--- |
| **[Модуль 4]** <br>• Написать структуру таблицы для замеров тела в базе данных <br>• Написать функцию расчета ИМТ на Python <br><br>**[Модуль 5]** <br>• Добавить постраничный вывод для списка прошлых занятий <br><br>**[Модуль 5]** <br>• Написать функцию выгрузки данных в текстовый формат | **[Модуль 3]** <br>• Написать функцию поиска максимального веса среди выполненных подходов <br><br>**[Модуль 2]** <br>• Связать таблицы тренировок и подходов через связи в базе данных | **[Модуль 2]** <br>• Написать проверку вводимых данных (вес и повторения должны быть строго больше нуля) | **[Модуль 1]** <br>• Создать таблицы для упражнений в базе данных <br><br>**[Модуль 1]** <br>• Написать скрипт для автоматического заполнения базы базовыми 30+ упражнениями <br><br>**[Модуль 1]** <br>• Написать сетевой адрес для приема и сохранения новых упражнений пользователя |
| **[Модуль 4]** <br>• Связать таблицу пользователя с историей его тренировок | | | **[Модуль 5]** <br>• Написать автоматические проверки (тесты) для модуля чтения текстовых файлов |

## Всем пока 👀

<div id="header" align="center">
  <img src="https://media3.giphy.com/media/v1.Y2lkPTZjMDliOTUybGRibXlhMzllbzZwZDIydDR1d3JhZTdnZHJhejh0YWNoMXc2ZmppbSZlcD12MV9pbnRlcm5hbF9naWZfYnlfaWQmY3Q9Zw/vikmf2KDVzxyE/giphy.gif" width="500"/>
</div>
