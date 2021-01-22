# Generated by Django 3.1.5 on 2021-01-21 06:53

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('productname', models.CharField(max_length=255)),
                ('dateentered', models.DateField()),
                ('price', models.DecimalField(decimal_places=2, max_digits=6)),
                ('producturl', models.URLField()),
                ('descriptiono', models.TextField()),
            ],
            options={
                'db_table': 'product',
            },
        ),
        migrations.CreateModel(
            name='TechType',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('typename', models.CharField(max_length=255)),
                ('typedescription', models.TextField(blank=True, null=True)),
            ],
            options={
                'db_table': 'techtype',
            },
        ),
        migrations.CreateModel(
            name='Review',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255)),
                ('reviewdate', models.DateField()),
                ('reviewtext', models.TextField()),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='club.product')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'db_table': 'review',
            },
        ),
        migrations.AddField(
            model_name='product',
            name='producttype',
            field=models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='club.techtype'),
        ),
        migrations.AddField(
            model_name='product',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to=settings.AUTH_USER_MODEL),
        ),
    ]
