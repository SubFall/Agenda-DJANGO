# Generated by Django 5.2 on 2025-05-03 23:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('contatos', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='contato',
            name='picture',
            field=models.ImageField(blank=True, upload_to='picture/%y/%m/'),
        ),
        migrations.AddField(
            model_name='contato',
            name='show',
            field=models.BooleanField(default=True),
        ),
    ]
