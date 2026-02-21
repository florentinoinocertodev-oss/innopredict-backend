# test_all_phases_1_to_5.py

from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)


def test_full_flow_phase_1_to_5():
    print("\n🚀 Iniciando teste completo Fases 1 → 5")

    # ----------------------------
    # FASE 1 - Criar usuário
    # ----------------------------
    user_payload = {
        "username": "testuser_phase5",
        "email": "testphase5@email.com"
    }

    user_response = client.post("/users/", json=user_payload)
    assert user_response.status_code == 200
    user_data = user_response.json()

    user_id = user_data["id"]
    print(f"✅ Usuário criado | ID: {user_id}")

    # ----------------------------
    # FASE 2 - Criar previsão
    # ----------------------------
    prediction_payload = {
        "user_id": user_id,
        "suggested_multiplier": 2.5,
        "confidence": 0.87,
        "message": "Multiplicador sugerido com alta confiança"
    }

    prediction_response = client.post("/predictions/", json=prediction_payload)
    assert prediction_response.status_code == 200
    prediction_data = prediction_response.json()

    prediction_id = prediction_data["id"]
    print(f"✅ Previsão criada | ID: {prediction_id}")

    # ----------------------------
    # FASE 3 - Criar analytics
    # ----------------------------
    analytics_payload = {
        "user_id": user_id,
        "predicted_multiplier": 2.5,
        "confidence": 0.87,
        "message": "Analytics confirmando previsão"
    }

    analytics_response = client.post("/analytics/", json=analytics_payload)
    assert analytics_response.status_code == 200
    print("✅ Analytics criado")

    # ----------------------------
    # FASE 5 - Criar histórico
    # ----------------------------
    history_payload = {
        "user_id": user_id,
        "prediction_id": prediction_id,
        "result_multiplier": 2.8
    }

    history_response = client.post("/history/", json=history_payload)
    assert history_response.status_code == 200
    history_data = history_response.json()

    assert history_data["user_id"] == user_id
    assert history_data["prediction_id"] == prediction_id
    assert history_data["result_multiplier"] == 2.8

    print(f"✅ Histórico criado | ID: {history_data['id']}")

    # ----------------------------
    # FASE 5 - Buscar histórico por usuário
    # ----------------------------
    get_history_response = client.get(f"/history/user/{user_id}")
    assert get_history_response.status_code == 200

    history_list = get_history_response.json()
    assert isinstance(history_list, list)
    assert len(history_list) > 0

    print("✅ Histórico recuperado com sucesso")

    # ----------------------------
    # VALIDAÇÕES FINAIS
    # ----------------------------
    print("\n🎉 TESTE COMPLETO PASSOU — Fases 1 → 5 OK!\n")
