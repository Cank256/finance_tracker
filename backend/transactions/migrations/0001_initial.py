# Generated by Django 4.1.13 on 2023-11-10 18:42

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    initial = True

    dependencies = [
        ("categories", "__first__"),
    ]

    operations = [
        migrations.CreateModel(
            name="Transaction",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("description", models.CharField(max_length=250)),
                ("amount", models.DecimalField(decimal_places=2, max_digits=12)),
                ("date", models.DateField()),
                (
                    "category",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="categories.category",
                    ),
                ),
            ],
        ),
    ]