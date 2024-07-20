# Generated by Django 4.2 on 2024-07-20 08:48

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0002_alter_classroom_class_name_alter_student_username'),
    ]

    operations = [
        migrations.AlterField(
            model_name='classroom',
            name='class_name',
            field=models.CharField(choices=[('PR', 'Primary'), ('JSS', 'Junior Secondary'), ('SSS', 'Senior Secondary')], max_length=100),
        ),
        migrations.CreateModel(
            name='CustomClassRoom',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('class_name', models.CharField(max_length=100)),
                ('school', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='custom_classrooms', to='accounts.school')),
            ],
        ),
    ]