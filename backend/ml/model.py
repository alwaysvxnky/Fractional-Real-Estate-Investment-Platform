# Simple ROI prediction model

def predict_roi(price, rent):
    """
    ROI = (Annual Rent / Property Price) * 100
    """

    if price <= 0:
        return 0

    yearly_rent = rent * 12
    roi = (yearly_rent / price) * 100

    return round(roi, 2)