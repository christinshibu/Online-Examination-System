from django.db import models
from django.contrib.auth.models import User

class Question(models.Model):
    text = models.TextField() # Question text [cite: 62]
    option1 = models.CharField(max_length=200) # Multiple options [cite: 63]
    option2 = models.CharField(max_length=200)
    option3 = models.CharField(max_length=200)
    option4 = models.CharField(max_length=200)
    correct_answer = models.CharField(max_length=200) # Correct answer [cite: 64]

    def __str__(self):
        return self.text

class Result(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE) # Secure login data [cite: 7, 95]
    score = models.IntegerField() # Score calculated [cite: 79]
    percentage = models.FloatField() # Percentage calculated [cite: 80]
    status = models.CharField(max_length=10) # Pass/Fail status [cite: 81]
    exam_date = models.DateTimeField(auto_now_add=True) # Date & time [cite: 142]

class StudentProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    phone_number = models.CharField(max_length=15)
    college_name = models.CharField(max_length=255)
    id_card_front = models.ImageField(upload_to='id_cards/')
    id_card_back = models.ImageField(upload_to='id_cards/')
    # New field for account status
    is_approved = models.BooleanField(default=False) 

    def __str__(self):
        return f"{self.user.username} - Approved: {self.is_approved}"