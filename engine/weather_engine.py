from rapidconnect import RapidConnect
import sys

city = sys.argv[1]


rapid = RapidConnect("default-application_59bbda2be4b0b0cacf7c7995",
                     "db4efe57-20a5-4f2d-966c-b292a14a8695")

result = rapid.call('YahooWeatherAPI', 'getWeatherForecast', {'location': city})

desc = result["query"]["results"]["channel"]["item"]["condition"]["text"]
temp = result["query"]["results"]["channel"]["item"]["condition"]["temp"]

print "It's " + desc + " in {}, with a temperature of {} Farenheit.".format(city.capitalize(), temp)
sys.stdout.flush()
