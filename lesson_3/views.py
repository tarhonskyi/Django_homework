from django.shortcuts import render
from django.http import HttpResponse


def task_1(request):
    lets_do_it = [{'priority': 100, 'task': 'Скласти перелік справ'},
                  {'priority': 150, 'task': 'Вивчати Django'},
                  {'priority': 1, 'task': 'Подумати про сенс життя'}]
    return HttpResponse(f'<h1>Plan</h1><p>{str(lets_do_it)}</p>')


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


def task_3(request):
    return render(request, 'lesson_3/task_3.html')


def task_3_file(request):
    with open('lesson_3/answer.txt', 'rb') as file:
        data = file.read()
    content = data
    response = HttpResponse(content, status=227, content_type='application/msword')
    response['Content-Disposition'] = 'attachment; filename="answer.doc"'
    return response


def task_5(request):
    lets_do_it = [{'priority': 100, 'task': 'Скласти перелік справ'},
                  {'priority': 150, 'task': 'Вивчати Django'},
                  {'priority': 1, 'task': 'Подумати про сенс життя'}]
    context = {"do_list": lets_do_it}
    return render(request, 'lesson_3/task_5.html', context)


def task_6(request):
    persons = [
        {'name': 'Шаддам IV', 'surname': 'Корріно'},
        {'name': 'Стать', 'surname': 'Атрейдес'},
        {'name': 'Франклін', 'surname': 'Герберт'}]
    context = {'persons': persons}
    return render(request, 'lesson_3/task_6.html', context)


def task_7(request, question_id=None):
    latest_question_list = [{'id': 1, 'question_text': 'У чому сенс життя?'},
                            {'id': 2, 'question_text': 'Що первинне: дух чи матерія?'},
                            {'id': 3, 'question_text': 'Чи існує свобода волі?'}]
    # latest_question_list = []
    if question_id:
        for question in latest_question_list:
            if question['id'] == question_id:
                context = {'question': question}
                return render(request, 'lesson_3/detail.html', context)
        else:
            return HttpResponse(f'Питання під таким номером {question_id} немає в списку')
    context = {'latest_question_list': latest_question_list}
    return render(request, 'lesson_3/task_7.html', context)

