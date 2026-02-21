# InnoPredictAutoplay Backend

## Setup no Termux

1. Entre na pasta:
cd ~/innopredict-backend

2. Ative o ambiente virtual:
source venv/bin/activate

3. Instale as dependências:
pip install -r requirements.txt

4. Rode o servidor:
uvicorn app.main:app --host 0.0.0.0 --port 8000 --reload

5. Teste o endpoint:
POST http://localhost:8000/predict
{
  "param1": 5.0,
  "param2": 3.2,
  "param3": 7.1
}

Saída esperada:
{
  "predicted_value": 5.1
}
