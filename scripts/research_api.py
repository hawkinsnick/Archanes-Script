#!/usr/bin/env python3
import argparse,json,pathlib
R=pathlib.Path(__file__).resolve().parents[1];F={"objects":"research/decorte-2018-corpus-register.json","signary":"research/signary-authority-register.json","formula":"research/formula-register.json","disagreements":"research/disagreement-register.json","lineage":"research/source-lineage-register.json"}
def rows(k):
 v=json.loads((R/F[k]).read_text())
 for z in ("records","objects","authorities","sequences","items","lineages"):
  if isinstance(v.get(z),list):return v[z]
 return [v]
p=argparse.ArgumentParser();p.add_argument("resource",choices=F);p.add_argument("--text",default="");p.add_argument("--limit",type=int,default=50);a=p.parse_args();q=a.text.casefold();x=[v for v in rows(a.resource) if not q or q in json.dumps(v,ensure_ascii=False).casefold()][:a.limit];print(json.dumps({"resource":a.resource,"records":x,"boundary":"Authority-attributed evidence; no project consensus on script membership, sign identity or reading."},ensure_ascii=False,indent=2))
