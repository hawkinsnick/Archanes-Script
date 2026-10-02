import json,pathlib
R=pathlib.Path(__file__).parents[1]
def L(p): return json.loads((R/p).read_text())
def test_archanes_boundary():
 p=L('project.json'); x=L('research/pre-expert-maximum.json')
 assert p['canonical_records']==0 and x['target']=='PRE_EXPERT_MAXIMUM'
 assert any(i['id']=='ARC-HUM-001' for i in x['human_only_boundary'])
def test_release_assurance():
 for p in ['research/evidence-matrix.json','research/rights-register.json','research/corpus-definition-register.json','research/expert-review-packet.json','research/acquisition-queue.json']: L(p)
 assert L('research/corpus-definition-register.json')['project_consensus'] is None
 assert len(L('research/object-seed-register.json')['objects'])>=4
