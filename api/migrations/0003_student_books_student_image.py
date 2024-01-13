# Generated by Django 4.2.7 on 2024-01-13 14:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0002_student'),
    ]

    operations = [
        migrations.AddField(
            model_name='student',
            name='books',
            field=models.TextField(default='List of books', max_length=1000),
        ),
        migrations.AddField(
            model_name='student',
            name='image',
            field=models.ImageField(default='Products/products.png', upload_to='Students'),
        ),
    ]
