# Lost and Found

## Introduction  
This project is a web-based lost and found item tracking system for users to report, browse, and manage lost or found objects in their community or organization.

## Problem Statement  
Losing personal items in public places is common, and there is no centralized, structured system for reporting or tracking such items. This project addresses this gap by providing a reliable platform to connect people who lost items with those who found them.

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

<img width="1328" alt="image" src="https://github.com/user-attachments/assets/5ba8f6e7-5a30-4a77-a9e9-ada3f6776ce0" />


<img width="1325" alt="image" src="https://github.com/user-attachments/assets/d89ef63b-3641-4158-a17c-d60db1a2a59c" />


<img width="1269" alt="image" src="https://github.com/user-attachments/assets/e2ffed23-8e71-4ac8-b634-258dd0641a24" />


<img width="1295" alt="image" src="https://github.com/user-attachments/assets/19a00758-f5cd-4a9d-bd88-314299ff7644" />


Owner or admin can change status of item and delete it
<img width="318" alt="image" src="https://github.com/user-attachments/assets/436104aa-958f-4248-9251-6a069ff76f21" />


## Testing

No tests have been implemented 

## Known Issues

1. No tests
2. Better frontend could be written 

## References

1) https://stackoverflow.com/questions/70977435/how-do-i-parse-a-string-in-django-templates
2) https://www.digitalocean.com/community/tutorials/how-to-use-postgresql-with-your-django-application-on-ubuntu-22-04
3) https://medium.com/@mateusz-jasinski/using-minio-with-django-for-local-development-80bda22927
4) https://www.papertrail.com/solution/guides/nginx/


## Team Members

# Zhangeldin Nurdaulet, 220103261, 13P 





