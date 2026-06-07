# Automated Outreach Pipeline

This repository implements an automated outreach pipeline for finding company contacts, enriching them, exporting to CSV, and sending outreach emails.

Related assignment: `SDE Assignment — Automated Outreach Pipeline - Vocallabs.pdf` (see repository root).

## Features implemented

- Discover people for a given company domain using the Prospeo API (`services/prospeo_service.py`).
- Enrich person data and extract email addresses.
- Export discovered contacts to `output/contacts.csv` (`services/export_service.py`).
- Send email via Brevo/Sib API (`services/brevo_service.py`).
- CLI entrypoint: `main.py` — prompts for a company domain and prints results.
- Minimal approval prompt in `services/approval_service.py`.

## Required environment variables

Copy `.env.example` to `.env` and fill in the keys, or set environment variables directly:

- `PROSPEO_API_KEY` - API key for Prospeo
- `BREVO_API_KEY` - API key for Brevo (Sendinblue)

Note: API keys should NOT be committed to the repository. Use GitHub Secrets for CI/deploy.

## Quick start

1. Create a virtual environment and install dependencies (requests, python-dotenv):

```powershell
python -m venv .venv
.\.venv\Scripts\Activate.ps1
pip install requests python-dotenv
```

2. Add credentials to `.env` (or set environment variables).

3. Run the CLI:

```powershell
python main.py
```

The script will search for people at the domain you enter, attempt enrichment, export `output/contacts.csv`, and print any found contact.

## Assignment checklist (status)

- [x] Search company domain and list potential contacts
- [x] Enrich contact data using Prospeo
- [x] Export contacts to CSV
- [x] Provide a function to send emails via Brevo
- [x] CLI to run the pipeline (`main.py`)
- [x] Basic approval prompt before outreach
- [ ] Tests (unit/integration)
- [ ] CI configuration
- [ ] Proper secrets handling (use GitHub Secrets; rotate exposed keys)
- [ ] Error reporting/structured logging

## Remediation performed

- Removed leaked secrets from git history and added `.env` and `prospeo_key.txt` to `.gitignore`.

**You must rotate the exposed API keys immediately.**

## Next recommended steps

- Add unit tests for services and mocks for network calls.
- Add GitHub Actions CI to run tests and linting.
- Replace direct `.env` keys with GitHub Secrets and environment injection in CI.

If you want, I can add tests and CI next, or help rotate and replace secrets and add secure configuration.
