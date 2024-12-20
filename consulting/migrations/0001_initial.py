# Generated by Django 5.1.3 on 2024-12-08 23:42

import ckeditor.fields
import django.db.models.deletion
import django_resized.forms
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Partners',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, verbose_name='Name')),
                ('image', models.ImageField(help_text='Size: 300x145', upload_to='partners/', verbose_name='Image')),
            ],
            options={
                'verbose_name': 'Partner',
                'verbose_name_plural': 'Partners',
            },
        ),
        migrations.CreateModel(
            name='Programs',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, verbose_name='Name')),
                ('slug', models.SlugField(max_length=70, unique=True, verbose_name='*')),
                ('description', models.CharField(max_length=300, verbose_name='Description')),
                ('author', models.CharField(max_length=100, verbose_name='Author')),
                ('home_image', models.ImageField(help_text='Size: 570x484', upload_to='news_shots/', verbose_name='Home Page Image')),
                ('image', models.ImageField(help_text='Size: 790x510', upload_to='programs/', verbose_name='Programs Page Image')),
                ('related_image', models.ImageField(help_text='Size: 150x150', upload_to='programs/', verbose_name='Related Programs Image')),
                ('specialisation', models.CharField(help_text='e.g: IT, Law or Business', max_length=100, verbose_name='Specialisation of university')),
                ('local_rating', models.CharField(max_length=50, verbose_name='Local rating')),
                ('global_rating', models.CharField(max_length=50, verbose_name='Global rating')),
                ('date_opened', models.CharField(max_length=20, verbose_name='The date opened')),
                ('first_detail_image', models.ImageField(help_text='Size: 720x720', upload_to='programs/', verbose_name='First Detail Image')),
                ('second_detail_image', models.ImageField(help_text='Size: 720x720', upload_to='programs/', verbose_name='Second Detail Image')),
                ('third_detail_image', models.ImageField(blank=True, help_text='Size: 720x720', upload_to='programs/', verbose_name='Third Detail Image')),
                ('fourth_detail_image', models.ImageField(blank=True, help_text='Size: 720x720', upload_to='programs/', verbose_name='Fourth Detail Image')),
                ('date', models.DateTimeField(auto_now_add=True, verbose_name='Date')),
                ('capital_letter', models.CharField(max_length=10, verbose_name='Capital letter')),
                ('text', ckeditor.fields.RichTextField(verbose_name='Text')),
                ('extra_text', ckeditor.fields.RichTextField(blank=True, verbose_name='Extra Text')),
            ],
            options={
                'verbose_name': 'Program',
                'verbose_name_plural': 'Programs',
            },
        ),
        migrations.CreateModel(
            name='Call',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='created at')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='updated at')),
                ('phone_number', models.CharField(max_length=32, verbose_name='phone number')),
                ('created_by', models.ForeignKey(editable=False, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='%(class)s_createdby', to=settings.AUTH_USER_MODEL)),
                ('modified_by', models.ForeignKey(blank=True, editable=False, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='%(class)s_modifiedby', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'call order',
                'verbose_name_plural': 'call orders',
                'db_table': 'call',
            },
        ),
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='created at')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='updated at')),
                ('name', models.CharField(max_length=256, verbose_name='name')),
                ('slug', models.SlugField(blank=True, max_length=256, null=True, unique=True, verbose_name='slug')),
                ('created_by', models.ForeignKey(editable=False, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='%(class)s_createdby', to=settings.AUTH_USER_MODEL)),
                ('modified_by', models.ForeignKey(blank=True, editable=False, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='%(class)s_modifiedby', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'category',
                'verbose_name_plural': 'categories',
                'db_table': 'category',
            },
        ),
        migrations.CreateModel(
            name='Ceo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='created at')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='updated at')),
                ('full_name', models.CharField(max_length=256, verbose_name='full name')),
                ('description', models.TextField(verbose_name='description')),
                ('image', django_resized.forms.ResizedImageField(crop=['middle', 'center'], force_format='WEBP', help_text='preferred size: 623x570', keep_meta=True, quality=95, scale=None, size=[623, 570], upload_to='ceo/%Y/%m', verbose_name='image')),
                ('created_by', models.ForeignKey(editable=False, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='%(class)s_createdby', to=settings.AUTH_USER_MODEL)),
                ('modified_by', models.ForeignKey(blank=True, editable=False, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='%(class)s_modifiedby', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'ceo',
                'verbose_name_plural': 'ceo',
                'db_table': 'ceo',
            },
        ),
        migrations.CreateModel(
            name='Company',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='created at')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='updated at')),
                ('title', models.CharField(max_length=256, verbose_name='title')),
                ('description', models.TextField(verbose_name='description')),
                ('image', django_resized.forms.ResizedImageField(crop=['middle', 'center'], force_format='WEBP', help_text='preferred size: 716x611', keep_meta=True, quality=95, scale=None, size=[716, 611], upload_to='company/%Y/%m', verbose_name='image')),
                ('created_by', models.ForeignKey(editable=False, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='%(class)s_createdby', to=settings.AUTH_USER_MODEL)),
                ('modified_by', models.ForeignKey(blank=True, editable=False, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='%(class)s_modifiedby', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'company',
                'verbose_name_plural': 'company',
                'db_table': 'company',
            },
        ),
        migrations.CreateModel(
            name='Contact',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='created at')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='updated at')),
                ('name', models.CharField(max_length=256, verbose_name='name')),
                ('number', models.CharField(max_length=256, verbose_name='phone number')),
                ('message', models.TextField(verbose_name='message')),
                ('created_by', models.ForeignKey(editable=False, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='%(class)s_createdby', to=settings.AUTH_USER_MODEL)),
                ('modified_by', models.ForeignKey(blank=True, editable=False, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='%(class)s_modifiedby', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'contact',
                'verbose_name_plural': 'contacts',
                'db_table': 'contact',
            },
        ),
        migrations.CreateModel(
            name='Faq',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='created at')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='updated at')),
                ('question', models.TextField(verbose_name='question')),
                ('answer', models.TextField(verbose_name='answer')),
                ('created_by', models.ForeignKey(editable=False, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='%(class)s_createdby', to=settings.AUTH_USER_MODEL)),
                ('modified_by', models.ForeignKey(blank=True, editable=False, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='%(class)s_modifiedby', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'faq',
                'verbose_name_plural': 'faq',
                'db_table': 'faq',
            },
        ),
        migrations.CreateModel(
            name='Feature',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='created at')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='updated at')),
                ('description', models.TextField(verbose_name='description')),
                ('created_by', models.ForeignKey(editable=False, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='%(class)s_createdby', to=settings.AUTH_USER_MODEL)),
                ('modified_by', models.ForeignKey(blank=True, editable=False, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='%(class)s_modifiedby', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'feature',
                'verbose_name_plural': 'features',
                'db_table': 'feature',
            },
        ),
        migrations.CreateModel(
            name='Header',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='created at')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='updated at')),
                ('title', models.TextField(verbose_name='title')),
                ('description', models.TextField(verbose_name='description')),
                ('created_by', models.ForeignKey(editable=False, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='%(class)s_createdby', to=settings.AUTH_USER_MODEL)),
                ('modified_by', models.ForeignKey(blank=True, editable=False, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='%(class)s_modifiedby', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'header',
                'verbose_name_plural': 'header',
                'db_table': 'header',
            },
        ),
        migrations.CreateModel(
            name='News',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='created at')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='updated at')),
                ('name', models.CharField(max_length=256, verbose_name='name')),
                ('slug', models.SlugField(blank=True, max_length=256, null=True, unique=True, verbose_name='slug')),
                ('description', models.TextField(verbose_name='description')),
                ('author', models.CharField(max_length=256, verbose_name='author')),
                ('home_image', models.ImageField(help_text='Size: 570x484', upload_to='news_shots/', verbose_name='Home Page Image')),
                ('detail_image', models.ImageField(help_text='Size: 790x510', upload_to='news_shots/', verbose_name='Inner Page Image')),
                ('related_image', models.ImageField(help_text='Size: 150x150', upload_to='programs/', verbose_name='Related News Image')),
                ('author_name', models.CharField(max_length=70, verbose_name='Author name')),
                ('author_image', models.ImageField(help_text='Size: 270x370', upload_to='news_shots/', verbose_name='Image')),
                ('author_text', models.CharField(max_length=70, verbose_name="Author's words")),
                ('author_instagram', models.CharField(max_length=100, verbose_name='Instagram link')),
                ('author_facebook', models.CharField(max_length=100, verbose_name='Facebook link')),
                ('author_telegram', models.CharField(max_length=100, verbose_name='Telegram link')),
                ('capital_letter', models.CharField(max_length=10, verbose_name='Capital letter')),
                ('text', ckeditor.fields.RichTextField(verbose_name='Article')),
                ('date', models.DateTimeField(auto_now_add=True, verbose_name='Date')),
                ('created_by', models.ForeignKey(editable=False, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='%(class)s_createdby', to=settings.AUTH_USER_MODEL)),
                ('modified_by', models.ForeignKey(blank=True, editable=False, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='%(class)s_modifiedby', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'News',
                'verbose_name_plural': 'News',
            },
        ),
        migrations.CreateModel(
            name='Comments',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, verbose_name='Name')),
                ('phone', models.CharField(blank=True, max_length=13, verbose_name='Phone number')),
                ('message', models.TextField(verbose_name='Message')),
                ('date', models.DateTimeField(auto_now_add=True, verbose_name='Date')),
                ('parent', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='consulting.comments', verbose_name='parent')),
                ('news', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='news_comments', to='consulting.news')),
            ],
            options={
                'verbose_name': 'Comment',
                'verbose_name_plural': 'Comments',
                'ordering': ['id'],
            },
        ),
        migrations.CreateModel(
            name='NewsCategory',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='created at')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='updated at')),
                ('name', models.CharField(max_length=256, verbose_name='name')),
                ('slug', models.SlugField(blank=True, max_length=256, null=True, unique=True, verbose_name='slug')),
                ('created_by', models.ForeignKey(editable=False, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='%(class)s_createdby', to=settings.AUTH_USER_MODEL)),
                ('modified_by', models.ForeignKey(blank=True, editable=False, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='%(class)s_modifiedby', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'news category',
                'verbose_name_plural': 'news categories',
                'db_table': 'news_category',
            },
        ),
        migrations.AddField(
            model_name='news',
            name='category',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='consulting.newscategory', verbose_name='CategoryNews'),
        ),
        migrations.CreateModel(
            name='Review',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='created at')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='updated at')),
                ('full_name', models.CharField(max_length=256, verbose_name='full name')),
                ('position', models.CharField(max_length=256, verbose_name='position')),
                ('image', django_resized.forms.ResizedImageField(crop=['middle', 'center'], force_format='WEBP', help_text='preferred size:80x80', keep_meta=True, quality=100, scale=None, size=[80, 80], upload_to='review/%Y/%m', verbose_name='image')),
                ('text', models.TextField(verbose_name='review text')),
                ('created_by', models.ForeignKey(editable=False, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='%(class)s_createdby', to=settings.AUTH_USER_MODEL)),
                ('modified_by', models.ForeignKey(blank=True, editable=False, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='%(class)s_modifiedby', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'review',
                'verbose_name_plural': 'reviews',
                'db_table': 'review',
            },
        ),
        migrations.CreateModel(
            name='Service',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='created at')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='updated at')),
                ('title', models.CharField(max_length=256, verbose_name='title')),
                ('description', models.TextField(verbose_name='description')),
                ('created_by', models.ForeignKey(editable=False, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='%(class)s_createdby', to=settings.AUTH_USER_MODEL)),
                ('modified_by', models.ForeignKey(blank=True, editable=False, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='%(class)s_modifiedby', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'service',
                'verbose_name_plural': 'services',
                'db_table': 'service',
            },
        ),
        migrations.CreateModel(
            name='Settings',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='created at')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='updated at')),
                ('title', models.CharField(max_length=256, verbose_name='website title')),
                ('address', models.CharField(max_length=256, verbose_name='address')),
                ('phone_number', models.CharField(max_length=32, verbose_name='phone number')),
                ('email', models.EmailField(max_length=256, verbose_name='email')),
                ('instagram_url', models.CharField(max_length=256, verbose_name='instagram url')),
                ('telegram_url', models.CharField(max_length=256, verbose_name='telegram url')),
                ('facebook_url', models.CharField(max_length=256, verbose_name='facebook url')),
                ('created_by', models.ForeignKey(editable=False, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='%(class)s_createdby', to=settings.AUTH_USER_MODEL)),
                ('modified_by', models.ForeignKey(blank=True, editable=False, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='%(class)s_modifiedby', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'settings',
                'verbose_name_plural': 'settings',
                'db_table': 'settings',
            },
        ),
        migrations.CreateModel(
            name='Statistics',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='created at')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='updated at')),
                ('title', models.CharField(max_length=256, verbose_name='title')),
                ('value', models.PositiveIntegerField(verbose_name='value')),
                ('created_by', models.ForeignKey(editable=False, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='%(class)s_createdby', to=settings.AUTH_USER_MODEL)),
                ('modified_by', models.ForeignKey(blank=True, editable=False, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='%(class)s_modifiedby', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'statistics',
                'verbose_name_plural': 'statistics',
                'db_table': 'statistics',
            },
        ),
        migrations.CreateModel(
            name='Subcategory',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='created at')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='updated at')),
                ('name', models.CharField(max_length=256, verbose_name='name')),
                ('slug', models.SlugField(blank=True, max_length=256, null=True, unique=True, verbose_name='slug')),
                ('category', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='subcategories', to='consulting.category', verbose_name='category')),
                ('created_by', models.ForeignKey(editable=False, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='%(class)s_createdby', to=settings.AUTH_USER_MODEL)),
                ('modified_by', models.ForeignKey(blank=True, editable=False, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='%(class)s_modifiedby', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'subcategory',
                'verbose_name_plural': 'subcategories',
                'db_table': 'subcategory',
            },
        ),
        migrations.CreateModel(
            name='Students',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, verbose_name='Name')),
                ('slug', models.SlugField(max_length=70, unique=True, verbose_name='*')),
                ('image', models.ImageField(help_text='Size: 720x720', upload_to='students/', verbose_name='Image')),
                ('detail_image', models.ImageField(help_text='Size: 720x720', upload_to='students/', verbose_name='Detail Page Image')),
                ('program_title', models.CharField(max_length=100, verbose_name='Program')),
                ('budget', models.CharField(max_length=100, verbose_name='Budget')),
                ('capital_letter', models.CharField(max_length=10, verbose_name='Capital letter')),
                ('text', ckeditor.fields.RichTextField(verbose_name='Text')),
                ('date', models.CharField(max_length=100, verbose_name='Date')),
                ('university', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='consulting.programs', verbose_name='University')),
                ('country', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='consulting.subcategory', verbose_name='SubCategory')),
            ],
            options={
                'verbose_name': 'Student',
                'verbose_name_plural': 'Students',
            },
        ),
        migrations.AddField(
            model_name='programs',
            name='subcategory',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='consulting.subcategory', verbose_name='SubCategory'),
        ),
        migrations.CreateModel(
            name='Team',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='created at')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='updated at')),
                ('full_name', models.CharField(max_length=256, verbose_name='full name')),
                ('position', models.CharField(max_length=256, verbose_name='position')),
                ('image', django_resized.forms.ResizedImageField(crop=['middle', 'center'], force_format='WEBP', help_text='preferred size:750x977', keep_meta=True, quality=95, scale=None, size=[750, 977], upload_to='team/%Y/%m', verbose_name='image')),
                ('description', models.TextField(verbose_name='description')),
                ('created_by', models.ForeignKey(editable=False, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='%(class)s_createdby', to=settings.AUTH_USER_MODEL)),
                ('modified_by', models.ForeignKey(blank=True, editable=False, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='%(class)s_modifiedby', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'team',
                'verbose_name_plural': 'team members',
                'db_table': 'team',
            },
        ),
    ]
