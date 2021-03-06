
---
## ๐ง About <a name = "about"></a>

The project was created for academic purposes. Consists of unification archive measurement data from range 2000-2019 with existing database.<br>
Measurement data were combined with meteorological data using Dask and distributed computing provided by Coiled<br>
The model was trained using Xgboost and Optuna for hyperparameter tunning, which reached an RMSE of 6,932 [ยตg / m3].

### Links to data:
https://powietrze.gios.gov.pl/pjp/archives
https://powietrze.gios.gov.pl/pjp/content/api 
https://danepubliczne.imgw.pl/data/<br>


## ๐ Installing

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
โโโ coiled-environment-py38.yml
โโโ data
โ   โโโ dictionaries
โ   โ   โโโ IndeksJakosciPowietrza.csv
โ   โ   โโโ Indeks\ jako\305\233ci\ powietrza\ gio\305\233.xlsx
โ   โ   โโโ IndeksJakosciPowietrza.xlsx
โ   โ   โโโ Kody_stacji_pomiarowych.xlsx
โ   โ   โโโ Matching_stations
โ   โ   โ   โโโ SmogoliczkaStacje.csv
โ   โ   โ   โโโ SynopStacje.csv
โ   โ   โโโ Metadane\ -\ stacje\ i\ stanowiska\ pomiarowe.xlsx
โ   โ   โโโ Normy.pkl
โ   โ   โโโ PomiarySample.pkl
โ   โ   โโโ response_api_gios.json
โ   โ   โโโ RodzajeParametrow.csv
โ   โ   โโโ rodzaje_parametrow.pkl
โ   โ   โโโ SensoryPomiarowe.csv
โ   โ   โโโ SensoryPomiarowe.pkl
โ   โ   โโโ stacje_pom_api.json
โ   โ   โโโ StacjePomiarowe.xlsx
โ   โ   โโโ stacjeSmogoliczka.csv
โ   โโโ IndeksJakosciPowietrza.csv
โ   โโโ train_data.csv
โโโ LICENSE
โโโ notebooks
โ   โโโ Air\ Quality\ Index\ Gios.ipynb
โ   โโโ eda\ without\ progress-Copy4.ipynb
โ   โโโ Filtering\ excel\ files\ and\ picking\ right\ parameters.ipynb
โ   โโโ Fixing\ missing\ lat\ and\ lon\ in\ stations\ .ipynb
โ   โโโ loader_sql.py
โ   โโโ Matching\ stations\ synop\ with\ Smogoliczka\ .ipynb
โ   โโโ Matching\ synop\ data\ with\ smogoliczka.ipynb
โ   โโโ Matching\ Synop\ with\ Smogoliczka\ final.ipynb
โ   โโโ ML\ PM2.5.ipynb
โ   โโโ New\ Strategy\ script\ for\ excel\ files.ipynb
โ   โโโ __pycache__
โ   โ   โโโ loader_sql.cpython-38.pyc
โ   โโโ Repairing\ stations\ names\ and\ merging\ into\ one\ .ipynb
โ   โโโ Smogoliczka\ API\ to\ pomiary_pivot.ipynb
โโโ poetry.lock
โโโ pyproject.toml
โโโ README.md
โโโ requirements.txt
```

## โ๏ธ Built Using <a name = "built_using"></a>

- [MsSQL](https://www.microsoft.com/pl-pl/sql-server/sql-server-downloads) - Database
- [S3Bucket](https://aws.amazon.com/s3/) - Cloud storage
- [Coiled](https://coiled.io/) - Distributed computing
- [Dask](https://dask.org/) - Preprocessing data
- [Optuna](https://optuna.org/) - Hyperparameter optimization
- [Xgboost](https://xgboost.readthedocs.io/en/latest/) - ML
