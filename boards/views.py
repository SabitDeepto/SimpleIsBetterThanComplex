from django.shortcuts import render
from django.http import HttpResponse
from .models import Board

def home(request):
	all_board = Board.objects.all()
	dic = {"list":all_board} 
	return render(request, 'home.html', dic)
