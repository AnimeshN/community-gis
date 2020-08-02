from django.db import models

from wagtail.core.models import Page
from wagtail.core.fields import RichTextField
from wagtail.admin.edit_handlers import FieldPanel
from wagtail.images.edit_handlers import ImageChooserPanel


class FgisCMSPage(Page):
    description= RichTextField(features=["bold","italic","link","images","ol","ul","document-link","link","image","embed"],blank=True)
    background_image= models.ForeignKey(
    		"wagtailimages.Image",
    		null=True,
    		blank=True,
    		on_delete=models.SET_NULL,
    		related_name="+"
   	)
    resources = RichTextField(blank=True)
    content_panels = Page.content_panels + [
    	 FieldPanel("title"),
         FieldPanel('resources', classname="full"),
    	 FieldPanel("description",classname='full'),
    	 ImageChooserPanel("background_image"),
    ]

    class Meta:
    	verbose_name = "Theme Page"
    	verbose_name_plural = "Theme Pages"