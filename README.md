# Smart City Waste Management — PR 15.2
![Build Status](https://github.com/MiraShitova/IoTSmart-15.2/actions/workflows/validate.yml/badge.svg)

### Pipeline Architecture
Система використовує чотириступеневий пайплайн: Валідація (Syntax/Lint), Тестування (Pytest), Збірка (Docker Multi-stage) та Публікація артефактів.

### Testing Strategy
- **Unit**: Логіка Rules DSL.
- **Integration**: Взаємодія Items та MQTT.
- **Regression**: Перевірка цілісності конфігурації.

### Demo Video
[Посилання на відео демонстрації пайплайну]