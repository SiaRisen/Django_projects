from django.shortcuts import render


DATA = {
    'omlet': {
        'яйца, шт': 2,
        'молоко, л': 0.1,
        'соль, ч.л.': 0.5,
    },
    'pasta': {
        'макароны, г': 0.3,
        'сыр, г': 0.05,
    },
    'buter': {
        'хлеб, ломтик': 1,
        'колбаса, ломтик': 1,
        'сыр, ломтик': 1,
        'помидор, ломтик': 1,
    },
    'tartar': {
        'маринованные огурцы, шт': 1,
        'укроп, пуч.': 1,
        'майонез, с.л.': 2,
        'чеснок, зуб.': 1,
    },
}


def receipts_view(request, dish):
    servings = int(request.GET.get('servings', 1))
    result = {ingredient: amount * servings for ingredient, amount in DATA[dish].items()}
    context = {
        'recipe': result,
    }
    return render(request, 'calculator/index.html', context)
