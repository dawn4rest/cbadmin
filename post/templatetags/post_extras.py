from django import template


register = template.Library()


@register.filter
def add_link(value):
    content = re.sub(r'\#'+tag.name+r'\b', '<a href="/post/explore/tags/'+tag.name+'">#'+tag.name+'</a>', content)
    return content # 원하는 문자열로 치환이 완료된 content를 리턴한다.


@register.filter
def split_tags(value):
    tags = []
    split_comma = value.split(',')

    for tag in split_comma:
        split_space = tag.split(" ")
        for tag in split_space:
            if tag:
                tags.append(tag)

    return tags
