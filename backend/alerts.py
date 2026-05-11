def send_hospital_alert():

    return "Nearest hospital alerted"


def request_ambulance():

    return "Ambulance request sent"


def connect_specialist():

    return "Connecting specialist doctor"


def nearest_hospital(location):

    hospitals = {
        "Bangalore": "Apollo Hospital",
        "Mysore": "Mysore Medical Center",
        "Tumkur": "District General Hospital"
    }

    return hospitals.get(location, "Nearest PHC Center")