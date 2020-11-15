<h1 align="center"><b>Tees.co.id Coding Test - Bajigur Cloth Backend API</b></h1>



Bajigur Cloth Backend API dibuat menggunakan bahasa python, framework fastAPI,
dan database mongoDB. Fitur utama (Highlight Feature) API ini adalah untuk
benefit admin, dan users sesuai dengan requirement coding test Tees.co.id.

### 
[![python](https://img.shields.io/badge/python-v3.9.0-blue)](https://www.python.org/downloads/release/python-390/)
[![fastapi](https://img.shields.io/badge/FastAPI-v0.61.2-brightgreen)](https://fastapi.tiangolo.com/)
[![mongoDB](https://img.shields.io/badge/mongoDB-4.2-lightgreen)](https://mongodb.com)
[![openAPI](https://img.shields.io/badge/openAPI-v3.0.2-yellowgreen)](https://www.openapis.org/)
[![swagger](https://img.shields.io/badge/swagger-valid-brightgreen)](https://swagger.io/)
[![uvicorn](https://img.shields.io/badge/uvicorn-v0.12.2-red)](https://www.uvicorn.org/)
[![heroku](https://img.shields.io/badge/heroku-server-9cf)](https://www.heroku.com/)


## Live API dan Dokumentasi
- Live API url: https://bajigur-cloth.herokuapp.com/
- Dokumentasi: https://bajigur-cloth.herokuapp.com/docs
<img src="https://raw.githubusercontent.com/rozy97/pic/master/fastapi-documentation.png">

## Requirements
1. <a href="https://nodejs.org/en/download/">Node Js</a>
2. Node_modules
3. <a href="https://www.getpostman.com/">Postman</a>
4. Web Server (ex. localhost)

## How to run the app ?
1. Open app's directory in CMD or Terminal
2. Type `npm install`
3. Make new file a called **.env**, set up first [here](#set-up-env-file)
4. Crate cloud mongoDB cluster using mongoDB atlas or using local mongoDB database
5. Connect your mongoDB to **config.js**
6. Open Postman desktop application or Chrome web app extension that has installed before
7. Choose HTTP Method and enter request url.(ex. localhost:3030/notes)
8. You can see all the end point [here](#end-point)

## End Point
**1. GET**
* `/users`
* `/packages/:id`
* `/history/:id` (Get history transaction by id)
* `/category

**2. POST**
* `/packages`
    * ``` { "title": "Xtra Combo", "description": "Fly in the sky", "image": "sky.jpg", "date_released": "2019-10-08", "genre_id": "2", "availability": "1" } ```

* `/history/:id`
    * ``` { "userrating": "req.body.rating" } ```
    
* `/category`
   * ``` { "name": "Roaming", "image": "http://picsum.co/tel.png" } ```

## End Point (API Documentation)
Open [documentation.rest]() file in vscode then run it to se more about API documentation. (dont forget to install REST client extension to enable running dotrest file documentation)
<img src="https://raw.githubusercontent.com/rozy97/pic/master/api-documentation.png">

## Contributors
<p align="center">
<table border="0">
  <tr>
    <td align="center">
      <a href="https://github.com/firmansyahfachmi">
        <img width="150" src="https://avatars1.githubusercontent.com/firmansyahfachmi" alt="M Fachmi Firmansyah"><br/>
          <sub><b>M Fachmi Firmansyah</b></sub>
      </a>
    </td>
    <td align="center">
      <a href="https://github.com/mahendragalih26">
        <img width="150" src="https://avatars1.githubusercontent.com/mahendragalih26" alt="Galih Mahendra W"><br/>
          <sub><b>Galih Mahendra W</b></sub>
      </a>
    </td>
    <td align="center">
      <a href="https://github.com/rozy97">
        <img width="150" src="https://avatars1.githubusercontent.com/rozy97" alt="Firmansyah Rozy"><br/>
          <sub><b>Firmansyah Rozy</b></sub>
      </a>
    </td>
    <td align="center">
      <a href="https://github.com/Gimindika">
        <img width="150" src="https://avatars1.githubusercontent.com/Gimindika" alt="Gerrit Indika Mulya"><br/>
          <sub><b>Gerrit Indika Mulya</b></sub>
      </a>
    </td>
  </tr>
</table>
</p>