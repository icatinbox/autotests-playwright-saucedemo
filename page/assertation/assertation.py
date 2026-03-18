import allure

from utils.utils import attach_allure_text

def assert_equal_str(expected_str, actual_str):
    with allure.step('Обрезаем пробелы и приводим к нижнему регистру'):
        actual_str = actual_str.strip().lower()
        expected_str = expected_str.strip().lower()
        attach_allure_text(name='Ожидаемая строка / фактическая строка',text=f'Ожидаемая строка:{expected_str},'
                                                                             f' Фактическая строка: {actual_str}')
    with allure.step('Проверка: Ожидаемая строка совпадает с фактической'):
        assert actual_str == expected_str

