[TOC]

# search_system

This is a search service implemented using Django, Redis, and MySQL. The service allows users to search for candidates by their skills, and provides related skills for each candidate.

## Requirements

To run the service, you need to have the following dependencies installed:

- Python 3.7+
- Django 3.2+
- Redis 5.0+
- MySQL 8+

Other dependencies are listed in the `requirements.txt` file. 

## Setup

1. Clone the repository to your local machine:

```bash
git clone https://github.com/henrybewell/search_system.git
```

2. Create a virtual environment for the project:

```bash
cd search_system
python -m venv venv
source venv/bin/activate
```

3. Install the dependencies:

```bash
pip install -r requirements.txt
```

4. Create a MySQL database for the project:

```bash
mysql -u root -p
CREATE DATABASE aspecta;
```

5. Configure the database settings in `settings.py`:

```
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'aspecta',
        'USER': 'your_mysql_username',
        'PASSWORD': 'your_mysql_password',
        'HOST': 'localhost',
        'PORT': '3306',
    }
}
```

6. Create the database tables:

```bash
python manage.py makemigrations
python manage.py migrate
```

7. Start the Redis server:

```bash
redis-server
```

8. Configure the cache settings in `settings.py`:

```
CACHES = {
    "default": {
        "BACKEND": "django_redis.cache.RedisCache",
        "LOCATION": "redis://127.0.0.1:6379",
        "OPTIONS": {
            "CLIENT_CLASS": "django_redis.client.DefaultClient",
        }
    }
}
```

9. Run the Django development server:

```bash
python manage.py runserver
```

## Usage

1. Create records which include some candidates, scores and their skills by `candidates.utils.export_csv_to_sql`

2. Platform Table

   In order to associate each candidate's skill score with the platform it was sourced from, you need to create a `platform` table in the MySQL database. The table should have the following columns:

   - `id`: An auto-incrementing integer ID for each platform.
   - `name`: The name of the platform.

   Once you've created the table, you can add new platforms to it using SQL commands. Then, when you add new skill scores to the `candidate_skill_scores` table, you can add ids to `platform_sources ` include the ID of the platform and  the ID of the candidate_skill_scores that the data was sourced from.

3. To search for candidates based on their skill sets, send a `POST` request to the `/search_candidates` endpoint with the following parameters:

   | Field name   | Type    | Description                                                  |
   | ------------ | ------- | ------------------------------------------------------------ |
   | `skill_name` | string  | The name of the skill to search for.                         |
   | `appid`      | string  | The unique identifier for your application.                  |
   | `page`       | integer | The page number of the search results to retrieve. Default: 1. |
   | `page_size`  | integer | The number of search results to return per page. Default: 10. |

   Example request body:

   ```json
   {
    "skill_name": "frontend",
    "appid": "<YOUR_APPID>",
    "page": 1,
    "page_size": 5
   }
   ```

   Response body:

   ```json
   {
    "count": 29,
    "candidates": [
        {
            "main_skill_score": "90.50",
            "candidate_name": "mdzqe",
            "related_skills": [
                {
                    "name": "test1",
                    "score": "92.00",
                    "sources": [
                        "meatamask"
                    ],
                    "average": 50.0
                },
                {
                    "name": "test2",
                    "score": "40.00",
                    "sources": [
                        "github",
                        "meatamask",
                        "csdn"
                    ],
                    "average": 40.0
                }
            ]
        },
        {
            "main_skill_score": "90.21",
            "candidate_name": "hizmy",
            "related_skills": [
                {
                    "name": "test1",
                    "score": "8.00",
                    "sources": [],
                    "average": 50.0
                }
            ]
        }
    ]
   }
   ```
   
   | Parameter        | Type   | Description                                                 |
   | ---------------- | ------ | ----------------------------------------------------------- |
   | count            | int    | Total number of candidates found based on the search query  |
   | candidates       | list   | List of candidate objects returned by the search service    |
   | candidate_name   | string | Name of the candidate                                       |
   | main_skill_score | string | Score of the candidate's main skill                         |
   | related_skills   | list   | List of related skill objects for the candidate             |
   | name             | string | Name of the related skill                                   |
   | score            | string | Score of the related skill                                  |
   | sources          | list   | List of sources that contributed to the related skill score |
   | average          | float  | Average score of the related skill across all sources       |

## Cache

This search service uses Redis as a cache to speed up search requests. Redis stores search results for a set amount of time (configured using the `CACHE_TTL` setting in `settings.py`) to avoid hitting the database for every search request.

## Database

This search service uses MySQL as the primary database to store information.

1. The `candidate_skill_scores` table stores candidates, skill and their scores information.
2. The `platform` table stores platform information,  such as github, metamask, etc.
3. The `platform_sources ` table stores  platform ID and candidate_skill_scores ID to associate each candidate's skill score and the platform it was sourced from.

## Authentication

To authenticate your requests, include your `appid` in the request body. The `appid` is a unique identifier for your application. Requests without a valid `appid` will receive a `403 Forbidden` response. Only  certain `appid` to use the service,default `Aspecta.ai` (you can assign a legal `appid` in `settings.APP_ID` by yourself)

## Contributions

Contributions are welcome! If you find any bugs or have suggestions for new features, feel free to open an issue or pull request.