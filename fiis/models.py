from django.db import models


class Fii(models.Model):
    name = models.CharField(max_length=6, unique=True)
    cards_ticker = models.JSONField(null=True, blank=True)
    equity_value = models.JSONField(null=True, blank=True)
    content_info = models.JSONField(null=True, blank=True)
    indicators = models.JSONField(null=True, blank=True)
    comunications = models.JSONField(null=True, blank=True)
    notices = models.JSONField(null=True, blank=True)
    properties = models.JSONField(null=True, blank=True)
    dividends = models.JSONField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    