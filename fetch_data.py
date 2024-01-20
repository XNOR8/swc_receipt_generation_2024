from dotenv import load_dotenv
import os
from supabase import create_client, Client


load_dotenv()

# Fetch env keys from .env file
supabase_url = os.environ.get("SUPABASE_URL")
supabase_key = os.environ.get("SUPABASE_KEY")
supabase: Client = create_client(supabase_url, supabase_key)


def fetch_data():
    response = (
        supabase.table("teams")
        .select(
            "created_at, transaction_id,team_id, users(email,name), events(roles(users(email)),event_name,registration_fees)"
        )
        .match({"transaction_verified": True, "payment_confirmation_mail_sent": False})
        .lte("transaction_verified_at", "2024-01-20 13:00:00")
        .execute()
    )
    return response.data
