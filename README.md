# Project Introduction

## Project access
> After the project is running, visit the following address. Change the IP address to your own. If it is local, it is localhost. The port is the set port. The default is 8080.


Frontend：/front/index.html

Backend：/backend/index.html

> The local default is these two addresses:
> 
> Frontend：[localhost:8080/front/index.html](localhost:8080/front/index.html)
> 
> Backend：[localhost:8080/backend/index.html](localhost:8080/backend/index.html)


> For test purpose, use username "admin" and password "123456", You can modify the database information in the src/main/resources/application.yml file
>
## Food delivery

&emsp;&emsp;This project is a front-end and back-end separated takeout management system of SpringBoot+MybatisPlus + Mysql technology stack.

&emsp;&emsp;The project is currently divided into two versions: V1 and V2. Compared with the V1 version, the V2 version incorporates Redis technology and some optimizations elsewhere.


- Frontend preview

![Frontend](https://github.com/codermast/Takeout-food/blob/master/resource/%E6%88%AA%E5%B1%8F2022-12-01%2019.32.09.png?raw=true)
- Backend preview

![Backend](https://github.com/codermast/Takeout-food/blob/master/resource/%E6%88%AA%E5%B1%8F2022-12-01%2019.37.24.png?raw=true)
## Tech Stacks
- SpringBoot
- MySql
- Mybatis Plus
- Redis

## Project module
- 🔺Backend
   - [x] Login module
   - [x] Employee management
   - [x] Category management
   - [x] Dishes management
   - [x] Package management
   - [x] Order management
- 🔻Frontend
   - [x] User modules
   - [x] Shopping cart module
   - [x] address module
   - [x] Order module
   - [x] Menu module

   ## Project deployment

   1. Download this project to the server.
   
   2. Modify the database information in the `src/main/resources/application.yml` file
   > What needs to be changed in V1 are the three places explained below.
      - Database name
      - database username
      - Database password
   > V2 also needs to add Redis configuration information
   3. When deploying on the server, package the project into a `jar` package and run it using `java -jar package name`
   4. Visit the backend: [localhost:8080/backend/page/login.html](http://localhost:8080/backend/page/login.html)
   5. Visit the front desk: [localhost:8080/front/page/login.html](http://localhost:8080/front/page/login.html)
## Version content
### V1 version
- SpringBoot
- MybatisPlus
- Mysql
- Session

### V2 version
- SpringBoot
- MybatisPlus
- Mysql
- Redis

**Content cached to Redis:**
- [x] Caching SMS verification codes
- [x] Caching dish information
- [x] Caching user information
- [x] Cache address information
- [x] Caching package information