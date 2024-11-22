from django.shortcuts import render
from members.models import Member

# Create your views here.
def member_list(request):
    member_id = Member.objects.all()
    context = {'members' : member_id}
    return render(request, 'member_list.html', context)