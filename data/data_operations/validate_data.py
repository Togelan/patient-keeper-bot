import re
from datetime import datetime, timedelta


class ValidationData:
    @staticmethod
    def validate_fio(fio: str) -> bool:
        indicator = r'^(?:[А-ЯЁ][а-яё]+|[A-Z][a-z]+)\s(?:[А-ЯЁ][а-яё]+|[A-Z][a-z]+)\s(?:[А-ЯЁ][а-яё]+|[A-Z][a-z]+)$'
        return re.match(indicator, fio) is not None

    @staticmethod
    def validate_birthdate(birthdate_str: str) -> bool:
        try:
            birthdate = datetime.strptime(birthdate_str, '%d.%m.%Y')
            current_date = datetime.now()

            if birthdate > current_date:
                return False
            elif current_date - birthdate > timedelta(days=365 * 100 + 25):
                return False

            return True
        except ValueError:
            return False

