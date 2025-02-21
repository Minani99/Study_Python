import random
from typing import Any

from bomb import Bomb
from box import Box
from character import Character
from item import Item
from mob import Monster as Mob
from pos import Pos


# 플레ㅣ어별 통계
# 이름, 이동횟수, 틱수, 승률, ...
# 랭킹
class Map:
    def __init__(root):
        root.map_size = [15, 15]  # x y
        root.map_info = []
        root.max_tick = 10000
        root.current_tick = 0

        root.box_dict = {}  # {pos: {hp: int, hit: bool}}
        root.item_dict = {}  # {pos: key}
        root.bomb_dict = {}  # {pos: {owner: str, power: int}}}

        root.char_stat = {}  #
        root.mob_dict = {}  # {boss: [{pos: Pos, hp: int, hit: bool}], minion: [{pos: Pos, hp: int, hit: bool}]}
        root.char_dict = {}
        root.rank = []

    def set_info(root, p: Pos, v):
        root.map_info[p.y][p.x] = v

    def set_box(root, p: Pos, box_id):
        root.set_info(p, box_id << 2)

    def set_item(root, p: Pos, item_id):
        root.set_info(p, item_id << 5)

    def set_empty(root, p: Pos):
        root.set_info(p, 0)

    def set_water(root, p: Pos):
        root.set_info(p, 1)

    def set_player_bomb(root, p: Pos):
        root.set_info(p, 2)

    def set_boss_bomb(root, p: Pos):
        root.set_info(p, 3)

    def set_boss_pattern(root, l: list):
        for i in l:
            p = Pos.from_list(i)
            if root.is_inside(p) and (not root.is_box(p) or root.is_broken_box(p)):
                root.set_boss_bomb(p)
                root.add_bomb("boss", p, 1)

    def get_info(root, p: Pos) -> Any:
        return root.map_info[p.y][p.x]

    def is_inside(root, p: Pos):
        return (0 <= p.x < root.map_size[0]) and (0 <= p.y < root.map_size[1])

    def all_pos(root):
        return [Pos(x, y) for y in range(root.map_size[0]) for x in range(root.map_size[1])]

    def is_item(root, p: Pos):
        return root.get_info(p) >= 32

    def is_box(root, p: Pos):
        return 32 > root.get_info(p) >= 4

    def is_broken_box(root, p: Pos):
        return root.is_box(p) and root.box_dict[p]["hp"] == 0

    def is_player_bomb(root, p: Pos):
        return root.get_info(p) == 2

    def is_boss_bomb(root, p: Pos):
        return root.get_info(p) == 3

    def is_bomb(root, p: Pos):
        return root.is_player_bomb(p) or root.is_boss_bomb(p)

    def is_water(root, p: Pos):
        return root.get_info(p) == 1

    def is_empty(root, p: Pos):
        return root.get_info(p) == 0

    def is_movable(root, p: Pos):
        return root.is_empty(p) or root.is_water(p) or root.is_item(p)

    def item_id(root, p: Pos):
        return root.get_info(p) >> 5

    def box_id(root, p: Pos):
        return (root.get_info(p) >> 2) & 7

    def get_item_id(root, s: str):
        return list(Item.ITEM_TYPES.keys()).index(s) + 1

    def get_item_name(root, p: Pos):
        if root.is_item(p):
            return list(Item.ITEM_TYPES.keys())[root.item_id(p) - 1]
        return None

    def add_bomb(root, name, pos, power):
        root.bomb_dict[pos] = {"owner": name, "power": power}

    def bomb_count(root, name):
        return sum(1 for i in root.bomb_dict if name == root.bomb_dict[i]["owner"])

    def char_pos(root):
        return Pos(root.char_stat["x"], root.char_stat["y"])

    def boss_pos(root, live=False, inline=False):
        output = []
        for b in root.mob_dict["boss"]:
            if live and b["hp"] <= 0:
                continue
            tmp = []
            for i in range(-1, 2):
                for j in range(-1, 2):
                    if inline:
                        output.append(b["pos"] + Pos(i, j))
                    else:
                        tmp.append(b["pos"] + Pos(i, j))
            if not inline:
                output.append(tmp)
        return output

    def minion_pos(root, live=False):
        return [m["pos"] for m in root.mob_dict["minion"] if not (live and m["hp"] <= 0)]

    def player_name(root):
        return root.char_stat["name"]

    ###########################################################################

    def initialize(root):
        root.map_info = [[0 for i in range(root.map_size[0])] for j in range(root.map_size[1])]  # 맵 사이즈

        # 박스&빈 공간
        for i in range(root.map_size[1]):  # y
            for j in range(root.map_size[0]):  # x
                point_num = random.uniform(0, 1)  # 확률
                if point_num > 0.3:  # 70% 박스
                    if point_num <= 0.37:
                        root.map_info[i][j] = 28  # 부서지지 않는 박스 -1
                    elif 0.37 < point_num <= 0.5:
                        root.map_info[i][j] = 12  # 박스 체력 3
                        # root.map_info[i][j] = 4  # 박스 체력 3
                    elif 0.5 < point_num <= 0.7:
                        root.map_info[i][j] = 8  # 박스 체력 2
                        # root.map_info[i][j] = 4  # 박스 체력 2
                    else:
                        root.map_info[i][j] = 4  # 박스 체력 1
                else:  # 아니면 빈 공간
                    root.map_info[i][j] = 0

        # 구역 9개
        for i in range(3):
            for j in range(3):
                root.map_info[(root.map_size[1] // 2) - 1 + j][
                    (root.map_size[0] // 2) - 1 + i] = 0  # 중앙 고정 값(보스) [13][13]
                root.map_info[(root.map_size[1] - 4) + j][(root.map_size[1] - 4) + i] = 0  # 오른쪽 모서리 아래 [23][23]
                root.map_info[(root.map_size[1] - 4) + j][i + 1] = 0  # 왼쪽 모서리 아래 # [23][3]
                root.map_info[j + 1][(root.map_size[1] - 4) + i] = 0  # 오른쪽 모서리 위 [3][23]
                root.map_info[j + 1][i + 1] = 0  # 왼쪽 위 모서리 # [3][3]
                root.map_info[(root.map_size[1] - 4) + j][(root.map_size[0] // 2) - 1 + i] = 0  # 아래 중앙 # [23][13]
                root.map_info[j + 1][(root.map_size[0] // 2) - 1 + i] = 0  # 위 중앙 # [3][13]
                root.map_info[(root.map_size[0] // 2) - 1 + j][i + 1] = 0  # 왼쪽 중앙 # [13][3]
                root.map_info[(root.map_size[0] // 2) - 1 + j][(root.map_size[1] - 4) + i] = 0  # 오른쪽 중앙 # [13][23]

        # 맵 외곽은 부서지지 않는 박스
        for i in range(root.map_size[0]):
            for j in range(root.map_size[0]):
                root.map_info[0][i] = 28  # 윗줄
                root.map_info[-1][i] = 28  # 아랫줄
                root.map_info[j][0] = 28  # 왼쪽줄
                root.map_info[j][-1] = 28  # 오른쪽줄

        # map size 13 13
        # print(i, j)
        # 12 12

        # 각 구역 중앙 값
        A_point = Pos(root.map_size[0] // 2, root.map_size[1] // 2)  # 중앙 보스 [12][12]
        B_point = Pos(root.map_size[0] - 3, 2)  # 오른쪽 모서리 위 [24][0]
        C_point = Pos(root.map_size[0] // 2, 2)  # 위 중앙 [24][12]
        D_point = Pos(2, 2)  # 왼쪽 위 모서리 # [24][24]
        E_point = Pos(2, root.map_size[1] // 2)  # 왼쪽 중앙 [12][24]
        F_point = Pos(root.map_size[0] - 3, root.map_size[1] // 2)  # 오른쪽 중앙 [12][0]
        G_point = Pos(2, root.map_size[1] - 3)  # 왼쪽 모서리 아래 # [0][24]
        H_point = Pos(root.map_size[0] // 2, root.map_size[1] - 3)  # 아래 중앙 [0][12]
        I_point = Pos(root.map_size[0] - 3, root.map_size[1] - 3)  # 오른쪽 모서리 아래 [0][0]

        # point_list = [A_point, B_point, ...]

        ###########################################################################
        point_list = [B_point, C_point, D_point, E_point, F_point, G_point, H_point, I_point]
        for i in range(len(point_list) - 1):
            r = random.randrange(i + 1, len(point_list))
            point_list[i], point_list[r] = point_list[r], point_list[i]
        # print(point_list)

        root.current_tick = 0

        root.box_dict = {}
        for i in range(root.map_size[0]):
            for j in range(root.map_size[1]):
                p = Pos(j, i)
                if root.is_box(p):
                    root.box_dict[p] = {"hp": root.box_id(p), "hit": False}
                # print(root.map_info[i][j], end="\t")

        # 박스 id(1~7), 아이템(1~7), 0(없음), 1(물줄기), 2(물풍선)
        # 000 000 00 / 32 4 1
        # print([value["hp"] for _, value in root.box_dict.items()])
        Box.init([value["hp"] for _, value in root.box_dict.items()])

        # for i in range(root.map_size[0]):
        #     for j in range(root.map_size[1]):
        #         print(root.map_info[i][j], end="\t")
        #     print()

        # 캐릭터
        # 이름 입력받고
        n = input("이름: ")
        while n == "":
            n = input("이름: ")
        root.char_stat = Character.init(x=point_list[1].x, y=point_list[1].y, name=n)
        # print(root.char_stat)

        # 보스 초기화
        root.mob_dict = {"boss": [{"pos": A_point, "hp": -1, "hit": False}],
                         "minion": [{"pos": point_list[i], "hp": -1, "hit": False} for i in range(2, 7)]}
        mob_a, mob_b = Mob.init(boss_coords=[i["pos"].to_list() for i in root.mob_dict["boss"]],
                                minion_coords=[i["pos"].to_list() for i in root.mob_dict["minion"]])
        # print(root.minion_pos())
        # print("init mob_b", mob_b)
        for i in range(len(mob_a)):
            root.mob_dict["boss"][i]["hp"] = mob_a[i]["hp"]
        for i in range(len(mob_b)):
            root.mob_dict["minion"][i]["hp"] = mob_b[i]["hp"]

    ###########################################################################

    def play(root):
        root.display()
        last_tick = False
        mob_b = [{"move": [0, 0]} for _ in root.mob_dict["minion"]]
        while not last_tick:
            # last tick 체크
            last_tick = root.game_state() != 2
            if last_tick:
                print("게임 끝남")
                break

            root.current_tick += 1

            root.char_dict = {
                "movement": [],
                "movecheck": [],
                "dropped_item": [],
                "hit_count": 0,
                "bomb": False,

                "bomb_hit": False,
                "clear": False,
                "nowtick": root.current_tick,
            }
            # i = input("test: ")
            # 입력
            root.is_movable_(root.inp_user_act())

            # 직전 틱의 물줄기는 빈칸으로 초기화
            for p in root.all_pos():
                if root.is_water(p):
                    root.set_empty(p)

            # 박스 맞음 상태 false로 초기화
            for key in root.box_dict:
                root.box_dict[key]["hit"] = False
            # 몹 맞음 상태 false로 초기화
            for b in root.mob_dict["boss"]:
                b["hit"] = False
            for m in root.mob_dict["minion"]:
                m["hit"] = False

            # 적 실제 이동
            for i in range(len(root.mob_dict["minion"])):
                p = Pos.from_list(mob_b[i]["move"])
                if root.is_inside(p) and not (root.is_box(p) or root.is_bomb(p)) and not (
                        p in root.boss_pos(live=True, inline=True)):
                    root.mob_dict["minion"][i]["pos"] = p

            # 캐릭터 물풍선 리스트에 추가
            if root.char_dict["bomb"]:
                root.add_bomb(root.player_name(), root.char_pos(), root.char_stat["b_range"])

            # bomb tick
            bomb_a, bomb_b = Bomb.tick(root.bomb_dict)
            root.bomb_dict = bomb_b
            # print("bomb_dict", root.bomb_dict)

            # 맵에 물풍선 놓기
            for p in root.bomb_dict:
                if root.bomb_dict[p]["owner"] == "boss":
                    # root.set_boss_bomb(p)
                    pass
                else:
                    root.set_player_bomb(p)

            # 캐릭터 이동 (임시)
            r = -1 if root.char_stat["reverse"] else 1
            mv = {"w": Pos(0, -r), "a": Pos(-r, 0), "s": Pos(0, r), "d": Pos(r, 0)}
            p = root.char_pos()
            for i in range(len(root.char_dict["movecheck"])):
                if root.char_dict["movecheck"][i]:
                    p += mv[root.char_dict["movement"][i]]
            root.char_stat["x"] = p.x
            root.char_stat["y"] = p.y

            # 아이템 맞았나 체크
            if root.is_item(root.char_pos()):
                iname = root.get_item_name(root.char_pos())
                # print(iname, "먹음")
                del root.item_dict[root.char_pos()]
                root.char_dict["dropped_item"].append(iname)
                root.set_empty(root.char_pos())
            # 아이템 먹으면 다음 틱부터 능력치 적용

            # print("item_dict", root.item_dict)
            # 터짐
            for p in bomb_a:
                for q in root.bomb(p, bomb_a[p]["power"]):
                    if root.is_box(q):
                        root.box_dict[q]["hit"] = True
                    elif q in root.item_dict:  # 아이템이 맞았는지
                        # print("아이템 물에 맞음")
                        del root.item_dict[q]
                        root.set_water(q)
                    else:
                        root.set_water(q)
                    # 적이 맞았는지
                    for i in range(len(root.boss_pos())):
                        if q in root.boss_pos()[i]:
                            root.mob_dict["boss"][i]["hit"] = True

                    for m in root.mob_dict["minion"]:
                        if q == m["pos"]:
                            m["hit"] = True
                    # 플레이어가 맞았는지
                    if q == root.char_pos():
                        # print("플레이어 물에 맞음")
                        root.char_dict["bomb_hit"] = True
            # print("item_dict", root.item_dict)

            # 적이랑 맞았는지 체크
            for p in root.boss_pos(live=True, inline=True):
                if root.char_pos() == p:
                    root.char_dict["hit_count"] = 1  # 임시
                    # print("플레이어 보스에 맞음")
            for p in root.minion_pos(live=True):
                if root.char_pos() == p and not root.is_water(root.char_pos()):
                    root.char_dict["hit_count"] = 1  # 임시
                    # print("플레이어 미니언에 맞음")

            # print("char_dict", root.char_dict)

            # root.char_dict["clear"] = False

            # character tick
            # print("character tick")
            root.char_stat = Character.tick(root.char_dict)
            # print("char_stat", root.char_stat)

            # box tick
            # print("box tick")
            box_a = Box.box_tick(damage_flags=[value["hit"] for _, value in root.box_dict.items()])
            for i, p in enumerate(root.box_dict):
                root.box_dict[p]["hp"] = box_a[i]["remaining_hp"]
                if root.is_broken_box(p):
                    if box_a[i]["item"] is not None:
                        root.set_item(p, root.get_item_id(box_a[i]["item"]))
                        root.item_dict[p] = box_a[i]["item"]
                    else:
                        root.set_empty(p)

            # mob tick
            # print("mob_dict", root.mob_dict)
            # print("mob tick")
            mob_a, mob_b = Mob.monster_tick(tick=root.current_tick,
                                            damage_info={"boss": [{"pos": i["pos"].to_list(), "hit": i["hit"]} for i in
                                                                  root.mob_dict["boss"]],
                                                         "minion": [{"pos": i["pos"].to_list(), "hit": i["hit"]} for i
                                                                    in root.mob_dict["minion"]]})
            # print("pattern", mob_a[0]["pattern"])
            # print("mob_b", mob_b)

            # 적 체력 설정
            for i in range(len(mob_a)):
                root.mob_dict["boss"][i]["hp"] = mob_a[i]["hp"]
            for i in range(len(mob_b)):
                root.mob_dict["minion"][i]["hp"] = mob_b[i]["hp"]
                if mob_b[i]["hp"] == 0 and mob_b[i]["dropitem"] is not None:
                    root.set_item(root.mob_dict["minion"][i]["pos"], root.get_item_id(mob_b[i]["dropitem"]))

            # 보스 패턴 설치
            root.set_boss_pattern(mob_a[0]["pattern"])

            # print(Box.save_stats_to_csv())
            root.display()
        input("계속하려면 아무 키 입력")

    def statistics(root):
        # 통계 출력
        print("### 통계 ###")
        c = Character.get_stats()
        b = Box.save_stats_to_csv()

        # 이동 횟수 출력
        print(f"# 이동 횟수 ↑: {c['up_count']}, ↓: {c['down_count']}, ←: {c['left_count']}, →: {c['right_count']}")
        print(f"# 방향키 전환된 횟수: {c['reverse_count']}\t물풍선 설치한 횟수: {c['bomb_count']}")
        print()
        print(f"# 아이템 먹은 횟수")
        print(f"악마: {c['devil_count']}, 물줄기: {c['plus_scope_count']}, 물풍선: {c['plus_bomb_count']}")
        print()
        print(f"# 데미지 받은 횟수: {c['damage_count']}\t체력 1로 활동한 횟수: {c['danger_count']}")
        print()
        print(f"# 총 부서진 박스: {b['total_destroyed_boxes']},\t총 드랍된 아이템 수: {b['total_dropped_items']}")
        print(f"# 드랍된 아이템")
        print(
            f"악마: {b['item_counts']['devil']}, 물줄기: {b['item_counts']['plus_scope']}, 물풍선: {b['item_counts']['plus_bomb']}")
        print(f"드랍률: {b['drop_probability']}")

        # 랭킹
        root.rank.append({"name": root.player_name(), "key1": c["damage_count"], "key2": root.current_tick})
        root.rank.sort(key=lambda x: (-x["key1"], -x["key2"]), reverse=True)
        print("### 랭킹 ###")
        print("순위\t이름\t피격\t틱")
        print("\n".join([f"{i + 1}등\t{e['name']}\t{e['key1']}\t{e['key2']}" for i, e in enumerate(root.rank)]))
        print()
        input("계속하려면 아무 키 입력")

    def display(root):
        ch_box = {1: "\033[48;2;204;153;153;38;2;000;000;000m１\033[0m",
                  2: "\033[48;2;204;153;153;38;2;000;000;000m２\033[0m",
                  3: "\033[48;2;204;153;153;38;2;000;000;000m３\033[0m", 7: "\U0001F7EB"}
        ch_item = {1: "\U0001F9E8", 2: "\U0001F386", 3: "\U0001F608"}

        tmp = [["" for _ in range(root.map_size[0])] for _ in range(root.map_size[1])]
        stat = {
            0: "플레이어 체력",
            1: root.char_stat["hp"],
            3: "보스 체력",
            4: sum(i["hp"] for i in root.mob_dict["boss"]),
            6: "현재 틱 / 전체 틱",
            7: f"{root.current_tick} / {root.max_tick}",
            9: "아이템 리스트",
            10: f"개수 {root.char_stat['b_count']}",
            11: f"범위 {root.char_stat['b_range']}",
            12: f"악마 {root.char_stat['devil']}"
        }

        for i in range(root.map_size[0]):
            for j in range(root.map_size[1]):
                # 해당 좌표
                p = Pos(j, i)
                # 빈공간
                if root.is_empty(p):
                    tmp[i][j] = "　"
                elif root.is_box(p) and root.box_dict[p]["hp"] > 0:
                    if root.box_id(p) == 7:
                        tmp[i][j] = ch_box[root.box_id(p)]
                    else:
                        tmp[i][j] = ch_box[root.box_dict[p]["hp"]]
                elif root.is_player_bomb(p):
                    tmp[i][j] = "\U0001F4A3"
                elif root.is_boss_bomb(p):
                    # tmp[i][j] = "\U0001F525"
                    tmp[i][j] = "\u2622\uFE0F"
                elif root.is_item(p):
                    tmp[i][j] = ch_item[root.item_id(p)]
                elif root.is_water(p):
                    tmp[i][j] = "\U0001F525"
                else:
                    tmp[i][j] = root.get_info(p)

        # 보스
        for b in root.mob_dict["boss"]:
            if b["hp"] <= 0:
                continue
            p = Pos(b["pos"].x, b["pos"].y)
            for i in range(-1, 2):
                for j in range(-1, 2):
                    q = p + Pos(i, j)
                    tmp[q.y][q.x] = "\U0001FAA6"
            tmp[p.y][p.x] = "\U0001F47B"

        # 쫄몹
        for m in root.mob_dict["minion"]:
            if m["hp"] > 0:
                tmp[m["pos"].y][m["pos"].x] = "\U0001F47E"

        # 캐릭터
        if root.is_water(root.char_pos()) or root.char_pos() in root.minion_pos(
                live=True) or root.char_pos() in root.boss_pos(live=True, inline=True):
            tmp[root.char_stat["y"]][root.char_stat["x"]] = "\U0001F62D"
        else:
            tmp[root.char_stat["y"]][root.char_stat["x"]] = "\U0001F600"

        for i in range(root.map_size[1]):
            for j in range(root.map_size[0]):
                print(tmp[i][j], end="\t")
            if i in stat:
                print(stat[i], end="")
            print()

        print("──────────────────────────────────────────────────")

    def game_state(root):
        if all(i["hp"] <= 0 for i in root.mob_dict["boss"]):  # 보스가 죽었으면
            # print("game state", 0)
            return 0  # 클리어
        elif root.char_stat["hp"] <= 0 or root.current_tick >= root.max_tick:
            # print("game state", 1)
            return 1  # 게임오버
        # print("game state", 2)
        return 2  # 진행중

    def bomb(root, p: Pos, power, s=None, pl=None):
        if s is None:
            s = set()
        if pl is None:
            pl = []
        ls = [i for i in range(1, power + 1)]
        dr = [[-1, 0], [1, 0], [0, -1], [0, 1]]
        root.bomb_dict.pop(p, None)
        s.add(p)
        for d in dr:
            for l in ls:
                q = Pos(p.x + d[0] * l, p.y + d[1] * l)
                if not root.is_inside(q):
                    break
                s.add(q)
                if root.is_box(q) and not root.is_broken_box(q):
                    break
                if root.is_bomb(q) and q not in pl:
                    pl.append(q)
                    if q in root.bomb_dict:
                        s |= root.bomb(q, root.bomb_dict[q]["power"], s, pl)
                    break
        return s

    ###########################################################################
    # 유저 행동 선택 입력받기
    def inp_user_act(root):
        tmp_tick = 0
        # bomb_count = 0
        directions = []
        install_bomb = False

        while (tmp_tick != 1):
            _inp = input("입력>>")
            # print(root.bomb_count("player"))
            # 이동 # 시작이 wasd 중 하나 여야하고, 총 입력 길이가 0보다 크고 케릭터의 이동 가능한 크기보다 같거나 작아야함
            if _inp:
                if _inp[0] in "wasd" and 0 < len(_inp) <= root.char_stat["speed"]:
                    # 입력 값의 모든 요소 확인
                    for ele in _inp:
                        if ele == "w":
                            directions.append(ele)
                        elif ele == "a":
                            directions.append(ele)
                        elif ele == "s":
                            directions.append(ele)
                        elif ele == "d":
                            directions.append(ele)
                        else:
                            # print("오류메시지~~~")
                            directions.clear()  # 초기화
                            break  # 다시 입력받으러 감

                # 물풍선 설치
                elif _inp[0] == "q":
                    if not root.is_bomb(root.char_pos()) and not root.is_water(root.char_pos()) and root.bomb_count(
                            root.player_name()) < root.char_stat[
                        "b_count"] and install_bomb != True and root.char_pos() not in root.boss_pos(live=True,
                                                                                                     inline=True):
                        install_bomb = True

                        tmp_tick = 0
                        # bomb_count += 1
                        continue

                    else:
                        continue

                # 이동 안함
                elif _inp[0] == "e":
                    tmp_tick = 1

                else:
                    # print("오류메시지~~~")
                    tmp_tick = 0
                    directions.clear()
                    install_bomb = False
                    continue

                tmp_tick = 1

            else:
                continue

        root.char_dict['bomb'] = install_bomb
        root.char_dict['movement'] = directions
        return directions

        # 이동가능여부

    def is_movable_(root, direction):  # is_moveable(inp_user_act()[0])
        c = root.char_pos()
        r = -1 if root.char_stat["reverse"] else 1
        key = {"w": Pos(0, -r), "a": Pos(-r, 0), "s": Pos(0, r), "d": Pos(r, 0)}
        root.char_dict["movecheck"] = [
            act in key and (root.is_movable(c + key[act]) or root.is_broken_box(c + key[act])) for act in direction]

    def game_start_screen(root):
        print("""
                 ██████╗ ██╗   ██╗███████╗██████╗ ██╗   ██╗ ██████╗ ███╗   ██╗ ██████╗      █████╗ ██████╗  ██████╗ █████╗ ██████╗ ███████╗
                ██╔════╝ ╚██╗ ██╔╝██╔════╝██╔══██╗╚██╗ ██╔╝██╔═══██╗████╗  ██║██╔════╝     ██╔══██╗██╔══██╗██╔════╝██╔══██╗██╔══██╗██╔════╝
                ██║  ███╗ ╚████╔╝ █████╗  ██████╔╝ ╚████╔╝ ██║   ██║██╔██╗ ██║██║  ███╗    ███████║██████╔╝██║     ███████║██║  ██║█████╗  
                ██║   ██║  ╚██╔╝  ██╔══╝  ██╔══██╗  ╚██╔╝  ██║   ██║██║╚██╗██║██║   ██║    ██╔══██║██╔══██╗██║     ██╔══██║██║  ██║██╔══╝  
                ╚██████╔╝   ██║   ███████╗██║  ██║   ██║   ╚██████╔╝██║ ╚████║╚██████╔╝    ██║  ██║██║  ██║╚██████╗██║  ██║██████╔╝███████╗
                 ╚═════╝    ╚═╝   ╚══════╝╚═╝  ╚═╝   ╚═╝    ╚═════╝ ╚═╝  ╚═══╝ ╚═════╝     ╚═╝  ╚═╝╚═╝  ╚═╝ ╚═════╝╚═╝  ╚═╝╚═════╝ ╚══════╝






                 ██╗       ███████╗████████╗ █████╗ ██████╗ ████████╗    ██████╗        ███████╗██╗  ██╗██╗████████╗                       
                ███║       ██╔════╝╚══██╔══╝██╔══██╗██╔══██╗╚══██╔══╝    ╚════██╗       ██╔════╝╚██╗██╔╝██║╚══██╔══╝                       
                ╚██║       ███████╗   ██║   ███████║██████╔╝   ██║        █████╔╝       █████╗   ╚███╔╝ ██║   ██║                          
                 ██║       ╚════██║   ██║   ██╔══██║██╔══██╗   ██║       ██╔═══╝        ██╔══╝   ██╔██╗ ██║   ██║                          
                 ██║██╗    ███████║   ██║   ██║  ██║██║  ██║   ██║       ███████╗██╗    ███████╗██╔╝ ██╗██║   ██║                          
                 ╚═╝╚═╝    ╚══════╝   ╚═╝   ╚═╝  ╚═╝╚═╝  ╚═╝   ╚═╝       ╚══════╝╚═╝    ╚══════╝╚═╝  ╚═╝╚═╝   ╚═╝                          
                                                                                                                        """)
        ii = input()
        while ii not in ["1", "2"]:
            ii = input()
        return ii


if __name__ == "__main__":
    map_ = Map()
    while True:
        if map_.game_start_screen() == "2":
            break
        map_.initialize()
        map_.play()
        map_.statistics()
