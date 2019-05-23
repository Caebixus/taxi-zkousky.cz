from django.conf.urls import url
from .views import QuizListView, CategoriesListView,\
    ViewQuizListByCategory, QuizUserProgressView, QuizMarkingList,\
    QuizMarkingDetail, QuizDetailView, QuizTake, index, login, signup, logout_user, jakToFunguje, profile, change_password, cookies, sitemap, clanky, clanek1, clanek2, clanek3
from django.urls import path, include


urlpatterns = [         url(regex=r'^$', view=index, name='index'),
                        url(regex=r'^login/$', view=login, name='login'),
                        url(regex=r'^profile/$', view=profile, name='profile'),
                        url(regex=r'^clanky/$', view=clanky, name='clanky'),
                        url(regex=r'^clanky/Jak-udelat-taxi-zkousky-co-nejrychleji/$', view=clanek1, name='clanek1'),
                        url(regex=r'^clanky/3-rady-pro-uspecne-slozeni-taxi-zkousek/$', view=clanek2, name='clanek2'),
                        url(regex=r'^clanky/taxi-zkousky-novela-zakona/$', view=clanek3, name='clanek3'),
                        url(regex=r'^jakToFunguje/$', view=jakToFunguje, name='jakToFunguje'),
                        url(regex=r'^sitemap/$', view=sitemap, name='sitemap'),
                        url(regex=r'^signup/$', view=signup, name='signup'),
                        url(regex=r'^cookies/$', view=cookies, name='cookies'),
                        url(regex=r'^password/$', view=change_password, name='change_password'),
                        url(regex=r'^logout/$', view=logout_user, name='logout'),
                       url(regex=r'^quizzes/$',
                           view=QuizListView.as_view(),
                           name='quiz_index'),

                       url(regex=r'^category/$',
                           view=CategoriesListView.as_view(),
                           name='quiz_category_list_all'),

                       url(regex=r'^category/(?P<category_name>[\w|\W-]+)/$',
                           view=ViewQuizListByCategory.as_view(),
                           name='quiz_category_list_matching'),

                       url(regex=r'^progress/$',
                           view=QuizUserProgressView.as_view(),
                           name='quiz_progress'),

                       url(regex=r'^marking/$',
                           view=QuizMarkingList.as_view(),
                           name='quiz_marking'),

                       url(regex=r'^marking/(?P<pk>[\d.]+)/$',
                           view=QuizMarkingDetail.as_view(),
                           name='quiz_marking_detail'),

                       #  passes variable 'quiz_name' to quiz_take view
                       url(regex=r'^(?P<slug>[\w-]+)/$',
                           view=QuizDetailView.as_view(),
                           name='quiz_start_page'),

                       url(regex=r'^(?P<quiz_name>[\w-]+)/take/$',
                           view=QuizTake.as_view(),
                           name='quiz_question'),

]
