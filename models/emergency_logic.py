
def human_emergency_check(oxygen, pulse):

    if oxygen < 90:
        return "HIGH RISK"

    elif pulse > 120:
        return "MEDIUM RISK"

    else:
        return "LOW RISK"


def animal_emergency_check(activity):

    if activity == "Very Low":
        return "HIGH RISK"

    else:
        return "LOW RISK"