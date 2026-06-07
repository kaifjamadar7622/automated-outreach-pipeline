import csv
from pathlib import Path


def export_contacts(contacts):

    if not contacts:
        return

    output_path = Path("output/contacts.csv")
    output_path.parent.mkdir(parents=True, exist_ok=True)

    fieldnames = list(contacts[0].keys())

    with output_path.open("w", newline="", encoding="utf-8") as csvfile:
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(contacts)

    print(f"Contacts exported to {output_path}")