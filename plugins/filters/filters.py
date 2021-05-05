from datetime import datetime

__all__ = ["parsedate", "formatdate", "categories_dict"]

def parsedate(value, formatstring='%Y-%m-%d %H:%M%z'):
    return datetime.strptime(value, formatstring)

def formatdate(value, formatstring='%b %-d %Y, %H:%M %Z'):
    return datetime.strftime(value, formatstring)

def categories_dict(value):
    return {c[0].name: c[1] for c in value}
        
