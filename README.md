<h1 align="center"><b>Tees.co.id Coding Test - Bajigur Cloth Backend API</b></h1>



Bajigur Cloth Backend API dibuat menggunakan bahasa python, framework fastAPI,
dan database mongoDB. Fitur utama (Highlight Feature) API ini adalah untuk
benefit admin, dan users sesuai dengan requirement coding test Tees.co.id.

### 
[![python](https://img.shields.io/badge/python-v3.9.0-blue)](https://www.python.org/downloads/release/python-390/)
[![pypi](https://warehouse-camo.ingress.cmh1.psfhosted.org/cd7ef4975d71b4a87a35b3c01b5b1ec8481c4549/68747470733a2f2f696d672e736869656c64732e696f2f707970692f762f7069702e737667)](https://pypi.org/project/pip/)
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
1. <a href="https://www.python.org/downloads/release/python-390/">python 3.9.0</a>
2. <a href="https://pypi.org/project/pip/">pip 20.2.4</a>


## How to run the app ?
1. `pip install -r requirements.txt`
2. `uvicorn server:app`
3. You can test the API via postman or documentation at http://localhost:8000/docs

## Penjelasan Fitur berdasarkan soal coding test
**Bajigur Cloth ingin memanfaatkan data belanja sebelumnya dari para member tersebut untuk memberikan experience berbelanja yang baik dan dapat dipersonalisasi.**


**1. Fitur apa yang krusial dibutuhkan oleh tim dan admin Bajigur Cloth untuk dapat memberikan pelayanan dengan baik?**
*  `POST /api/v1/admin/coupons` admin membuat kupon sesuai kebutuhan
*  `POST /api/v1/admin/coupons/share` pemberian kupon kepada user untuk menambah daya beli
*  `POST /api/v1/admin/coupons/share/{user_id}` pemberian kupon ke user tertentu sesuai kebutuhan
*  `POST /api/v1/admin/items/apply_discount` memberi diskon ke produk yang kurang laku atau produk lama untuk meningkatkan penjualan

**2. Fitur apa yang krusial dibutuhkan member Bajigur Cloth untuk dapat berbelanja dengan baik?**
*  `GET /api/v1/users/product_suggestions` menampilkan list produk berdasarkan riwayat order, riwayat pencarian, wishlist, etc.
*  `GET /api/v1/users/product_discounts` menampilkan list produk yang sedang diskon agar user tidak ketinggalan promosi
*  `GET /api/v1/users/user_membership_level` menampilkan status level user. semakin tinggi level, maka semakin banyak benefit seperti kupon & diskon. point level akan bertambah setiap user melakukan order

##
***firmansyah rozy***
