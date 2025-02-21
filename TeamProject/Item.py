import random as rm
import pandas as pd


class Item:
    # 아이템 종류 딕셔너리
    ITEM_TYPES = {
        "plus_bomb": {"name": "폭탄 소지+", "effects": {"b_count": 1}},
        "plus_scope": {"name": "폭발 범위+", "effects": {"b_range": 1}},
        "skate": {"name": "스케이트", "effects": {"speed": 1}},
        "devil": {"name": "악마", "effects": {"reverse": 5}},
        "kick": {"name": "킥", "effects": {"kick": True}},
    }

    # 생성자 (좌표값, 아이템 이름, life)
    def __init__(root, item_type="nothing", life=True):
        if item_type not in root.ITEM_TYPES:
            raise ValueError(f"'{item_type}'은(는) 유효하지 않은 아이템 태입입니다.")
        root.item_type = item_type
        root.name = root.ITEM_TYPES[item_type]["name"]
        root.effects = root.ITEM_TYPES[item_type]["effects"]
        root.life = life

    # 디버깅용 str
    def __str__(root):
        return f"Item(name={root.name}, effects={root.effects})"

    # 아이템 명띄울려면 이케해야함
    def __repr__(root):
        return root.__str__()

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

    def __init__(root, hp=1, unbreakable=False):
        root.__hp = hp
        root.__max_hp = hp
        root.__unbreakable = unbreakable
        root._dropped = False  # 아이템 드롭 여부 플래그

    @property
    def hp(root):
        return root.__hp

    @property
    def max_hp(root):
        return root.__max_hp

    @property
    def unbreakable(root):
        return root.__unbreakable

    def damaged_by_bomb(root, damage=1):
        if root.unbreakable:
            return False

        if root.__hp <= 0:  # 이미 파괴된 박스는 카운트하지 않음
            return False

        root.__hp -= damage
        if root.__hp <= 0:
            Box.stats["total_destroyed_boxes"] += 1
            return True
        return False

    def drop_item(root):
        if root.__hp > 0 or root._dropped:  # HP가 0 이상이거나 이미 드롭된 경우
            return None

        drop_chance = rm.random()
        if drop_chance < 0.7:  # 70% 확률로 아이템 드롭
            root._dropped = True
            item_type = rm.choice(list(Item.ITEM_TYPES.keys()))
            Box.stats["total_dropped_items"] += 1
            Box.stats["item_counts"][item_type] = Box.stats["item_counts"].get(item_type, 0) + 1
            return item_type

        root._dropped = True
        return None

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
            Box.stats["drop_probability"] = int((Box.stats["total_dropped_items"] / Box.stats["total_destroyed_boxes"]) * 100)

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

        if final_stats["item_counts"]:
            item_counts_list = []
            for key, value in final_stats["item_counts"].items():
                item_counts_list.append(f"{key}: {value}")
            item_counts_str = "\n".join(item_counts_list)
        else:
            item_counts_str = "없음"

        formatted_stats = f"""
파괴된 총 박스 수: {final_stats['total_destroyed_boxes']}
드롭된 총 아이템 수: {final_stats['total_dropped_items']}
드롭된 아이템 목록:
{item_counts_str}
아이템 드롭 확률: {final_stats['drop_probability']}"""

        return formatted_stats


Box.init([1, 2, 3, 7, 1, 1])  # 박스 초기화

# 틱 1
print(Box.box_tick(damage_flags=[True, True, True, True, True, True]))

# 틱 2
print(Box.box_tick(damage_flags=[True, True, True, True, True, True]))

# 게임 종료
print(Box.box_tick(damage_flags=[True, True, True, True, True, True], game_over=True))
