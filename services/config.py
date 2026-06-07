import os
from dotenv import load_dotenv

# Load .env into environment (safe to call multiple times)
load_dotenv()


def get_env_var(name: str, required: bool = True) -> str | None:
    """Return environment variable or raise a clear error when required.

    This centralizes environment access so callers get a standardized
    error when a required variable is missing.
    """
    val = os.getenv(name)
    if required and (val is None or val == ""):
        raise RuntimeError(f"Missing required environment variable: {name}")
    return val
