from django.contrib import admin
from ui.models import History

@admin.register(History)
class HistoryAdmin(admin.ModelAdmin):
    list_display = ('verb', 'tense', 'question', 'negative', 'affix', 'morph', 'created_at')
