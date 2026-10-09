## Всем привет 👋
<div id="header" align="center"> 
  <img src="https://media2.giphy.com/media/v1.Y2lkPTZjMDliOTUyZjAwazQ3bHFwbWhnNW0ybzlkbXZ3anRqOHl5aGQ5dHNoOGxhenZuOCZlcD12MV9pbnRlcm5hbF9naWZfYnlfaWQmY3Q9Zw/kt8o8lrHgDlkI/giphy.gif" width="400"/>
</div>
<div align="center">
  <img src="https://img.shields.io/badge/%D0%B7%D0%B0%D0%B9%D1%87%D0%B8%D0%BA%20%D1%83%D1%81%D1%82%D0%B0%D0%BB-99%25-orange" alt="Зайчик устал на:"/>
</div>

## Это учебный гитхаб профиль 🚨

![GitHub Stats](https://github-readme-stats.vercel.app/api?username=tino7568&theme=radical)

## Канбан-проект: Дневник тренировок 🏋️‍♂️

### Пользовательские истории 👥

<details>
<summary><b>📦 Модуль 1. Справочник упражнений (Exercise Catalog Module)</b></summary>
<blockquote>
<b>Класс:</b> <code>Exercise</code> / <code>CatalogService</code><br>
<b>Функционал:</b> Хранение списка упражнений, группировка по мышечным группам (грудь, спина, ноги и т.д.), добавление кастомных упражнений пользователя.
</blockquote>
</details>

<details>
<summary><b>📦 Модуль 2. Журнал тренировочной сессии (Workout Session Module)</b></summary>
<blockquote>
<b>Класс:</b> <code>Workout</code> / <code>SetEntry</code><br>
<b>Функционал:</b> Создание новой тренировки (дата, название). Фиксация сетов внутри упражнения: порядковый номер подхода, рабочий вес, количество повторений.
</blockquote>
</details>

<details>
<summary><b>📦 Модуль 3. Анализ прогресса и Рекордов (Progress Tracker Module)</b></summary>
<blockquote>
<b>Класс:</b> <code>ProgressAnalytics</code><br>
<b>Функционал:</b> Поиск личного рекорда (максимальный вес), расчет суммарного тоннажа (общий поднятый вес), отслеживание роста рабочих весов от даты к дате.
</blockquote>
</details>

<details>
<summary><b>📦 Модуль 4. Профиль и Антропометрия (User Profile & Body Metrics)</b></summary>
<blockquote>
<b>Класс:</b> <code>UserProfile</code> / <code>BodyMetricLog</code><br>
<b>Функционал:</b> Логирование веса тела, замеров (бицепс, талия и т.д.), расчет индекса массы тела (ИМТ) и установка целевых показателей для тренировочных циклов.
</blockquote>
</details>

<details>
<summary><b>📦 Модуль 5. История и Экспорт данных (History & Data Export Module)</b></summary>
<blockquote>
<b>Класс:</b> <code>HistoryService</code> / <code>ExportManager</code><br>
<b>Функционал:</b> Пагинация прошлых тренировок, фильтрация по календарю, экспорт всей истории в CSV/JSON для бэкапа (чтобы не потерять данные при замене телефона).
</blockquote>
</details>

---

### 🏄‍♂️ Канбан

| 📝 Что надо сделать (Todo) | ⏳ В процессе (In Progress) | 💀 Тестирование (Test) | ✅ Всё готово (Done) |
| :--- | :--- | :--- | :--- |
| **[Модуль 4]** <br>• Спроектировать класс `BodyMetricLog` <br>• Написать метод расчета ИМТ <br><br>**[Модуль 5]** <br>• Добавить пагинацию для списка сессий в `HistoryService` <br><br>**[Модуль 5]** <br>• Реализовать `ExportManager` для выгрузки в JSON | **[Модуль 3]** <br>• Написать алгоритм поиска личного рекорда в `ProgressAnalytics` <br><br>**[Модуль 2]** <br>• Реализовать класс `Workout` и связать с `SetEntry` | **[Модуль 2]** <br>• Проверить валидацию данных в `SetEntry` (вес > 0, повторения > 0) | **[Модуль 1]** <br>• Спроектировать структуру данных для `Exercise` <br><br>**[Модуль 1]** <br>• Реализовать базовый список дефолтных упражнений <br><br>**[Модуль 1]** <br>• Протестировать `CatalogService` на корректность фильтрации <br><br>**[Модуль 1]** <br>• Добавить метод создания кастомных упражнений |
| **[Модуль 4]** <br>• Создать класс `UserProfile` и настроить связи | | | **[Модуль 5]** <br>• Покрыть тестами парсер CSV в модуле экспорта |


## Всем пока 👀

<div id="header" align="center">
  <img src="https://media3.giphy.com/media/v1.Y2lkPTZjMDliOTUybGRibXlhMzllbzZwZDIydDR1d3JhZTdnZHJhejh0YWNoMXc2ZmppbSZlcD12MV9pbnRlcm5hbF9naWZfYnlfaWQmY3Q9Zw/vikmf2KDVzxyE/giphy.gif" width="500"/>
</div>
