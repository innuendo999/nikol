"""JSON-LD helpers. Existing structured data from the old pages is reused (it was already rich);
new pages get WebPage + BreadcrumbList + Service + FAQPage that reference the same business/person @ids."""
import json, os, re
from lib import ROOT, SITE, CAL, GBP, IG, FB, TH

YT = 'https://www.youtube.com/@nikolpavlova_mua'

BUSINESS = {'@id': SITE + '/#business'}
PERSON = {'@id': SITE + '/#person'}


def load(name):
    data = json.load(open(os.path.join(ROOT, '_build', 'schema', name + '.json'), encoding='utf-8'))
    return [patch(d) for d in data]


def strip(html):
    return re.sub(r'\s+', ' ', re.sub(r'<[^>]+>', '', html)).replace('&amp;', '&').strip()


BUSINESS_NAME = 'Vizážistka Nikol Pavlova'          # exactly as on the Google Business Profile
ALT_NAMES = ['Nikol Pavlova – vizážistka Praha', 'Nikol Pavlova – makeup artist Prague', 'Nikol Pavlova MUA']
SAME_AS = [GBP, IG, FB, TH, YT]
PERSON_SAME_AS = [IG, FB, TH, YT]


def patch(obj):
    """Normalise legacy data: one domain, one business entity, consistent NAP and sameAs."""
    s = json.dumps(obj, ensure_ascii=False)
    s = s.replace('https://nikol.makeup', SITE).replace(SITE + '/en/#business', SITE + '/#business')
    return _fix(json.loads(s))


def _fix(node):
    if isinstance(node, list):
        return [_fix(n) for n in node]
    if not isinstance(node, dict):
        return node
    node = {k: _fix(v) for k, v in node.items()}
    if node.get('@type') == 'PostalAddress':
        cs = node.get('addressLocality') == 'Praha'
        node = {'@type': 'PostalAddress', 'streetAddress': 'Prvního pluku 8a', 'postalCode': '180 00',
                'addressLocality': 'Praha' if cs else 'Prague', 'addressRegion': 'Praha' if cs else 'Prague',
                'addressCountry': 'CZ'}
    if node.get('@type') == 'GeoCoordinates':
        node = {'@type': 'GeoCoordinates', 'latitude': 50.092, 'longitude': 14.439}
    if node.get('@id') == SITE + '/#business' and len(node) > 1:
        node['name'] = BUSINESS_NAME
        node['alternateName'] = ALT_NAMES
        node['sameAs'] = SAME_AS
        node['hasMap'] = GBP
    if node.get('@id') == SITE + '/#person' and len(node) > 1:
        node['sameAs'] = PERSON_SAME_AS
        node['worksFor'] = BUSINESS
    return node


def breadcrumb(path, items):
    return {'@type': 'BreadcrumbList', '@id': SITE + path + '#breadcrumb', 'itemListElement': [
        {'@type': 'ListItem', 'position': i + 1, 'name': n, 'item': SITE + h} for i, (n, h) in enumerate(items)]}


def faq(path, lang, items):
    return {'@type': 'FAQPage', '@id': SITE + path + '#faq', 'inLanguage': lang, 'mainEntity': [
        {'@type': 'Question', 'name': strip(q), 'acceptedAnswer': {'@type': 'Answer', 'text': strip(a)}} for q, a in items]}


def offer(o):
    """o: a service name, or (name, price in CZK) for a fixed price."""
    if isinstance(o, tuple):
        name, price = o
        return {'@type': 'Offer', 'itemOffered': {'@type': 'Service', 'name': name},
                'price': str(price), 'priceCurrency': 'CZK'}
    return {'@type': 'Offer', 'itemOffered': {'@type': 'Service', 'name': o}}


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
             offer(o) for o in offers]}} if offers else {})},
        breadcrumb(path, crumb_items),
        faq(path, lang, faq_items),
    ]
    return [{'@context': 'https://schema.org', '@graph': graph}]


def person(lang):
    """The one Person node every page uses: same @id, sameAs and employer everywhere."""
    return {'@type': 'Person', '@id': SITE + '/#person', 'name': 'Nikol Pavlova',
            'jobTitle': 'Vizážistka' if lang == 'cs' else 'Makeup artist',
            'image': SITE + '/img/nikol.jpg', 'url': SITE + ('/' if lang == 'cs' else '/en/'),
            'worksFor': BUSINESS, 'knowsLanguage': ['cs', 'en', 'uk'], 'sameAs': PERSON_SAME_AS}


def business_ref(lang):
    """Compact business node for pages that do not carry the full LocalBusiness block,
    so publisher/worksFor resolve on the page itself (same @id as the home page)."""
    return {'@type': ['LocalBusiness', 'BeautySalon'], '@id': SITE + '/#business', 'name': BUSINESS_NAME,
            'url': SITE + '/', 'telephone': '+420608178390', 'image': SITE + '/img/nikol.jpg',
            'address': {'@type': 'PostalAddress', 'streetAddress': 'Prvního pluku 8a', 'postalCode': '180 00',
                        'addressLocality': 'Praha' if lang == 'cs' else 'Prague', 'addressCountry': 'CZ'},
            'hasMap': GBP, 'founder': PERSON, 'sameAs': SAME_AS}
