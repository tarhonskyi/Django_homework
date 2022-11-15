from django.urls import path
from .views import (task_1, task_2, luk, lea, khan,
                    task_3, task_3_file, task_5, task_6,
                    task_7)

app_name = 'lesson_3'

urlpatterns = [
    path('task_1/', task_1, name='task_3_1'),
    path('task_2/', task_2, name='task_2'),
    path('task_2/luk/', luk, name='luk'),
    path('task_2/lea/', lea, name='lea'),
    path('task_2/khan/', khan, name='khan'),
    path('task_3/', task_3, name='task_3'),
    path('task_3/file/', task_3_file, name='file'),
    path('task_5/', task_5, name='task_5'),
    path('task_6/', task_6, name='task_6'),
    path('task_7/polls/', task_7, name='task_7'),
    path('task_7/polls/<int:question_id>/', task_7, name='question_detail')
]
