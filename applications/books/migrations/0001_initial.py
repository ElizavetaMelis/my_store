# Generated by Django 4.0.2 on 2022-02-27 08:30

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('author', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Book',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255)),
                ('date_of_publish', models.DateTimeField()),
                ('picture', models.ImageField(blank=True, upload_to='media')),
                ('price', models.DecimalField(decimal_places=2, max_digits=5)),
                ('is_bestseller', models.BooleanField()),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='book', to='author.author')),
            ],
        ),
    ]
