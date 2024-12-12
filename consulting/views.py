from django.shortcuts import render, get_object_or_404
from django.http import HttpResponseRedirect
from django.contrib import messages
from django.urls import reverse
from django.views.generic.base import View
from django.views.generic import ListView
from django.core.paginator import Paginator
from django.db.models import Q, Count

from consulting import models
from consulting import forms


class HomeView(View):
    def get(self, request):
        company = models.Company.objects.last()
        settings = models.Settings.objects.last()
        features = models.Feature.objects.all().order_by("id")[:4]
        statistics = models.Statistics.objects.all()[:4]
        blogs = models.News.objects.all().order_by("-id")[:4]

        context = {
                "company": company,
                "settings": settings,
                "features": features,
                "statistics": statistics,
                "programs": None,
                "students": None,
                "blogs": blogs,
                }
        return render(request, 'index-3.html', context)


class AboutView(View):
    def get(self, request):
        faq = models.Faq.objects.all()[:5]
        header = models.Header.objects.last()
        team = models.Team.objects.all()
        reviews  = models.Review.objects.all().order_by('-id')[:10]
        settings = models.Settings.objects.last()
        services = models.Service.objects.all().order_by("id")[:3]
        ceo = models.Ceo.objects.last()
        statistics = models.Statistics.objects.all()[:4]

        context = {
            'faq':faq,
            'header':header,
            'team':team,
            'reviews':reviews,
            "settings": settings,
            "services": services,
            "ceo": ceo,
            "statistics": statistics,
        }

        return render(request, 'about-us.html', context)


class StudentListView(View):
    def get(self, request):
        students = models.Students.objects.all()
        paginator = Paginator(students, 6)
        page_number = request.GET.get('page')
        page_obj = paginator.get_page(page_number)
        context = {
            'students':students,
            'page_obj':page_obj,
        }
        return render(request, 'p-wide.html', context)


class StudentDetailView(View):
    def get(self, request, slug):
        student = get_object_or_404(models.Students, slug=slug)
        students = models.Students.objects.all().order_by('-id')[:3]
        context = {
            'student':student,
            'students':students,
        }
        return render(request, 'portfolio-right.html', context)


class NewsListView(View):
    def get(self, request):
        news = models.News.objects.all().order_by("-id")
        paginator = Paginator(news, 9)
        page_number = request.GET.get('page')
        page_obj = paginator.get_page(page_number)
        context = {
            'page_obj':page_obj,
        }
        return render(request, 'news.html', context)


class CategoryNewsView(View):
    def get(self, request, slug):
        category = get_object_or_404(models.NewsCategory, slug=slug)
        news = models.News.objects.filter(category=category).order_by("-id")
        paginator = Paginator(news, 9)
        page_number = request.GET.get('page')
        page_obj = paginator.get_page(page_number)
        context = {
            'category': category,
            'page_obj':page_obj,
        }
        return render(request, 'news-category.html', context)


class NewsDetailView(View):
    def get(self, request, slug):
        news = models.News.objects.annotate(comment_count=Count("comments")).get(slug=slug)
        related_news = models.News.objects.exclude(slug=slug).filter(category=news.category).order_by('-id')[:3]
        recent_news = models.News.objects.exclude(slug=slug).exclude(category=news.category).order_by('-id')[:5]
        category = models.NewsCategory.objects.all().annotate(count=Count("news"))

        context = {
            'news':news,
            'related_news':related_news,
            'recent_news':recent_news,
            'categories': category,
        }
        return render(request, 'news-detail.html', context)


class NewsSearchView(ListView):
	model = models.News
	template_name = 'news-search.html'

	def get_queryset(self):
		query = self.request.GET.get('search', None)
		object_list = models.News.objects.filter(
			Q(name__icontains = query) | Q(description__icontains = query) | Q(author__icontains = query)
            ).order_by("-id")[:24]
		return object_list


class AddCommentView(View):
    def post(self, request, pk):
        if request.method == 'POST':
            form = forms.CommentForm(request.POST)
            if form.is_valid():
                create = form.save(commit=False)
                if request.POST.get("parent", None):
                    form.parent_id = int(request.POST.get('parent'))
                news = get_object_or_404(models.News, id=pk)
                create.news=news
                form.save()
                return HttpResponseRedirect(reverse('consulting:news-detail', kwargs={'slug': news.slug}))
        else:
            form = forms.CommentForm()
        return render(request, 'news-detail.html', {'form':form})


class ProgramListView(View):
    def get(self, request):
        programs = models.Programs.objects.all()
        related_programs = models.Programs.objects.all().order_by('-id')[:3]
        program_name = models.Programs.objects.filter().only('name')[:7]
        category = models.Subcategory.objects.all()
        paginator = Paginator(programs, 6)
        page_number = request.GET.get('page')
        page_obj = paginator.get_page(page_number)
        context = {
            'page_obj':page_obj,
            'category':category,
            'program_name':program_name,
            'related_programs':related_programs,
        }
        return render(request, 'programs.html', context)


class CategoryProgramView(View):
    def get(self, request, slug):
        subcategory = get_object_or_404(models.Subcategory, slug=slug)
        programs = models.Programs.objects.filter(subcategory=subcategory)
        paginator = Paginator(programs, 6)
        page_number = request.GET.get('page')
        page_obj = paginator.get_page(page_number)
        category = models.Subcategory.objects.all()
        related_programs = models.Programs.objects.filter().order_by('-id')[:3]
        program_name = models.Programs.objects.filter().only('name')[:7]
        context = {
            'page_obj':page_obj,
            'category':category,
            'related_programs':related_programs,
            'program_name':program_name,
        }
        return render(request, 'program-category.html', context)


class ProgramDetailView(View):
    def get(self, request, programs_slug):
        program = get_object_or_404(models.Programs, slug=programs_slug)
        related_programs = models.Programs.objects.all().order_by('-id')[:3]
        context = {
            'program':program,
            'related_programs':related_programs,
        }
        return render(request, 'portfolio-standar.html', context)


class ProgramSearchView(View):
    def get(self, request):
        query = request.GET.get('search', None)
        object_list = models.Programs.objects.filter(Q(name__icontains = query) | Q(description__icontains = query) |
        Q(author__icontains = query) | Q(date__icontains = query)
        )
        return render(request, 'search.html', {'object_list':object_list})


class ContactView(View):
    def get(self, request):
        form = forms.ContactForm()
        context = {
        'form':form,
        }
        return render(request, 'contact.html', context)

    def post(self, request):
        form = forms.ContactForm(request.POST)
        if form.is_valid():
            form.save()
            form = forms.ContactForm()
            messages.add_message(request, messages.SUCCESS, 'We received your phone number. We will call you as soon as possible.')
        else:
            form = forms.ContactForm()
            messages.add_message(request, messages.WARNING, 'We failed to receive your number. Please try again!')
        return render(request, 'contact.html', {'form':form,})


class OrderCallView(View):
    def post(self, request):
        if request.method == 'POST':
            phone = request.POST.get("phone")
            try:
                models.Call.objects.create(phone_number=phone)
                messages.add_message(request, messages.SUCCESS, 'We received your phone number. We will call you as soon as possible.')
                return HttpResponseRedirect(reverse('consulting:home'))
            except:
                messages.add_message(request, messages.WARNING, 'We failed to receive your number. Please try again!')
                return HttpResponseRedirect(reverse('consulting:home'))
