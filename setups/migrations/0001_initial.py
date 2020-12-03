# Generated by Django 3.1.4 on 2020-12-03 19:49

from django.db import migrations, models
import django.db.models.deletion
import django_enum_choices.choice_builders
import django_enum_choices.fields
import setups.enums


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('django_celery_beat', '0014_remove_clockedschedule_enabled'),
    ]

    operations = [
        migrations.CreateModel(
            name='Setup',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=70)),
                ('status', django_enum_choices.fields.EnumChoiceField(choice_builder=django_enum_choices.choice_builders.value_value, choices=[('Active', 'Active'), ('Disabled', 'Disabled')], default=setups.enums.SetupStatus['active'], enum_class=setups.enums.SetupStatus, max_length=8)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('time_interval', django_enum_choices.fields.EnumChoiceField(choice_builder=django_enum_choices.choice_builders.value_value, choices=[('1 min', '1 min'), ('5 mins', '5 mins'), ('1 hour', '1 hour')], default=setups.enums.TimeInterval['five_mins'], enum_class=setups.enums.TimeInterval, max_length=6)),
                ('task', models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='django_celery_beat.periodictask')),
            ],
            options={
                'verbose_name': 'Setup',
                'verbose_name_plural': 'Setups',
            },
        ),
    ]
