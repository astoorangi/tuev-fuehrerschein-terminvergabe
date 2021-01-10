import requests

dateUrl = "https://www.tuv.com/tos-pti-relaunch-2019/rest/ajax/getVacanciesByMonth"


def genPayloadDates(
    month, year, locationId, vehicleServicesId="4007", vehicleTypeId="44"
):  # default for theoretical driving test
    return f'{{"locale":"de-DE","isLegacyTos":false,"filterMonth":{month},"filterYear":{year},"vehicleServices":[{{"id":{vehicleServicesId}}}],"vehicleType":{{"id":{vehicleTypeId}}},"vics":[{{"id":{locationId},"externalLocale":"de-DE"}}]}}'
