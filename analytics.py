class AnalyticsModule:
    def __init__(self):
        # Инициализация (здесь могут быть заглушки при необходимости)
        pass

    def get_max_weight(self, weights: list) -> float:
        """
        Возвращает самый большой поднятый вес из списка сессий/подходов.
        """
        # Защита от пустого списка (Edge Case)
        if not weights:
            return 0.0
            
        # Логика поиска максимального веса
        max_w = float('-inf')
        for w in weights:
            # Пропускаем или обрабатываем только корректные типы данных
            if isinstance(w, (int, float)):
                if w > max_w:
                    max_w = float(w)
                    
        # Если в списке не было валидных чисел
        if max_w == float('-inf'):
            return 0.0

        return max_w
