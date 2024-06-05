# Generated by Django 5.0.6 on 2024-06-05 07:33

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
                ('title', models.CharField(max_length=60)),
                ('brand', models.CharField(max_length=60)),
                ('short_desc', models.CharField(max_length=300)),
                ('long_desc', models.TextField()),
                ('org_price', models.IntegerField()),
                ('dis_price', models.IntegerField()),
                ('img', models.ImageField(upload_to='image/')),
            ],
        ),
    ]
