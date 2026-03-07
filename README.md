# OpenHAB IoT Ecosystem

Цей проєкт реалізує автоматизовану систему розумного будинку на базі OpenHAB.

## Архітектура
- **OpenHAB**: Центр керування.
- **Mosquitto**: MQTT broker для обміну повідомленнями.
- **InfluxDB**: База даних часових рядів (Persistence).
- **Grafana**: Візуалізація даних.

## Швидкий старт
1. Скопіюйте налаштування: `cp .env.example .env`
2. Запустіть стек: `docker compose up -d`
3. Панелі керування:
   - OpenHAB: `http://localhost:8080`
   - Grafana: `http://localhost:3000`

## Бекапи
Скрипти автоматизації знаходяться в папці `/scripts`.
- Запуск бекапу: `./scripts/backup.sh`
- Планування (Cron): `0 3 * * * /path/to/scripts/backup.sh`

## Troubleshooting
- Якщо контейнери не запускаються, перевірте логі: `docker compose logs -f`
- Переконайтеся, що порти 8080, 1883 та 3000 вільні.