# Generated by Django 3.2.6 on 2021-08-29 05:11

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('reviews', '0034_auto_20170809_2034'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Activity',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('activity_type', models.CharField(choices=[('F', 'Follow'), ('C', 'Comment'), ('S', 'Star')], max_length=1)),
                ('content', models.CharField(blank=True, max_length=500)),
                ('date', models.DateTimeField(auto_now_add=True)),
                ('from_user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('review', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='reviews.review')),
                ('to_user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='+', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'activity',
                'verbose_name_plural': 'activities',
            },
        ),
    ]
