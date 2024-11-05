from koshelek_project.data.user_data import *
import pytest
import allure


class TestRegistration:

    @pytest.fixture(autouse=True)
    def setup(self, registration):
        self.registration = registration
        self.registration.verify_url_page_and_form_visible()

    @pytest.mark.parametrize(
        "user_data, expected_messages", [
            (
                    invalid,
                    {
                        'username': 'Допустимые символы (от 6 до 32): a-z, 0-9, _. Имя должно начинаться с буквы',
                        'email': 'Формат e-mail: username@test.ru',
                        'password': 'Пароль должен содержать минимум 8 символов'
                    }),
            (
                    empty,
                    {
                        'username': 'Поле не заполнено',
                        'email': 'Поле не заполнено',
                        'password': 'Поле не заполнено'
                    }),
            (
                    with_spase,
                    {
                        'username': 'Поле не заполнено',
                        'email': 'Поле не заполнено',
                        'password': 'Поле не заполнено'
                    }),
        ],ids=['invalid_data', 'empty_data', 'with_space_data'])
    def test_registration_with_various_data(self, request, user_data, expected_messages, registration_helpers):
        allure.dynamic.title(f'Registration with various data: {request.node.callspec.id}')
        registration_helpers.register_user(user_data)
        registration_helpers.verify_all_fields(expected_messages)


    @allure.title('Registration with correct data and without user agreement')
    def test_registration_without_user_agreement_and_correct_data(self, registration, registration_helpers):
        registration_helpers.register_user(correct, check_agreement=False)
        registration_helpers.verify_all_fields()

    @pytest.mark.parametrize(
        "user_data, alert_message, expected_messages", [
            (
                max_count_and_one,
                'Превышен лимит символов: 32 максимум',
                {
                    'username': 'Допустимые символы (от 6 до 32): a-z, 0-9, _. Имя должно начинаться с буквы',
                    'password': 'Пароль должен содержать от 8 до 64 символов, включая заглавные буквы и цифры',
                    'referral_code': 'Неверный формат ссылки'
                }
            ),
            (
                    with_hyphen,
                    f'Введены недопустимые символы: {with_hyphen.username}',
                    {
                        'username': 'Допустимые символы (от 6 до 32): a-z, 0-9, _. Имя должно начинаться с буквы',
                        'password': 'Пароль должен содержать от 8 до 64 символов, включая заглавные буквы и цифры',
                        'referral_code': 'Неверный формат ссылки'
                    }
            )
        ], ids=['max_count_and_one', 'with_hyphen']
    )
    def test_registration_with_max_count_data_and_one(self, request, user_data, alert_message, expected_messages, registration_helpers):
        allure.dynamic.title(f'Registration with various data: {request.node.callspec.id}')
        registration_helpers.register_user(user_data, alert_message)
        registration_helpers.verify_all_fields(expected_messages)

    @pytest.mark.parametrize(
        "user_data, expected_messages", [
            (
                    max_count,
             {
                'password': 'Пароль должен содержать от 8 до 64 символов, включая заглавные буквы и цифры',
                'referral_code': 'Неверный формат ссылки'
            }),
            (
                    with_max_number,
             {
                'password': 'Пароль должен содержать от 8 до 64 символов, включая заглавные буквы и цифры',
                'referral_code': 'Неверный формат ссылки'
             })
        ], ids=['max_count', 'with_max_number'])
    def test_registration_with_max_values(self, request, user_data, expected_messages, registration_helpers):
        allure.dynamic.title(f'Registration with various data: {request.node.callspec.id}')
        registration_helpers.register_user(user_data)
        registration_helpers.verify_all_fields(expected_messages)

    @pytest.mark.parametrize(
        "user_data, alert_message, expected_messages", [
            (
                with_hebrew,
                f'Введены недопустимые символы: {with_hebrew.username}',
                {
                    'username': 'Допустимые символы (от 6 до 32): a-z, 0-9, _. Имя должно начинаться с буквы',
                    'password': 'Пароль должен содержать от 8 до 64 символов, включая заглавные буквы и цифры'
                }
            ),
            (
                with_cross_script,
                'Введены недопустимые символы: &lt;&gt;(&quot;)&#x2F;',
                {
                    'username': 'Допустимые символы (от 6 до 32): a-z, 0-9, _. Имя должно начинаться с буквы',
                    'email': 'Формат e-mail: username@test.ru',
                    'referral_code': 'Неверный формат ссылки'
                }
            ),
            (
                with_sql_injection,
                'Введены недопустимые символы: ;',
                {
                    'username': 'Допустимые символы (от 6 до 32): a-z, 0-9, _. Имя должно начинаться с буквы',
                    'email': 'Формат e-mail: username@test.ru',
                    'password': 'Пароль должен содержать от 8 до 64 символов, включая заглавные буквы и цифры',
                    'referral_code': 'Неверный формат ссылки'
                }
            )
        ],
        ids=['hebrew_data', 'cross_script_data', 'sql_injection_data']
    )
    def test_registration_with_special_characters(self, request, user_data, alert_message, expected_messages, registration_helpers):
        allure.dynamic.title(f'Registration with various data: {request.node.callspec.id}')
        registration_helpers.register_user(user_data, alert_message)
        registration_helpers.verify_all_fields(expected_messages)