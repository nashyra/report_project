from django.shortcuts import render
from django.http.response import HttpResponse
from django import forms
from django.core.exceptions import ValidationError

# Create your views here.
class FormNums(forms.Form):
    num4 = forms.IntegerField(widget=forms.NumberInput, help_text = "A number")
    
    def clean(self):
        data = super(FormNums, self).clean()
        try:
            num=int(data['num4'])
        except:
            raise ValidationError("Int is required")
        return data

def convert_int(number):
    result = 0
    try:
        result = int(number)
    except:
        pass
    return result

def home(request, num1, num2):
    #print(type(num1)) #type me permite mostrar el tipo de los valores
    #print (request.GET)
    num4 = 0
    num3 = convert_int(request.GET.get('num3','0'))
    
    if request.method == 'POST':
        form = FormNums(request.POST)
        if form.is_valid():
            num4 = convert_int(form.cleaned_data['num4'])
    else:
        form = FormNums()
    
    result = int(num1) + int(num2) + num3 + num4
    return render(request, 'home.html', {
                    'result': result,
                    'values': [num1, num2, num3, num4],
                    'form': form
    })
    #return HttpResponse("Hola a todos %d" % (result,)) #el %d significa q solo voy a tener numeros
