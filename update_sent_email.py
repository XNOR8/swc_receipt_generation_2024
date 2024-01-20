from dotenv import load_dotenv
import os
from supabase import create_client, Client


load_dotenv()

# Fetch env keys from .env file
supabase_url = os.environ.get("SUPABASE_URL")
supabase_key = os.environ.get("SUPABASE_KEY")
supabase: Client = create_client(supabase_url, supabase_key)


def update_sent_email(team_id):
    supabase.table("teams").update({"payment_confirmation_mail_sent": True}).eq(
        "team_id", team_id
    ).execute()
