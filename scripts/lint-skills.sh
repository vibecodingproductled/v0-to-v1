#!/usr/bin/env bash
# Skill linter: validate every skills/*/SKILL.md against the Agent Skills
# contract. Malformed frontmatter fails silently in Claude Code (the skill
# just never loads), so this check is the only place the failure is visible.
# Run in CI or locally before committing a skill.
cd "$(dirname "$0")/.." || exit 1
python3 - << 'PY'
import os, re, sys, glob

try:
    import yaml  # preinstalled on GitHub runners; optional locally
except ImportError:
    yaml = None
    print('NOTE: PyYAML not available; skipping strict YAML parse '
          '(pip install pyyaml for the full check)')

fail = 0
def err(skill, msg):
    global fail
    print(f'ERROR [{skill}]: {msg}')
    fail = 1

skill_dirs = sorted(d for d in glob.glob('skills/*/') if os.path.isdir(d))
if not skill_dirs:
    err('repo', 'no skills/*/ directories found')

for d in skill_dirs:
    skill = os.path.basename(d.rstrip('/'))
    path = os.path.join(d, 'SKILL.md')

    # Every skill folder must contain a SKILL.md
    if not os.path.exists(path):
        err(skill, 'missing SKILL.md')
        continue

    raw = open(path, encoding='utf-8').read()
    lines = raw.splitlines()

    # Frontmatter must open on line 1 and close before EOF
    if not lines or lines[0].strip() != '---':
        err(skill, 'SKILL.md must start with `---` YAML frontmatter on line 1')
        continue
    try:
        end = next(i for i, l in enumerate(lines[1:], 1) if l.strip() == '---')
    except StopIteration:
        err(skill, 'frontmatter never closed (no second `---`)')
        continue
    fm = '\n'.join(lines[1:end])
    body = lines[end + 1:]

    # Frontmatter must be VALID YAML, not just look like it. A plain
    # (unquoted) scalar containing ": " -- e.g.
    #   description: Covers the full architecture: CLAUDE.md, rules, ...
    # is a YAML syntax error, and a strict parser will reject the whole
    # frontmatter, so the skill silently never loads.
    if yaml is not None:
        try:
            parsed = yaml.safe_load(fm)
            if not isinstance(parsed, dict):
                err(skill, 'frontmatter does not parse to a YAML mapping')
        except yaml.YAMLError as e:
            err(skill, f'frontmatter is not valid YAML: {str(e).splitlines()[0]}')
    else:
        # Fallback heuristic: a single-line unquoted description with a
        # colon-space in its value is the common way this breaks.
        m = re.search(r'^description:\s+([^>|"\'].*:\s.*)$', fm, re.M)
        if m:
            err(skill, 'single-line `description` contains ": " -- invalid as a '
                       'plain YAML scalar; use a block scalar (`description: >-`) '
                       'or quote the value')

    # name: required, must match the folder, lowercase-hyphen only.
    # A mismatch means the skill installs under one name but announces
    # another, so explicit invocation breaks.
    m = re.search(r'^name:\s*(.+)$', fm, re.M)
    if not m:
        err(skill, 'frontmatter missing `name`')
    else:
        name = m.group(1).strip().strip('"\'')
        if name != skill:
            err(skill, f'`name: {name}` does not match folder name `{skill}`')
        if not re.fullmatch(r'[a-z0-9]+(-[a-z0-9]+)*', name):
            err(skill, f'`name: {name}` must be lowercase letters/digits/hyphens')

    # description: required, non-empty, <=1024 chars, no XML/angle brackets.
    # This text is injected into the system prompt; it is the ONLY thing the
    # model sees when deciding whether to load the skill.
    m = re.search(r'^description:\s*(.*)$', fm, re.M)
    if not m:
        err(skill, 'frontmatter missing `description`')
    else:
        desc = m.group(1).strip()
        if desc in ('|', '>', '|-', '>-', ''):
            # block scalar: collect the indented continuation lines
            start = fm.splitlines().index(m.group(0))
            block = []
            for l in fm.splitlines()[start + 1:]:
                if l.startswith((' ', '\t')) or l.strip() == '':
                    block.append(l.strip())
                else:
                    break
            desc = ' '.join(b for b in block if b)
        if not desc:
            err(skill, '`description` is empty')
        if len(desc) > 1024:
            err(skill, f'`description` is {len(desc)} chars (max 1024)')
        if re.search(r'<[^>]+>', desc):
            err(skill, '`description` contains angle brackets / XML tags')

    # Body <500 lines: beyond that, move depth into references/ so the
    # always-loaded core stays cheap (progressive disclosure).
    if len(body) > 500:
        err(skill, f'SKILL.md body is {len(body)} lines (keep under 500; '
                   f'move depth into references/)')

if fail == 0:
    print(f'OK: {len(skill_dirs)} skills pass lint.')
sys.exit(fail)
PY
