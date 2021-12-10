from django import template
from webpages.views import article
from webpages.models import blogs


register = template.Library()

@register.inclusion_tag('article.html')
def bold(text,data):
    
    poll = blogs.objects.values('hyp_link','hyp_text')
    a="<a href= "+poll[data-1]['hyp_link']+" >"+poll[data-1]['hyp_text']+"</a>"
            
    text=text.replace(poll[data-1]['hyp_text'] ,a)
    text=text.replace('**','<strong>',1).replace('**','</strong>',1)
    text=text.replace('p^','<p>')
    text=text.replace('p^','</p>')
    text=text.replace('b^','<h2 style="font-size: 1.5em;font-weight: bold;">')
    text=text.replace('/^b','</h2>')
    text=text.replace('^^','<h3 style="font-size:1.17em;font-weight: bold;">')
    text=text.replace('/^*','</h3>')
    print(text)
    return text


# def bold(text,abc):
#     print(abc)
#     text=text.replace('**','<strong>',1).replace('**','</strong>',1)
    
#     text=text.replace('Ekal Shiksha',"<a href='http://www.ekalshiksha.in' >Read Article</a>")
    
#     return text
register.filter('bold', bold)