# Generated by Django 3.2.4 on 2022-03-24 14:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('web', '0004_alter_flan_price'),
    ]

    operations = [
        migrations.CreateModel(
            name='Locales',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('comuna', models.CharField(max_length=64)),
                ('direccion', models.TextField()),
                ('telefono', models.CharField(max_length=64)),
                ('image_url', models.URLField()),
            ],
        ),
    ]
