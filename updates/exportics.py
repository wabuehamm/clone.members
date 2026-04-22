from os import environ
import mechanize

br = mechanize.Browser()
br.set_handle_robots(False)
br.open(environ.get("ELGG_URL"))
br.select_form(action="%s/action/login" % environ.get("ELGG_URL"))
br["username"] = environ.get("ELGG_USER")
br["password"] = environ.get("ELGG_PASSWORD")
br.submit()

br.open(
    "%s/event_calendar/ical/export?method=ical&filter=all" % environ.get("ELGG_URL")
)
br.select_form(
    action="%s/action/event_calendar/export" %environ.get("ELGG_URL")
)
br["start_date"] = "2026-01-01"
br["end_date"] = "2026-12-31"
response = br.submit()
f = open("Calendar.ics", "w")
f.write(response.read().decode("utf-8"))
f.close()
