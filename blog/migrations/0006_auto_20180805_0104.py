# Generated by Django 2.1 on 2018-08-04 16:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0005_auto_20180805_0040'),
    ]

    operations = [
        migrations.CreateModel(
            name='Tag',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, unique=True)),
            ],
        ),
        migrations.AddField(
            model_name='post',
            name='tag_set',
            field=models.ManyToManyField(to='blog.Tag'),
        ),
    ]
