# Generated by Django 2.2 on 2020-11-03 04:14

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('toko', '0002_auto_20201030_0346'),
    ]

    operations = [
        migrations.CreateModel(
            name='Cate',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name_c', models.CharField(default='', max_length=30)),
                ('toko', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='kategori', to='toko.Toko')),
            ],
        ),
        migrations.CreateModel(
            name='Units',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.TextField(default='')),
            ],
        ),
        migrations.CreateModel(
            name='Prod',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('kode', models.CharField(max_length=10)),
                ('name', models.CharField(max_length=30)),
                ('price', models.PositiveIntegerField(default=0)),
                ('stok', models.PositiveSmallIntegerField(default=0)),
                ('image', models.TextField(default='')),
                ('cate', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='termasuk', to='products.Cate')),
                ('toko', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='products', to='toko.Toko')),
            ],
        ),
    ]
