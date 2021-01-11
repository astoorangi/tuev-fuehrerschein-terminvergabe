import requests
import datetime
import json

dateUrl = "https://www.tuv.com/tos-pti-relaunch-2019/rest/ajax/getVacanciesByMonth"


def genPayloadDates(
    month, year, locationId, vehicleServicesId="4007", vehicleTypeId="44"
):  # default for theoretical driving test
    return f'{{"locale":"de-DE","isLegacyTos":false,"filterMonth":{month},"filterYear":{year},"vehicleServices":[{{"id":{vehicleServicesId}}}],"vehicleType":{{"id":{vehicleTypeId}}},"vics":[{{"id":{locationId},"externalLocale":"de-DE"}}]}}'


def getAvaiblableDates(month, year, locationId):
    payload = genPayloadDates(month, year, locationId)
    headers = {
        "Accept": "application/json",
        "Content-Type": "application/json; charset=utf-8",
    }
    response = requests.post(dateUrl, data=payload, headers=headers)
    response.close()
    res = response.json()

    dates = []
    for i in res["vacancies"]:
        date = datetime.datetime.strptime(i["date"], "%Y-%m-%d")
        dates.append(date)
        print(date)
