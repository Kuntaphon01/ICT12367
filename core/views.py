from django.shortcuts import render, redirect, get_object_or_404
from .forms import ActivityForm
from .models import Activity

def activity_form(request, pk=None):
    if pk:
        activity = get_object_or_404(Activity, pk=pk)
        form = ActivityForm(request.POST or None, request.FILES or None, instance=activity)
    else:
        form = ActivityForm(request.POST or None, request.FILES or None)
    
    if form.is_valid():
        form.save()
        return redirect('activity_list')
    
    return render(request, 'core/form.html', {'form': form})

def activity_list(request):
    activities = Activity.objects.all().order_by('-date')
    return render(request, 'core/list.html', {'activities': activities})

def activity_edit(request, pk):
    return activity_form(request, pk)

def activity_delete(request, pk):
    activity = get_object_or_404(Activity, pk=pk)
    if request.method == 'POST':
        activity.delete()
        return redirect('activity_list')
    return render(request, 'core/confirm_delete.html', {'activity': activity})
