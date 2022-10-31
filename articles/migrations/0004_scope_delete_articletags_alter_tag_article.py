# Generated by Django 4.1.2 on 2022-10-30 11:40

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('articles', '0003_rename_tag_name_tag_name'),
    ]

    operations = [
        migrations.CreateModel(
            name='Scope',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('is_main', models.BooleanField()),
                ('article', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='scopes', to='articles.article')),
                ('tag', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='scopes', to='articles.tag', verbose_name='Раздел')),
            ],
        ),
        migrations.DeleteModel(
            name='ArticleTags',
        ),
        migrations.AlterField(
            model_name='tag',
            name='article',
            field=models.ManyToManyField(related_name='tags', through='articles.Scope', to='articles.article'),
        ),
    ]