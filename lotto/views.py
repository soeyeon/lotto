from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from .lotto import lotto


def lottopage(self):
    context = {}
    return render(self, 'lotto/lottopage.html', context)

def lottoresult(self):
    inputLotto = str(self.POST['inputVal'])
    print(inputLotto)
    result_all = lotto(inputLotto)
    this_time = next(result_all)
    this_date = next(result_all)
    win_numbers = next(result_all)
    bonus_number = next(result_all)
    my_numbers = next(result_all)
    my_rank = next(result_all)
    context = {
        'tt' : this_time,
        'td' : this_date,
        'wns' : win_numbers,
        'bon' : bonus_number,
        'mns' : my_numbers,
        'mr' : my_rank,
    }
    return render(self, 'lotto/lottoresult.html', context)
