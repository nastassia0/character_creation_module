class Bird:
    def __init__(self, name, size):
        self.name = name
        self.size = size

    def describe(self):
        return f'Размер птицы {self.name} — {self.size}.'


class Parrot(Bird):
    def __init__(self, name, size, color):
        super().__init__(name, size)
        self.color = color

    def describe(self, full=False):
        if not full:
            return super().describe()
        return (f'Попугай {self.name} — заметная птица, окрас её перьев — '
                f'{self.color}, а размер — {self.size}. Интересный '
                f'факт: попугаи чувствуют ритм, а вовсе не бездумно '
                f'двигаются под музыку. Если сменить композицию, то '
                f'и темп движений птицы изменится.')


class Penguin(Bird):
    def __init__(self, name, size, genus):
        super().__init__(name, size)
        self.genus = genus

    def describe(self, full=False):
        if not full:
            return super().describe()
        return (f'Размер пингвина {self.name} из рода {self.genus} — '
                f'{self.size}. Интересный факт: однажды группа '
                f'геологов-разведчиков похитила пингвинье яйцо, '
                f'и их принялась преследовать вся стая, не пытаясь, '
                f'впрочем, при этом нападать. Посовещавшись, '
                f'похитители вернули птицам яйцо, и те отстали.')


kesha = Parrot('Ара', 'средний', 'красный')
kowalski = Penguin('Королевский', 'большой', 'Aptenodytes')

# Вызов метода у созданных объектов.
print(kesha.describe())
print(kowalski.describe(True))
