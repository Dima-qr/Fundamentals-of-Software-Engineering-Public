import sys

expressions = [
    ("1. '123е'", lambda: int('123е')),
    ("2. '91.4'", lambda: int('91.4')),
    ("3. 524.345 ** 435345345311145345", lambda: int(524.345 ** 435345345311145345)),
    ("4. '7.1 + 4'", lambda: int('7.1 + 4')),
    ("5. '4' - 2", lambda: int('4' - 2)),
    ("6. '4 - 2'", lambda: int('4 - 2')),
    ("7. '42'", lambda: int('42')),
    ("8. -12.12", lambda: int(-12.12))
]

for name, expr in expressions:
    try:
        result = expr()
        print(f"{name} -> УСПЕШНО: {result}")
    except Exception as e:
        print(f"{name} -> ОШИБКА: {type(e).__name__}: {e}")
