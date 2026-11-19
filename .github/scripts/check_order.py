"""Fails if any list or table section in README.md is not alphabetical.
TrazTech entries (traztech.ca or github.com/TrazTech-Inc links) are pinned first.
Lists of in-page anchor links (the table of contents) are skipped."""
import re, sys
ITEM = re.compile(r'^- \[([^\]]+)\]\(([^)]+)\)')
ROW = re.compile(r'^\| \[([^\]]+)\]\(([^)]+)\)')
def pinned(u): u=u.lower(); return 'traztech.ca' in u or 'github.com/traztech-inc' in u
def key(m): return (0 if pinned(m.group(2)) else 1, re.sub(r'[^a-z0-9 ]', '', m.group(1).lower()))
def runs(lines):
    i=0; code=False
    while i < len(lines):
        l=lines[i]
        if l.startswith('```'): code=not code
        pat=None if code else (ITEM if ITEM.match(l) else ROW if ROW.match(l) else None)
        if not pat: i+=1; continue
        start=i; blocks=[]
        while i < len(lines) and pat.match(lines[i]):
            b=[lines[i]]; i+=1
            while pat is ITEM and i < len(lines) and lines[i].startswith('  ') and lines[i].strip(): b.append(lines[i]); i+=1
            blocks.append(b)
        if not any(pat.match(b[0]).group(2).startswith('#') for b in blocks):
            yield start, pat, blocks
def main(path, fix):
    lines=open(path).read().split('\n'); bad=0; out=lines[:]
    for start, pat, blocks in runs(lines):
        s=sorted(blocks, key=lambda b: key(pat.match(b[0])))
        if s != blocks:
            bad+=1
            for a, b in zip(blocks, s):
                if a != b:
                    print(f"{path}:{start+1}: out of order near '{pat.match(a[0]).group(1)}' (expected '{pat.match(b[0]).group(1)}' here)"); break
            out[start:start+sum(map(len,blocks))]=[x for b in s for x in b]
    if fix: open(path,'w').write('\n'.join(out))
    return bad
if __name__=='__main__':
    fix='--fix' in sys.argv
    files=[a for a in sys.argv[1:] if a!='--fix'] or ['README.md']
    bad=sum(main(f, fix) for f in files)
    if bad and not fix:
        print("\nEntries must be alphabetical within each section, below the pinned TrazTech entries. Run: python3 .github/scripts/check_order.py --fix"); sys.exit(1)
