class Certificate:
    def __init__(self, cert_value):
        self.thickness = cert_value[3]
        self.metal_grade = cert_value[9]  # Марка металла
        self.gost = cert_value[10]  # Гост материала
        self.melting_number = cert_value[11]  # Номер плавки
        self.batch_number = cert_value[11]  # Номер партии
        self.certificate_number = cert_value[12]  # Номер сертификата
        self.date_of_certificate = cert_value[12]  # Дата сертификата
        self.limit_fluidity = cert_value[13]  # Предел текучести
        self.temporary_resistance = cert_value[14]  # Временное сопротивление
        self.relative_extension = cert_value[15]  # Относительное удлинение
        self.relative_narrowing = cert_value[16]  # Относительное сужение
        self.impact_strength_before_aging = cert_value[17]  # Ударная вязкость до старения
        self.impact_strength_after_aging = cert_value[18]  # Ударная вязкость после старения
        self.sample_type = cert_value[19]  # Тип образца
        self.impact_strength_below_zero = cert_value[20]  # Ударная вязкость ниже ноля
        self.temperature_below_zero = cert_value[21]  # Температура ниже ноля
        self.sample_type_below_zero = cert_value[22]  # Тип образка ниже ноля
        self.additional_data = cert_value[23]  # Доболнительные данные
        self.chemical_composition = []  # Хим.состав


if __name__ == '__main__':
    bob = Certificate(10)
    print(bob.thickness)
