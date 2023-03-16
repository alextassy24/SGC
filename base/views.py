from django.shortcuts import render, redirect
from django.db.models import Q
from django.contrib import messages
from .models import Price, Portofolio_Item, Question, Portofolio_Photo
from .forms import QuestionForm, MessageForm

def home(request):
    return render(request, 'home.html')

def about(request):
    return render(request, 'about.html')

def contact(request):
    return render(request, 'contact.html')

def faq(request):
    q = request.GET.get('q') if request.GET.get('q') != None else ''
    question = Question.objects.filter(
        Q(subject__icontains=q) |
        Q(name__icontains=q) |
        Q(description__icontains=q) 
        
    )
    # question = Question.objects.all()
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

def view_more(request, pk):
    portofolio = Portofolio_Item.objects.get(id=pk)
    photos = portofolio.photos.all()
    context = {
        'portofolio': portofolio,
        'photos': photos
    }
    return render(request, 'portofolio_item.html', context)

def contact(request):
    form = MessageForm()
    if request.method == "POST":
        form = MessageForm(request.POST)
        if form.is_valid():
            question = form.save(commit=False)
            question.save()
            messages.success(request, 'Your message has been sent!')
            return redirect('home')
        else:
            messages.error(request, 'An error occurred!')
    return render(request, 'contact.html', {'form':form})  