from django.shortcuts import render

def calculator_view(request):
    if request.method == 'GET':
        return render(request, 'calculator.html')

    elif request.method == 'POST':
        print(request.POST)

        context = {
            'num_1': request.POST.get('number_1'),
            'num_2': request.POST.get('number_2'),
            'category': request.POST.get('category'),
            'sign': None,
            'total': None,
            'equally': '=',
            'result': 'Result : '
        }
        if request.POST.get('category') == 'add':
            context['sign'] = '+'
            context['total'] = int(context['num_1'])+int(context['num_2'])
            return render(request, 'calculator.html', context)
        elif request.POST.get('category') == 'subtract':
            context['sign'] = '-'
            context['total'] = int(context['num_1'])-int(context['num_2'])
            return render(request, 'calculator.html', context)
        elif request.POST.get('category') == 'multiply':
            context['sign'] = '*'
            context['total'] = int(context['num_1'])*int(context['num_2'])
            return render(request, 'calculator.html', context)
        elif request.POST.get('category') == 'divide':
            context['sign'] = ':'
            context['total'] = int(context['num_1'])/int(context['num_2'])
            return render(request, 'calculator.html', context)
        else:
            return render(request, 'calculator.html')




