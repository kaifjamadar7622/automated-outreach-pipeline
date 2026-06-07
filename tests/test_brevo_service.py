from services.brevo_service import BrevoService


class DummyResponse:
    def __init__(self, payload):
        self._payload = payload

    def json(self):
        return self._payload


def test_send_email_monkeypatched(monkeypatch):
    expected = {"messageId": "123"}

    def fake_post(*args, **kwargs):
        return DummyResponse(expected)

    monkeypatch.setattr("services.brevo_service.requests.post", fake_post)
    monkeypatch.setattr("services.brevo_service.get_env_var", lambda n: "dummy")

    svc = BrevoService()
    res = svc.send_email("a@b.com", "A", "subj", "<p>hi</p>")

    assert res == expected
