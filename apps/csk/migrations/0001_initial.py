# Generated by Django 4.1.7 on 2023-03-25 17:19

from django.conf import settings
import django.core.validators
from django.db import migrations, models
import django.db.models.deletion
import multiselectfield.db.fields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auths', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='MasterUser',
            fields=[
                ('customuser_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to=settings.AUTH_USER_MODEL)),
                ('service_master', multiselectfield.db.fields.MultiSelectField(choices=[('электрик', 'Электрик'), ('сантехник', 'Сантехник'), ('инженер', 'Инженер'), ('жилые и коммунальные службы', 'Жилые и коммунальные службы'), ('архитектор/дизайнер', 'Архитектор/Дизайнер'), ('юрист', 'Юрист'), ('прочее', 'Прочее')], max_length=87, validators=[django.core.validators.MaxValueValidator(10)])),
                ('avg_rating', models.FloatField(default=0.0, validators=[django.core.validators.MinValueValidator(0.0), django.core.validators.MaxValueValidator(5.0)])),
                ('is_busy', models.BooleanField(default=False)),
            ],
            options={
                'verbose_name': 'мастер',
                'verbose_name_plural': 'мастера',
                'ordering': ('-datetime_created',),
            },
            bases=('auths.customuser',),
        ),
        migrations.CreateModel(
            name='Rating',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('rating_points', models.IntegerField(choices=[(1, 'Очень низко'), (2, 'Низко'), (3, 'Средне'), (4, 'Хорошо'), (5, 'Прекрасно')], default=1)),
            ],
        ),
        migrations.CreateModel(
            name='Service',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('status_points', models.IntegerField(choices=[(1, 'Электрик'), (2, 'Сантехник'), (3, 'Инженер'), (4, 'Жилые и коммунальные службы'), (5, 'Архитектор/Дизайнер'), (6, 'Юрист'), (7, 'Прочее')], default=7)),
            ],
        ),
        migrations.CreateModel(
            name='Status',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('status_points', models.IntegerField(choices=[(1, 'Срочный запрос'), (2, 'Запрос в процессе'), (3, 'Запрос осуществлен'), (4, 'Запрос отклонен')], default=2)),
            ],
        ),
        migrations.CreateModel(
            name='UserCall',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('personal_account', models.CharField(max_length=12, verbose_name='лицевой счёт')),
                ('problem', models.TextField(verbose_name='причина обращения')),
                ('datetime_created', models.DateTimeField(auto_now_add=True, verbose_name='время создание')),
                ('caller', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='заказчик')),
                ('master_id', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='master_id', to='csk.masteruser')),
            ],
            options={
                'verbose_name': 'обращение',
                'verbose_name_plural': 'обращения',
                'ordering': ('-datetime_created',),
            },
        ),
        migrations.CreateModel(
            name='MasterUserRating',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('master_user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='csk.masteruser')),
                ('rating', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='csk.rating')),
            ],
        ),
        migrations.AddField(
            model_name='masteruser',
            name='ratings',
            field=models.ManyToManyField(through='csk.MasterUserRating', to='csk.rating'),
        ),
    ]
