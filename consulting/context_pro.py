from consulting import models


def view_all(request):
    context = {
        'header': models.Header.objects.last(),
        'program_categories': models.Category.objects.all(),
        'news_categories': models.NewsCategory.objects.filter(news__gt=0).distinct(),
        'settings': models.Settings.objects.last(),
        'services': models.Service.objects.all().order_by("id")[:3]
    }
    return context
