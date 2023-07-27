from django.contrib import auth, messages
from django.contrib.auth.models import User
from django.shortcuts import render, redirect
from django.urls import reverse
from .models import District, Branch, Material, Customer


def home(request):
    districts = District.objects.all()
    return render(request, 'home.html', {'districts': districts})

def district_wikipedia(request, district_id):
    return redirect('https://en.wikipedia.org/')

def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = auth.authenticate(username=username, password=password)

        if user is not None:
            auth.login(request, user)
            return redirect('customer_form')
        else:
            messages.info(request, "InValid credentials")
    return render(request, 'login.html')

def register(request):
    if request.method == 'POST':
        username = request.POST['username']
        password1 = request.POST['password1']
        password2 = request.POST['password2']
        if password1 == password2:
            if User.objects.filter(username=username).exists():
                messages.info(request, "user taken")
                return redirect('register')
            else:
                user = User.objects.create_user(username=username, password=password1)
                user.save()
                return redirect('login')
                print("user created")
        else:
            messages.info(request, "wrong password")
            return redirect('register')
        return redirect('/')

    return render(request, 'register.html')

def customer_form(request):
    if request.method == 'POST':
        name = request.POST['name']
        dob = request.POST['dob']
        age = request.POST['age']
        gender = request.POST['gender']
        phone_number = request.POST['phone_number']
        mail_id = request.POST['mail_id']
        address = request.POST['address']
        district_id = request.POST['district']
        print("district",district_id)
        branch_id = request.POST['branch']
        account_type = request.POST['account_type']
        materials_provide_ids = request.POST.getlist('materials_provide')

        district = District.objects.get(pk=district_id)
        branch = Branch.objects.get(pk=branch_id)
        materials_provide = Material.objects.filter(pk__in=materials_provide_ids)

        customer = Customer.objects.create(
            name=name,
            dob=dob,
            age=age,
            gender=gender,
            phone_number=phone_number,
            mail_id=mail_id,
            address=address,
            district=district,
            branch=branch,
            account_type=account_type
        )
        customer.materials_provide.set(materials_provide)

        return redirect('application_accepted')

    districts = District.objects.all()
    district_id = request.POST.get('district')
    branches = Branch.objects.all()

    materials = Material.objects.all()

    return render(request, 'customer_form.html', {'districts': districts, 'branches': branches, 'materials': materials})

    # if request.method == 'POST':
    #     form = CustomerForm(request.POST)
    #     if form.is_valid():
    #         form.save()
    #         return redirect('application_accepted')
    # else:
    #     form = CustomerForm()
    # return render(request, 'customer_form.html', {'form': form})


def application_accepted(request):
    return render(request, 'application_accepted.html')

def logout(request):
    auth.logout(request)
    return redirect('/')