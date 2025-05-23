# Lost and Found

## Introduction  
This is an online lost and found system that enables users to report, search, and manage objects lost or found within their organization or community.

## Problem Statement  
Losing personal items in public places is not rare, and there lacks a structured, centralized mechanism for reporting or searching for such items. This project bridges this gap by developing a reliable platform to connect people who lost something with people who found something.

## Objectives  
- To provide an easy-to-use platform for posting lost and found items.  
- To streamline item tracking and management.  
- To minimize the time and effort involved in returning lost items to their owners.

## Technology Stack  
- **Frontend:** HTML/CSS  
- **Backend:** Python, Django  
- **Database:** Django ORM (PostgreSQL)  
- **Others:**  
  - Docker  
  - Nginx  
  - MinIO (for storing uploaded media)  
  - Silk (for profiling and performance analysis)

## Installation Instructions  

1. clone the project
```
git clone https://github.com/luciorim/LostAndFoundApp_13P.git
```

2. go to project directory
```
cd LostAndFoundApp_13P
```

3. run server (Check that ports :8000 :5432 :9000 :9001 is free)
```
make up
```
4. open localhost in your browser

## Usage Guide

```
  on localhost/api/docs/ you can find rest api endpoins, but is not mentadory because the app uses template rendering
```
<img width="1440" alt="image" src="https://github.com/user-attachments/assets/e1991e20-19b3-4651-b805-9a8ba01b18aa" />


<img width="1328" alt="image" src="https://github.com/user-attachments/assets/5ba8f6e7-5a30-4a77-a9e9-ada3f6776ce0" />


<img width="1325" alt="image" src="https://github.com/user-attachments/assets/d89ef63b-3641-4158-a17c-d60db1a2a59c" />


<img width="1269" alt="image" src="https://github.com/user-attachments/assets/e2ffed23-8e71-4ac8-b634-258dd0641a24" />


<img width="1295" alt="image" src="https://github.com/user-attachments/assets/19a00758-f5cd-4a9d-bd88-314299ff7644" />


Owner or admin can change status of item and delete it


<img width="318" alt="image" src="https://github.com/user-attachments/assets/436104aa-958f-4248-9251-6a069ff76f21" />


<img width="1419" alt="image" src="https://github.com/user-attachments/assets/fdebf7ad-c01d-48f7-979c-3a8f5d1652d4" />


<img width="1375" alt="image" src="https://github.com/user-attachments/assets/b9e88e30-8002-46f6-a1e9-f044cb0d69ad" />


<img width="1433" alt="image" src="https://github.com/user-attachments/assets/c28cdd2b-7e60-4b64-922b-1b4c8abacd14" />


## Testing

No tests have been implemented. Instead you can test full functionality manually via UI. 
Admin user already created: 
login: admin
pass: admin

## Known Issues

1. No tests
2. Better frontend could be written
3. Didn't complete rest-api part to migrate project to modern architecture 

## References

1) https://stackoverflow.com/questions/70977435/how-do-i-parse-a-string-in-django-templates
2) https://www.digitalocean.com/community/tutorials/how-to-use-postgresql-with-your-django-application-on-ubuntu-22-04
3) https://medium.com/@mateusz-jasinski/using-minio-with-django-for-local-development-80bda22927
4) https://www.papertrail.com/solution/guides/nginx/


## Team Members

# Zhangeldin Nurdaulet, 220103261, 13P 





