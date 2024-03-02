# Generated by Django 5.0.2 on 2024-03-02 13:49

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Staff',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('full_name_amh', models.CharField(max_length=40)),
                ('full_name_eng', models.CharField(max_length=30)),
                ('gender', models.CharField(choices=[('ሴት', 'ሴት'), ('ወ', 'ወ')], default='ወ', max_length=4)),
                ('place_of_work', models.CharField(max_length=15)),
                ('pension_id_no', models.CharField(max_length=25)),
                ('date_of_birth', models.DateField()),
                ('ethnicity', models.CharField(blank=True, choices=[('አማራ', 'አማራ'), ('ኦሮሞ', 'ኦሮሞ'), ('ጉራጌ', 'ጉራጌ'), ('ሱማሌ', 'ሱማሌ')], max_length=8)),
                ('edu_type', models.CharField(max_length=25)),
                ('edu_level', models.CharField(max_length=25)),
                ('hired_year', models.DateField()),
                ('years_of_service', models.CharField(max_length=25)),
                ('marital_status', models.CharField(choices=[('ያገባች', 'ያገባች'), ('ያገባ', 'ያገባ'), ('ያላገባች', 'ያላገባች'), ('ያላገባ', 'ያላገባ'), ('የፈታ/ች', 'የፈታ/ች')], default='ያላገባ', max_length=25)),
                ('position', models.CharField(max_length=55)),
                ('position_grade', models.CharField(max_length=6)),
                ('salary', models.DecimalField(decimal_places=2, max_digits=10)),
                ('hire_type', models.CharField(choices=[('ቋሚ', 'ቋሚ'), ('ጊዜያዊ', 'ጊዜያዊ')], default='ጊዜያዊ', max_length=6)),
            ],
        ),
    ]