# Generated by Django 5.0.7 on 2024-08-18 01:00

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Fii',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=6)),
                ('cards_ticker', models.JSONField(blank=True, null=True)),
                ('equity_value', models.JSONField(blank=True, null=True)),
                ('content_info', models.JSONField(blank=True, null=True)),
                ('indicators', models.JSONField(blank=True, null=True)),
                ('comunications', models.JSONField(blank=True, null=True)),
                ('notices', models.JSONField(blank=True, null=True)),
                ('properties', models.JSONField(blank=True, null=True)),
                ('dividends', models.JSONField(blank=True, null=True)),
            ],
        ),
    ]
