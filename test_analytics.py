from analytics import AnalyticsModule

def run_tests():
    analytics = AnalyticsModule()
    
    print("--- Запуск тестирования ---")

    # 1. Позитивный тест (Happy Path)
    res1 = analytics.get_max_weight([40, 55.5, 60, 52.5])
    print(f"Тест 1 (Ожидается 60.0): {res1}")
    assert res1 == 60.0
    
    # 2. Граничный случай: Пустой список (Edge Case)
    res2 = analytics.get_max_weight([])
    print(f"Тест 2 (Ожидается 0.0): {res2}")
    assert res2 == 0.0

    # 3. Негативный тест: Отрицательные веса (Потенциальный баг)
    res3 = analytics.get_max_weight([-10, -50])
    print(f"Тест 3 (Отрицательные числа): {res3}")
    
    # 4. Негативный тест: Неверный тип данных (Строка вместо числа)
    res4 = analytics.get_max_weight([50, "сто", 70])
    print(f"Тест 4 (Передача строки): {res4}")

if __name__ == "__main__":
    run_tests()
