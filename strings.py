"""Strings exercises"""


def html_tag(tag_name, **attributes):
   
    parts = " ".join([
        f'{param}="{value}"'
        for param, value in attributes.items()
    ])
    return f'<{tag_name} {parts}>'

   


def dollars(amount):
    """Format a number with a dollar sign and two decimal places."""
    return "${0:.2f}".format(amount)


def split_in_half(iterable):
    """Return two halves of the given iterable."""
    mid_point = int(len(iterable) / 2)
    return (iterable[:mid_point], iterable[mid_point:])

print(html_tag('p', id='intro', class_='basic', style='color:red'))