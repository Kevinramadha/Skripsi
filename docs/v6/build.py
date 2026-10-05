import sys, os
sys.path.insert(0, '/tmp/pptwork/v5')
exec(open('/tmp/pptwork/v6/lamp_lib.py').read())
PARTS = sys.argv[1].split(',') if len(sys.argv) > 1 else ['A']
OUT = sys.argv[2] if len(sys.argv) > 2 else '/tmp/pptwork/v6/test.pptx'
prs = Presentation('/tmp/pptwork/v6/final_in.pptx')
D = Deck(prs, prs.slides[74])
for P in PARTS:
    exec(open(f'/tmp/pptwork/v6/part{P}.py').read())
FUNCS = [f.strip() for f in os.environ.get('FUNCS', '').split(',') if f.strip()]
for fn in FUNCS:
    globals()[fn](D)
n0 = len(prs.slides) - len(D.new)
prs.save(OUT)
print('new slides:', len(D.new), 'from index', n0 + 1)
