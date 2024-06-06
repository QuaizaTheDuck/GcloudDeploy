# Generated by Django 5.0.6 on 2024-05-31 11:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0003_contactentry'),
    ]

    operations = [
        migrations.CreateModel(
            name='Mecz',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('data', models.DateField()),
                ('godzina', models.TimeField()),
                ('gospodarz', models.CharField(max_length=100)),
                ('logo_gospodarza', models.ImageField(upload_to='logos/')),
                ('wynik', models.CharField(blank=True, max_length=10, null=True)),
                ('przeciwnik', models.CharField(max_length=100)),
                ('logo_przeciwnika', models.ImageField(upload_to='logos/')),
            ],
        ),
    ]