from celery import shared_task
from django.conf import settings
from scrapers.scraper_fii import ScraperFii
from fiis.models import Fii


    

@shared_task
def get_data_fiis():
    scraper = ScraperFii()
    
    urls = scraper.get_urls()
    for url in urls:
        name_fii = url.split('/')[-2].lower()
        data_fii = scraper.scrap_page(url)
        
        fii = Fii.objects.filter(name=name_fii)
        if not fii:
            Fii.objects.create(
                name=url.split('/')[-2],
                **data_fii
            )
        else:
            fii.update(
                **data_fii
            )
        