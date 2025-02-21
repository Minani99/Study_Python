import random as ra


from item import Item


class Boss:
   def __init__(root, name, hp, phase, size, coord):
       root.name = name
       root.hp = hp
       root.phase = phase
       root.size = size
       root.coord = coord


   # 보스의 체력 리턴
   def get_monster_hp(root):
       return root.hp


   # 보스의 페이즈 설정
   def set_phase(root, v_phase):
       root.phase = v_phase


   # 보스 체력 감소
   def reduce_hp(root, damage):
       root.hp -= damage
       if root.hp < 0:
           root.hp = 0
       root.update_phase()
       return root.hp




   # 보스의 페이즈 업데이트
   def update_phase(root):
       if root.hp > 7:
           root.phase = 1
       elif 4 <= root.hp <= 7:
           root.phase = 2
       elif root.hp > 0:
           root.phase = 3
       else:
           root.phase = 0  # 사망

   # 물풍선 공격 패턴 생성
   def make_atk(root, coord, phase):
       X, Y = coord[0] - 3, coord[1] - 3
       water_coord = []
       plus_range = 7
       num = 0
       bomb_range = 0
       if phase == 1:
           bomb_range = 3
       elif phase == 2:
           bomb_range = 2
       elif phase == 3:
           bomb_range = 1

       while num < 3:
           for x in range(X, X + plus_range, bomb_range):
               for y in range(Y, Y + plus_range, bomb_range):
                   if x == X or y == Y or x == X + plus_range - 1 or y == Y + plus_range - 1:
                       water_coord.append([x, y])
           num += 1
           plus_range += 6

           # 떨어지는 거리?
           X -= 3
           Y -= 3

       return water_coord


   # 보스 공격 이벤트
   def event_boss_atk(root, tick, coord):
       if (
           (root.phase == 1 and tick % 10 == 0)
           or (root.phase == 2 and tick % 10 == 0)
           or (root.phase == 3 and tick % 10 == 0)
       ):
           return root.make_atk(coord, root.phase)
       return []


class Minion:
   def __init__(root, name, hp, size, coord):
       root.name = name
       root.hp = hp  # 미니언 체력 초기화
       root.size = size
       root.coord = coord


   # 미니언의 체력 리턴
   def get_minion_hp(root):
       return root.hp


   # # 미니언의 체력 설정
   # def set_minion_hp(root, v_hp):
   #     root.hp = v_hp


   # 미니언 좌표 갱신
   def renew_min_coord(root, coord, movable):
       if not movable:
           return coord
       # x = coord[0] + ra.choice([-1, 0, 1])
       # y = coord[1] + ra.choice([-1, 0, 1])
       # return [x, y]
       r = ra.choice([[-1, 0], [1, 0], [0, -1], [0, 1]])
       return [coord[0] + r[0], coord[1] + r[1]]


   # 미니언 아이템 드롭
   def drop_item(root):
       drop_chance = ra.random()
       if drop_chance < 0.7:
           item_type = ra.choice(list(Item.ITEM_TYPES.keys()))
           return item_type
           #return Item(item_type, life=True)
       return None


# 미니언 체력 감소
   def reduce_hp(root):
       root.hp -= 1
       if root.hp < 0:
           root.hp = 0
       return root.hp


class Monster:
   __mon_list = []  # 몬스터 리스트


   @classmethod
   def init(cls, **kwargs):
       cls.__mon_list = []
       boss_coords = kwargs.get("boss_coords", [])
       minion_coords = kwargs.get("minion_coords", [])


       # 보스와 미니언 세팅
       boss_dict = {f"boss{i + 1}": coord for i, coord in enumerate(boss_coords)}
       minion_dict = {f"minion{i + 1}": coord for i, coord in enumerate(minion_coords)}
       cls.make_monster_list(cls.__mon_list, boss_dict, minion_dict)


       # 1틱 정보 리턴
       boss_info = [
           {
               "name": boss.name,
               "hp": boss.get_monster_hp(),
               "phase": boss.phase,
               "pattern": [],
           }
           for boss in cls.__mon_list if isinstance(boss, Boss)
       ]
       minion_info = [
           {
               "name": minion.name,
               "hp": minion.get_minion_hp(),
               "move": minion.coord,
               "dropitem": None,
           }
           for minion in cls.__mon_list if isinstance(minion, Minion)
       ]
       return boss_info, minion_info


   @classmethod
   def make_monster_list(cls, mon_list, boss_coords, minion_coords):
       # 보스 생성
       for name, coord in boss_coords.items():
           boss = Boss(name, 10, 1, 3, coord)
           mon_list.append(boss)


       # 미니언 생성
       for name, coord in minion_coords.items():
           minion = Minion(name, 1, 1, coord)
           mon_list.append(minion)


   @classmethod
   def monster_tick(cls, **kwargs):
       tick = kwargs.get("tick", 1)  # 현재 틱
       damage_info = kwargs.get("damage_info", {})


       boss_info = []  # 보스 정보
       minion_info = []  # 미니언 정보


       minions = [m for m in cls.__mon_list if isinstance(m, Minion)]  # 미니언 객체만 추출
       bosses = [b for b in cls.__mon_list if isinstance(b, Boss)]  # 보스 객체만 추출


       # 보스 처리
       boss_damage_info = damage_info.get("boss", [])


       for boss in bosses:
           boss_damage = [
               i for i in boss_damage_info if i["pos"] == boss.coord and i["hit"] #한번에처리
           ]
           if boss_damage:
               boss.reduce_hp(len(boss_damage))


           boss_info.append(
               {
                   "name": boss.name,
                   "hp": boss.get_monster_hp(),
                   "phase": boss.phase,
                   "pattern": boss.event_boss_atk(tick, boss.coord),
               }
           )
       # 미니언 처리
       minion_damage_info = damage_info.get("minion", [])
       for i, minion in enumerate(minions):
           #전부hp가 깎이는 오류 수정
           if len(minion_damage_info) > i:
               hit = minion_damage_info[i].get("hit", False)  # True/False 값 확인
               if hit:
                   minion.reduce_hp()
                   drop_item = minion.drop_item()
               else:
                   drop_item = None
           else:
               drop_item = None


           minion.coord = minion_damage_info[i]["pos"]


           minion_info.append(
               {
                   "name": minion.name,
                   "hp": minion.get_minion_hp(),
                   "move": minion.renew_min_coord(minion.coord, True),
                   #"dropitem": drop_item.name if drop_item else None,
                   "dropitem": drop_item if drop_item else None,
               }
           )


       return boss_info, minion_info