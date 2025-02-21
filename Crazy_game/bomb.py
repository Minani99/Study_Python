# 맵 > 물풍선 정보
# [{pos: Pos, owner: str, power: int}, ...]

# 물풍선 > 맵 정보
# 현재 터지는 물풍선[], 남은 물풍선[]
# [{pos: Pos, owner: str, power: int}, ...]

BOMB_TIMER = 2

class _Bomb:
    def __init__(root, owner="player", power=1):
        root.owner = owner
        root.power = power
        root.timer = BOMB_TIMER

    def tick(root):
        root.timer -= 1

class Bomb:
    current_tick = 0
    bomb_list = {} # {pos: _Bomb}
    
    @classmethod
    def tick(cls, info):
        d = [] # 삭제될 폭탄들
        for p in info:
            if p in cls.bomb_list: # 둘 다 있음: 틱-1
                cls.bomb_list[p].tick()
                if cls.bomb_list[p].timer < 0:
                    d.append(p)
            else: # info엔 있는데 list에는 없음: 설치
                cls.bomb_list[p] = _Bomb(info[p].get("owner"), info[p].get("power"))
        for p in cls.bomb_list:
            if p in info.keys():
                continue 
            d.append(p) # list에는 있는데 info에는 없음: 터짐

        for p in d:
            del cls.bomb_list[p]

        a, b = {}, {}
        for p in cls.bomb_list:
            t = a if cls.bomb_list[p].timer == 0 else b
            t[p] = {"owner": cls.bomb_list[p].owner, "power": cls.bomb_list[p].power}
        cls.current_tick += 1
        return a, b