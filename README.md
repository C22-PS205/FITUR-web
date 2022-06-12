# bangkit2022-C22-PS205
# FITUR-web for Bangkit Capstone Project 2022
## Prerequisite
- Python 3

## Setup


Clone the repository and go to the cloned folder.
```bash
git clone https://github.com/C22-PS205/FITUR-web
cd Fitur-web
```

Create python virtual environment.
```bash
pip install virtualenv
virtualenv venv
```

Initialize virtual environment :
```bash
source venv/bin/activate
```
for windows :
```
.\venv\bin\activate
```

run the app with Flask
```bash
flask run
```

For the finishing, open http://127.0.0.1:5000/ on your browser.

## API

### Recognize Image

----
return as render_template
* **URL**

  /result

* **Method:**

  `POST`

* **Content-Type**

  `multipart/form-data`

* **Data Params**

   `image=[file]`

* **Success Response:**

  * **Code:** 200 <br />
