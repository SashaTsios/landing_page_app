from datetime import datetime
from django.shortcuts import render, redirect
from core.forms import ContactUsForm
from core.models import Feedback_new, Subject, Author, NumOfParticipant

# Create your views here.
def landing_page_view(request):
    # students_list = ["Al", "Rom", "Ir", "Bo", "Serh", "And"]
    # random.shuffle(students_list)
    message = request.GET.get("message")
    if message:
        pass

    return render(
        request,
        "landing_page.html",
        context={"message": message, "name": "Vasyl", "now": datetime.now(),},
    )


def about_page_view(request):
    return render(
        request,
        "about_page.html",
        context={
            "course": "Python",
            "num_students": 6,
            "students_list": {
                "alex": {"right_side": True, "birhtday": datetime(2020, 2, 3)},
                "roman": {"right_side": True},
                "ira": {"right_side": True},
                "bohdan": {"right_side": True},
                "serhii": {"right_side": False},
                "andrii": {"right_side": False},
            },
            "end": datetime(2020, 2, 20),
        },
    )


def contact_us_view(request):
    # https://docs.djangoproject.com/en/3.0/topics/forms/
    LAST_MESSAGE = "DEFAULT"
    LAST_NAME = "BOT"
    if request.method == "POST":
        form = ContactUsForm(request.POST)
        if form.is_valid():
            print("PerFECT")
            LAST_MESSAGE = request.POST.get("message22")
            LAST_NAME = request.POST.get("name22")

            feedback = Feedback_new.objects.create(
                name_m=LAST_NAME, text_m=LAST_MESSAGE
            )  # as in models
            #  return redirect('/feedbacks/')

            response = redirect("feedbacks")
            response["Location"] += "?from=contact-us"
            return response
    else:
        print("GET method")
        form = ContactUsForm()
    return render(
        request,
        "contact_us.html",
        context={"message44": LAST_MESSAGE, "name44": LAST_NAME, "form": form},
    )


def feedbacks_view(request):
    has_contacted = bool(request.GET.get("from"))  #  == 'contact-us'
    feedbacks = Feedback_new.objects.filter(is_active=True)
    return render(
        request,
        "feedbacks.html",
        context={"feedbacks": feedbacks, "has_contacted": has_contacted},
    )


def subjects_view(request):
    # subjects = Subject.objects.filter(is_active=True)
    # subjects = Subject.objects.all()
    author_name = request.GET.get("author")
    stats = request.GET.get("statistic_s")
    if author_name:
        author_obj = Author.objects.filter(name_a=author_name).first()  # в моделі Author беремо перший екземпляр із  name_a=author_name із введеним імям
        subjects = Subject.objects.filter(is_active_s=True, author=author_obj)
    elif stats:
        stats_obj = NumOfParticipant.objects.filter(name_num=stats).first()  # в моделі NumOfParticipant беремо перший екземпляр із  name_num=author_name із введеним (name_num=stats iz Model)
        subjects = Subject.objects.filter(is_active_s=True, statistic_s=stats_obj)
    else:
        subjects = Subject.objects.filter(is_active_s=True)
    return render(request, "subjects.html", context={"subjects": subjects,},)


def subject_item_view(request, subject_name_s): # subject_name_s беремо звідси: path('subjects/<str:subject_name_s>/',
    subject_item = Subject.objects.filter(is_active_s=True, bot_name_s=subject_name_s).first()
    return render(request, "bot.html", context={"bot": subject_item,},)

def subject_stats_view(request, statistic_s1): # statistic_s беремо звідси: path('subjects/<str:subject_name_s>/',
    subject_item = Subject.objects.filter(is_active_s=True, statistic_s=statistic_s1).first()
    return render(request, "bot.html", context={"bot": subject_item,},)