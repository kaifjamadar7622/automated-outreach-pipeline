# services/approval_service.py

def approval_summary(contacts):

    print("\nSUMMARY")
    print("=" * 50)

    print(f"Contacts Found: {len(contacts)}")

    for c in contacts[:5]:
        print(
            f"{c['name']} | "
            f"{c['title']}"
        )

    choice = input(
        "\nProceed with outreach? (y/n): "
    )

    return choice.lower() == "y"