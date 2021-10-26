from django.contrib import admin
from django.contrib.admin.filters import ListFilter
from .models import Book, Student

# Register your models here.
# admin.site.register(Book)
admin.site.register(Student)




####2ND METHOD OF IT. ESPECIALLY IF YOU WANT TO CUSTOMIZE THE FACE

@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    list_display = ["title", "no_of_pages", "isbn", "date"]
    list_editable = ["isbn"]
    list_filter = ["date"]
    list_per_page = 2
    search_fields = ["title", "body", "author"]
    # pass