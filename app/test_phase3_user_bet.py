import requests

BASE_URL = "http://127.0.0.1:8001"

def test_create_user_and_bet():
    # --- Criar usuário ---
    user_data = {
        "username": "florentino",
        "email": "florentinoinocerto@gmail.com"
    }
    response = requests.post(f"{BASE_URL}/users/", json=user_data)

    try:
        user_response = response.json()
    except Exception:
        user_response = {"detail": "Resposta não é JSON", "raw": response.text}

    if "id" not in user_response:
        # Usuário já existe ou erro, tentamos buscar o ID
        print(f"Usuário existente ou erro: {user_response}")
        # Para simplificação, assumimos que ID = 1 se já existia
        user_id = 1
    else:
        user_id = user_response["id"]
        print(f"Usuário criado com sucesso: {user_response}")

    # --- Criar aposta ---
    bet_data = {
        "user_id": user_id,
        "bet_platform": "ElephantBet",
        "stake": 500,
        "game_type": "aviator"
    }
    bet_response_raw = requests.post(f"{BASE_URL}/predictions/predict", json=bet_data)

    print("Status code:", bet_response_raw.status_code)
    print("Body:", bet_response_raw.text)

    # Tenta parsear JSON apenas se houver conteúdo
    try:
        bet_response = bet_response_raw.json()
        print(f"Aposta criada com sucesso: {bet_response}")
    except Exception:
        print("Falha ao criar aposta, resposta não é JSON ou vazia.")

if __name__ == "__main__":
    test_create_user_and_bet()
