import requests
import json

BASE_URL = "http://127.0.0.1:8001"

def test_prediction():
    url = f"{BASE_URL}/predictions/predict"
    payload = {
        "user_id": 101,
        "bet_platform": "ElephantBet",
        "stake": 500,
        "game_type": "aviator"
    }
    headers = {"Content-Type": "application/json"}
    response = requests.post(url, headers=headers, data=json.dumps(payload))
    print("=== Prediction Test ===")
    if response.status_code == 200:
        print("Success:", response.json())
    else:
        print("Failed:", response.status_code, response.text)
    return response.json() if response.status_code == 200 else None

def test_analytics():
    url = f"{BASE_URL}/analytics/predict"
    payload = {
        "stake": 500,
        "historical_data": [1.2, 1.5, 1.4, 1.3, 1.6]
    }
    headers = {"Content-Type": "application/json"}
    response = requests.post(url, headers=headers, data=json.dumps(payload))
    print("=== Analytics Test ===")
    if response.status_code == 200:
        print("Success:", response.json())
    else:
        print("Failed:", response.status_code, response.text)
    return response.json() if response.status_code == 200 else None

if __name__ == "__main__":
    print("Running INO-Predict Express Full Phase Test...")
    prediction_result = test_prediction()
    analytics_result = test_analytics()
    print("\n=== Summary ===")
    print("Prediction Result:", prediction_result)
    print("Analytics Result:", analytics_result)
