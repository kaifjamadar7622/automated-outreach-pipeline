from services.prospeo_service import ProspeoService


def main():

    service = ProspeoService()

    company_domain = input(
        "Enter company domain (example: openai.com): "
    ).strip()

    print("\nSearching contacts...")
    print("=" * 50)

    result = service.find_first_valid_email(
        company_domain
    )

    if result:

        print("\nCONTACT FOUND")
        print("=" * 50)

        print(f"Name     : {result['name']}")
        print(f"Role     : {result['title']}")
        print(f"Email    : {result['email']}")
        print(f"Person ID: {result['person_id']}")

    else:

        print("\nNo valid email found.")
        print(
            "Try another company domain or check your credits."
        )


if __name__ == "__main__":
    main()