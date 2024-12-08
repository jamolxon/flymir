from consulting import models


def view_all(request):
    context = {
        'header': models.Header.objects.last(),
        'categories': models.Category.objects.all(),
        'news_category': models.NewsCategory.objects.all(),
        'settings': models.Settings.objects.last(),
        'services': models.Service.objects.all().order_by("id")[:3]
    }
    return context
