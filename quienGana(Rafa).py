def quienGana(j1: str, j2: str) -> str : 
  if ((j1 == "Piedra" and j2 == "Tijera") or (j1 == "Tijera" and j2 == "Papel") or (j1 == "Papel" and j2 == "Piedra")):
    return "Jugador1"
  elif ((j2 == "Piedra" and j1 == "Tijera") or (j2 == "Tijera" and j1 == "Papel") or (j2 == "Papel" and j1 == "Piedra")):
    return "Jugador2"
  else:
    return "Empate"
