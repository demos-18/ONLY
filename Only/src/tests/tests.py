from src.page_object.page_object import HandlingClass
import pytest


@pytest.mark.xfail(reason="Вебдрайвер не может заполнить поле 'Номер телефона'. Не возможно пройти проверку на то, что"
                          "вы не являетесь роботом.")
def test_positive_fill_form(chrome):
    """Провеяет, что анкету можно отправить при верном заполнении всех полей."""
    page = HandlingClass(chrome)
    page.go_to_site()
    page.name_field().click()
    page.name_field().clear()
    page.name_field().send_keys("Иван")
    page.email_field().click()
    page.email_field().clear()
    page.email_field().send_keys("ivan.dan452@gmail.com")
    page.phone_field().click()
    page.phone_field().clear()
    page.phone_field().send_keys("9225169845")
    page.company_field().click()
    page.company_field().clear()
    page.company_field().send_keys("TestCase")
    page.complex_work_button().click()
    page.project_description_field().click()
    page.project_description_field().clear()
    page.project_description_field().send_keys("Выполняю тестовое задание.")
    page.price_less_than_two().click()
    page.from_socials_button().click()
    page.i_am_not_a_robot_button().click()

    assert page.name_field().get_attribute("value") == "Иван"
    assert page.email_field().get_attribute("value") == "ivan.dan452@gmail.com"
    assert page.phone_field().get_attribute("value") == "9225169845"
    assert page.project_description_field().get_attribute("data-gtm-form-interact-field-id") == "0"
    assert page.sent_button().isEnabled()





