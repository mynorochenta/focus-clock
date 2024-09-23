from django.shortcuts import render

# Create your views here.
from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.http import JsonResponse
from .models import PomodoroSession
from django.views.decorators.csrf import csrf_exempt
import json

def pomodoro_view(request):
    sessions = PomodoroSession.objects.all().order_by('-start_time')
    return render(request, 'pomodoro.html', {'sessions': sessions})

@csrf_exempt
def save_session(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        duration = data.get('duration')
        completed = data.get('completed', False)
        
        session = PomodoroSession.objects.create(
            user=request.user,
            duration=duration,
            completed=completed
        )
        
        return JsonResponse({'status': 'success', 'session_id': session.id})
    return JsonResponse({'status': 'error', 'message': 'Invalid request method'})

def get_sessions(request):
    sessions = PomodoroSession.objects.all().order_by('-start_time')[:10]
    sessions_data = [{'start_time': session.start_time.strftime('%Y-%m-%d %H:%M:%S'), 
                      'completed': session.completed} for session in sessions]
    return JsonResponse({'sessions': sessions_data})