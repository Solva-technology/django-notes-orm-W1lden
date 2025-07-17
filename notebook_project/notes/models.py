from django.db import models

from .constants import CHARFIELD_MAX_LENGTH


class User(models.Model):
    name = models.CharField(max_length=CHARFIELD_MAX_LENGTH, verbose_name="Имя")
    email = models.EmailField(unique=True, verbose_name="Электронная почта")

    class Meta:
        verbose_name = "Пользователь"
        verbose_name_plural = "Пользователи"

    def __str__(self) -> str:
        return self.name


class UserProfile(models.Model):
    bio = models.TextField(verbose_name="Биография")
    birth_date = models.DateField(verbose_name="Дата рождения")
    user = models.OneToOneField(
        User, on_delete=models.CASCADE, verbose_name="Пользователь"
    )

    class Meta:
        verbose_name = "Профиль пользователя"
        verbose_name_plural = "Профили пользователей"

    def __str__(self) -> str:
        return f"Profile: {self.user.name}"


class Status_choices(models.TextChoices):
    active = "active"
    archived = "archived"
    deleted = "deleted"


class Status(models.Model):
    name = models.CharField(
        max_length=CHARFIELD_MAX_LENGTH,
        choices=Status_choices.choices,
        default=Status_choices.active,
        verbose_name="Имя",
    )
    is_final = models.BooleanField(verbose_name="Окончательный")

    class Meta:
        verbose_name = "Статус"
        verbose_name_plural = "Статусы"

    def __str__(self) -> str:
        return f"Status: {self.name}"


class Category(models.Model):
    title = models.CharField(max_length=CHARFIELD_MAX_LENGTH, verbose_name="Название")
    description = models.TextField(verbose_name="Описание")

    class Meta:
        verbose_name = "Категория"
        verbose_name_plural = "Категории"

    def __str__(self) -> str:
        return f"Category: {self.title}"


class Note(models.Model):
    text = models.TextField(verbose_name="Текст")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Создан в")
    author = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name="Автор")
    status = models.ForeignKey(Status, on_delete=models.CASCADE, verbose_name="Статус")
    categories = models.ManyToManyField(Category, verbose_name="Категории")

    class Meta:
        verbose_name = "Заметка"
        verbose_name_plural = "Заметки"

    def __str__(self) -> str:
        return f"Note author: {self.author.name}"
