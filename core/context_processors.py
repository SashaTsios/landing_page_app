from random import shuffle

def student_names(request):
    people = ["0Al", "0Rom", "0Ir", "0o", "0Serh", "0And"]
    shuffle(people)
    return{"people":people}