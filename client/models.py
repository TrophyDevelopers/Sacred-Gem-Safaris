"""

from django.db import models

from wagtail import blocks
from wagtail.models import Page
from wagtail.fields import StreamField
from wagtail.admin.panels import FieldPanel
from wagtail.images.blocks import ImageChooserBlock



class ClientPage(Page):
    intro = models.CharField(max_length=250)
    main_image = models.ForeignKey(
        'wagtailimages.Image',
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name='+'
    )
    body = StreamField([
        ('rich_text', blocks.RichTextBlock(icon='doc-full', label='Rich Text')),
        ('html', blocks.RawHTMLBlock(icon='site', label='HTML')),
        ('image', ImageChooserBlock()),
    ])

    
    content_panels = Page.content_panels + [
        
        FieldPanel('intro'),
        FieldPanel('body')
    ]

    template = 'client/index.html'


class DestinationPage(Page):
    intro = models.CharField(max_length=250)
    main_image = models.ForeignKey(
        'wagtailimages.Image',
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name='+'
    )
    body = StreamField([
        ('rich_text', blocks.RichTextBlock(icon='doc-full', label='Rich Text')),
        ('html', blocks.RawHTMLBlock(icon='site', label='HTML')),
        ('image', ImageChooserBlock()),
    ])

    
    content_panels = Page.content_panels + [
        
        FieldPanel('intro'),
        FieldPanel('body')
    ]

    template = 'client/destination/destination.html'


class ExperiencePage(Page):
    intro = models.CharField(max_length=250)
    main_image = models.ForeignKey(
        'wagtailimages.Image',
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name='+'
    )
    body = StreamField([
        ('rich_text', blocks.RichTextBlock(icon='doc-full', label='Rich Text')),
        ('html', blocks.RawHTMLBlock(icon='site', label='HTML')),
        ('image', ImageChooserBlock()),
    ])

    
    content_panels = Page.content_panels + [
        
        FieldPanel('intro'),
        FieldPanel('body')
    ]

    template = 'client/experience/experience.html'



class FormPage(Page):
    intro = models.CharField(max_length=250)
    main_image = models.ForeignKey(
        'wagtailimages.Image',
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name='+'
    )
    body = StreamField([
        ('rich_text', blocks.RichTextBlock(icon='doc-full', label='Rich Text')),
        ('html', blocks.RawHTMLBlock(icon='site', label='HTML')),
        ('image', ImageChooserBlock()),
    ])

    
    content_panels = Page.content_panels + [
        
        FieldPanel('intro'),
        FieldPanel('body')
    ]

    template = 'client/form/form.html'



class CheckoutPage(Page):
    intro = models.CharField(max_length=250)
    main_image = models.ForeignKey(
        'wagtailimages.Image',
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name='+'
    )
    body = StreamField([
        ('rich_text', blocks.RichTextBlock(icon='doc-full', label='Rich Text')),
        ('html', blocks.RawHTMLBlock(icon='site', label='HTML')),
        ('image', ImageChooserBlock()),
    ])

    
    content_panels = Page.content_panels + [
        
        FieldPanel('intro'),
        FieldPanel('body')
    ]

    template = 'client/shop/checkout.html'



class BlogsPage(Page):
    intro = models.CharField(max_length=250)
    main_image = models.ForeignKey(
        'wagtailimages.Image',
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name='+'
    )
    body = StreamField([
        ('rich_text', blocks.RichTextBlock(icon='doc-full', label='Rich Text')),
        ('html', blocks.RawHTMLBlock(icon='site', label='HTML')),
        ('image', ImageChooserBlock()),
    ])

    
    content_panels = Page.content_panels + [
        
        FieldPanel('intro'),
        FieldPanel('body')
    ]

    template = 'client/blog/blog.html'



"""