import json

from services.prospeo_service import ProspeoService


class DummyResponse:
    def __init__(self, payload):
        self._payload = payload

    def raise_for_status(self):
        return None

    def json(self):
        return self._payload


def test_search_people_calls_api(monkeypatch):
    payload = {"results": [{"person": {"full_name": "Test User"}}]}

    def fake_post(*args, **kwargs):
        return DummyResponse(payload)

    # patch requests.post used inside the service
    monkeypatch.setattr("services.prospeo_service.requests.post", fake_post)
    # ensure API key is provided via config
    monkeypatch.setattr("services.prospeo_service.get_env_var", lambda n: "dummy")

    svc = ProspeoService()
    res = svc.search_people("example.com")

    assert res == payload


def test_enrich_person_returns_json(monkeypatch):
    payload = {"person": {"email": "x@example.com"}}

    def fake_post(*args, **kwargs):
        return DummyResponse(payload)

    monkeypatch.setattr("services.prospeo_service.requests.post", fake_post)
    monkeypatch.setattr("services.prospeo_service.get_env_var", lambda n: "dummy")

    svc = ProspeoService()
    res = svc.enrich_person("personid")

    assert res == payload
