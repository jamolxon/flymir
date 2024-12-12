from enum import unique
from django.db import models
from django.urls import reverse
from django.utils.translation import gettext_lazy as _

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


class Comment(models.Model):
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


# Programs Model
class Programs(models.Model):
    name = models.CharField('Name', max_length=100)
    slug = models.SlugField('*', unique=True, max_length=70)
    description = models.CharField('Description', max_length=300)
    author = models.CharField('Author', max_length=100)
    home_image = models.ImageField('Home Page Image', help_text='Size: 570x484', upload_to='news_shots/')
    image = models.ImageField('Programs Page Image', help_text='Size: 790x510', upload_to='programs/')
    related_image = models.ImageField('Related Programs Image', help_text='Size: 150x150', upload_to='programs/')
    subcategory = models.ForeignKey(Subcategory, on_delete=models.CASCADE, null=True, verbose_name='SubCategory')
    specialisation = models.CharField('Specialisation of university', help_text='e.g: IT, Law or Business', max_length=100)
    local_rating = models.CharField('Local rating', max_length=50)
    global_rating = models.CharField('Global rating', max_length=50)
    date_opened = models.CharField('The date opened', max_length=20)
    first_detail_image = models.ImageField('First Detail Image', help_text='Size: 720x720', upload_to='programs/')
    second_detail_image = models.ImageField('Second Detail Image', help_text='Size: 720x720', upload_to='programs/')
    third_detail_image = models.ImageField('Third Detail Image', help_text='Size: 720x720',blank=True, upload_to='programs/')
    fourth_detail_image = models.ImageField('Fourth Detail Image', help_text='Size: 720x720', blank=True, upload_to='programs/')
    date = models.DateTimeField('Date', auto_now_add=True)
    capital_letter = models.CharField('Capital letter', max_length=10)
    text = RichTextField('Text',)
    extra_text = RichTextField('Extra Text', blank=True)

    def get_absolute_url(self):
        return reverse('consulting:ProgramsDetailView', kwargs={'programs_slug':self.slug})

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Program'
        verbose_name_plural = 'Programs'


# Students Model
class Students(models.Model):
    name = models.CharField('Name', max_length=100)
    slug = models.SlugField('*', unique=True, max_length=70)
    image = models.ImageField('Image', help_text='Size: 720x720', upload_to='students/')
    detail_image = models.ImageField('Detail Page Image', help_text='Size: 720x720', upload_to='students/')
    country = models.ForeignKey(Subcategory, on_delete=models.CASCADE, null=True, verbose_name='SubCategory')
    university = models.ForeignKey(Programs, on_delete=models.CASCADE, null=True, verbose_name='University')
    program_title = models.CharField('Program', max_length=100)
    budget = models.CharField('Budget', max_length=100)
    capital_letter = models.CharField('Capital letter', max_length=10)
    text = RichTextField('Text',)
    date = models.CharField('Date', max_length=100)

    def get_absolute_url(self):
        return reverse('consulting:StudentsDetailView', kwargs={'students_slug':self.slug})

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Student'
        verbose_name_plural = 'Students'


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


# Partners Model
class Partners(models.Model):
    name = models.CharField('Name', max_length=100)
    image = models.ImageField('Image', help_text='Size: 300x145', upload_to='partners/')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Partner'
        verbose_name_plural = 'Partners'


# class Flag(models.Model):
#     subcategory = models.ForeignKey(Subcategory, on_delete=models.CASCADE, null=True, verbose_name='Country')
#     image = models.ImageField('Image', help_text='Size: 300x145', upload_to='flags/')

#     def __str__(self):
#         return f"{self.subcategory} has been added to flag bar"

#     class Meta:
#         verbose_name = 'Flag'
#         verbose_name_plural = 'Flags'


