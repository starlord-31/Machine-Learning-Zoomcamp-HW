import requests

url = 'http://localhost:9696/predict'

player_id = 'xyz-123'
player_attributes = {
    'age': 25.0, 
    'ball_control': 59.0, 
    'dribbling': 63.0, 
    'slide_tackle': 68.0, 
    'stand_tackle': 73.0, 
    'aggression': 72.0, 
    'reactions': 68.0, 
    'att_position': 30.0, 
    'interceptions': 65.0, 
    'vision': 30.0, 
    'composure': 50.0,
    'crossing': 33.0, 
    'short_pass': 64.0, 
    'long_pass': 49.0, 
    'acceleration': 51.0, 
    'stamina': 65.0, 
    'sprint_speed': 62.0, 
    'heading': 64.0, 
    'shot_power': 54.0, 
    'finishing': 50.0, 
    'long_shots': 51.0, 
    'curve': 52.0, 
    'fk_acc': 64.0, 
    'penalties': 51.0, 
    'volleys': 33.0, 
    'gk_positioning': 10.0, 
    'gk_diving': 11.0, 
    'gk_handling': 6.0, 
    'gk_kicking': 7.0, 
    'gk_reflexes': 9.0
}

response = requests.post(url, json=player_attributes).json()
print(response)