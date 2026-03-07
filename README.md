#  Smart Greenhouse: DevOps & CI/CD Edition

Цей репозиторій містить розширену версію системи "Smart Greenhouse", інтегровану з пайплайнами GitHub Actions для автоматизації тестування, валідації та збірки Docker-образів.

[![Config Validation](https://github.com/MiraShitova/IoTSmart-15.2/actions/workflows/validate.yml/badge.svg)](https://github.com/MiraShitova/IoTSmart-15.2/actions/workflows/validate.yml)
[![Logic Tests](https://github.com/MiraShitova/IoTSmart-15.2/actions/workflows/test.yml/badge.svg)](https://github.com/MiraShitova/IoTSmart-15.2/actions/workflows/test.yml)
[![Docker Build](https://github.com/MiraShitova/IoTSmart-15.2/actions/workflows/build.yml/badge.svg)](https://github.com/MiraShitova/IoTSmart-15.2/actions/workflows/build.yml)

## Архітектура пайплайну (Pipeline Architecture)
Проєкт використовує чотири основні workflows для забезпечення якості коду та надійності розгортання:

1. **Configuration Validation (`validate.yml`)**: Автоматична перевірка синтаксису файлів конфігурації OpenHAB (.items, .rules, .sitemaps) через Docker-контейнер.
2. **Automated Testing (`test.yml`)**: Запуск Unit-тестів на Python за допомогою фреймворку pytest для перевірки логіки автоматизації насоса та порогів вологості.
3. **Docker Image Build (`build.yml`)**: Збірка образу з використанням Multi-stage Dockerfile. Включає етап підготовки конфігурацій та створення фінального оптимізованого образу на базі Alpine Linux.
4. **Deployment Simulation (`deploy.yml`)**: Заглушка для розгортання системи на Edge-пристрої після успішного проходження всіх попередніх етапів.



##  Стратегія тестування (Testing Strategy)
Для проєкту реалізовано декілька рівнів перевірки:
* **Unit Tests**: Тестування логічної функції `get_pump_status` у файлі `tests/test_rules.py`. Перевіряється коректність увімкнення насоса при вологості < 50%.
* **Syntax Checking**: Перевірка DSL Rules та конфігурацій OpenHAB на відповідність стандартам версії 4.x.
* **Regression Testing**: Кожен новий Push автоматично перевіряє, чи не зламали нові зміни існуючу логіку системи.

##  Docker & Оптимізація
Dockerfile проєкту реалізований за принципом Multi-stage build:
* **Stage 1 (Builder)**: Використовує повний образ OpenHAB для валідації конфігів.
* **Stage 2 (Final)**: Базується на Alpine-версії для мінімізації розміру образу та покращення безпеки.