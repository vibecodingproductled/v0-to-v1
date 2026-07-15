#!/usr/bin/env bash
# Repo self-check: verify that relative markdown links and backticked
# references/*.md paths in skills resolve to real files. This applies the
# phantom-reference discipline (ai-harness-design anti-pattern #12) to the
# repo itself. Run in CI or as a pre-commit hook.
cd "$(dirname "$0")/.." || exit 1
python3 - << 'PY'
import os, re, sys, glob

fail = 0
files = glob.glob('skills/**/*.md', recursive=True) + ['README.md']

def strip_code(text):
    text = re.sub(r'```.*?```', '', text, flags=re.S)   # fenced blocks
    return text

for f in files:
    raw = open(f, encoding='utf-8').read()
    text = strip_code(raw)
    base = os.path.dirname(f)

    # Markdown links
    for m in re.finditer(r'\[[^\]]*\]\(([^)\s]+)\)', re.sub(r'`[^`]*`', '', text)):
        link = m.group(1)
        if link.startswith(('http', '#', 'mailto:')):
            continue
        target = os.path.normpath(os.path.join(base, link.split('#')[0]))
        if not os.path.exists(target):
            print(f'ERROR broken link: {f} -> {link}')
            fail = 1

    # Backticked references/*.md paths must resolve within the same skill
    if f.startswith('skills/'):
        skilldir = '/'.join(f.split('/')[:2])
        for m in re.finditer(r'`(references/[A-Za-z0-9._/\-]+\.md)`', text):
            ref = m.group(1)
            if not (os.path.exists(os.path.join(skilldir, ref))
                    or os.path.exists(os.path.join(base, ref))):
                print(f'ERROR phantom reference: {f} mentions `{ref}` '
                      f'but no such file exists in {skilldir}')
                fail = 1

if fail == 0:
    print('OK: all internal references resolve.')
sys.exit(fail)
PY
