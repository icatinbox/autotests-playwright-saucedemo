import allure

def attach_allure_text(name, text):
    allure.attach(text or "", name, attachment_type=allure.attachment_type.TEXT)
