import requests

BASE_URL = "http://127.0.0.1:8001"

def test_phase_1_prediction():
    print("=== Teste Fase 1: Previsão ===")
    payload = {
        "user_id": 1,
        "bet_platform": "ElephantBet",
        "stake": 500,
        "game_type": "aviator"
    }
    response = requests.post(f"{BASE_URL}/predictions/predict", json=payload)
    print("Status code:", response.status_code)
    print("Body:", response.json())

def test_phase_2_analytics():
    print("\n=== Teste Fase 2: Analytics ===")
    payload = {
        "stake": 500,
        "historical_data": [1.2, 1.5, 1.4, 1.3, 1.6]
    }
    response = requests.post(f"{BASE_URL}/analytics/predict", json=payload)
    print("Status code:", response.status_code)
    print("Body:", response.json())

def test_phase_3_user_bet():
    print("\n=== Teste Fase 3: Usuário + Aposta ===")
    user_payload = {
        "username": "florentino",
        "email": "florentinoinocerto@gmail.com"
    }
    user_response = requests.post(f"{BASE_URL}/users/", json=user_payload)
    print("Usuário criado com sucesso:", user_response.json())

    bet_payload = {
        "user_id": user_response.json().get("id", 1),
        "bet_platform": "ElephantBet",
        "stake": 500,
        "game_type": "aviator"
    }
    bet_response = requests.post(f"{BASE_URL}/predictions/predict", json=bet_payload)
    print("Aposta criada com sucesso:", bet_response.json())

def test_phase_4_combined():
    print("\n=== Teste Fase 4: Combinado ===")
    # Combina previsão + analytics + usuário
    user_payload = {
        "username": "florentino2",
        "email": "florentino2@gmail.com"
    }
    user_response = requests.post(f"{BASE_URL}/users/", json=user_payload)
    user_id = user_response.json().get("id", 2)
    print("Usuário criado:", user_response.json())

    prediction_payload = {
        "user_id": user_id,
        "bet_platform": "ElephantBet",
        "stake": 700,
        "game_type": "aviator"
    }
    prediction_response = requests.post(f"{BASE_URL}/predictions/predict", json=prediction_payload)
    print("Previsão combinada:", prediction_response.json())

    analytics_payload = {
        "stake": 700,
        "historical_data": [1.3, 1.5, 1.7, 1.2, 1.4]
    }
    analytics_response = requests.post(f"{BASE_URL}/analytics/predict", json=analytics_payload)
    print("Analytics combinada:", analytics_response.json())

if __name__ == "__main__":
    test_phase_1_prediction()
    test_phase_2_analytics()
    test_phase_3_user_bet()
    test_phase_4_combined()
