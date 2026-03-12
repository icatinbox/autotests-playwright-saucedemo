import allure

from utils.utils import attach_allure_text

def asser_equal_text(expected_text, actual_text):
    with allure.step('Обрезаем текст и приводим к нижнему регистру'):
        actual_text = actual_text.strip().lower()
        expected_text = expected_text.strip().lower()
        attach_allure_text(name='Ожидаемый / фактический текст',text=f'Ожидаемый текст:{actual_text}, Фактический текст: {actual_text}')
    with allure.step('Проверка: Ожидаемый текст совпадает с фактическим'):
        assert actual_text == expected_text