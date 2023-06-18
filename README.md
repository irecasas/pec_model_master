# pec_model_master

## Estructura del proyecto

```
.
├── README.md
├── notebooks  
│   ├── data
│   │   └── titanic.csv
│   └── exploracion_dato.ipynb
├── pec_model_master                                         # Paquete instalable
│   ├── __init__.py
│   ├── pec_pipelines
│   │   ├── feature_engineering 
│   │   │   ├── WOE_encoder.py
│   │   │   ├── __init__.py
│   │   │   ├── generic_cleaner.py
│   │   │   └── utils.py
│   │   ├── model
│   │   │   └── catboost_20230618T211618.pkl
│   │   └── preproces_pipeline.py
│   └── training_model.py                               # Ejecutable 
├── poetry.lock
├── pyproject.toml
├── tests
│   └── test_utils.py
```

## Requerimientos
* python3.9
* poetry

## Como ejecutar

En el directorio del proyecto, abrir un terminal y crear un entorno virtual con poetry con el siguiente comando:
```
poetry shell
```
Instalar las dependencias con el siguiente comando:
```
poetry install
```
Para generar una versión más reciente del modelo:
```
python3 pec_model_master/training_model.py
```

## Ejecutar los test
Desde la raiz del proyecto y dentro del entorno virtual, lanzar el siguiente comando:
```
PYTHONPATH="$PYTHONPATH:$(pwd)/pec_model_master:$(pwd)/tests" python -m unittest discover -s tests
```

## Publicar librería
Ajustar la versión dentro del archivo [pyproject.toml](pyproject.toml)
Lanzar los siguientes comandos:
```
poetry build 
```
```
poetry publish 
```

## Instalar librería
```
pip install pec_model_master
```