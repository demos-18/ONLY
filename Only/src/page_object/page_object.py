from src.base_page.base_page import BasePage
from src.base_page.base_page import ElementHasCssClass
from selenium.webdriver.common.by import By


class PageLocators:
    """Здесь представлен список локаторов элементов страницы.
    NAME = (By.type_of_locator, 'locator')."""
    HEADER = (By.CLASS_NAME, "sc-60972c5f-0 igbGlc")
    NAME_FIELD = (By.CSS_SELECTOR, "[name = name]")
    EMAIL_FIELD = (By.CSS_SELECTOR, "[name = email]")
    PHONE_NUMBER_FIELD = (By.CSS_SELECTOR, "[name = phone]")
    COMPANY_FIELD = (By.CSS_SELECTOR, "[name = company]")
    COMPLEX_WORK_BUTTON = (By.CSS_SELECTOR, "#__next > div.sc-b2411e17-0.frBgcN.open.openBrief > "
                                            "div.sc-89f88016-0.eRwyBg > div > div.sc-60972c5f-11.hGkDOA > form > "
                                            "div:nth-child(2) > div.sc-60972c5f-6.iVzsq > label:nth-child(1)")
    SITE_BUTTON = (By.CSS_SELECTOR, "#__next > div.sc-b2411e17-0.frBgcN.open.openBrief > div.sc-89f88016-0.eRwyBg > "
                                    "div > div.sc-60972c5f-11.hGkDOA > form > div:nth-child(2) > "
                                    "div.sc-60972c5f-6.iVzsq > label:nth-child(2)")
    SERVICE_BUTTON = (By.CSS_SELECTOR, "#__next > div.sc-b2411e17-0.frBgcN.open.openBrief > div.sc-89f88016-0.eRwyBg > "
                                       "div > div.sc-60972c5f-11.hGkDOA > form > div:nth-child(2) > "
                                       "div.sc-60972c5f-6.iVzsq > label:nth-child(3)")
    DESIGN_BUTTON = (By.CSS_SELECTOR, "#__next > div.sc-b2411e17-0.frBgcN.open.openBrief > div.sc-89f88016-0.eRwyBg > "
                                      "div > div.sc-60972c5f-11.hGkDOA > form > div:nth-child(2) > "
                                      "div.sc-60972c5f-6.iVzsq > label:nth-child(4)")
    UX_BUTTON = (By.CSS_SELECTOR, "#__next > div.sc-b2411e17-0.frBgcN.open.openBrief > div.sc-89f88016-0.eRwyBg > div >"
                                  " div.sc-60972c5f-11.hGkDOA > form > div:nth-child(2) > div.sc-60972c5f-6.iVzsq >"
                                  "label:nth-child(5)")
    BRANDING_BUTTON = (By.CSS_SELECTOR, "#__next > div.sc-b2411e17-0.frBgcN.open.openBrief > div.sc-89f88016-0.eRwyBg >"
                                        " div > div.sc-60972c5f-11.hGkDOA > form > div:nth-child(2) > "
                                        "div.sc-60972c5f-6.iVzsq > label:nth-child(6)")
    PROJECT_DESCRIPTION_FIELD = (By.CSS_SELECTOR, ".sc-30c137f2-1.iQiCsE.sc-60972c5f-8.eGNoom")
    PIN_FILE_BUTTON = (By.CSS_SELECTOR, ".sc-80120d97-3.MPznd")
    BUDGET_LESS_THAN_TWO = (By.CSS_SELECTOR, "#__next > div.sc-b2411e17-0.frBgcN.open.openBrief > "
                                             "div.sc-89f88016-0.eRwyBg > div > div.sc-60972c5f-11.hGkDOA > form > "
                                             "div:nth-child(3) > div > label:nth-child(1)")
    BUDGET_TWO_TO_THREE = (By.CSS_SELECTOR, "#__next > div.sc-b2411e17-0.frBgcN.open.openBrief > "
                                            "div.sc-89f88016-0.eRwyBg > div > div.sc-60972c5f-11.hGkDOA > form > "
                                            "div:nth-child(3) > div > label:nth-child(2)")
    BUDGET_THREE_TO_FIVE = (By.CSS_SELECTOR, "#__next > div.sc-b2411e17-0.frBgcN.open.openBrief >"
                                             " div.sc-89f88016-0.eRwyBg > div > div.sc-60972c5f-11.hGkDOA >"
                                             " form > div:nth-child(3) > div > label:nth-child(3)")
    BUDGET_FIVE_TO_TEN = (By.CSS_SELECTOR, "#__next > div.sc-b2411e17-0.frBgcN.open.openBrief > "
                                           "div.sc-89f88016-0.eRwyBg > div > div.sc-60972c5f-11.hGkDOA > form > "
                                           "div:nth-child(3) > div > label:nth-child(4)")
    BUDGET_TEN_TO_TWENTY = (By.CSS_SELECTOR, "#__next > div.sc-b2411e17-0.frBgcN.open.openBrief > "
                                             "div.sc-89f88016-0.eRwyBg > div > div.sc-60972c5f-11.hGkDOA > form > "
                                             "div:nth-child(3) > div > label:nth-child(5)")
    BUDGET_GREATER_THAN_TWENTY = (By.CSS_SELECTOR, "#__next > div.sc-b2411e17-0.frBgcN.open.openBrief > "
                                                   "div.sc-89f88016-0.eRwyBg > div > div.sc-60972c5f-11.hGkDOA > form >"
                                                   " div:nth-child(3) > div > label:nth-child(6)")
    FROM_RATINGS = (By.CSS_SELECTOR, "#__next > div.sc-b2411e17-0.frBgcN.open.openBrief > div.sc-89f88016-0.eRwyBg > "
                                     "div > div.sc-60972c5f-11.hGkDOA > form > div:nth-child(4) > div > "
                                     "label:nth-child(1)")
    FROM_COPYRIGHT = (By.CSS_SELECTOR, "#__next > div.sc-b2411e17-0.frBgcN.open.openBrief > div.sc-89f88016-0.eRwyBg > "
                                       "div > div.sc-60972c5f-11.hGkDOA > form > div:nth-child(4) > div > "
                                       "label:nth-child(2)")
    FROM_SOCIALS = (By.CSS_SELECTOR, "#__next > div.sc-b2411e17-0.frBgcN.open.openBrief > div.sc-89f88016-0.eRwyBg > "
                                     "div > div.sc-60972c5f-11.hGkDOA > form > div:nth-child(4) > div > "
                                     "label:nth-child(3)")
    FROM_RECOMMENDATION = (By.CSS_SELECTOR, "#__next > div.sc-b2411e17-0.frBgcN.open.openBrief > "
                                            "div.sc-89f88016-0.eRwyBg > div > div.sc-60972c5f-11.hGkDOA > form > "
                                            "div:nth-child(4) > div > label:nth-child(4)")
    FAMILIAR = (By.CSS_SELECTOR, "#__next > div.sc-b2411e17-0.frBgcN.open.openBrief > div.sc-89f88016-0.eRwyBg > div > "
                                 "div.sc-60972c5f-11.hGkDOA > form > div:nth-child(4) > div > label:nth-child(5)")
    I_NOT_A_ROBOT = (By.CSS_SELECTOR, ".recaptcha-checkbox-border")
    SENT_BUTTON = (By.CSS_SELECTOR, ".sc-de2cbdbd-2.dYqUsO")


class ExpectedAttributes:
    """Здесь представлен список ожидаемых атрибутов элементов страницы.
    ATTRIBUTE_NAME = 'attribute_value'."""


class HandlingClass(BasePage):
    """Здесь представлен список методов для взаимодействия с элементами страницы."""
    def header(self):
        header = self.find_element(PageLocators.HEADER, time=10)
        return header

    def name_field(self):
        name_field = self.find_element(PageLocators.NAME_FIELD, time=10)
        return name_field

    def email_field(self):
        email_field = self.find_element(PageLocators.EMAIL_FIELD, time=10)
        return email_field

    def phone_field(self):
        phone_field = self.find_element(PageLocators.PHONE_NUMBER_FIELD, time=10)
        return phone_field

    def company_field(self):
        company_field = self.find_element(PageLocators.COMPANY_FIELD, time=10)
        return company_field

    def complex_work_button(self):
        complex_work_button = self.find_element(PageLocators.COMPLEX_WORK_BUTTON, time=10)
        return complex_work_button

    def site_button(self):
        site_button = self.find_element(PageLocators.SITE_BUTTON, time=10)
        return site_button

    def service_button(self):
        service_button = self.find_element(PageLocators.SERVICE_BUTTON, time=10)
        return service_button

    def design_button(self):
        design_button = self.find_element(PageLocators.DESIGN_BUTTON, time=10)
        return design_button

    def ux_button(self):
        ux_button = self.find_element(PageLocators.UX_BUTTON, time=10)
        return ux_button

    def branding_button(self):
        branding_button = self.find_element(PageLocators.BRANDING_BUTTON, time=10)
        return branding_button

    def project_description_field(self):
        project_description_field = self.find_element(PageLocators.PROJECT_DESCRIPTION_FIELD, time=10)
        return project_description_field

    def price_less_than_two(self):
        price_less_than_two = self.find_element(PageLocators.BUDGET_LESS_THAN_TWO, time=10)
        return price_less_than_two

    def price_two_to_three(self):
        price_two_to_three = self.find_element(PageLocators.BUDGET_TWO_TO_THREE, time=10)
        return price_two_to_three

    def price_three_to_five(self):
        price_three_to_five = self.find_element(PageLocators.BUDGET_THREE_TO_FIVE, time=10)
        return price_three_to_five

    def price_five_to_ten(self):
        price_five_to_ten = self.find_element(PageLocators.BUDGET_FIVE_TO_TEN, time=10)
        return price_five_to_ten

    def price_ten_to_twenty(self):
        price_ten_to_twenty = self.find_element(PageLocators.BUDGET_TEN_TO_TWENTY, time=10)
        return price_ten_to_twenty

    def price_greater_than_twenty(self):
        price_greater_than_twenty = self.find_element(PageLocators.BUDGET_GREATER_THAN_TWENTY, time=10)
        return price_greater_than_twenty

    def from_ratings_button(self):
        from_ratings_button = self.find_element(PageLocators.FROM_RATINGS, time=10)
        return from_ratings_button

    def from_copyright_button(self):
        from_copyright_button = self.find_element(PageLocators.FROM_COPYRIGHT, time=10)
        return from_copyright_button

    def from_socials_button(self):
        from_socials_button = self.find_element(PageLocators.FROM_SOCIALS, time=10)
        return from_socials_button

    def from_recommendation_button(self):
        from_recommendation_button = self.find_element(PageLocators.FROM_RECOMMENDATION, time=10)
        return from_recommendation_button

    def familiar_button(self):
        familiar_button = self.find_element(PageLocators.FAMILIAR, time=10)
        return familiar_button

    def i_am_not_a_robot_button(self):
        i_am_not_a_robot_button = self.find_element(PageLocators.I_NOT_A_ROBOT, time=10)
        return i_am_not_a_robot_button

    def sent_button(self):
        sent_button = self.find_element(PageLocators.SENT_BUTTON, time=10)
        return sent_button





