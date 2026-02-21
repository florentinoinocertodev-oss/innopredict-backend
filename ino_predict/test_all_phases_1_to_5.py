import requests

BASE_URL = "http://127.0.0.1:8001"

def test_phase1_prediction():
    payload = {
        "user_id": 1,
        "bet_platform": "ElephantBet",
        "stake": 500,
        "game_type": "aviator"
    }
    response = requests.post(f"{BASE_URL}/predictions/predict", json=payload)
    print("=== Teste Fase 1: Previsão ===")
    print("Status code:", response.status_code)
    print("Body:", response.json())
    return response.json()

def test_phase2_analytics():
    payload = {
        "user_id": 1,
        "stake": 500,
        "historical_data": [1.2, 1.5, 1.3, 1.7]  # exemplo de histórico do usuário
    }
    response = requests.post(f"{BASE_URL}/analytics/predict", json=payload)
    print("\n=== Teste Fase 2: Analytics ===")
    print("Status code:", response.status_code)
    print("Body:", response.json())
    return response.json()

def test_phase3_user_bet():
    # Criar usuário
    user_payload = {
        "username": "florentino",
        "email": "florentinoinocerto@gmail.com"
    }
    user_response = requests.post(f"{BASE_URL}/users/", json=user_payload).json()
    print("\n=== Teste Fase 3: Usuário + Aposta ===")
    print("Usuário criado com sucesso:", user_response)

    # Criar aposta vinculada ao usuário
    bet_payload = {
        "user_id": user_response.get("id", 1),
        "bet_platform": "ElephantBet",
        "stake": 500,
        "game_type": "aviator"
    }
    bet_response = requests.post(f"{BASE_URL}/predictions/predict", json=bet_payload).json()
    print("Aposta criada com sucesso:", bet_response)
    return user_response, bet_response

def test_phase4_combined():
    # Novo usuário para teste combinado
    user_payload = {
        "username": "florentino2",
        "email": "florentino2@gmail.com"
    }
    user_response = requests.post(f"{BASE_URL}/users/", json=user_payload).json()
    
    # Previsão combinada
    combined_payload = {
        "user_id": user_response.get("id", 2),
        "bet_platform": "ElephantBet",
        "stake": 500,
        "game_type": "aviator"
    }
    prediction_response = requests.post(f"{BASE_URL}/predictions/predict", json=combined_payload).json()
    
    # Analytics combinada
    analytics_payload = {
        "user_id": user_response.get("id", 2),
        "stake": 500,
        "historical_data": [1.1, 1.4, 1.3, 1.6]
    }
    analytics_response = requests.post(f"{BASE_URL}/analytics/predict", json=analytics_payload).json()
    
    print("\n=== Teste Fase 4: Combinado ===")
    print("Usuário criado:", user_response)
    print("Previsão combinada:", prediction_response)
    print("Analytics combinada:", analytics_response)
    return user_response, prediction_response, analytics_response

def test_phase5_history():
    user_id = 1
    response = requests.get(f"{BASE_URL}/history/user/{user_id}")
    print("\n=== Teste Fase 5: Histórico/Combinado ===")
    print("Status code:", response.status_code)
    print("Histórico do usuário 1:", response.json())
    return response.json()

if __name__ == "__main__":
    test_phase1_prediction()
    test_phase2_analytics()
    test_phase3_user_bet()
    test_phase4_combined()
    test_phase5_history()
