import requests

BASE_URL = "http://127.0.0.1:8001"

def test_all_phases_1_to_4():
    print("=== INO-Predict Express Teste Fases 1 a 4 ===\n")

    # --- Fase 1/2: Criar usuário ---
    user_data = {
        "username": "florentino",
        "email": "florentinoinocerto@gmail.com"
    }

    user_response = requests.post(f"{BASE_URL}/users/", json=user_data)
    try:
        user_json = user_response.json()
    except Exception:
        user_json = {"detail": "Resposta vazia ou não JSON"}

    if "id" not in user_json:
        # Usuário já existe ou resposta incompleta
        print(f"Usuário já cadastrado ou erro: {user_json}")
        # Tentar obter o ID do usuário existente
        # Assumindo ID = 1 se não houver retorno
        user_id = user_json.get("id", 1)
    else:
        print(f"Usuário criado com sucesso: {user_json}")
        user_id = user_json["id"]

    # --- Fase 3: Criar aposta / previsão ---
    bet_data = {
        "user_id": user_id,
        "bet_platform": "ElephantBet",
        "stake": 500,
        "game_type": "aviator"
    }

    bet_response = requests.post(f"{BASE_URL}/predictions/predict", json=bet_data)
    try:
        bet_json = bet_response.json()
        print(f"Aposta criada com sucesso: {bet_json}")
    except Exception:
        print(f"Falha ao criar aposta, resposta não é JSON ou vazia.\nStatus code: {bet_response.status_code}\nBody: {bet_response.text}")
        bet_json = None

    # --- Fase 4: Analytics ---
    analytics_data = {
        "stake": 500,
        "historical_data": [1.2, 1.5, 1.4, 1.3, 1.6]
    }

    analytics_response = requests.post(f"{BASE_URL}/analytics/predict", json=analytics_data)
    try:
        analytics_json = analytics_response.json()
        print(f"Analytics gerado com sucesso: {analytics_json}")
    except Exception:
        print(f"Falha no analytics, resposta não é JSON ou vazia.\nStatus code: {analytics_response.status_code}\nBody: {analytics_response.text}")
        analytics_json = None

    # --- Resumo final ---
    print("\n=== Resumo Final ===")
    print(f"Usuário ID: {user_id}")
    print(f"Aposta / Previsão: {bet_json}")
    print(f"Analytics: {analytics_json}")
    print("\nTeste completo das fases 1 a 4 finalizado.")

if __name__ == "__main__":
    test_all_phases_1_to_4()
