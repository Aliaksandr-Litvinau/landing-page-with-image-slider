from django.shortcuts import render

from nasa.models import Images, SliderImages


def get_home_page(request):
    images_slider = Images.objects.all()
    all_images = list()
    for image in images_slider:
        image_sl = SliderImages.objects.all().filter(title=image)
        images = [img.image.url for img in image_sl]
        image_id = '{}_{}'.format(image.title, image.id)
        nav_image_id = 'nav_{}_{}'.format(image.title, image.id)
        if image.cover:
            cover = 'url("{}")'.format(image.cover.url)
        else:
            cover = '#507D2A'
        data_image = {
            'title': image.title,
            'cover': cover,
            'image_id': image_id,
            'nav_image_id': nav_image_id,
            'images': images

        }
        all_images.append(data_image)

    return render(request, 'nasa/home.html', {'imgs': all_images})
