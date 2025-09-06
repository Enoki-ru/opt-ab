# opt_ab

<a target="_blank" href="https://cookiecutter-data-science.drivendata.org/">
    <img src="https://img.shields.io/badge/CCDS-Project%20template-328F97?logo=cookiecutter" />
</a>

Модуль для изучения A/B тестирования, методов улучшения A/B, сравнения частотных методов с Байесовскими методами тестирования.



## Классы
1. `freq_tools`  # Инструменты для частотного подхода
2. `bayes_tools`  # Инструменты для байесовского подхода
3. `boosts_tools`  # Инструменты для улучшения Тестирования
4. `gen_data`  # Инструменты для генерации данных


## To-Do
- [ ] Написать модуль для расчета всех параметров Частотного A/B эксперимента. t-test, u-test, z-test
- [ ] Написать модуль для генерации случайных данных Размера X
- [ ] Написать модуль для генерации отчетов и графиков по проведению A/B эксперимента
- [ ] Написать модуль для расчета всех параметров Байесовского A/B эксперимента


## Project Organization

```
├── LICENSE            <- Open-source license if one is chosen
├── Makefile           <- Makefile with convenience commands like `make data` or `make train`
├── README.md          <- The top-level README for developers using this project.
├── data
│   ├── external       <- Data from third party sources.
│   ├── interim        <- Intermediate data that has been transformed.
│   ├── processed      <- The final, canonical data sets for modeling.
│   └── raw            <- The original, immutable data dump.
│
├── docs               <- A default mkdocs project; see www.mkdocs.org for details
│
├── models             <- Trained and serialized models, model predictions, or model summaries
│
├── notebooks          <- Jupyter notebooks. Naming convention is a number (for ordering),
│                         the creator's initials, and a short `-` delimited description, e.g.
│                         `1.0-jqp-initial-data-exploration`.
│
├── pyproject.toml     <- Project configuration file with package metadata for 
│                         optab and configuration for tools like black
│
├── references         <- Data dictionaries, manuals, and all other explanatory materials.
│
├── reports            <- Generated analysis as HTML, PDF, LaTeX, etc.
│   └── figures        <- Generated graphics and figures to be used in reporting
│
├── requirements.txt   <- The requirements file for reproducing the analysis environment, e.g.
│                         generated with `pip freeze > requirements.txt`
│
├── setup.cfg          <- Configuration file for flake8
│
└── optab   <- Source code for use in this project.
    │
    ├── __init__.py             <- Makes optab a Python module
    │
    ├── config.py               <- Store useful variables and configuration
    │
    ├── dataset.py              <- Scripts to download or generate data
    │
    ├── features.py             <- Code to create features for modeling
    │
    ├── modeling                
    │   ├── __init__.py 
    │   ├── predict.py          <- Code to run model inference with trained models          
    │   └── train.py            <- Code to train models
    │
    └── plots.py                <- Code to create visualizations
```

--------

