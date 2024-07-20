# Generated by Django 4.2 on 2024-07-20 09:07

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0003_alter_classroom_class_name_customclassroom'),
    ]

    operations = [
        migrations.AddField(
            model_name='student',
            name='custom_classroom',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='students', to='accounts.customclassroom'),
        ),
        migrations.AlterField(
            model_name='student',
            name='classroom',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='students', to='accounts.classroom'),
        ),
    ]
