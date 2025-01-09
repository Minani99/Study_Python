import csv

from item import Item


class Character:
   # 상하좌우 이동 횟수, 거꾸로 간 횟수, 폭탄 놓은 횟수, 아이템 먹은 횟수, 데미지입은 횟수
   tic_count = 0 #현재 틱
   #카운트 변수 딕셔너리
   stats = {
           "up_count" : 0,
           "down_count" : 0,
           "left_count" : 0,
           "right_count" : 0,
           "reverse_count" : 0,
           "bomb_count" : 0,
           "devil_count" : 0,
           "skate_count" : 0,
           "kick_count" : 0,
           "plus_scope_count" : 0,
           "plus_bomb_count" : 0,
           "damage_count" : 0,
           "danger_count" : 0
           }


   result = {}


   def __init__(self,x,y,name):
       self.hp = 3 #캐릭터의 체력
       self.speed = 1 #캐릭터의 스피드 초기값
       self.max_speed = 1 #캐릭터의 스피드 최댓값
       self.b_count = 1 #캐릭터의 물풍선 개수 초기값
       self.max_b_count = 3 #캐릭터의 물풍선 개수 최댓값
       self.b_range = 1 #캐릭터의 물풍선 사거리 초기값
       self.max_b_range = 5 #캐릭터의 물풍선 사거리 최댓값
       self.x = x #캐릭터의 x좌표
       self.y = y #캐릭터의 y좌표
       self.kick = False #아이템 kick 여부
       self.death = False #캐릭터 사망
       self.devil = False
       self.reverse = 0 #아이템 악마 여부
       self.max_reverse = 5 #아이템 악마 스택 최댓값
       self.name = name


   def move_up(self, y): #이동 함수
       if self.reverse != 0: #거꾸로 이동
           self.y += y
           self.reverse -= 1
           if self.reverse == 0:
               self.devil = False #악마 상태 여부
           Character.stats["reverse_count"] += 1
       else:
            self.y -= y
       Character.stats["up_count"] += 1




   def move_down(self,y):
       if self.reverse != 0:
           self.y -= y
           self.reverse -= 1
           if self.reverse == 0:
               self.devil = False
           Character.stats["reverse_count"] += 1
       else:
            self.y += y
       Character.stats["down_count"] += 1


   def move_left(self,x):
       if self.reverse != 0:
           self.x += x
           self.reverse -= 1
           if self.reverse == 0:
               self.devil = False
           Character.stats["reverse_count"] += 1
       else:
            self.x -= x
       Character.stats["left_count"] += 1


   def move_right(self,x):
       if self.reverse != 0:
           self.x -= x
           self.reverse -= 1
           if self.reverse == 0:
               self.devil = False
           Character.stats["reverse_count"] += 1
       else:
            self.x += x
       Character.stats["right_count"] += 1


   instance = None
   @classmethod
   def init(cls,x,y,name): #캐릭터 인스턴스 생성
       cls.stats = {
           "up_count": 0,
           "down_count": 0,
           "left_count": 0,
           "right_count": 0,
           "reverse_count": 0,
           "bomb_count": 0,
           "devil_count": 0,
           "skate_count": 0,
           "kick_count": 0,
           "plus_scope_count": 0,
           "plus_bomb_count": 0,
           "damage_count": 0,
           "danger_count": 0
       }
       cls.instance = cls(x,y,name)
       return cls.instance.get_state()


   @classmethod
   def tick(cls,info): #맵에서 정보 받기
       cls.set_char(cls.instance, info)
       return cls.instance.get_state() #현재 캐릭터 정보 리턴

   @classmethod
   def get_stats(cls):
       return cls.instance.count_stats()

   def set_char(self, info): #받아온 정보 업데이트
       Character.tic_count= info["nowtick"]
       self.get_damage(info["hit_count"])
       if info["bomb_hit"] == True:
           self.get_damage(1)
       for move,bool in zip(info["movement"],info["movecheck"]):
           if move == "w" and bool == True:
               self.move_up(1)
           elif move == "a" and bool == True:
               self.move_left(1)
           elif move == "s" and bool == True:
               self.move_down(1)
           elif move == "d" and bool == True:
               self.move_right(1)
       self.item_count(info["dropped_item"])
       self.apply_item_effect(Item.return_effect(info["dropped_item"]))
       if info["bomb"] == True:
           self.stats["bomb_count"] += 1
       if self.hp == 1:
           Character.stats["danger_count"] += 1

   def item_count(self, item_list):
       if len(item_list) != 0:
           for item in item_list:
               if item in Item.ITEM_TYPES:
                   item_count = item + "_count"
                   Character.stats[item_count] += 1

   def get_damage(self,damage): #캐릭터가 데미지 입었을 때
       if damage == 0:
           return
       self.hp -= damage

       if self.hp <= 0:
           self.death=True
       Character.stats["damage_count"] += 1


   def get_state(self): #현재 캐릭터의 상태
       Character.result = {
                       "name" : self.name,
                       "hp": self.hp,
                       "speed": self.speed,
                       "b_count": self.b_count,
                       "b_range": self.b_range,
                       "x": self.x,
                       "y": self.y,
                       "kick": self.kick,
                       "death": self.death,
                       "reverse": self.reverse,
                       "devil" : self.devil
                     }
       return Character.result


   @classmethod
   def count_stats(cls): #통계 딕셔너리 리턴
       return Character.stats


   def count_csv(self,stats): #통계 딕셔너리로 csv 파일 생성 후 리턴
       with open('mycsv.csv', 'w') as f:
           w = csv.writer(f)
           w.writerow(Character.stats.keys())
           w.writerow(Character.stats.values())
           return 'mycsv.csv'


   def apply_item_effect(self, effects): #아이템 문자열 또는 리스트 받아서 캐릭터 정보 업데이트
       for i in effects:
           for stat, value in i.items(): # 'speed' , 1
               if hasattr(self, stat):
                   current_value = getattr(self, stat) # current_value = 1
                   if isinstance(current_value, bool):  # Boolean 값
                       setattr(self, stat, True)
                   elif isinstance(current_value, int):  # 숫자 값
                       if stat == "reverse":
                           self.devil = True
                       max_stat = f"max_{stat}" # max_{speed} max_stat = 'max_speed' max_kick x
                       if hasattr(self, max_stat):  # 최대값 확인 , self , 'max_speed'
                           max_value = getattr(self, max_stat) #3
                           new_value = min(current_value + value, max_value) # min(1 + 1 = 2 , 3) = 2
                       else:
                           new_value = current_value + value #self f max_? ++++++++++
                       setattr(self, stat, new_value) # self speed에 2를 넣어라


                   print(f"아이템 효과 적용됨: {stat}: {getattr(self, stat)}")
               else:
                   print(f"캐릭터에 {stat} 속성이 없어 효과를 적용할 수 없습니다.")