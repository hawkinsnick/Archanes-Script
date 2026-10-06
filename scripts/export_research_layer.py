#!/usr/bin/env python3
import argparse,json,pathlib
R=pathlib.Path(__file__).resolve().parents[1];p=argparse.ArgumentParser();p.add_argument("output");a=p.parse_args();d=json.loads((R/"research/decorte-2018-corpus-register.json").read_text());out=pathlib.Path(a.output);out.write_text(json.dumps(d["records"],ensure_ascii=False,indent=2)+"\n");out.with_suffix(out.suffix+".manifest.json").write_text(json.dumps({"records":16,"authority":"Decorte 2018","consensus_corpus":False,"rights":"Structured publication-derived assertions; component image/drawing rights remain separate."},indent=2)+"\n")
