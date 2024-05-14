import datetime


class Operation:
    def __init__(
            self,
            pk: int,
            state: str,
            date: str,
            amount: str,
            currency: str,
            description: str,
            to_: str,
            from_: str = None
            ):
        self.pk = pk
        self.state = state
        self.date = date
        self.amount = amount
        self.currency = currency
        self.description = description
        self.to_ = self.hide_payment_data(to_)
        self.from_ = self.hide_payment_data(from_) if from_ is not None else ""

    def hide_payment_data(self, payment_data) -> str:
        """
        :param payment_data: Получает на вход платежные данные
        :return: Возвращает платежные данные в замаскированом виде
        """
        if payment_data.startswith('Счет'):
            return f"Счет **{payment_data[-4:]}"

        card_number_start_index = len(payment_data) - 16
        return (
            f"{payment_data[0:card_number_start_index]}"
            f"{payment_data[card_number_start_index:card_number_start_index + 4]} "
            f"{payment_data[card_number_start_index + 4:card_number_start_index + 6]}** **** "
            f"{payment_data[-4:]}"
        )

    def convert_payment_date(self) -> str:
        """
        Получает дату в ISO формате
        :return: Возвращает дату в формате ДД.ММ.ГГГГ
        """
        payment_date = datetime.datetime.fromisoformat(self.date)
        return payment_date.strftime("%d.%m.%Y")

    def __lt__(self, other):
        return self.date < other.date

    def __gt__(self, other):
        return self.date > other.date

    def __str__(self):
        date = self.convert_payment_date()
        return (
            f"{date} {self.description}\n"
            f"{self.from_} -> {self.to_}\n"
            f"{self.amount} {self.currency}\n"
        )
