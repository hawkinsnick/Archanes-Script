import json,pathlib
R=pathlib.Path(__file__).parents[1]
def L(p): return json.loads((R/p).read_text())
def test_archanes_boundary():
 p=L('project.json'); x=L('research/pre-expert-maximum.json')
 assert p['canonical_records']==0
 assert x['target']=='PRE_EXPERT_MAXIMUM'
 assert any(i['id']=='ARC-HUM-001' for i in x['human_only_boundary'])
