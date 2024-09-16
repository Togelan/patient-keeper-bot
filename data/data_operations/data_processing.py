from datetime import datetime, timedelta


class DataProcessing:
    @staticmethod
    def create_specific_string(list_patients: list) -> str:
        return '\n'.join([f"{i + 1}. {item}" for i, item in enumerate(list_patients)])

    @staticmethod
    def get_week_dates() -> tuple:
        today_date = datetime.now().date()
        start_of_week = today_date - timedelta(days=today_date.weekday())  # Понедельник текущей недели
        week_dates = [(start_of_week + timedelta(days=i)).strftime('%d.%m.%Y') for i in
                      range((today_date - start_of_week).days + 1)]
        return tuple(week_dates)