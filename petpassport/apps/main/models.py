from django.db import models


class Record(models.Model):
    """Тестовая модель"""
    title = models.CharField('Заголовок', max_length = 50)
    record = models.TextField('Описание')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Запись'
        verbose_name_plural = 'Записи'


class PetSex(models.Model):
    """Пол питомца"""
    sex = models.CharField('Пол питомца', max_length = 15)

    def __str__(self):
        return self.sex

    class Meta:
        verbose_name = 'Пол животного'
        verbose_name_plural = 'Пол животных'


class PetTypes(models.Model):
    """Тип животного (кошка/собака/etc)"""
    type = models.CharField('Тип питомца', max_length = 100)

    def __str__(self):
        return self.type

    class Meta:
        verbose_name = 'Тип питомца'
        verbose_name_plural = 'Типы питомцев'


class Chip(models.Model):
    """Чип животного"""
    number = models.BigIntegerField('Номер чипа', blank = True)
    date = models.DateField('Дата чипирования', blank = True)

    def __int__(self):
        return self.number

    class Meta:
        verbose_name = 'Чип питомца'
        verbose_name_plural = 'Чипы питомцев'


class Tattoo(models.Model):
    """Клеймо животного"""
    identifier = models.CharField('Идентификатор клейма', max_length = 50, blank = True)
    date = models.DateField('Дата установки клейма', blank = True)

    def __str__(self):
        return self.identifier

    class Meta:
        verbose_name = 'Клеймо питомца'
        verbose_name_plural = 'Клейма питомцев'


class Food(models.Model):
    """Еда животного"""
    name = models.CharField('Название корма', max_length = 100)
    note = models.TextField('Заметка о корме', blank = True)
    grams_per_day = models.PositiveSmallIntegerField('Вес корма (граммов в день)', blank = True)
    start_day = models.DateField('Дата начала использования корма', blank = True)
    finish_day = models.DateField('Дата окончания использования корма', blank = True)
    link = models.URLField('Сылка на корм', blank = True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Корм питомца'
        verbose_name_plural = 'Корма питомцев'


class Accessory(models.Model):
    """Аксессуары животного (ошейники, шампуни, наполнитель для лотка, etc)"""
    name = models.CharField('Название аксессуара', max_length = 100)
    note = models.TextField('Заметка об аксессуаре', max_length = 300, blank = True)
    link = models.URLField('Сылка на аксессуар', max_length = 150, blank = True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Аксессуар питомца'
        verbose_name_plural = 'Аксессуары питомцев'


class EventsType(models.Model):
    """Типы событий"""
    name = models.CharField('Тип события', max_length = 60)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Тип события питомца'
        verbose_name_plural = 'Типы событий питомцев'


class PetEvents(models.Model):
    """События животного"""
    type = models.ForeignKey(EventsType, verbose_name = 'Тип события', on_delete = models.SET_NULL, null = True,
                             blank = True)
    note = models.TextField('Заметка о событии', max_length = 300, blank = True)
    date = models.DateTimeField('Дата и время события', blank = True)

    def __str__(self):
        return str(self.type)

    class Meta:
        verbose_name = 'Событие питомца'
        verbose_name_plural = 'События питомцев'


class VaccinationType(models.Model):
    """Типы вакцин"""
    name = models.CharField('Тип вакцины', max_length = 100)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Тип вакцины'
        verbose_name_plural = 'Типы вакцин'


class Vaccination(models.Model):
    """Вакцинация животного"""
    type = models.ForeignKey(VaccinationType, verbose_name = 'Тип вакцины', on_delete = models.SET_NULL, null = True)
    note = models.TextField('Заметка о вакцинации', max_length = 300, blank = True)
    date = models.DateField('Дата вакцинации', null = True, blank = True)

    def __str__(self):
        return self.type

    class Meta:
        verbose_name = 'Вакцинация питомца'
        verbose_name_plural = 'Вакцинации питомцев'


class CastrationStatus(models.Model):
    """Информация о стерилилизации или кастрации животного"""
    sterilized = models.BooleanField('Животное кастрировано', blank = True)
    date = models.DateField('Дата кастрации', blank = True)

    def __tuple__(self):
        return self.sterilized, self.date

    class Meta:
        verbose_name = 'Кастрация питомца'
        verbose_name_plural = 'Кастрации питомцев'


class Deworming(models.Model):
    """Информация о дегельминтизации животного"""
    product_name = models.CharField('Название препарата', max_length = 150, blank = True)
    link = models.URLField('Ссылка на препарат', max_length = 150, blank = True)
    date = models.DateField('Дата дегельминтизации', blank = True)

    def __str__(self):
        return self.product_name

    class Meta:
        verbose_name = 'Дегельминтизация питомца'
        verbose_name_plural = 'Дегельминтизации питомцев'


class Pet(models.Model):
    """Все данные по питомцу"""

    owner = models.CharField('Имя владельца', max_length = 50)
    name = models.CharField('Кличка питомца', max_length = 50)
    sex = models.ForeignKey(PetSex, verbose_name = 'Пол питомца', on_delete = models.SET_NULL, blank = True,
                            null = True)
    coat = models.CharField('Окрас питомца', max_length = 100, blank = True)
    pet_type = models.ForeignKey(PetTypes, verbose_name = 'Тип питомца', on_delete = models.SET_NULL, null = True,
                                 blank = True)
    breed = models.CharField('Порода питомца', max_length = 100, blank = True)
    birthday = models.DateField('Дата рождения питомца', blank = True)
    current_age = models.PositiveSmallIntegerField('Текущий возраст питомца', default = 0, blank = True)
    chip = models.ForeignKey(Chip, verbose_name = 'Чип питомца', on_delete = models.SET_NULL, null = True, blank = True)
    tattoo = models.ForeignKey(Tattoo, verbose_name = 'Клеймо питомца', on_delete = models.SET_NULL, null = True,
                               blank = True)
    food = models.ForeignKey(Food, verbose_name = 'Корм питомца', on_delete = models.SET_NULL, null = True,
                             blank = True)
    character_traits = models.TextField('', max_length = 500, blank = True)
    accessory = models.ForeignKey(Accessory, verbose_name = 'Аксессуары питомца', on_delete = models.SET_NULL,
                                  null = True, blank = True)
    events = models.ForeignKey(PetEvents, verbose_name = 'События питомца', on_delete = models.SET_NULL,
                               null = True, blank = True)
    vaccination = models.ForeignKey(Vaccination, verbose_name = 'Вакцинация питомца', on_delete = models.SET_NULL,
                                    null = True, blank = True)
    castration_status = models.ForeignKey(CastrationStatus, verbose_name = 'Кастрация питомца',
                                          on_delete = models.SET_NULL, null = True, blank = True)
    deworming = models.ForeignKey(Deworming, verbose_name = 'Дегельминтизация питомца',
                                  on_delete = models.SET_NULL, null = True, blank = True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Питомец'
        verbose_name_plural = 'Питомцы'