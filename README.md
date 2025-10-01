# Python Projects – APIs, Flask & Discord Bot  

This repository contains small but practical projects built with **Python**. They showcase the use of external libraries, APIs, and testing practices.  


## Projects  

### 1. Joke Teller – `CuentaChistes.py` or `JokeTeller.py`  
A program that consumes the **JokeAPI** to tell jokes in Spanish or English.  
- User can select the language.  
- If the joke has two parts (setup & delivery), the second part is displayed after 1 second (or user input).  

**Tech stack**:  
- `requests`  
- `time`  


### 2. Employee Management API – `app.py`  
A **Flask** web API to manage employees in a company.  

**Employee data**:  
- Full name  
- Email  
- Position  
- Salary  

**Available endpoints**:  
- Add employee  
- Delete employee  
- Update employee info (e.g. apply a raise)  

**Tech stack**:  
- `flask`  
- `json`  

#### Installation
1. Install Python 3.x
2. Create a virtual environment:
```powershell
pip install virtualenv
virtualenv myprojectenv
.\myprojectenv\Scripts\Activate.ps1
```
3. Install dependencies:
```powershell
pip install flask marshmallow
```
#### Run the App
1. Always run the Flask server first in a separate terminal:
```powershell
python .\app.py
```
- The API runs at: http://127.0.0.1:5000/api
2. Use a second PowerShell window to run Invoke-RestMethod commands
3. Restarting Flask will reset the list.

#### Using the API (PowerShell)

*Add a new employee (POST)*
```powershell
Invoke-RestMethod -Uri "http://127.0.0.1:5000/api/empleados" `
-Method POST `
-Headers @{ "Content-Type" = "application/json" } `
-Body '{"nombre": "Alice", "correo": "alice@example.com", "cargo": "Manager", "salario": 7000}'
```
*Update employee (PUT)*
```powershell
Invoke-RestMethod -Uri "http://127.0.0.1:5000/api/empleados/1" `
-Method PUT `
-Headers @{ "Content-Type" = "application/json" } `
-Body '{"salario": 7500}'
```
*Delete employee (DELETE)*
```powershell
Invoke-RestMethod -Uri "http://127.0.0.1:5000/api/empleados/1" -Method DELETE
```
#### Files Explained
proyecto_empleados/
- / __init__.py    Creates the Flask app and registers blueprints
- models.py        Employee class and in-memory list
- routes.py        API endpoints (CRUD operations)
- services.py      Business logic (add, delete, modify employees)
- schemas.py       Marshmallow schema for validation & serialization


### 3. Discord Joke Bot – `bot.py`  
A **Discord bot** that uses **JokeAPI** to tell jokes in English or Spanish, tagging the user who requested it.  

**Commands**:  
- `!chiste` → Joke in Spanish  
- `!joke` → Joke in English  

If the joke has two parts, they are shown in separate messages with a 1-second delay.  

**Unit Testing** with `unittest`:  
- Single-part joke in Spanish  
- Two-part joke in Spanish  
- Single-part joke in English  
- Two-part joke in English  

**Tech stack**:  
- `discord.py` (https://discordpy.readthedocs.io/en/stable/)  
- `requests`  
- `unittest` (built-in with Python)  
- `asyncio` (built-in with Python) 

#### Setup & Run the Bot 
1. Go to Discord Developer Portal and create a bot.
2. Copy your bot token.
3. Open bot.py and replace:
```python
client.run('INSERT TOKEN HERE')
```
4. Run the bot:
```bash
python bot.py
```
#### Files Explained
- api.py         Function to fetch jokes from JokeAPI
- bot.py         Discord bot implementation with commands
- test_bot.py    Unit tests for the API function

## Notes
- The Discord bot requires a valid token stored in a .env file.
- The Employee API can be tested with tools like Postman, Invoke-RestMethod or curl.
- These projects are intended for learning, experimentation, and as part of a personal portfolio.