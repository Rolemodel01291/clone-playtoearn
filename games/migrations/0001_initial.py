# Generated by Django 3.2.4 on 2021-06-30 06:34

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Game',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=255, verbose_name='name')),
                ('detail_link', models.CharField(max_length=255, null=True, verbose_name='detail_link')),
                ('profile_pic', models.CharField(max_length=255, null=True, verbose_name='profile_pic')),
                ('short_desc', models.CharField(max_length=255, null=True, verbose_name='short_desc')),
                ('genres', models.CharField(max_length=255, null=True, verbose_name='genres')),
                ('block_chains', models.CharField(max_length=255, null=True, verbose_name='block_chains')),
                ('devices', models.CharField(max_length=255, null=True, verbose_name='devices')),
                ('status', models.CharField(max_length=255, null=True, verbose_name='status')),
                ('nft', models.CharField(max_length=255, null=True, verbose_name='nft')),
                ('f2p', models.CharField(max_length=255, null=True, verbose_name='f2p')),
                ('p2e', models.CharField(max_length=255, null=True, verbose_name='p2e')),
                ('p2e_score', models.JSONField(null=True)),
                ('social_24h', models.CharField(max_length=255, null=True, verbose_name='social_24h')),
                ('social_7d', models.CharField(max_length=255, null=True, verbose_name='social_7d')),
                ('is_new', models.IntegerField(null=True)),
                ('description', models.CharField(max_length=255, null=True, verbose_name='description')),
                ('social_urls', models.JSONField(null=True)),
                ('p2e_score_data', models.JSONField(null=True)),
                ('supported_nfts', models.JSONField(null=True)),
                ('supported_tokens', models.JSONField(null=True)),
                ('app_images', models.JSONField(null=True)),
                ('app_video', models.CharField(max_length=255, null=True, verbose_name='app_video')),
                ('related_games', models.JSONField(null=True)),
                ('facebook_url', models.CharField(max_length=255, null=True, verbose_name='facebook_url')),
                ('twitter_url', models.CharField(max_length=255, null=True, verbose_name='twitter_url')),
                ('total_data', models.JSONField(null=True)),
                ('ethereum_data', models.JSONField(null=True)),
            ],
            options={
                'verbose_name': 'Game',
                'verbose_name_plural': 'Games',
                'db_table': 'games',
            },
        ),
        migrations.CreateModel(
            name='GameHistory',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('date', models.DateField(null=True)),
                ('user_id', models.IntegerField(null=True)),
                ('transactions', models.IntegerField(null=True)),
                ('volume', models.FloatField(null=True)),
                ('total_volume', models.FloatField(null=True)),
                ('game_id', models.ForeignKey(db_column='game_id', on_delete=django.db.models.deletion.CASCADE, to='games.game')),
            ],
            options={
                'verbose_name': 'GameHistory',
                'verbose_name_plural': 'GameHistory',
                'db_table': 'game_history',
            },
        ),
        migrations.CreateModel(
            name='GameContract',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('number', models.CharField(max_length=255, verbose_name='number')),
                ('game_id', models.ForeignKey(db_column='game_id', on_delete=django.db.models.deletion.CASCADE, to='games.game')),
            ],
            options={
                'verbose_name': 'GameContract',
                'verbose_name_plural': 'GameContracts',
                'db_table': 'game_contracts',
            },
        ),
    ]