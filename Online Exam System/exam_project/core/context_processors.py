from .models import StudentProfile

def student_status(request):
    if request.user.is_authenticated:
        try:
            profile = StudentProfile.objects.get(user=request.user)
            return {'is_verified': profile.is_approved}
        except StudentProfile.DoesNotExist:
            return {'is_verified': False}
    return {}