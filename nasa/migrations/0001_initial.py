# Generated by Django 4.1 on 2023-06-26 07:35

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import filer.fields.file
import filer.fields.image


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('filer', '0015_alter_file_owner_alter_file_polymorphic_ctype_and_more'),
        migrations.swappable_dependency(settings.FILER_IMAGE_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Images',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255)),
                ('cover', filer.fields.image.FilerImageField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='image_covers', to=settings.FILER_IMAGE_MODEL)),
                ('disclaimer', filer.fields.file.FilerFileField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='image_covers_disclaimer', to='filer.file')),
            ],
        ),
        migrations.CreateModel(
            name='SliderImages',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('my_order', models.PositiveIntegerField(default=0)),
                ('image', filer.fields.image.FilerImageField(on_delete=django.db.models.deletion.CASCADE, related_name='slider_images', to=settings.FILER_IMAGE_MODEL, verbose_name='Изображение')),
                ('title', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='images', to='nasa.images', verbose_name='Слайдер')),
            ],
            options={
                'ordering': ['my_order'],
            },
        ),
    ]
