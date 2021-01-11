import requests
import datetime
import json

dateUrl = "https://www.tuv.com/tos-pti-relaunch-2019/rest/ajax/getVacanciesByMonth"
appointmentUrl = "https://www.tuv.com/tos-pti-relaunch-2019/rest/ajax/getVacanciesByDay"
headers = {
    "Accept": "application/json",
    "Content-Type": "application/json; charset=utf-8",
}


def genPayloadDates(
    month, year, locationId, vehicleServicesId="4007", vehicleTypeId="44"
):  # default for theoretical driving test
    return f'{{"locale":"de-DE","isLegacyTos":false,"filterMonth":{month},"filterYear":{year},"vehicleServices":[{{"id":{vehicleServicesId}}}],"vehicleType":{{"id":{vehicleTypeId}}},"vics":[{{"id":{locationId},"externalLocale":"de-DE"}}]}}'


def genPayloadAppointments(
    date, locationId, vehicleServicesId="4007", vehicleTypeId="44"
):
    return f'{{"locale":"de-DE","isLegacyTos":false,"date":{{"date":"{date.strftime("%Y-%m-%d")}"}},"vehicleServices":[{{"id":{vehicleServicesId}}}],"vehicleType":{{"id":{vehicleTypeId}}},"vics":[{{"id":{locationId},"externalLocale":"de-DE"}}]}}'


def getAvaiblableDates(month, year, locationId):
    payload = genPayloadDates(month, year, locationId)
    response = requests.post(dateUrl, data=payload, headers=headers)
    response.close()
    res = response.json()

    dates = []
    for i in res["vacancies"]:
        date = datetime.datetime.strptime(i["date"], "%Y-%m-%d")
        dates.append(date)

    return dates


def getAvaiblableAppointmentsByDate(date, locationId):
    payload = genPayloadAppointments(date, locationId)
    response = requests.post(appointmentUrl, data=payload, headers=headers)
    response.close()
    res = response.json()

    appointments = []
    for i in res["timetables"][0]["timeRangeVacancies"]:
        for j in i["timeslots"]:
            time = j["availableDates"]
            if time != []:
                timeObj = datetime.datetime.strptime(time[0], "%H:%M")
                appointments.append(
                    date.replace(
                        hour=int(timeObj.strftime("%H")),
                        minute=int(timeObj.strftime("%M")),
                    )
                )
    return appointments
