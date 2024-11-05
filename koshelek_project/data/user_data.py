class UserData:
    def __init__(self, username, email, password, referral_code):
        self.username = username
        self.email = email
        self.password = password
        self.referral_code = referral_code

empty = UserData(
    username='',
    email='',
    password='',
    referral_code=''
)
with_spase = UserData(
    username=' ',
    email=' ',
    password=' ',
    referral_code=' '
)
invalid = UserData(
    username='test',
    email='test@',
    password='test',
    referral_code='test'
)
correct = UserData(
    username='Andrey',
    email='andrey@gmail.com',
    password='Andrey1234*andrey',
    referral_code='Andrey'
)
max_count_and_one = UserData(
    username='a' * 32 + '1',
    email='a' * 32 + '@gmail.com',
    password='a' * 64 + '1',
    referral_code='a' * 64 + '1'
)
max_count = UserData(
    username='b' * 32,
    email='b' * 32 + '@gmail.com',
    password='b' * 64,
    referral_code='b' * 64
)
with_hyphen = UserData(
    username='-',
    email='-' + '@gmail.com',
    password='-' * 64,
    referral_code='-' * 64
)
with_max_number = UserData(
    username='1' * 32,
    email='1' * 32 + '@gmail.com',
    password='1' * 64,
    referral_code='1' * 64
)
with_hebrew = UserData(
    username='אנדרי',
    email='אנדרי@gmail.com',
    password='אנדרי1234*אנדרי',
    referral_code='אנדרי'
)
with_cross_script = UserData(
    username='<script>alert("XSS")</script>',
    email='<script>alert("XSS")</script>@gmail.com',
    password='<script>alert("XSS")</script>1234',
    referral_code='<script>alert("XSS")</script>'
)
with_sql_injection = UserData(
    username='Andrey; DROP TABLE users;',
    email='Andrey; DROP TABLE users;@gmail.com',
    password='Andrey; DROP TABLE users;1234',
    referral_code='Andrey; DROP TABLE users;'
)

