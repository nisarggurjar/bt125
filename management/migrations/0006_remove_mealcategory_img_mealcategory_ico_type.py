# Generated by Django 5.1.5 on 2025-02-02 19:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("management", "0005_alter_mealcategory_img"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="mealcategory",
            name="img",
        ),
        migrations.AddField(
            model_name="mealcategory",
            name="ico_type",
            field=models.CharField(blank=True, max_length=128, null=True),
        ),
    ]
