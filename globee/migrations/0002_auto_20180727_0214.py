# Generated by Django 2.0.7 on 2018-07-27 00:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('globee', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='globeeipn',
            name='confirmation_speed',
            field=models.CharField(choices=[('low', 'low speed / low risk'), ('medium', 'medium speed / medium risk'), ('high', 'high speed with / risk')], default='medium', max_length=50),
        ),
    ]
