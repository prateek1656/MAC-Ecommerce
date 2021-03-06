# Generated by Django 3.1.7 on 2021-10-09 11:54

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Blogpost',
            fields=[
                ('post_id', models.AutoField(primary_key=True, serialize=False)),
                ('title', models.CharField(default='', max_length=50)),
                ('head0', models.CharField(default='', max_length=50)),
                ('c_head0', models.CharField(default='', max_length=5000)),
                ('head1', models.CharField(default='', max_length=50)),
                ('c_head1', models.CharField(default='', max_length=5000)),
                ('head2', models.CharField(default='', max_length=50)),
                ('c_head2', models.CharField(default='', max_length=5000)),
                ('author_name', models.CharField(default='', max_length=50)),
                ('pub_date', models.DateField()),
                ('thumbnail', models.ImageField(default='', upload_to='shop/images')),
            ],
        ),
    ]
