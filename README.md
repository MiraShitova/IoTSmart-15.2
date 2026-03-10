# SmartHome CI/CD — Варіант 1

![Validation](https://github.com/MiraShitova/IoTSmart-15.1/actions/workflows/validate.yml/badge.svg)
![Testing](https://github.com/MiraShitova/IoTSmart-15.1/actions/workflows/test.yml/badge.svg)

## Pipeline Architecture
Пайплайн складається з чотирьох етапів: валідація конфігурації, автоматичне тестування логіки, безпекова збірка Docker-образу та публікація артефактів.

## Testing Strategy
Використовується піраміда тестування:
- **Unit**: перевірка окремих правил DSL.
- **Integration**: валідація зв'язків між Items та Things.
- **Regression**: перевірка стабільності конфігурації після змін.

## Docker Strategy
Використовується **Multi-stage build** для зменшення розміру образу та **Trivy Scanner** для пошуку вразливостей.