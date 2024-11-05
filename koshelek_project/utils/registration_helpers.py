class RegistrationHelpers:
    def __init__(self, registration):
        self.registration = registration

    def alert_info_message(self, locator, message):
        self.registration.verify_alert_message(locator, self.registration.alert_message, message)

    def register_user(self, user_data, alert_message=None, check_agreement=True):
        self.registration.fill_username(user_data.username)
        if alert_message:
            self.alert_info_message(self.registration.username, alert_message)
        self.registration.fill_email(user_data.email)
        self.registration.fill_password(user_data.password)
        self.registration.fill_referral_code(user_data.referral_code)
        if check_agreement:
            self.registration.check_user_agreement()
        self.registration.click_on_submit_button()

    def verify_field(self, field, expected_color, message_type, expected_message):
        self.registration.verify_alert_color(field, expected_color)
        self.registration.verify_alert_message(field, message_type, expected_message)

    def verify_all_fields(self, expected_messages=None):
        if expected_messages is None:
            expected_messages = {}
        for field, message in expected_messages.items():
            self.verify_field(
                getattr(self.registration, field),
                self.registration.red_color_border,
                self.registration.alert_message if field != 'password' else self.registration.error_message,
                message
            )
