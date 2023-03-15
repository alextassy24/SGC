from django.shortcuts import render, redirect
from django.contrib import messages
from .models import Price, Portofolio_Item, Question
from .forms import QuestionForm

def home(request):
    return render(request, 'home.html')

def about(request):
    return render(request, 'about.html')

def contact(request):
    return render(request, 'contact.html')

def faq(request):
    question = Question.objects.all()
    context = {
        'questions': question
    }
    return render(request, 'faq.html',context)

def faq_form(request):
    form = QuestionForm()
    if request.method == "POST":
        form = QuestionForm(request.POST)
        if form.is_valid():
            question = form.save(commit=False)
            question.save()
            messages.success(request, 'Your question has been sent!')
            return redirect('faq')
        else:
            messages.error(request, 'An error occurred!')
    return render(request, 'faq-form.html', {'form':form})

def portofolio(request):
    portofolio = Portofolio_Item.objects.all()
    context = {
        'portofolios': portofolio
    }
    return render(request, 'portofolio.html',context)

def products(request, pk):
    product = Price.objects.get(id=pk)
    context = {
        'product': product
    }
    return render(request, 'products.html',context)

def price_list(request):
    price_list = Price.objects.all()
    context = {
        'prices': price_list
    }
    return render(request, 'price_list.html',context)