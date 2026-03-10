# IoT Smart System CI/CD — PR 15.2

![Validation Status](https://github.com/MiraShitova/IoTSmart-15.2/actions/workflows/validate.yml/badge.svg)
![Testing Status](https://github.com/MiraShitova/IoTSmart-15.2/actions/workflows/test.yml/badge.svg)

## Pipeline Architecture
Система використовує чотириступеневий пайплайн автоматизації:
1. Validation: Перевірка синтаксису конфігураційних файлів OpenHAB та лінтинг YAML/JSON форматів.
2. Automated Testing: Запуск юніт та інтеграційних тестів за допомогою Pytest для перевірки логіки правил.
3. Build & Security: Збірка Docker-образу (Multi-stage) та сканування на вразливості сканером Trivy.
4. Deployment: Публікація перевірених конфігурацій як артефактів збірки.

## Workflow Descriptions
- validate.yml: Виконує syntax check для Items, Things, Sitemaps та Rules DSL.
- test.yml: Проводить автоматичне тестування логічних виразів у правилах.
- build.yml: Забезпечує інтеграцію з Docker та виконання security scanning.
- deploy.yml: Відповідає за Artifact publishing та збереження стабільних версій коду.

## Testing Strategy
- Unit Tests: Перевірка окремих елементів Rules DSL та наявності необхідних Items.
- Integration Tests: Валідація зв'язків між фізичними описами (Things) та віртуальними об'єктами.
- Configuration Tests: Перевірка цілісності структури папок та форматів файлів.
- Regression Tests: Запобігання помилкам у існуючій логіці при додаванні нових функцій.

## Docker Image Strategy
Використовується Multi-stage Dockerfile для оптимізації розміру образу та розділення середовища тестування від середовища виконання. Додатково впроваджено Image tagging strategy на основі Git tags.
