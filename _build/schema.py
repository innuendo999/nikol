"""JSON-LD helpers. Existing structured data from the old pages is reused (it was already rich);
new pages get WebPage + BreadcrumbList + Service + FAQPage that reference the same business/person @ids."""
import json, os, re
from lib import ROOT, SITE, CAL

BUSINESS = {'@id': SITE + '/#business'}
PERSON = {'@id': SITE + '/#person'}


def load(name):
    data = json.load(open(os.path.join(ROOT, '_build', 'schema', name + '.json'), encoding='utf-8'))
    return [patch(d) for d in data]


def strip(html):
    return re.sub(r'\s+', ' ', re.sub(r'<[^>]+>', '', html)).replace('&amp;', '&').strip()


def patch(obj):
    """Normalise legacy data: one domain, correct Calendly link, x-default free."""
    s = json.dumps(obj, ensure_ascii=False)
    s = s.replace('https://nikol.makeup', SITE)
    return json.loads(s)


def breadcrumb(path, items):
    return {'@type': 'BreadcrumbList', '@id': SITE + path + '#breadcrumb', 'itemListElement': [
        {'@type': 'ListItem', 'position': i + 1, 'name': n, 'item': SITE + h} for i, (n, h) in enumerate(items)]}


def faq(path, lang, items):
    return {'@type': 'FAQPage', '@id': SITE + path + '#faq', 'inLanguage': lang, 'mainEntity': [
        {'@type': 'Question', 'name': strip(q), 'acceptedAnswer': {'@type': 'Answer', 'text': strip(a)}} for q, a in items]}


def service_page(lang, path, title, desc, service_name, service_type, image, crumb_items, faq_items, offers=None):
    graph = [
        {'@type': 'WebPage', '@id': SITE + path + '#webpage', 'url': SITE + path, 'name': title, 'description': desc,
         'inLanguage': lang, 'isPartOf': {'@id': SITE + '/#website'}, 'about': {'@id': SITE + path + '#service'},
         'breadcrumb': {'@id': SITE + path + '#breadcrumb'}, 'primaryImageOfPage': SITE + image},
        {'@type': 'Service', '@id': SITE + path + '#service', 'name': service_name, 'serviceType': service_type,
         'description': desc, 'url': SITE + path, 'image': SITE + image, 'provider': BUSINESS,
         'areaServed': [{'@type': 'City', 'name': 'Praha' if lang == 'cs' else 'Prague'},
                        {'@type': 'Country', 'name': 'Česká republika' if lang == 'cs' else 'Czech Republic'}],
         'availableLanguage': ['cs', 'en', 'uk'],
         'potentialAction': {'@type': 'ReserveAction', 'target': {'@type': 'EntryPoint', 'urlTemplate': CAL}},
         **({'hasOfferCatalog': {'@type': 'OfferCatalog', 'name': service_name, 'itemListElement': [
             {'@type': 'Offer', 'itemOffered': {'@type': 'Service', 'name': o}} for o in offers]}} if offers else {})},
        breadcrumb(path, crumb_items),
        faq(path, lang, faq_items),
    ]
    return [{'@context': 'https://schema.org', '@graph': graph}]
