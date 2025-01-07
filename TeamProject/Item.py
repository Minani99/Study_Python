import random as rm
import pandas as pd


class Item:
    # 아이템 종류 딕셔너리
    ITEM_TYPES = {
        "plus_bomb": {"name": "폭탄 소지+", "effects": {"b_count": 1}},
        "plus_scope": {"name": "폭발 범위+", "effects": {"b_range": 1}},
        "skate": {"name": "스케이트", "effects": {"speed": 1}},
        "reverse": {"name": "악마", "effects": {"reverse": 5}},
        "kick": {"name": "킥", "effects": {"kick": True}},
    }

    # 생성자 (좌표값, 아이템 이름, life)
    def __init__(self, item_type="nothing", life=True):
        if item_type not in self.ITEM_TYPES:
            raise ValueError(f"'{item_type}'은(는) 유효하지 않은 아이템 태입입니다.")
        self.item_type = item_type
        self.name = self.ITEM_TYPES[item_type]["name"]
        self.effects = self.ITEM_TYPES[item_type]["effects"]
        self.life = life

    # 디버깅용 str
    def __str__(self):
        return f"Item(name={self.name}, effects={self.effects})"

    # 아이템 명띄울려면 이케해야함
    def __repr__(self):
        return self.__str__()

    # 아이템 이름을 받으면 효과를 반환해주는 메소드
    @classmethod
    def return_effect(cls, item_names):
        # 배열인지 확인
        if isinstance(item_names, str):
            item_names = [item_names]
        # 배열 형태가 아니라면 에러 반환
        if not isinstance(item_names, list):
            raise TypeError("아이템 이름은 문자열 또는 리스트여야 합니다.")

        # 반환할 효과들
        r_effects = []
        for name in item_names:
            if name in cls.ITEM_TYPES:
                r_effects.append(cls.ITEM_TYPES[name]["effects"])
            else:
                raise ValueError(f"'{name}'은(는) 유효하지 않은 아이템 이름입니다.")
        return r_effects if len(r_effects) > 1 else r_effects[0]  # 추가된게 있을때만 반환

    @classmethod
    def to_csv(cls):
        droplist = []
        cls.tick_result = Box.box_tick(damage_flags=[True, True, True, True, True, True, True, True, True, True, True])
        for index, box_status in enumerate(cls.tick_result):
            item = box_status["item"]
            item_info = f"드롭된 아이템 = {item}" if item else "아이템 없음"
            print(f"박스 {index + 1}: 남은 체력={box_status['remaining_hp']}, {item_info}")

        for index, box_status in enumerate(cls.tick_result):
            droplist.append(box_status)

        df = pd.DataFrame(droplist)
        df.to_csv("droplist.csv", index=False)
        print("\n결과가 'droplist.csv' 파일에 저장되었습니다.")


class Box:
    # 생성된 박스를 담아둘 리스트
    boxes = []
    # 틱 (count)
    tick = 0

    stats = {"broken_box": 0,
             "create_box": 0,
             }

    @classmethod
    def count_stats(cls, tick):

        pass

    # 생성자 (박스 좌표, 박스 체력, 부숴짐 여부)
    def __init__(self, hp=1, unbreakable=False):
        self.__hp = hp
        self.__max_hp = hp

        self.__unbreakable = unbreakable

    @property
    def hp(self):
        return self.__hp

    @property
    def max_hp(self):
        return self.__max_hp

    @property
    def unbreakable(self):
        return self.__unbreakable

    @unbreakable.setter
    def unbreakable(self, set_box):
        self.__unbreakable = set_box

    # 박스에 데미지를 주는 메소드(1씩)
    def damaged_by_bomb(self, damage=1):
        if self.unbreakable:
            print(f"이 박스는 안부숴짐ㅋ")
            return False

        # hp가 0이되면
        self.__hp -= damage
        if self.__hp == 0:
            print("박스가 파괴되었습니다!")
            return True
        elif 0 < self.__hp < 3:
            print("데이지 1 얻음")
            return True
        return False

    # 아이템 떨궈주는 메소드
    def drop_item(self):
        # 0보다 클땐 뭐 안함
        if self.__hp > 0:
            return None
        # 아이템 드롭 확률
        drop_chance = rm.random()
        # 70%
        if drop_chance < 0.7:
            item_type = rm.choice(list(Item.ITEM_TYPES.keys()))
            # 떨어진 위치랑 아이템 타입을 알려줌
            return item_type
        return None

    # 박스 초기 설정
    @classmethod
    def init(cls, box_set):
        for config in box_set:
            if not isinstance(config, int):
                raise ValueError("box_config의 각 항목은 정수여야 합니다.")
            if config == 7:
                unbreakable = True
            elif 1 <= config <= 3:
                unbreakable = False
            else:
                raise ValueError("hp는 1에서 3 사이이거나 7이어야 합니다.")

            cls.boxes.append(cls(hp=config, unbreakable=unbreakable))

    # 맵에서 박스의 리스트를 받았을 때
    @classmethod
    def box_tick(cls, **kwargs):
        damage_flags = kwargs.get("damage_flags", [])
        # game_set = kwargs.get("game_set", bool)
        # if game_set is True:
        #     pass

        if len(damage_flags) != len(cls.boxes):
            raise ValueError("damage_flags 리스트의 길이는 생성된 박스의 수와 같아야 합니다.")

        box_list = []
        for i_box, damaged in zip(cls.boxes, damage_flags):
            if damaged:
                i_box.damaged_by_bomb()

            box_dict = {
                "remaining_hp": i_box.hp,
                "item": i_box.drop_item() if i_box.hp <= 0 else None,
            }
            box_list.append(box_dict)

        cls.tick += 1
        return box_list


Box.init(box_set=[1, 2, 2, 7, 1, 1, 3, 1, 1, 1])

droplist = []

print("\n초기 박스 상황:")
for i, box in enumerate(Box.boxes):
    print(f"박스 {i + 1}: 체력={box.hp}, 최대 체력={box.max_hp}, 부서짐 여부={'부서지지 않음' if box.unbreakable else '부서짐 가능'}")

print("\n폭탄 피해 적용 및 박스 상태 업데이트:")
tick_result = Box.box_tick(damage_flags=[True, True, True, True, True, True, True, True, True, True])

for index, box_status in enumerate(tick_result):
    item = box_status["item"]
    item_info = f"드롭된 아이템={item}" if item else "아이템 없음"
    print(f"박스 {index + 1}: 남은 체력={box_status['remaining_hp']}, {item_info}")

print("\n부서지지 않는 박스 확인:")
for i, box in enumerate(Box.boxes):
    if box.unbreakable:
        print(f"박스 {i + 1}: 부서지지 않음 (체력={box.hp})")

# 결과를 CSV 파일에 저장
droplist = []
for index, box_status in enumerate(tick_result):
    droplist.append(box_status)

df = pd.DataFrame(droplist)
df.to_csv("droplist.csv", index=False)
print("\n결과가 'droplist.csv' 파일에 저장되었습니다.")
