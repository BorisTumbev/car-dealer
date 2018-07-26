from django.shortcuts import reverse
from django.utils.safestring import mark_safe
from django.forms import widgets
from django.conf import settings


class RelatedFieldWidgetCanAdd(widgets.Select):

    def __init__(self, related_model, related_url=None, *args, **kw):

        super().__init__(*args, **kw)

        if not related_url:
            rel_to = related_model
            info = (rel_to._meta.app_label, rel_to._meta.object_name.lower())
            related_url = 'admin:%s_%s_add' % info

        self.related_url = related_url

    def render(self, name, value, *args, **kwargs):
        self.related_url = reverse(self.related_url)
        output = [super().render(name, value, *args, **kwargs)]
        output.append('<a href="%s" class="add-another" >' % (self.related_url))
        output.append('<img src="%simages/plus.jpeg" width="15" height="15" alt="%s"/></a>' % (settings.MEDIA_URL, 'Add Another'))
        return mark_safe(''.join(output))