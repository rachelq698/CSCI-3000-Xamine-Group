# Generated by Django 3.0.5 on 2020-04-29 01:44

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('xamine', '0035_auto_20200427_2303'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='team',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='orders', to='xamine.Team'),
        ),
    ]
