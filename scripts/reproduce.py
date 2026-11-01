from pathlib import Path
import argparse,csv,hashlib,json,shutil
r=Path(__file__).resolve().parents[1]
a=argparse.ArgumentParser();a.add_argument('target',nargs='?',default='all');a.add_argument('--out',required=True);args=a.parse_args()
out=Path(args.out).resolve();out.mkdir(parents=True,exist_ok=False)
def sha(p):return hashlib.sha256(p.read_bytes()).hexdigest()
if args.target=='all':
 for name in ['screening_ledger','report_decisions','study_appraisal','DOME_domains','SYRCLE_domains']:
  data=json.loads((r/'data/evidence/frozen_v8/inputs'/(name+'.json')).read_text(encoding='utf-8'))
  if isinstance(data,dict):data=data.get('records',data.get('rows',[]))
  keys=list(dict.fromkeys(k for row in data for k in row))
  with (out/(name+'.csv')).open('w',encoding='utf-8-sig',newline='') as f:
   w=csv.DictWriter(f,fieldnames=keys);w.writeheader()
   for row in data:w.writerow({k:json.dumps(v,ensure_ascii=False) if isinstance(v,(dict,list)) else v for k,v in row.items()})
 refs=json.loads((r/'data/evidence/references_v11.json').read_text(encoding='utf-8'))
 (out/'reference_index.txt').write_text('\n'.join(x['formatted'] for x in refs),encoding='utf-8')
 for p in (r/'table').glob('*.csv'):shutil.copy2(p,out/p.name)
for f in json.loads((r/'config/figures.json').read_text(encoding='utf-8')):
 if args.target not in ['all','figure'+str(f['figure'])]:continue
 src=r/f['file'];assert sha(src)==f['sha256'],src
 shutil.copy2(src,out/src.name)
report={p.name:sha(p) for p in out.iterdir() if p.is_file()}
(out/'replay_checksums.json').write_text(json.dumps(report,indent=2),encoding='utf-8')
print('Rebuilt',len(report),'evidence, table, reference and preserved-figure outputs.')
