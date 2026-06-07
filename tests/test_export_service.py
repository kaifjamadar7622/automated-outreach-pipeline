import csv
from pathlib import Path

from services.export_service import export_contacts


def test_export_contacts_creates_csv(tmp_path, monkeypatch):
    # run from isolated temp dir so output/ is created there
    monkeypatch.chdir(tmp_path)

    contacts = [
        {"name": "Alice Example", "email": "alice@example.com"},
        {"name": "Bob Example", "email": "bob@example.com"},
    ]

    export_contacts(contacts)

    out = tmp_path / "output" / "contacts.csv"
    assert out.exists()

    # basic CSV content verification
    with out.open("r", encoding="utf-8") as f:
        reader = csv.DictReader(f)
        rows = list(reader)

    assert len(rows) == 2
    assert rows[0]["name"] == "Alice Example"
