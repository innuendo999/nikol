"""Inline style declarations used in templates, mapped to named utility classes.
build.py appends these rules to site.css; lib.write() swaps style="" for the class."""
import re

U = {
    'display:flex;gap:12px;flex-wrap:wrap': 'actions',
    'display:flex;flex-wrap:wrap;gap:10px': 'actions-sm',
    'display:flex;flex-wrap:wrap;gap:10px;list-style:none;padding:0': 'actions-sm list-reset',
    'display:flex;gap:18px;flex-wrap:wrap': 'meta-row',
    'display:flex;gap:14px;flex-wrap:wrap': 'meta-row-sm',
    'align-self:flex-start': 'self-start',
    'align-items:end': 'items-end',
    'display:flex;flex-direction:column;gap:18px': 'stack-18',
    'display:flex;flex-direction:column;gap:20px': 'stack-20',
    'display:flex;flex-direction:column;gap:22px': 'stack-22',
    'display:flex;flex-direction:column;gap:24px': 'stack-24',
    'display:flex;flex-direction:column;gap:28px': 'stack-28',
    'display:flex;flex-direction:column;gap:48px': 'stack-48',
    'display:flex;justify-content:space-between;gap:16px;align-items:baseline': 'row-between',
    'display:flex;align-items:center;gap:14px': 'byline',
    'display:flex;justify-content:space-between;align-items:center;gap:24px;flex-wrap:wrap;border-top:1px solid var(--ink);padding-top:20px': 'byline-bar',
    'flex-direction:row;flex-wrap:wrap;justify-content:space-between;align-items:center;gap:20px': 'note--row',
    'flex:1 1 300px;display:flex;flex-direction:column;gap:6px': 'author-body',
    'background:var(--ox);color:var(--paper);padding:44px;display:flex;flex-direction:column;gap:18px;margin-top:24px': 'cta-box',
    'margin:0;padding:0;border:0;color:var(--paper)': 'cta-box__title',
    'display:block': 'd-block',
    'height:100%': 'h-full',
    'height:100%;min-height:420px': 'h-full min-h-420',
    'min-height:60vh': 'min-h-60vh',
    'grid-template-columns:repeat(auto-fit,minmax(min(100%,260px),1fr))': 'cards-auto',
    'object-position:50% 15%': 'fp-15',
    'object-position:50% 20%': 'fp-20',
    'object-position:50% 25%': 'fp-25',
    'object-position:50% 30%': 'fp-30',
    'object-position:60% 30%': 'fp-60-30',
    'width:52px;height:52px;border-radius:50%;object-fit:cover;object-position:50% 20%': 'avatar',
    'width:220px': 'w-220',
    'max-width:460px': 'mw-460',
    'max-width:480px': 'mw-480',
    'max-width:640px': 'mw-640',
    'max-width:1180px': 'mw-1180',
    'margin:0': 'm-0',
    'margin-top:8px': 'mt-8',
    'margin-top:16px': 'mt-16',
    'padding-bottom:48px': 'pb-48',
    'border-top:1px solid var(--ink)': 'bt-ink',
    'border-top:0': 'bt-0',
    'color:#fff': 'c-white',
    'color:var(--text)': 'c-text',
    'color:var(--ox)': 'c-ox',
    'font-size:15px;color:var(--muted2)': 'fine-print',
    'font-size:15px;line-height:1.7': 'small-copy',
    'font-size:15px;font-weight:600': 'cap-title',
    'font-size:16px': 'fs-16',
    'font-size:18px': 'fs-18',
    'font-size:18px;font-weight:600': 'note-title',
    'font-size:20px': 'fs-20',
    'font-size:20px;font-weight:600': 'author-name',
    'font-size:20px;color:#E9DCD8': 'lead-on-dark',
    'font-size:20px;color:#F4D6CF': 'lead-on-ox',
    'font-size:24px;font-weight:500': 'title-24',
    'font-size:28px': 'fs-28',
    'font-size:30px': 'fs-30',
    'font-size:30px;font-weight:500;line-height:1.1': 'feat-title',
    'font-size:clamp(22px,2.2vw,28px);line-height:1.2': 'lead-fluid',
    'font-size:clamp(24px,2.4vw,30px);line-height:1.15': 'mos-title',
    'font-size:clamp(24px,2.6vw,34px)': 'cap-fluid',
    'font-size:clamp(34px,9vw,150px)': 'h1-404',
}

def css():
    # !important mirrors the precedence the inline styles had over component rules
    imp = lambda d: ';'.join(x + '!important' for x in d.split(';'))
    out = [f'.{c}{{{imp(d)}}}' for d, c in U.items() if ' ' not in c]
    out += ['.list-reset{list-style:none!important;padding:0!important}', '.min-h-420{min-height:420px!important}']
    return '\n'.join(out) + '\n'


TAG = re.compile(r'<([a-zA-Z][a-zA-Z0-9]*)([^<>]*?)\sstyle="([^"]*)"([^<>]*)>')


def apply(html):
    def repl(m):
        tag, before, style, after = m.groups()
        if style not in U:
            raise ValueError('unmapped inline style: ' + style)
        cls = U[style]
        attrs = before + after
        cm = re.search(r'\sclass="([^"]*)"', attrs)
        if cm:
            attrs = attrs.replace(cm.group(0), f' class="{cm.group(1)} {cls}"', 1)
        else:
            attrs = f' class="{cls}"' + attrs
        return f'<{tag}{attrs}>'
    prev = None
    while prev != html:
        prev, html = html, TAG.sub(repl, html)
    return html
