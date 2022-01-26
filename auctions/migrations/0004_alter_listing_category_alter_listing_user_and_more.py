# Generated by Django 4.0 on 2022-01-24 18:01

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('auctions', '0003_rename_bids_bid_rename_comments_comment_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='listing',
            name='Category',
            field=models.CharField(blank=True, choices=[('Technology', 'Tech'), ('House Appliances', 'House'), ('Kitchen', 'Kitchen'), ('Sports Wear', 'Sport')], max_length=20),
        ),
        migrations.AlterField(
            model_name='listing',
            name='User',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='auctions.user'),
        ),
        migrations.CreateModel(
            name='User_Listing',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Listing', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='auctions.listing')),
                ('User', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='auctions.user')),
            ],
        ),
    ]
