# Generated by Django 4.1.3 on 2022-11-05 21:11

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ("api", "0003_historicpayments"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="order",
            name="commissions",
        ),
        migrations.RemoveField(
            model_name="order",
            name="date",
        ),
        migrations.AddField(
            model_name="order",
            name="commission",
            field=models.ForeignKey(
                blank=True,
                default=1,
                on_delete=django.db.models.deletion.CASCADE,
                to="api.commission",
            ),
            preserve_default=False,
        ),
    ]
