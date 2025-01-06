import random as rm


class Item:
    ITEM_TYPES = {
        "plus_bomb": {"name": "폭탄 소지+", "effects": {"b_count": 1}},
        "plus_scope": {"name": "폭발 범위+", "effects": {"b_range": 1}},
        "skate": {"name": "스케이트", "effects": {"speed": 1}},
        "reverse": {"name": "악마", "effects": {"reverse": 5}},
        "kick": {"name": "킥", "effects": {"kick": True}},
    }

    def __init__(self, x=0, y=0, item_type="nothing", life=True):
        if item_type not in self.ITEM_TYPES:
            raise ValueError(f"Invalid item_type: {item_type}")
        self.x = x
        self.y = y
        self.item_type = item_type
        self.name = self.ITEM_TYPES[item_type]["name"]
        self.effects = self.ITEM_TYPES[item_type]["effects"]
        self.life = life

    def __str__(self):
        return f"Item(name={self.name}, effects={self.effects})"

    def __repr__(self):
        return self.__str__()

    @classmethod
    def return_effect(cls, item_names):
        if isinstance(item_names, str):
            if item_names in cls.ITEM_TYPES:
                return cls.ITEM_TYPES[item_names]["effects"]
            else:
                raise ValueError(f"'{item_names}'은(는) 존재하지 않는 아이템입니다.")
        elif isinstance(item_names, list):
            r_effects = []
            for name in item_names:
                if name in cls.ITEM_TYPES:
                    r_effects.append(cls.ITEM_TYPES[name]["effects"])
                else:
                    raise ValueError(f"'{name}'은(는) 존재하지 않는 아이템입니다.")
            return r_effects
        else:
            raise TypeError("아이템 이름은 리스트로 전달되어야 합니다.")


class Box:
    boxes = []  # 클래스 레벨에서 박스를 저장
    tick = 0

    def __init__(self, b_x, b_y, hp=1, unbreakable=False):
        self.hp = hp  # 현재 체력
        self.max_hp = hp  # 초기 체력 저장
        self.x = b_x  # X 좌표
        self.y = b_y  # Y 좌표
        self.unbreakable = unbreakable
        self.damaged = False  # 데미지 여부 플래그

    def damaged_by_bomb(self):
        if self.unbreakable:
            print(f"이 박스는 깨지지 않습니다! ({self.x}, {self.y})")
            return False

        self.hp -= 1  # 체력 감소
        if self.hp < self.max_hp:  # 초기 체력보다 낮아졌다면 데미지 받은 것으로 간주
            self.damaged = True

        if self.hp <= 0:  # 체력이 0 이하이면 박스 파괴
            print(f"박스가 파괴되었습니다! ({self.x}, {self.y})")
            return True
        return False

    def reset_damage(self):
        # 상태 초기화 메서드 (다음 틱에서 데미지 여부를 리셋)
        self.damaged = False

    def drop_item(self):
        drop_chance = rm.random()  # 0.0 ~ 1.0 사이의 랜덤 값
        if drop_chance < 0.7:  # 70% 확률로 아이템 생성
            item_type = rm.choice(list(Item.ITEM_TYPES.keys()))  # ITEM_TYPES의 키에서 랜덤 선택
            return Item(self.x, self.y, item_type, life=True)  # 선택된 타입으로 아이템 객체 생성
        else:
            return None

    @classmethod
    def init(cls, box_count):
        for _ in range(box_count):
            x = rm.randint(0, 9)  # 임의로 한 좌표
            y = rm.randint(0, 9)
            r_box = cls(x, y, hp=rm.randint(1, 3))
            cls.boxes.append(r_box)

    @classmethod
    def box_tick(cls, **kwargs):
        damage_positions = kwargs.get("damage_positions", [])  # 데미지를 받을 좌표 리스트
        damage_value = kwargs.get("damage_value", 1)  # 기본 데미지 값
        box_list = []

        for now_box in cls.boxes:
            # 박스가 데미지 받을 위치 확인
            if (now_box.x, now_box.y) in damage_positions:
                now_box.damaged_by_bomb(damage=damage_value)

            box_dict = {
                "remaining_hp": now_box.hp,  # 남은 체력
                "item": now_box.drop_item() if now_box.hp <= 0 else None,  # 파괴된 경우 아이템 드롭
            }
            now_box.reset_damage()  # 다음 틱을 위해 초기화
            box_list.append(box_dict)

        cls.tick += 1  # 틱 증가
        return box_list


Box.init(box_count=10)

print("초기 박스 상태:")
for i, box in enumerate(Box.boxes):
    print(f"박스 {i + 1} 초기 체력: {box.hp}")
    box.damaged_by_bomb()

tick_result = Box.box_tick()

print("틱 결과:")
for index, box_status in enumerate(tick_result):
    print(f"박스 {index + 1}: {box_status}")

effect = Item.return_effect("plus_bomb")
print(effect)

effects = Item.return_effect(["plus_bomb", "skate", "kick"])
print(effects)