from django.urls import path
from .views import task_1, task_2, luk, lea, khan, task_5

app_name = 'lesson_3'

urlpatterns = [
    path('task_1/', task_1, name='task_3_1'),
    path('task_2/', task_2, name='task_2'),
    path('task_2/luk/', luk, name='luk'),
    path('task_2/lea/', lea, name='lea'),
    path('task_2/khan/', khan, name='khan'),
    path('task_5/', task_5, name='task_5'),
]
