from django.urls import path

from consulting import views

app_name = 'consulting'

urlpatterns = [
    path('', views.HomeView.as_view(), name='home'),
    path('about/', views.AboutView.as_view(), name='about'),
    path('news/', views.NewsListView.as_view(), name='news-list'),
    path('news/<str:slug>/', views.NewsDetailView.as_view(), name='news-detail'),
    path('news/category/<str:slug>/', views.CategoryNewsView.as_view(), name='category-news-list'),
    path('search-news/', views.NewsSearchView.as_view(), name='news-search'),
    path('programs/', views.ProgramListView.as_view(), name='program-list'),
    path('programs/<str:slug>/', views.ProgramDetailView.as_view(), name='program-detail'),
    path('search-programs/', views.ProgramSearchView.as_view(), name='program-search'),
    path('students/', views.StudentListView.as_view(), name='student-list'),
    path('students/<str:slug>/', views.StudentDetailView.as_view(), name='student-detail'),
    path('programs/category/<str:slug>/', views.CategoryProgramView.as_view(), name='category-program-list'),
    path('comment/<int:pk>/', views.AddCommentView.as_view(), name='comment'),
    path('contact/', views.ContactView.as_view(), name='contact'),
    path('order-call/', views.OrderCallView.as_view(), name='order-call'),
]
