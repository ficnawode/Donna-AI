from donna_candidate import DonnaCandidate
from forms_caller import FormsCaller

company_reqs = '''
A person who is good at coordinating large projects, excells at teamwork and has at least some programming experience
'''


def test_evaluate():
    form_id = '1fbog0GLT9gmdGR09MVUy13ZamgeSFr72sHioOoAi-BI'
    fc = FormsCaller(form_id)
    dc = DonnaCandidate(fc.get_qa()[0], company_reqs)
    assert dc.code_qa[0] != ''
    assert dc.utest_qa[0] != ''
    dc.evaluate()
    soft_score = dc.soft_skill_rating
    print(dc)
    assert dc.full_name != ''
    assert dc.email != ''
    assert dc.phone_number != ''
    assert dc.soft_skill_rating != -1
    assert dc.code_check != ''
    assert dc.code_rating != -1
    assert dc.unit_test_rating != ''
    assert dc.total_rating != -1
    assert dc.cv != ''
    assert soft_score > 0 and soft_score <= 100


def test_serialize():
    form_id = '1fbog0GLT9gmdGR09MVUy13ZamgeSFr72sHioOoAi-BI'
    fc = FormsCaller(form_id)
    dc = DonnaCandidate(fc.get_qa()[0], company_reqs)
    dc.evaluate()
    print(dc)
    dc_recreated = DonnaCandidate.from_dict(dc.to_dict(), company_reqs)
    assert dc_recreated.full_name != ''
    assert dc_recreated.email != ''
    assert dc_recreated.phone_number != ''
    assert dc_recreated.soft_skill_rating != -1
    assert dc_recreated.code_check != ''
    assert dc_recreated.code_rating != -1
    assert dc_recreated.unit_test_rating != ''
    assert dc_recreated.total_rating != -1
    assert dc_recreated.cv != ''
