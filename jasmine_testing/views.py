from django.shortcuts import render, redirect


# Create your views here.
def run_jasmine(request):
    if request.user.is_superuser:
        return render(request, 'jasmine_testing/jasmine.html')
    else:
        return redirect('people:person-list')
