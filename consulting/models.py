from django.db import models
from django.urls import reverse
from django.utils.translation import gettext_lazy as _
from django.utils import timezone

from ckeditor.fields import RichTextField
from django_resized import ResizedImageField

from helpers.models import BaseModel


class Category(BaseModel):
    name = models.CharField(_("name"), max_length=256)
    slug = models.SlugField(_("slug"), max_length=256, unique=True, blank=True, null=True)

    class Meta:
        db_table = "category"
        verbose_name = _("category")
        verbose_name_plural = _("categories")

    def __str__(self):
        return f"{self.name}"


class Subcategory(BaseModel):
    category = models.ForeignKey(Category, on_delete=models.CASCADE, null=True, related_name="subcategories", verbose_name=_("category"))
    name = models.CharField(_("name"), max_length=256)
    slug = models.SlugField(_("slug"), max_length=256, unique=True, blank=True, null=True)

    class Meta:
        db_table = "subcategory"
        verbose_name = _("subcategory")
        verbose_name_plural = _("subcategories")

    def __str__(self):
        return f"{self.name}"


class Contact(BaseModel):
    name = models.CharField(_("name"), max_length=256)
    number = models.CharField(_("phone number"), max_length=256)
    message = models.TextField(_("message"))

    class Meta:
        db_table = "contact"
        verbose_name = _("contact")
        verbose_name_plural = _("contacts")

    def __str__(self):
        return f"{self.name}"


class NewsCategory(BaseModel):
    name = models.CharField(_("name"), max_length=256)
    slug = models.SlugField(_("slug"), unique=True, max_length=256, blank=True, null=True)

    class Meta:
        db_table = "news_category"
        verbose_name = _("news category")
        verbose_name_plural = _("news categories")

    def __str__(self):
        return f"{self.name}"


class News(BaseModel):
    name = models.CharField(_("name"), max_length=256)
    slug = models.SlugField(_("slug"), max_length=256, unique=True, blank=True, null=True)
    description = models.TextField(_("description"))
    category = models.ForeignKey(NewsCategory, on_delete=models.CASCADE, null=True, verbose_name=_("category"), related_name="news")
    author = models.CharField(_("author"), max_length=256)
    image = ResizedImageField(_("image"), size=[790, 510], crop=["middle", "center"], quality=95, help_text="preferred size: 790x510", upload_to="news/%Y/%m")
    date = models.DateTimeField(_("date"), auto_now_add=True)
    text = RichTextField(_("text"))

    class Meta:
        db_table = "news"
        verbose_name = _("news")
        verbose_name_plural = _("news")

    def __str__(self):
        return f"{self.name}"


class Comment(BaseModel):
    name = models.CharField(_("name"), max_length=256)
    message = models.TextField(_("message"))
    parent = models.ForeignKey('self', verbose_name = 'parent', on_delete=models.SET_NULL, null=True, blank=True, related_name="children")
    news = models.ForeignKey(News, on_delete=models.CASCADE, null=True, related_name='comments', verbose_name=_("news"))
    date = models.DateTimeField(_("date"), auto_now_add=True)

    class Meta:
        db_table = "comment"
        ordering = ["-id"]
        verbose_name = _("comment")
        verbose_name_plural = _("comments")

    def __str__(self):
        return f"{self.name}"


class Program(BaseModel):
    name = models.CharField(_("name"), max_length=256)
    slug = models.SlugField(_("slug"), max_length=256, unique=True, blank=True, null=True)
    description = models.TextField(_("description"))
    image = ResizedImageField(_("image"), size=[790, 510], crop=["middle", "center"], quality=97, help_text="preferred size: 790x510", upload_to="program/%Y/%m")
    subcategory = models.ForeignKey(Subcategory, on_delete=models.CASCADE, null=True, verbose_name=_("subcategory"), related_name="programs")
    specialisation = models.CharField(_("specialisation"), help_text='e.g: IT, Law, Business', max_length=256)
    local_rating = models.CharField(_("local rating"), max_length=256)
    global_rating = models.CharField(_("global rating"), max_length=256)
    date_opened = models.CharField(_("date opened"), max_length=256)
    text = RichTextField(_("text"))
    published_date = models.DateTimeField(_("published date"), auto_now_add=True)

    class Meta:
        db_table = "program"
        verbose_name = _("program")
        verbose_name_plural = _("programs")

    def __str__(self):
        return f"{self.name}"


class Student(BaseModel):
    name = models.CharField(_("name"), max_length=256)
    slug = models.SlugField(_("slug"), unique=True, blank=True, null=True, max_length=256)
    country = models.ForeignKey(Subcategory, on_delete=models.CASCADE,  verbose_name=_("country"), related_name="students")
    university = models.ForeignKey(Program, on_delete=models.CASCADE,  verbose_name=_("university"), related_name="students")
    image = ResizedImageField(_("image"), size=[720, 720], crop=["middle", "center"], quality=97, help_text="preferred size: 720x720", upload_to="student/%Y/%m")
    program_type = models.CharField(_("program type"), max_length=256)
    date = models.DateField(_("date"), default=timezone.now)
    text = RichTextField(_("text"))

    class Meta:
        db_table = "student"
        verbose_name = _("student")
        verbose_name_plural = _("students")

    def __str__(self):
        return f"{self.name}"


class StudentComment(BaseModel):
    name = models.CharField(_("name"), max_length=256)
    message = models.TextField(_("message"))
    parent = models.ForeignKey('self', verbose_name = 'parent', on_delete=models.SET_NULL, null=True, blank=True, related_name="children")
    student = models.ForeignKey(Student, on_delete=models.CASCADE, null=True, related_name='comments', verbose_name=_("student"))
    date = models.DateTimeField(_("date"), auto_now_add=True)

    class Meta:
        db_table = "student_comment"
        ordering = ["-id"]
        verbose_name = _("student comment")
        verbose_name_plural = _("student comments")

    def __str__(self):
        return f"{self.name}"


class Header(BaseModel):
    title = models.TextField(_("title"))
    description = models.TextField(_("description"))

    class Meta:
        db_table = "header"
        verbose_name = _("header")
        verbose_name_plural = _("header")

    def __str__(self):
        return f"{self.title}"


class Feature(BaseModel):
    description = models.TextField(_("description"))

    class Meta:
        db_table = "feature"
        verbose_name = _("feature")
        verbose_name_plural = _("features")

    def __str__(self):
        return f"{self.description}"


class Company(BaseModel):
    title = models.CharField(_("title"), max_length=256)
    description = models.TextField(_("description"))
    image = ResizedImageField(_("image"), size=[716, 611], crop=["middle", "center"], quality=95, help_text="preferred size: 716x611", upload_to="company/%Y/%m")

    class Meta:
        db_table = "company"
        verbose_name = _("company")
        verbose_name_plural = _("company")


    def __str__(self):
        return f"{self.title}"


class Ceo(BaseModel):
    full_name = models.CharField(_("full name"), max_length=256)
    description = models.TextField(_("description"))
    image = ResizedImageField(_("image"), size=[623, 570], crop=["middle", "center"], quality=95, help_text="preferred size: 623x570", upload_to="ceo/%Y/%m")

    class Meta:
        db_table = "ceo"
        verbose_name = _("ceo")
        verbose_name_plural = _("ceo")

    def __str__(self):
        return f"{self.full_name}"


class Statistics(BaseModel):
    title = models.CharField(_("title"), max_length=256)
    value = models.PositiveIntegerField(_("value"))

    class Meta:
        db_table = "statistics"
        verbose_name = _("statistics")
        verbose_name_plural = _("statistics")

    def __str__(self):
        return f"{self.title}"


class Faq(BaseModel):
    question = models.TextField(_("question"))
    answer = models.TextField(_("answer"))

    class Meta:
        db_table = "faq"
        verbose_name = _("faq")
        verbose_name_plural = _("faq")

    def __str__(self):
        return f"{self.question}"


class Team(BaseModel):
    full_name = models.CharField(_("full name"), max_length=256)
    position = models.CharField(_("position"), max_length=256)
    image = ResizedImageField(_("image"), size=[750, 977], crop=["middle", "center"], quality=95, help_text="preferred size:750x977", upload_to="team/%Y/%m")
    description = models.TextField(_("description"))

    class Meta:
        db_table = "team"
        verbose_name = _("team")
        verbose_name_plural = _("team members")

    def __str__(self):
        return f"{self.full_name}"


class Review(BaseModel):
    full_name = models.CharField(_("full name"), max_length=256)
    position = models.CharField(_("position"), max_length=256)
    image = ResizedImageField(_("image"), size=[80, 80], crop=["middle", "center"], quality=100, help_text="preferred size:80x80", upload_to="review/%Y/%m")
    text = models.TextField(_("review text"))

    class Meta:
        db_table = "review"
        verbose_name = _("review")
        verbose_name_plural = _("reviews")

    def __str__(self):
        return f"{self.full_name}"


class Service(BaseModel):
    title = models.CharField(_("title"), max_length=256)
    description = models.TextField(_("description"))

    class Meta:
        db_table = "service"
        verbose_name = _("service")
        verbose_name_plural = _("services")


    def __str__(self):
        return f"{self.title}"



class Settings(BaseModel):
    title = models.CharField(_("website title"), max_length=256)
    address = models.CharField(_("address"), max_length=256)
    phone_number = models.CharField(_("phone number"), max_length=32)
    email = models.EmailField(_("email"), max_length=256)
    instagram_url = models.CharField(_("instagram url"), max_length=256)
    telegram_url = models.CharField(_("telegram url"), max_length=256)
    facebook_url = models.CharField(_("facebook url"), max_length=256)

    class Meta:
        db_table = "settings"
        verbose_name = _("settings")
        verbose_name_plural = _("settings")

    def __str__(self):
        return f"{self.id}"


class Call(BaseModel):
    phone_number = models.CharField(_("phone number"), max_length=32)

    class Meta:
        db_table = "call"
        verbose_name = _("call order")
        verbose_name_plural = _("call orders")

    def __str__(self):
        return f"{self.phone_number}"


class Scholarship(BaseModel):
    name = models.CharField(_("name"), max_length=256)
    url = models.CharField(_("url"), max_length=256)

    class Meta:
        db_table = "scholarship"
        verbose_name = _("scholarship")
        verbose_name_plural = _("scholarships")

    def __str__(self):
        return f"{self.name}"


# Partners Model
class Partners(BaseModel):
    name = models.CharField('Name', max_length=100)
    image = models.ImageField('Image', help_text='Size: 300x145', upload_to='partners/')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Partner'
        verbose_name_plural = 'Partners'


# class Flag(BaseModel):
#     subcategory = models.ForeignKey(Subcategory, on_delete=models.CASCADE, null=True, verbose_name='Country')
#     image = models.ImageField('Image', help_text='Size: 300x145', upload_to='flags/')

#     def __str__(self):
#         return f"{self.subcategory} has been added to flag bar"

#     class Meta:
#         verbose_name = 'Flag'
#         verbose_name_plural = 'Flags'


