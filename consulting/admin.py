from django.contrib import admin

from consulting import models

admin.site.register(models.Header)
admin.site.register(models.Settings)
admin.site.register(models.Feature)
admin.site.register(models.Company)
admin.site.register(models.Ceo)
admin.site.register(models.NewsCategory)
admin.site.register(models.News)
admin.site.register(models.Category)
admin.site.register(models.Subcategory)
admin.site.register(models.Faq)
admin.site.register(models.Team)
admin.site.register(models.Review)
admin.site.register(models.Statistics)
admin.site.register(models.Service)
admin.site.register(models.Comment)
admin.site.register(models.StudentComment)
admin.site.register(models.Contact)
admin.site.register(models.Student)
admin.site.register(models.Program)
admin.site.register(models.Scholarship)


# @admin.register(Categories)
# class CategoryAdmin(admin.ModelAdmin):
#     list_display = ['name',]
#     list_filter = ('name',)
#     prepopulated_fields = {'slug':('name',)}

# @admin.register(SubCategory)
# class SubCategoryAdmin(admin.ModelAdmin):
#     list_display = ['name',]
#     list_filter = ('name',)
#     prepopulated_fields = {'slug':('name',)}

# @admin.register(Faq)
# class FAQAdmin(admin.ModelAdmin):
#     list_display = ['question',]
#     list_filter = ('question', 'answer',)

# @admin.register(Team)
# class TeamAdmin(admin.ModelAdmin):
#     list_display = ['name', 'position',]
#     list_filter = ('name', 'position',)

# @admin.register(Review)
# class ReviewsAdmin(admin.ModelAdmin):
#     list_display = ['name', 'position',]
#     list_filter = ('name', 'position')

# @admin.register(Students)
# class StudentsAdmin(admin.ModelAdmin):
#     list_display = ['name', 'university',]
#     list_filter = ('name', 'university',)
#     prepopulated_fields = {'slug':('name', 'country', 'university', 'date',)}

# @admin.register(Services)
# class ServicesAdmin(admin.ModelAdmin):
#     list_display = ['name', 'title',]
#     list_filter = ('name', 'title',)
#     prepopulated_fields = {'slug':('name', 'title')}

# @admin.register(CategoryNews)
# class CategoryNewsAdmin(admin.ModelAdmin):
#     list_display = ['name',]
#     list_filter = ('name',)
#     prepopulated_fields = {'slug':('name',)}

# @admin.register(News)
# class NewsAdmin(admin.ModelAdmin):
#     list_display = ['name', 'category',]
#     list_filter = ('name', 'category',)
#     prepopulated_fields = {'slug':('name', 'category',)}

# @admin.register(Comments)
# class CommentsAdmin(admin.ModelAdmin):
#     list_display = ['name', 'phone',]
#     list_filter = ('name', 'phone',)

# @admin.register(Flag)
# class FlagAdmin(admin.ModelAdmin):
#     list_display = ['subcategory', 'image',]
#     list_filter = ('subcategory',)

# @admin.register(Partners)
# class PartnersAdmin(admin.ModelAdmin):
#     list_display = ['name', 'image',]
#     list_filter = ('id', 'name',)

# @admin.register(Programs)
# class ProgramsAdmin(admin.ModelAdmin):
#     list_display = ['name', 'subcategory',]
#     list_filter = ('name', 'subcategory',)
#     prepopulated_fields = {
#         'slug':('name', 'subcategory',)
#     }

# @admin.register(Contact)
# class ContactAdmin(admin.ModelAdmin):
#     list_display = ['name', 'number',]
#     list_filter = ('name', 'number',)

# @admin.register(OrderPhone)
# class OrderPhoneAdmin(admin.ModelAdmin):
#     list_display = ['phone',]
#     list_filter = ('phone',)
