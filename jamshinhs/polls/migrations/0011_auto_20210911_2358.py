# Generated by Django 3.2.6 on 2021-09-11 14:58

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0010_auto_20210911_2337'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='user',
            name='extra_time',
        ),
        migrations.AlterField(
            model_name='apply',
            name='activity',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='polls.activity', verbose_name='활동'),
        ),
        migrations.AlterField(
            model_name='apply',
            name='student_id',
            field=models.IntegerField(verbose_name='학번'),
        ),
    ]
