# Generated by Django 3.1.6 on 2021-02-12 13:34

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Produto',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, verbose_name='Nome do Produto:')),
                ('price', models.DecimalField(decimal_places=2, help_text='Ex.: 123.45', max_digits=9, verbose_name='Valor:')),
                ('image_url', models.ImageField(upload_to='', verbose_name='Imagem:')),
            ],
        ),
    ]