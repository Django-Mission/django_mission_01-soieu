from xml.dom.minidom import Document
from django.shortcuts import render
from django.http import HttpResponse
import random
# Create your views here.


def calculator(request):
    # return HttpResponse('계산기 기능 구현 시작입니다.')
    print(f'request = {request}')
    # 1. 데이터 확인
    num1 = request.GET.get('num1')
    operators = request.GET.get('operators')
    num2 = request.GET.get('num2')

    # 2. 계산
    if operators == '+':
        result = int(num1) + int(num2)
    elif operators == '-':
        result = int(num1) - int(num2)
    elif operators == '*':
        result = int(num1) * int(num2)
    elif operators == '/':
        result = int(num1) / int(num2)
    else:
        result = 0

    # 3. 응답
    return render(request, 'calculator.html', {'result': result})


def lottoa(request):
    result = []
 
    result = random.sample(range(1, 46), 7)

    return render(request, 'lottoA.html', {'result': result})


def lottobinput(request):
    return render(request, 'lottoBInput.html')


def lottoboutput(request):
    ct = request.GET.get('ct')
    ct = int(ct)
    result = []
    some = []
    

    for i in range(ct):
        some = random.sample(range(1, 46), 7)
        result.append(some)

    return render(request, 'lottoBOutput.html', {'ct':ct, 'result': result})
