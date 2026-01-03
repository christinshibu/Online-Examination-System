from django.shortcuts import render, redirect
from .models import Question, Result
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login ,logout
from django.contrib.auth.models import User
from .models import StudentProfile
import csv
import io
from django.contrib import messages

@login_required
def profile_view(request):
    try:
        # Retrieve the profile associated with the logged-in user
        profile = StudentProfile.objects.get(user=request.user)
        return render(request, 'profile.html', {'profile': profile})
    except StudentProfile.DoesNotExist:
        # Handle cases where a profile is missing (like for an admin)
        messages.warning(request, "No student profile found for this account.")
        return redirect('dashboard')

@login_required 
def exam_view(request):
    try:
        # Security Cycle: Verification check before exam initiation
        profile = StudentProfile.objects.get(user=request.user)
        
        if not profile.is_approved:
            # Prevents unapproved students from accessing the Exam Module
            results = Result.objects.filter(user=request.user).order_by('-exam_date')
            return render(request, 'dashboard.html', {
                'results': results,
                'error': 'Your account is pending verification. Please wait for Admin approval.'
            })
    except StudentProfile.DoesNotExist:
        # Prevent admins or broken accounts from starting an exam
        messages.error(request, "Only registered students with profiles can take exams.")
        return redirect('dashboard')

    questions = Question.objects.all() 
    if request.method == 'POST':
        score = 0
        for q in questions:
            selected = request.POST.get(f'question_{q.id}')
            if selected == q.correct_answer:
                score += 1
        
        total = questions.count()
        percent = (score / total) * 100 if total > 0 else 0
        status = "Pass" if percent >= 40 else "Fail"

        # Persistent storage for future reference
        Result.objects.create(user=request.user, score=score, percentage=percent, status=status)
        return render(request, 'result.html', {'score': score, 'percent': percent, 'status': status})

    return render(request, 'exam.html', {'questions': questions})

def student_login(request):
    if request.method == "POST":
        u = request.POST.get('username')
        p = request.POST.get('password')
        user = authenticate(request, username=u, password=p)
        if user is not None:
            login(request, user)
            # Authority Check: Redirect based on role
            if user.is_staff:
                return redirect('/admin/') # Send Admin to the authority panel
            return redirect('dashboard')   # Send Students to their dashboard
        else:
            return render(request, 'login.html', {'error': 'Invalid Credentials'})
    return render(request, 'login.html')

def register_student(request):
    if request.method == "POST":
        # Get basic details [cite: 23]
        uname = request.POST.get('username')
        pword = request.POST.get('password')
        phone = request.POST.get('phone')
        college = request.POST.get('college')
        
        # Get ID photos
        id_front = request.FILES.get('id_front')
        id_back = request.FILES.get('id_back')

        # Create User and Profile [cite: 24, 27]
        user = User.objects.create_user(username=uname, password=pword)
        StudentProfile.objects.create(
            user=user, 
            phone_number=phone, 
            college_name=college,
            id_card_front=id_front,
            id_card_back=id_back
        )
        return redirect('login')
    return render(request, 'register.html')

@login_required
def dashboard(request):
    # If the user is an Admin/Staff, redirect to Admin Panel or show Admin Data
    if request.user.is_staff:
        # Option A: Redirect directly to the Admin Panel
        return redirect('/admin/') 
        
    # Standard Student Logic
    results = Result.objects.filter(user=request.user).order_by('-exam_date')
    return render(request, 'dashboard.html', {'results': results})  

def student_logout(request):
    logout(request) # Destroys the user session
    return redirect('login') # Redirects back to the secure login module

def upload_questions(request):
    if request.method == "POST":
        csv_file = request.FILES.get('file')
        
        # Validation to ensure a file is selected [cite: 50, 133]
        if not csv_file.name.endswith('.csv'):
            messages.error(request, 'This is not a CSV file')
            return redirect('upload_questions')

        data_set = csv_file.read().decode('UTF-8')
        io_string = io.StringIO(data_set)
        next(io_string) # Skip the header row [cite: 68]

        for column in csv.reader(io_string, delimiter=',', quotechar="|"):
            # Create Question object from CSV columns [cite: 61, 71]
            Question.objects.create(
                text=column[0],
                option1=column[1],
                option2=column[2],
                option3=column[3],
                option4=column[4],
                correct_answer=column[5]
            )
        messages.success(request, 'Question Bank updated successfully!')
        return redirect('dashboard')

    return render(request, 'upload_questions.html')


@login_required
def edit_profile(request):
    profile = StudentProfile.objects.get(user=request.user)
    if request.method == "POST":
        # Update logic for basic details
        profile.phone_number = request.POST.get('phone')
        profile.college_name = request.POST.get('college')
        
        # Check if new photos are uploaded
        if request.FILES.get('id_front'):
            profile.id_card_front = request.FILES.get('id_front')
        if request.FILES.get('id_back'):
            profile.id_card_back = request.FILES.get('id_back')
            
        profile.save()
        # Add the success notification here
        messages.success(request, "Your profile has been updated successfully!") 
        return redirect('profile')
    return render(request, 'edit_profile.html', {'profile': profile})