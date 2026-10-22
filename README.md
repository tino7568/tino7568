## Всем привет 👋
<div id="header" align="center"> 
  <img src="https://media2.giphy.com/media/v1.Y2lkPTZjMDliOTUyZjAwazQ3bHFwbWhnNW0ybzlkbXZ3anRqOHl5aGQ5dHNoOGxhenZuOCZlcD12MV9pbnRlcm5hbF9naWZfYnlfaWQmY3Q9Zw/kt8o8lrHgDlkI/giphy.gif" width="400"/>
</div>
<div align="center">
  <img src="https://img.shields.io/badge/%D0%B7%D0%B0%D0%B9%D1%87%D0%B8%D0%BA%20%D1%83%D1%81%D1%82%D0%B0%D0%BB-99%25-orange" alt="Зайчик устал на:"/>
</div>

## Это учебный гитхаб профиль 🚨

![GitHub Stats](https://github-readme-stats.vercel.app/api?username=tino7568&theme=radical)

## Проект для колледжа: Дневник тренировок 🏋️‍♂️

### Пользовательские истории 👥

**📦 Модуль 1. Справочник упражнений**
* **Файлы:** `models/exercise.py` / `services/catalog.py`
* **История:** Я, как пользователь, хочу выбирать упражнения по названию мышцы, чтобы не запутаться в незнакомых названиях.

**📦 Модуль 2. Журнал тренировочной сессии**
* **Файлы:** `models/workout.py` / `schemas/set_entry.py`
* **История:** Я, как пользователь, хочу записывать количество сделанных повторений, чтобы помнить свою прошлую нагрузку.

**📦 Модуль 3. Анализ прогресса и Рекордов**
* **Файлы:** `services/analytics.py`
* **История:** Я, как пользователь, хочу видеть свой самый большой поднятый вес, чтобы замечать личный прогресс.

**📦 Модуль 4. Профиль и Антропометрия**
* **Файлы:** `models/user.py` / `schemas/metrics.py`
* **История:** Я, как пользователь, хочу записывать свой текущий вес в килограммах, чтобы следить за изменениями тела.

**📦 Модуль 5. История и Экспорт данных**
* **Файлы:** `services/history.py` / `utils/export.py`
* **История:** Я, как пользователь, хочу скачивать историю своих занятий на компьютер, чтобы не потерять её при удалении приложения.

---

### Канбан-доска 🏄‍♂️

https://github.com/users/tino7568/projects/1/views/1

### Команда 😎

* Белоконь код (Я😎😎😎😎😎😎😎😎😎)
* Борисенков дизайн
* Болотников тестирование
* Вереуссел бета тестирование

# Отчет по лабораторной работе №3

## Таблица Bug Report

| ID | Модуль и метод | Входные данные | Ожидаемый результат | Фактический результат |
| :--- | :--- | :--- | :--- | :--- |
| **BUG-01** | `AnalyticsModule.get_max_weight` | Список с отрицательным весом: `[-20, -10]` | Метод должен проигнорировать отрицательные значения или выдать ошибку (вес не может быть меньше 0). | Метод вернул `-10.0` как максимальный вес. |
| **BUG-02** | `AnalyticsModule.get_max_weight` | Список со строкой: `[50, "100", 60]` | Система должна отфильтровать строку или вызвать контролируемое исключение. | Программа упала с критической ошибкой `TypeError`. |


## Всем пока 👀

<div id="header" align="center">
  <img src="https://media3.giphy.com/media/v1.Y2lkPTZjMDliOTUybGRibXlhMzllbzZwZDIydDR1d3JhZTdnZHJhejh0YWNoMXc2ZmppbSZlcD12MV9pbnRlcm5hbF9naWZfYnlfaWQmY3Q9Zw/vikmf2KDVzxyE/giphy.gif" width="500"/>
</div>
