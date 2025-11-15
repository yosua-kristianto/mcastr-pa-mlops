# # McAstr PA's MLOps

This repository contains implementation of MLOps worker for my blog post titled 
**"Building an Emotion Aware Response Model through Sentiment Analysis and Information Crowding Architecture"**.

## Installation guide:

1. Create a python Virtual Environment

Run `python -m venv .venv`

2. Activate the virtual environment

> Linux
> 
> `source /.venv/bin/activate`

> Windows
> 
> `/.venv/Scripts/activate`

3. Install all required dependencies

> `pip install -r requirements.txt`

4. Run MySQL database

You can either pull it from Docker and run the instance, or install it from MySQL's official download link.

5. Create `.env` file

The environment variable file used to store credential and secrets value. See `.env.example` file for references. 
Put the `.env` file in the root of project. This is an example for my local `.env` file:

```env
DATABASE_HOST=localhost
DATABASE_PORT=3306
DATABASE_USER=root
DATABASE_PASSWORD=root
DATABASE_NAME=mcastr_pa_system
```

5. Run database migration from the FastAPI Backend Projct

If you haven't clone the backend project, clone the [McAstr PA BE repository](https://github.com/yosua-kristianto/mcastr-pa-be).

Follow guide within readme.md for database setup, and run the migration from the root of the bckend project with this command below:

`python /resources/database/migration.py`

6. (Optional) You may want to pre-seed the data if needed.

7. Initializing knowledge

The implementation of this project, uses knowledge from [adhamelkomy's kaggle repository.](https://www.kaggle.com/datasets/adhamelkomy/twitter-emotion-dataset)
Download the emotion.csv in the root of this project.

8. Running the Project

`python main.py`

# Contribution

Interested to contribute in this repository? Any questions or feedbacks?

Feel free to email me to yosua_kristianto144@outlook.com