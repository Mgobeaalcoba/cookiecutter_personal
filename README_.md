Requiremientos
Anaconda >= 4.x
git >= 2.x
Cookiecutter Python package >= 1.4.0: Esto puede ser instalado con pip o conda dependiendo cómo tú manejas tus paquetes de Python:
pip install cookiecutter

o

conda install -c conda-forge cookiecutter
Crear un nuevo proyecto

En el directorio en el que quieras guardar tu proyecto generado:

cookiecutter https://github.com/Mgobeaalcoba/cookiecutter_personal.git

Estructura de directorios y archivos resultantes
{{ cookiecutter.project_slug }}
    ├── data
    │   ├── processed      <- The final, canonical data sets for modeling.
    │   └── raw            <- The original, immutable data dump.
    │
    ├── notebooks          <- Jupyter notebooks. Naming convention is a number (for ordering),
    │                         the creator's initials, and a short `-` delimited description, e.g.
    │                         `1.0-jvelezmagic-initial-data-exploration`.
    │
    ├── .gitignore         <- Files to ignore by `git`.
    │
    ├── environment.yml    <- The requirements file for reproducing the analysis environment.
    │
    └── README.md          <- The top-level README for developers using this project.
