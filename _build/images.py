"""Generate responsive WebP variants into /assets/img. Run: python3 _build/images.py"""
import json, os
from PIL import Image
ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
OUT = os.path.join(ROOT, 'assets', 'img')
os.makedirs(OUT, exist_ok=True)
SRC = {
  'nikol-hero': ('img/nikol.jpg', [640, 1280]),
  'nikol-portrait': ('img/nikol-pavlova.jpg', [400, 800]),
  'nikol-header': ('img/nikol-header.webp', [400, 800]),
  'nikol-footer': ('img/nikol-footer.webp', [800, 1080]),
  'contact': ('img/portfolio/commercial-2-min.jpg', [800, 1600]),
  'wedding-prague': ('img/wedding/wedding-prague-1.png', [800, 1200]),
  'course': ('img/courses/IMG_7417.jpg', [600, 1000, 1400]),
}
for i in range(1, 16): SRC[f'wedding-{i}'] = (f'img/wedding/wedding-{i}.png', [400, 800])
for i in range(1, 18): SRC[f'evening-{i}'] = (f'img/evening/evening-{i}.png', [400, 800])
for i in range(1, 4): SRC[f'nude-{i}'] = (f'img/nude/nude-{i}.png', [400, 800])
for i in range(1, 7): SRC[f'commercial-{i}'] = (f'img/commercial/commercial-{i}.png', [400, 800])
meta = {}
for name, (src, widths) in SRC.items():
    im = Image.open(os.path.join(ROOT, src)).convert('RGB')
    W, H = im.size
    out = []
    for w in widths:
        w = min(w, W)
        h = round(H * w / W)
        fn = f'{name}-{w}.webp'
        p = os.path.join(OUT, fn)
        if not os.path.exists(p):
            im.resize((w, h), Image.LANCZOS).save(p, 'WEBP', quality=78, method=6)
        out.append([w, h])
    meta[name] = out
sig = Image.open(os.path.join(ROOT, 'img/services/signature3.png')).convert('RGBA')
for w in (440, 872):
    p = os.path.join(OUT, f'signature-{w}.webp')
    if not os.path.exists(p):
        sig.resize((w, round(sig.size[1] * w / sig.size[0])), Image.LANCZOS).save(p, 'WEBP', quality=85, method=6)
meta['signature'] = [[440, round(263*440/872)], [872, 263]]
json.dump(meta, open(os.path.join(ROOT, '_build', 'images.json'), 'w'), indent=0)
print(len(meta), 'images')
