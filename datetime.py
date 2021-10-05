from datetime import date, datetime

today = date.today()
now = datetime.now()


def say_time(voice_instance):
    current_time = now.strftime("%I:%M %p")
    voice_instance.say(current_time)


def say_date(voice_instance):
    date = today.strftime("%B %d %Y")
    voice_instance.say(date)


def say_day(voice_instance):
    day = today.strftime("%A")
    voice_instance.say(day)


def parse_query(command):
    query = ""

    if "ceasul" in command:
        query = "time"
    elif "dată" in command:
        query = "date"
    elif "zi" in command:
        query = "day"

    return query


def execute_query(query, voice_instance):
    actions = {
        "time": say_time,
        "date": say_date,
        "day": say_day,
    }

    actions[query](voice_instance)


def run(command, args, voice_instance):
    query = parse_query(command)
    execute_query(query, voice_instance)
