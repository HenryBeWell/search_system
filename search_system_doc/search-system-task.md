# SDE Coding Challenge @ Aspecta.ai

Thank you for applying for the SDE position at Aspecta.ai. We will ask you to complete a coding challenge to show your expertise. 

You will have 3 days to complete several tasks. During the challenge period, if you have any questions, please contact rick@aspecta.ai. 

## Task description
* You will have the following resources:
	1) A scenario description received from the Product team.
	2) One `.csv` data file received from the Alg team, containing necessary data for building a search service.
	3) One API call example.

* You are asked to complete the following coding tasks:
	1) **Construct Database**. Using the give `.csv` file, construct a SQL or MongoDB database.
	2) **Build Search Service**. Develop a search service that opens an API to external users. See an API query/output example in this doc.
	3) **Build Cache System (Optional)**. Build a cache system so that a repeat query will not consume computation resources.
	4) **Build Authorization System (Optional)**. Build an authorization system, allow only users with certain `appid` to use the service (you can assign a legal `appid` by yourself).
	5) **Load Testing (Optional)**. After deploying the search system, use any framework you like to do load testing and analyze how the cache system and authorization system influence the efficiency.

## Task requirements
* *Implementation.*
    * You may use any frameworks, libraries, or languages you deem appropriate to build this project. However, using a modern framework, such as Flask, is preferred, as it aligns best with our current development practices.
    * You can build the service on your localhost (127.0.0.1). If you wish to build the service on a remote server, we are happy to provide one.
    * Efficiency is a key index of the search service. Try to use any methods you know to improve efficiency.

* *Time.* 
    * This project should take no more than 8 hours of work, and should be completed within 3 days of receipt. 
    * In case you don't have time to finish all the tasks, please try to do the tasks in order, since they come from simple to hard. 


## Deliverables
1. A **private** GitHub code repo with all necessary files for us to run the code locally. Add sirui@aspecta.ai as a member with admin access, so that we can review the code and also test it ourselves. **Please do not post publicly.**
2. In the repo, have a README file for documentation. Document the steps for us to install dependencies and launch the project. You can also include your high-level thought process for any important design/implementation decisions you have made.
3. Try to use small commits, and keep commit messages informative.

## Task resources
### Scenario description
The Aspecta.ai Talent Compute Engine has computed skill scores for millions of talents. Now we wish to build a downstream application that use the scores to provide candidates search services.

1. Given the output scores of the engine, you need to build a database to store the scores.
2. The search service inputs `(skill_name, page, page_size)`. Then you need to find candidates sorted by their `skill_name` scores, and return proper candidates with ranks defined by `page` and `page_size`. E.g., if `page=2, page_size=10` then return the candidates that are ranked 11-20. 
3. To provide users with more information, you also need to return other related skills the candidates have and the average score of each skill.
4. To promote service efficiency and security, you are suggested to build a cache system and authorization system. You are also suggested to use load-testing tools to analyze efficiency.
5. You can find an API query/output example in this doc.

### Data files
A `candidate_skill_scores.csv` file is attached. Each row is a record. `candidate_name` is anonymized.

### API call
* *Example search API call*
```
curl --header "Content-Type: application/json" \
  --request POST \
  --data '{"skill_name": "smart contracts", "appid": "<YOUR_APPID>", "page":1, "page_size": 5}' \
  http://<YOUR_IP>/search_candidates
```
* *Example return*
```
{
    "candidates": [
        {
            "candidate_name": "aantonop",
            "main_skill_score": 100.0,
            "related_skills": [
                {
                    "name": "backend",
                    "score": 73.99,
                    "average": 73.92,
                    "sources": [
                        "github"
                    ]
                },
                {
                    "name": "ethereum",
                    "score": 96.05,
                    "average": 76.36,
                    "sources": [
                        "github"
                    ]
                },
                {
                    "name": "smart contracts",
                    "score": 100.0,
                    "average": 78.75,
                    "sources": [
                        "github"
                    ]
                },
                {
                    "name": "solidity",
                    "score": 96.45,
                    "average": 76.44,
                    "sources": [
                        "github"
                    ]
                },
                {
                    "name": "bitcoin",
                    "score": 94.0,
                    "average": 76.73,
                    "sources": [
                        "github"
                    ]
                },
                {
                    "name": "database",
                    "score": 0.0,
                    "average": 75.37,
                    "sources": null
                },
                {
                    "name": "cryptocurrency",
                    "score": 0.0,
                    "average": 77.13,
                    "sources": null
                },
                {
                    "name": "frontend",
                    "score": 0.0,
                    "average": 73.45,
                    "sources": null
                },
                {
                    "name": "hyperledger",
                    "score": 0.0,
                    "average": 80.28,
                    "sources": null
                }
            ]
        },
        {
            "candidate_name": "github-actions[bot]",
            "main_skill_score": 100.0,
            "related_skills": [
                {
                    "name": "frontend",
                    "score": 100.0,
                    "average": 73.45,
                    "sources": [
                        "github"
                    ]
                },
                {
                    "name": "backend",
                    "score": 100.0,
                    "average": 73.92,
                    "sources": [
                        "github"
                    ]
                },
                {
                    "name": "cryptocurrency",
                    "score": 100.0,
                    "average": 77.13,
                    "sources": [
                        "github"
                    ]
                },
                {
                    "name": "ethereum",
                    "score": 100.0,
                    "average": 76.36,
                    "sources": [
                        "github"
                    ]
                },
                {
                    "name": "database",
                    "score": 100.0,
                    "average": 75.37,
                    "sources": [
                        "github"
                    ]
                },
                {
                    "name": "smart contracts",
                    "score": 100.0,
                    "average": 78.75,
                    "sources": [
                        "github"
                    ]
                },
                {
                    "name": "hyperledger",
                    "score": 89.05,
                    "average": 80.28,
                    "sources": [
                        "github"
                    ]
                },
                {
                    "name": "solidity",
                    "score": 95.51,
                    "average": 76.44,
                    "sources": [
                        "github"
                    ]
                },
                {
                    "name": "bitcoin",
                    "score": 96.23,
                    "average": 76.73,
                    "sources": [
                        "github"
                    ]
                }
            ]
        },
        {
            "candidate_name": "ethers",
            "main_skill_score": 100.0,
            "related_skills": [
                {
                    "name": "ethereum",
                    "score": 89.32,
                    "average": 76.36,
                    "sources": [
                        "github"
                    ]
                },
                {
                    "name": "smart contracts",
                    "score": 100.0,
                    "average": 78.75,
                    "sources": [
                        "github"
                    ]
                },
                {
                    "name": "solidity",
                    "score": 95.68,
                    "average": 76.44,
                    "sources": [
                        "github"
                    ]
                },
                {
                    "name": "bitcoin",
                    "score": 91.62,
                    "average": 76.73,
                    "sources": [
                        "github"
                    ]
                },
                {
                    "name": "frontend",
                    "score": 0.0,
                    "average": 73.45,
                    "sources": null
                },
                {
                    "name": "backend",
                    "score": 0.0,
                    "average": 73.92,
                    "sources": null
                },
                {
                    "name": "cryptocurrency",
                    "score": 0.0,
                    "average": 77.13,
                    "sources": null
                },
                {
                    "name": "database",
                    "score": 0.0,
                    "average": 75.37,
                    "sources": null
                },
                {
                    "name": "hyperledger",
                    "score": 0.0,
                    "average": 80.28,
                    "sources": null
                }
            ]
        },
        {
            "candidate_name": "frangio",
            "main_skill_score": 100.0,
            "related_skills": [
                {
                    "name": "ethereum",
                    "score": 96.13,
                    "average": 76.36,
                    "sources": [
                        "github"
                    ]
                },
                {
                    "name": "backend",
                    "score": 75.52,
                    "average": 73.92,
                    "sources": [
                        "github"
                    ]
                },
                {
                    "name": "smart contracts",
                    "score": 100.0,
                    "average": 78.75,
                    "sources": [
                        "github"
                    ]
                },
                {
                    "name": "solidity",
                    "score": 98.3,
                    "average": 76.44,
                    "sources": [
                        "github"
                    ]
                },
                {
                    "name": "frontend",
                    "score": 0.0,
                    "average": 73.45,
                    "sources": null
                },
                {
                    "name": "cryptocurrency",
                    "score": 0.0,
                    "average": 77.13,
                    "sources": null
                },
                {
                    "name": "database",
                    "score": 0.0,
                    "average": 75.37,
                    "sources": null
                },
                {
                    "name": "hyperledger",
                    "score": 0.0,
                    "average": 80.28,
                    "sources": null
                },
                {
                    "name": "bitcoin",
                    "score": 0.0,
                    "average": 76.73,
                    "sources": null
                }
            ]
        },
        {
            "candidate_name": "renovate[bot]",
            "main_skill_score": 100.0,
            "related_skills": [
                {
                    "name": "frontend",
                    "score": 100.0,
                    "average": 73.45,
                    "sources": [
                        "github"
                    ]
                },
                {
                    "name": "backend",
                    "score": 100.0,
                    "average": 73.92,
                    "sources": [
                        "github"
                    ]
                },
                {
                    "name": "cryptocurrency",
                    "score": 92.92,
                    "average": 77.13,
                    "sources": [
                        "github"
                    ]
                },
                {
                    "name": "ethereum",
                    "score": 100.0,
                    "average": 76.36,
                    "sources": [
                        "github"
                    ]
                },
                {
                    "name": "database",
                    "score": 100.0,
                    "average": 75.37,
                    "sources": [
                        "github"
                    ]
                },
                {
                    "name": "smart contracts",
                    "score": 100.0,
                    "average": 78.75,
                    "sources": [
                        "github"
                    ]
                },
                {
                    "name": "hyperledger",
                    "score": 89.83,
                    "average": 80.28,
                    "sources": [
                        "github"
                    ]
                },
                {
                    "name": "solidity",
                    "score": 100.0,
                    "average": 76.44,
                    "sources": [
                        "github"
                    ]
                },
                {
                    "name": "bitcoin",
                    "score": 93.52,
                    "average": 76.73,
                    "sources": [
                        "github"
                    ]
                }
            ]
        }
    ]
}
```
