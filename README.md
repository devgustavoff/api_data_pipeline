# api_data_pipeline
Essa é uma pipelina de dados automatica que obtem dados do clima de 5 cidades do Brasil.
Os dados obtidos são nome das cidades, temperatura, humidade, descrição e timestamp do momento que foi coletado.
Os dados foram coletados da API: [OpenWeather](https://openweathermap.org/current?collection=current_forecast).
Nesse projeto foi usado cron para agendar a execução do script para que ele rode a cada 1 hora.

# Como rodar o projeto
### Instalar dependencias:
```bash
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
```
### Subir o container com o banco de dados Postgresql:
```bash
docker compose up
```
### Criar tabela no banco de dados:
```bash
docker cp sql/schema.sql weather_postgres:/schema.sql
docker exec -it weather_postgres psql -U postgres -d weather -f /schema.sql
```
### Agendar execução automatica com cron
Abra o crontab:
```bash
crontab -e
```
Adicione a linha abaixo para rodar a cada 1 hora:
```bash
0 * * * * /home/<seu-usuario>/.venv/bin/python /home/<seu-usuario>/api_data_pipeline/src/main.py
```

```sql
SELECT *
FROM weather_readings
ORDER BY collected_at DESC
LIMIT 10;
```
```
      name      | temperature | humidity |   description    |    collected_at     
----------------+-------------+----------+------------------+---------------------
 Rio De Janeiro |        26.2 |       79 | overcast clouds  | 2026-04-10 10:00:00
 Curro Velho    |        27.2 |       86 | scattered clouds | 2026-04-10 10:00:00
 Salvador       |        26.1 |       79 | clear sky        | 2026-04-10 10:00:00
 Boa Vista      |        26.2 |       67 | overcast clouds  | 2026-04-10 10:00:00
 Rio Branco     |        24.4 |       96 | overcast clouds  | 2026-04-10 10:00:00
 Rio Branco     |        23.8 |       97 | overcast clouds  | 2026-04-10 09:00:00
 Rio De Janeiro |        27.4 |       84 | broken clouds    | 2026-04-10 09:00:00
 Curro Velho    |        25.8 |       91 | broken clouds    | 2026-04-10 09:00:00
 Salvador       |          26 |       80 | clear sky        | 2026-04-10 09:00:00
 Boa Vista      |        25.2 |       75 | overcast clouds  | 2026-04-10 09:00:00
(10 rows)
```