from django.db import models
from filer.fields.file import FilerFileField
from filer.fields.image import FilerImageField


class Images(models.Model):
    title = models.CharField(max_length=255)
    cover = FilerImageField(related_name="image_covers", null=True, blank=True, on_delete=models.CASCADE)
    disclaimer = FilerFileField(null=True, blank=True, related_name="image_covers_disclaimer", on_delete=models.CASCADE)

    def __str__(self):
        return self.title


class SliderImages(models.Model):
    title = models.ForeignKey(Images, verbose_name='Слайдер', on_delete=models.CASCADE, related_name='images')
    my_order = models.PositiveIntegerField(default=0, blank=False, null=False)
    image = FilerImageField(verbose_name='Изображение', on_delete=models.CASCADE, related_name='slider_images')

    class Meta:
        ordering = ['my_order']
