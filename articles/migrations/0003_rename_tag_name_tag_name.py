# Generated by Django 4.1.2 on 2022-10-30 11:35

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('articles', '0002_articletags_alter_article_options_tag_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='tag',
            old_name='tag_name',
            new_name='name',
        ),
    ]