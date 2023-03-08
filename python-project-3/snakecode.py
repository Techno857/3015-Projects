import random


def avoid_borders(data, possible_moves):
    my_head = data['you']['head']
    
    if my_head['x'] == data['board']['width']-1:
      possible_moves.remove("right")
    if my_head['x'] == 0:
      possible_moves.remove("left")
    if my_head['y'] == data['board']['height']-1:
      possible_moves.remove("up")
    if my_head['y'] == 0:
      possible_moves.remove("down")

def avoid_myself(data, my_head, my_body, possible_moves):
    for dictionary in my_body:
      if my_head["x"] + 1 == dictionary["x"] and my_head["y"] == dictionary["y"] and 'right' in possible_moves:
        possible_moves.remove("right")
      elif my_head["x"] - 1 == dictionary["x"] and my_head["y"] == dictionary["y"] and 'left' in possible_moves:
        possible_moves.remove("left")
      elif my_head["y"] + 1 == dictionary["y"] and my_head["x"] == dictionary["x"] and 'up' in possible_moves:
        possible_moves.remove("up")
      elif my_head["y"] - 1 == dictionary["y"] and my_head["x"] == dictionary["x"] and 'down' in possible_moves:
        possible_moves.remove("down")

def snake_safe(data, my_head, possible_moves):
  for hazard in data['board']['hazards']:
    if my_head['x'] + 1 == hazard['x'] and my_head['y'] == my_head['y'] and 'right' in possible_moves:
      possible_moves.remove('right')
    elif my_head["x"] - 1 == hazard["x"] and my_head["y"] == hazard["y"] and 'left' in possible_moves:
      possible_moves.remove("left")
    elif my_head["y"] + 1 == hazard["y"] and my_head["x"] == hazard["x"] and 'up' in possible_moves:
      possible_moves.remove("up")
    elif my_head["y"] - 1 == hazard["y"] and my_head["x"] == hazard["x"] and 'down' in possible_moves:
      possible_moves.remove("down")

  for snake_bodies in data['board']['snakes']:
    for body in snake_bodies['body']:
      if my_head['x'] + 1 == body['x'] and body['y'] == my_head['y'] and 'right' in possible_moves:
        possible_moves.remove('right')
      elif my_head["x"] - 1 == body["x"] and my_head["y"] == body["y"] and 'left' in possible_moves:
        possible_moves.remove("left")
      elif my_head["y"] + 1 == body["y"] and my_head["x"] == body["x"] and 'up' in possible_moves:
        possible_moves.remove("up")
      elif my_head["y"] - 1 == body["y"] and my_head["x"] == body["x"] and 'down' in possible_moves:
        possible_moves.remove("down")


def dinner_time(data, my_head, possible_moves):
  current_health = data['you']['health']
  priority_moves = []

  if current_health < 65:
    try:
      if my_head['x'] < data['board']['food'][0]['x'] and 'right' in possible_moves:
        priority_moves.append('right')
      if my_head['x'] > data['board']['food'][0]['x'] and 'left' in possible_moves:
        priority_moves.append('left')
      if my_head['y'] > data['board']['food'][0]['y'] and 'down' in possible_moves:
        priority_moves.append('down')
      if my_head['y'] < data['board']['food'][0]['y'] and 'up' in possible_moves:
        priority_moves.append('up')

    except:
      return priority_moves

  return priority_moves 




def choose_move(data: dict) -> str:

  my_head = data["you"]["head"]  # A dictionary of x/y coordinates like {"x": 0, "y": 0}
  my_body = data["you"]["body"]  # A list of x/y coordinate dictionaries like [ {"x": 0, "y": 0}, {"x": 1, "y": 0}, {"x": 2, "y": 0} ]

  possible_moves = ["up", "down", "left", "right"]

  avoid_borders(data, possible_moves)
  print('happens first')

  avoid_myself(data, my_head, my_body, possible_moves)
  print('happens second')

  snake_safe(data, my_head, possible_moves)
  print('happens third')

  when_hungry = dinner_time(data, my_head, possible_moves)
  print('happens fourth')

  print(possible_moves)
  print(when_hungry)
  print(data['you']['health'])

  if when_hungry == []:
    move = random.choice(possible_moves)
    print(f'went for a random, at turn: {data["turn"]}\n')
  elif len(when_hungry) > 0:
    move = random.choice(when_hungry)
    print(f"went for food, at turn: {data['turn']}\n" )
  

  return move