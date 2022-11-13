from django.shortcuts import render
from django.http import HttpResponse


def task_1(request):
    lets_do_it = [{'priority': 100, 'task': 'Скласти перелік справ'},
                  {'priority': 150, 'task': 'Вивчати Django'},
                  {'priority': 1, 'task': 'Подумати про сенс життя'}]
    return HttpResponse('Plan\n' + str(lets_do_it))


def task_2(request):
    return render(request, 'lesson_3/task_2.html')


def luk(request):
    return HttpResponse("""
                        <h1>Сторінка Люка:</h1>
                        <p>Люк Скайуокер — один із головних персонажів всесвіту «Зоряних війн», джедай, син сенатора 
                        з Набу Падме Амідали Наберрі та лицаря-джеда Енакіна Скайуокера.</p>
                        """)


def lea(request):
    return HttpResponse("""
                        <h1>Сторінка Леї:</h1>
                        <p>Лея Органа — дочка лицаря-джеда Енакіна Скайуокера та сенатора Падме Амідали Наберрі.</p>
                        """)


def khan(request):
    return HttpResponse("""
                        <h1>Сторінка Хана:</h1>
                        <p>Хан. Соло — пілот космічного корабля «Тисячолітній сокіл», його бортмеханіком та другим 
                        пілотом є вуки на ім'я Чубакка.</p>
                        """)


def task_5(request):
    lets_do_it = [{'priority': 100, 'task': 'Скласти перелік справ'},
                  {'priority': 150, 'task': 'Вивчати Django'},
                  {'priority': 1, 'task': 'Подумати про сенс життя'}]
    context = {"do_list": lets_do_it}
    return render(request, 'lesson_3/task_5.html', context)

