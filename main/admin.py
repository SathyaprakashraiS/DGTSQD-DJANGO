from django.contrib import admin
from .models import review
from .models import news
from .models import event
from .models import UserProfile
from .models import project
from .models import achievements
from .models import report
# Register your models here.
admin.site.register(review)
admin.site.register(news)
admin.site.register(event)
admin.site.register(project)
admin.site.register(achievements)
admin.site.register(report)

class UserProfileAdmin(admin.ModelAdmin):
    list_display = ('user', 'phone', 'img', 'about')


admin.site.register(UserProfile, UserProfileAdmin)