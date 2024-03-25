# Generated by Django 4.2.11 on 2024-03-25 20:49

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0003_post_choice_category'),
    ]

    operations = [
        migrations.AlterField(
            model_name='postcategory',
            name='category',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='news.category'),
        ),
        migrations.AlterField(
            model_name='postcategory',
            name='posts',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='news.post'),
        ),
    ]