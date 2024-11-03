class UserData:
    def __init__(self, username, email, password, referral_code):
        self.username = username
        self.email = email
        self.password = password
        self.referral_code = referral_code

empty = UserData('', '', '', '')
with_spase = UserData(' ', ' ', ' ', ' ')
invalid = UserData('test', 'test@', 'test', 'test')
correct = UserData('Andrey', 'andrey@gmail.com', 'Andrey1234*andrey', 'Andrey')
max_count_and_one = UserData('a' * 32 + '1', 'a' * 32 + '@gmail.com', 'a' * 64 + '1', 'a' * 64 + '1')
max_count = UserData('b' * 32, 'b' * 32 + '@gmail.com', 'b' * 64, 'b' * 64)
with_hyphen = UserData('-', '-' + '@gmail.com', '-' * 64, '-' * 64)
with_max_number = UserData('1' * 32, '1' * 32 + '@gmail.com', '1' * 64, '1' * 64)
with_hebrew = UserData('אנדרי', 'אנדרי@gmail.com', 'אנדרי1234*אנדרי', 'אנדרי')
with_cross_script = UserData('<script>alert("XSS")</script>', '<script>alert("XSS")</script>@gmail.com',
                                '<script>alert("XSS")</script>1234',
                             '<script>alert("XSS")</script>')
with_sql_injection = UserData('Andrey; DROP TABLE users;', 'Andrey; DROP TABLE users;@gmail.com',
                                'Andrey; DROP TABLE users;1234', 'Andrey; DROP TABLE users;')
