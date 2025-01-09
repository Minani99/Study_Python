import random as rm
import pandas as pd

from item import Item


class Box:
    # 생성된 박스를 담아둘 리스트
    boxes = []

    # 통계 데이터
    stats = {
        "total_destroyed_boxes": 0,
        "total_dropped_items": 0,
        "item_counts": {},
        "drop_probability": 0,
    }

    def __init__(self, hp=1, unbreakable=False):
        self.__hp = hp
        self.__max_hp = hp
        self.__unbreakable = unbreakable
        self._dropped = False  # 아이템 드롭 여부 플래그

    @property
    def hp(self):
        return self.__hp

    @property
    def max_hp(self):
        return self.__max_hp

    @property
    def unbreakable(self):
        return self.__unbreakable

    def damaged_by_bomb(self, damage=1):
        if self.unbreakable:
            return False

        if self.__hp <= 0:  # 이미 파괴된 박스는 카운트하지 않음
            return False

        self.__hp -= damage
        if self.__hp <= 0:
            Box.stats["total_destroyed_boxes"] += 1
            return True
        return False

    def drop_item(self):
        if self.__hp > 0 or self._dropped:  # HP가 0 이상이거나 이미 드롭된 경우
            return None

        drop_chance = rm.random()
        if drop_chance < 0.7:  # 70% 확률로 아이템 드롭
            self._dropped = True
            item_type = rm.choice(list(Item.ITEM_TYPES.keys()))
            Box.stats["total_dropped_items"] += 1
            Box.stats["item_counts"][item_type] = Box.stats["item_counts"].get(item_type, 0) + 1
            return item_type

        self._dropped = True
        return None

    @classmethod
    def init(cls, box_set):
        cls.boxes = []

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

    @classmethod
    def box_tick(cls, **kwargs):
        damage_flags = kwargs.get("damage_flags", [])
        if len(damage_flags) != len(cls.boxes):
            raise ValueError("damage_flags 리스트의 길이는 생성된 박스의 수와 같아야 합니다.")

        box_list = []
        for i_box, damaged in zip(cls.boxes, damage_flags):
            if damaged:
                i_box.damaged_by_bomb()

            box_dict = {
                "remaining_hp": i_box.hp,
                "item": i_box.drop_item(),
            }
            box_list.append(box_dict)

        # 드롭 확률 계산
        if Box.stats["total_destroyed_boxes"] > 0:
            Box.stats["drop_probability"] = round(
                (Box.stats["total_dropped_items"] / Box.stats["total_destroyed_boxes"]) * 100, 2)

        # 게임 종료 처리
        game_over = kwargs.get("game_over", False)
        if game_over:
            return cls.save_stats_to_csv()

        return box_list

    @classmethod
    def save_stats_to_csv(cls):
        final_stats = {
            "total_destroyed_boxes": cls.stats["total_destroyed_boxes"],
            "total_dropped_items": cls.stats["total_dropped_items"],
            "item_counts": cls.stats["item_counts"],
            "drop_probability": f"{cls.stats['drop_probability']}%",
        }

        # CSV 파일 저장
        df = pd.DataFrame([{
            "total_destroyed_boxes": final_stats["total_destroyed_boxes"],
            "total_dropped_items": final_stats["total_dropped_items"],
            "item_counts": "; ".join([f"{key}: {value}" for key, value in final_stats["item_counts"].items()]),
            "drop_probability": final_stats["drop_probability"],
        }])
        df.to_csv("game_stats.csv", index=False)

        return final_stats
