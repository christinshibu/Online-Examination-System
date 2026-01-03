from django.contrib import admin
from django.utils.html import format_html
from .models import StudentProfile, Question, Result

@admin.register(StudentProfile)
class StudentProfileAdmin(admin.ModelAdmin):
    # Consolidated display list
    list_display = ('user', 'phone_number', 'college_name', 'is_approved', 'show_id_front', 'show_id_back')
    list_editable = ('is_approved',)
    
    # Adding Search and Filters for the Administrative Module
    search_fields = ('user__username', 'phone_number', 'college_name')
    list_filter = ('is_approved', 'college_name')

    def show_id_front(self, obj):
        if obj.id_card_front:
            return format_html('<img src="{}" style="width: 50px; height:auto; border-radius:5px;">', obj.id_card_front.url)
        return "No Image"
    
    def show_id_back(self, obj):
        if obj.id_card_back:
            return format_html('<img src="{}" style="width: 50px; height:auto; border-radius:5px;">', obj.id_card_back.url)
        return "No File"

    show_id_front.short_description = 'ID Front'
    show_id_back.short_description = 'ID Back'

@admin.register(Question)
class QuestionAdmin(admin.ModelAdmin):
    list_display = ('text', 'correct_answer')
    search_fields = ('text',)

@admin.register(Result)
class ResultAdmin(admin.ModelAdmin):
    list_display = ('user', 'score', 'percentage', 'status', 'exam_date')
    list_filter = ('status', 'exam_date')
    search_fields = ('user__username',)