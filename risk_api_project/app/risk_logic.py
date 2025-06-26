def calculate_risk(data):
    score = 0
    breakdown = {}

    if data["region"] == "EU" and data["data_sensitivity"].lower() == "high":
        score += 30
        breakdown["EU + High Sensitivity"] = 30

    if data["processor_name"] == "UnknownVendor":
        score += 20
        breakdown["Unknown Vendor"] = 20

    if data["purpose"].lower() == "marketing":
        score += 15
        breakdown["Marketing Purpose"] = 15

    score = min(score, 100)
    return score, breakdown
