# IC-3002 Proyecto 3

Esqueleto para el proyecto de algoritmos concurrentes para el curso IC-3002 Análisis de Algoritmos.

Este proyecto requiere python3.

Para instalar las dependencias correr:

```bash
pip3 install -r requirements.txt
```

Para correr todas las pruebas automatizadas:

```bash
pytest
```

Para correr solo algunas pruebas automatizadas, por ejemplo todas las pruebas cuyo nombre inicia con `test_validar`:

```bash
pytest -v -k "test_validar" dominio_tsp_test.py
```
