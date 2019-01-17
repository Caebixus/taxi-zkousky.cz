# Generated by Django 2.0.7 on 2019-01-02 16:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mcq', '0003_auto_20190102_2123'),
    ]

    operations = [
        migrations.AlterField(
            model_name='mcqquestion',
            name='answer_order',
            field=models.CharField(blank=True, choices=[('content', 'Content'), ('none', 'None')], help_text='The order in which multichoice \\ answer options are displayed \\ to the user', max_length=100, null=True, verbose_name='Answer Order'),
        ),
    ]
