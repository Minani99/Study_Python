import pandas as pd


class Item:
    # 아이템 종류 딕셔너리
    ITEM_TYPES = {
        "plus_bomb": {"name": "폭탄 소지+", "effects": {"b_count": 1}},
        "plus_scope": {"name": "폭발 범위+", "effects": {"b_range": 1}},
        # "skate": {"name": "스케이트", "effects": {"speed": 1}},
        "devil": {"name": "악마", "effects": {"reverse": 5}},
        # "kick": {"name": "킥", "effects": {"kick": True}},
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
        return r_effects

    @classmethod
    def to_csv(cls, tick):
        d_droplist = []
        cls.tick_result = tick
        for index, box_status in enumerate(cls.tick_result):
            item = box_status["item"]
            item_info = f"드롭된 아이템 = {item}" if item else "아이템 없음"
            print(f"박스 {index + 1}: 남은 체력={box_status['remaining_hp']}, {item_info}")

        for index, box_status in enumerate(cls.tick_result):
            d_droplist.append(box_status)

        df = pd.DataFrame(d_droplist)
        df.to_csv("droplist.csv", index=False)
        print("\n결과가 'droplist.csv' 파일에 저장되었습니다.")
