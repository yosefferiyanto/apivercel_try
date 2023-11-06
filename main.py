import pandas as pd
from fastapi import FastAPI, HTTPException, Header

df = pd.read_csv('players.csv')

app = FastAPI()

API_KEY = "testingapitokenkey1234" # Testing API token key 1234

@app.get("/")
def home():
    return {"message":"Welcome to All Players API, place to get player list"}

@app.get("/players")
def getAllPlayers(api_key: str = Header(None)):
    print(api_key)
    if api_key is None or api_key != API_KEY:
        raise HTTPException(status_code=401, detail="Invalid API Key")
    else:
        return df.to_dict(orient='records')
    
@app.get("/players/state/{state}")
def getPlayerbyState(state:str,api_key:str=Header(None)):
    print(state)
    print(api_key)
    if api_key is None or api_key != API_KEY:
        raise HTTPException(status_code=401, detail="Invalid API Key")
    else:
        player_by_state = df[df['state']==state]
        return player_by_state.to_dict(orient='records')
    
@app.get("/players/year/{year}")
def getPlayerbyYear(year:str,api_key:str=Header(None)):
    print(year)
    print(api_key)
    if api_key is None or api_key != API_KEY:
        raise HTTPException(status_code=401, detail="Invalid API Key")
    else:
        player_by_year = df[df['year']==year]
        return player_by_year.to_dict(orient='records')
    
@app.get("/players/position/{position}")
def getPlayerbyPosition(position:str,api_key:str=Header(None)):
    print(position)
    print(api_key)
    if api_key is None or api_key != API_KEY:
        raise HTTPException(status_code=401, detail="Invalid API Key")
    else:
        player_by_position = df[df['position']==position]
        return player_by_position.to_dict(orient='records')