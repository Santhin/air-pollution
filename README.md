
---
## 🧐 About <a name = "about"></a>

The project was created for academic purposes. Consists of unification archive measurement data from range 2000-2019 with existing database.<br>
Measurement data were combined with meteorological data using Dask and distributed computing provided by Coiled<br>
The model was trained using Xgboost and Optuna for hyperparameter tunning, which reached an RMSE of 6,932 [µg / m3].

### Links to data:
https://powietrze.gios.gov.pl/pjp/archives
https://powietrze.gios.gov.pl/pjp/content/api 
https://danepubliczne.imgw.pl/data/<br>


## 🏁 Installing

- Python 3.8.3

```
git clone https://github.com/Santhin/air-pollution.git
```

Installing dependencies:

```
pip install -r requirements.txt
or 
poetry install
```
Run jupyter notebook with:
```
jupyter notebook
```
To install coiled software environment:
```
import coiled

coiled.create_software_environment(
    name="my-software-env",
    conda="coiled-environment-py38.yml",
)
```

### Project structure
```
├── coiled-environment-py38.yml
├── data
│   ├── dictionaries
│   │   ├── IndeksJakosciPowietrza.csv
│   │   ├── Indeks\ jako\305\233ci\ powietrza\ gio\305\233.xlsx
│   │   ├── IndeksJakosciPowietrza.xlsx
│   │   ├── Kody_stacji_pomiarowych.xlsx
│   │   ├── Matching_stations
│   │   │   ├── SmogoliczkaStacje.csv
│   │   │   └── SynopStacje.csv
│   │   ├── Metadane\ -\ stacje\ i\ stanowiska\ pomiarowe.xlsx
│   │   ├── Normy.pkl
│   │   ├── PomiarySample.pkl
│   │   ├── response_api_gios.json
│   │   ├── RodzajeParametrow.csv
│   │   ├── rodzaje_parametrow.pkl
│   │   ├── SensoryPomiarowe.csv
│   │   ├── SensoryPomiarowe.pkl
│   │   ├── stacje_pom_api.json
│   │   ├── StacjePomiarowe.xlsx
│   │   └── stacjeSmogoliczka.csv
│   ├── IndeksJakosciPowietrza.csv
│   └── train_data.csv
├── LICENSE
├── notebooks
│   ├── Air\ Quality\ Index\ Gios.ipynb
│   ├── eda\ without\ progress-Copy4.ipynb
│   ├── Filtering\ excel\ files\ and\ picking\ right\ parameters.ipynb
│   ├── Fixing\ missing\ lat\ and\ lon\ in\ stations\ .ipynb
│   ├── loader_sql.py
│   ├── Matching\ stations\ synop\ with\ Smogoliczka\ .ipynb
│   ├── Matching\ synop\ data\ with\ smogoliczka.ipynb
│   ├── Matching\ Synop\ with\ Smogoliczka\ final.ipynb
│   ├── ML\ PM2.5.ipynb
│   ├── New\ Strategy\ script\ for\ excel\ files.ipynb
│   ├── __pycache__
│   │   └── loader_sql.cpython-38.pyc
│   ├── Repairing\ stations\ names\ and\ merging\ into\ one\ .ipynb
│   └── Smogoliczka\ API\ to\ pomiary_pivot.ipynb
├── poetry.lock
├── pyproject.toml
├── README.md
└── requirements.txt
```

## ⛏️ Built Using <a name = "built_using"></a>

- [MsSQL](https://www.microsoft.com/pl-pl/sql-server/sql-server-downloads) - Database
- [S3Bucket](https://aws.amazon.com/s3/) - Cloud storage
- [Coiled](https://coiled.io/) - Distributed computing
- [Dask](https://dask.org/) - Preprocessing data
- [Optuna](https://optuna.org/) - Hyperparameter optimization
- [Xgboost](https://xgboost.readthedocs.io/en/latest/) - ML
