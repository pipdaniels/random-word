import requests
from django.conf import settings
from huey import crontab
from huey.contrib.djhuey import db_periodic_task
from demo.models import Word

# Create your views here.



@db_periodic_task(crontab(hour="18", minute="00"), retries=2, retry_delay=10)
def fetch_daily_word():
    r = requests.get(
        f"https://api.wordnik.com/v4/words.json/wordOfTheDay?api_key={settings.WORDNIK_API_KEY}")
    if r.status_code !=200:
        raise Exception("Unable tofetch d ata from WordNIP API")
    else:
        data = r.json()
        Word.objects.get_or_create(
            word=data["word"],
            part_of_speech=data["definitions"][0]["partOfSpeech"],
            definition=data["definitions"][0]["text"],
            example=data["examples"][0]["text"]
    )