# Generated by Django 4.2.7 on 2024-01-06 22:48

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=60)),
                ('price', models.DecimalField(decimal_places=2, max_digits=6)),
                ('description', models.TextField(default='Description', max_length=1000)),
                ('image', models.ImageField(default='Products/products.png', upload_to='Products')),
            ],
        ),
    ]
