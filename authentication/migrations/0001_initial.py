# Generated by Django 2.2.10 on 2021-09-20 17:11

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='business_details',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('category', models.CharField(max_length=100)),
                ('bank_name', models.CharField(max_length=50)),
                ('bsb', models.CharField(max_length=50)),
                ('business_name', models.CharField(max_length=50)),
                ('business_desc', models.CharField(max_length=200)),
                ('business_address', models.CharField(max_length=200)),
                ('email', models.EmailField(max_length=50)),
                ('Abin', models.CharField(max_length=50)),
                ('subcategory', models.CharField(max_length=50)),
                ('Account_holder', models.CharField(max_length=50)),
                ('account_number', models.CharField(max_length=50)),
                ('image1', models.ImageField(blank=True, null=True, upload_to='images')),
            ],
        ),
        migrations.CreateModel(
            name='mobile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sId', models.IntegerField()),
                ('phone', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='transactions',
            fields=[
                ('transactionId', models.AutoField(primary_key=True, serialize=False)),
                ('transactionName', models.CharField(max_length=500)),
            ],
        ),
    ]
