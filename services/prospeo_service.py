import requests
from services.export_service import export_contacts
from services.config import get_env_var


# Load API key via centralized config loader (raises if missing)
API_KEY = get_env_var("PROSPEO_API_KEY")


class ProspeoService:

    def __init__(self):
        self.api_key = API_KEY
        self.base_url = "https://api.prospeo.io"

        self.headers = {
            "X-KEY": self.api_key,
            "Content-Type": "application/json"
        }

    def search_people(self, company_domain):

        url = f"{self.base_url}/search-person"

        payload = {
            "page": 1,
            "filters": {
                "company": {
                    "websites": {
                        "include": [company_domain]
                    }
                }
            }
        }

        try:
            response = requests.post(
                url,
                headers=self.headers,
                json=payload,
                timeout=30
            )

            response.raise_for_status()
            return response.json()

        except Exception as e:
            print(f"Search Error: {e}")
            return None

    def enrich_person(self, person_id):

        url = f"{self.base_url}/enrich-person"

        payload = {
            "data": {
                "person_id": person_id
            }
        }

        try:
            response = requests.post(
                url,
                headers=self.headers,
                json=payload,
                timeout=30
            )

            return response.json()

        except Exception as e:
            print(f"Enrichment Error: {e}")
            return None

    def find_first_valid_email(self, company_domain):

        search_result = self.search_people(company_domain)

        if not search_result:
            return None

        results = search_result.get("results", [])

        contacts = []

        print(f"\nFound {len(results)} contacts\n")

        for person_data in results:

            person = person_data.get("person", {})

            name = person.get("full_name", "Unknown")
            title = person.get("current_job_title", "Unknown")
            person_id = person.get("person_id")
            linkedin_url = person.get("linkedin_url", "")

            contacts.append({
                "name": name,
                "title": title,
                "linkedin": linkedin_url
            })

            print(f"Trying: {name}")
            print(f"Role: {title}")

            if not person_id:
                print("No Person ID\n")
                continue

            enriched = self.enrich_person(person_id)

            if not enriched:
                print("Enrichment Failed\n")
                continue

            if enriched.get("error"):
                print(
                    f"Skipped ({enriched.get('error_code')})\n"
                )
                continue

            email_obj = (
                enriched
                .get("person", {})
                .get("email", {})
            )

            print("Email Object:", email_obj)

            email = email_obj.get("email")

            if email:

                export_contacts(contacts)

                print(f"SUCCESS: {email}\n")

                return {
                    "name": name,
                    "title": title,
                    "email": email,
                    "linkedin": linkedin_url,
                    "person_id": person_id,
                    "data": enriched
                }

            print("No Email Found\n")

        export_contacts(contacts)

        print("\nCSV exported successfully.")
        print("Check: output/contacts.csv")

        return None