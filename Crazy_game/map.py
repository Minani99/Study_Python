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
    def __init__(self):
        self.map_size = [15, 15]  # x y
        self.map_info = []
        self.max_tick = 10000
        self.current_tick = 0

        self.box_dict = {}  # {pos: {hp: int, hit: bool}}
        self.item_dict = {}  # {pos: key}
        self.bomb_dict = {}  # {pos: {owner: str, power: int}}}

        self.char_stat = {}  #
        self.mob_dict = {}  # {boss: [{pos: Pos, hp: int, hit: bool}], minion: [{pos: Pos, hp: int, hit: bool}]}
        self.char_dict = {}
        self.rank = []

    def set_info(self, p: Pos, v):
        self.map_info[p.y][p.x] = v

    def set_box(self, p: Pos, box_id):
        self.set_info(p, box_id << 2)

    def set_item(self, p: Pos, item_id):
        self.set_info(p, item_id << 5)

    def set_empty(self, p: Pos):
        self.set_info(p, 0)

    def set_water(self, p: Pos):
        self.set_info(p, 1)

    def set_player_bomb(self, p: Pos):
        self.set_info(p, 2)

    def set_boss_bomb(self, p: Pos):
        self.set_info(p, 3)

    def set_boss_pattern(self, l: list):
        for i in l:
            p = Pos.from_list(i)
            if self.is_inside(p) and (not self.is_box(p) or self.is_broken_box(p)):
                self.set_boss_bomb(p)
                self.add_bomb("boss", p, 1)

    def get_info(self, p: Pos) -> Any:
        return self.map_info[p.y][p.x]

    def is_inside(self, p: Pos):
        return (0 <= p.x < self.map_size[0]) and (0 <= p.y < self.map_size[1])

    def all_pos(self):
        return [Pos(x, y) for y in range(self.map_size[0]) for x in range(self.map_size[1])]

    def is_item(self, p: Pos):
        return self.get_info(p) >= 32

    def is_box(self, p: Pos):
        return 32 > self.get_info(p) >= 4

    def is_broken_box(self, p: Pos):
        return self.is_box(p) and self.box_dict[p]["hp"] == 0

    def is_player_bomb(self, p: Pos):
        return self.get_info(p) == 2

    def is_boss_bomb(self, p: Pos):
        return self.get_info(p) == 3

    def is_bomb(self, p: Pos):
        return self.is_player_bomb(p) or self.is_boss_bomb(p)

    def is_water(self, p: Pos):
        return self.get_info(p) == 1

    def is_empty(self, p: Pos):
        return self.get_info(p) == 0

    def is_movable(self, p: Pos):
        return self.is_empty(p) or self.is_water(p) or self.is_item(p)

    def item_id(self, p: Pos):
        return self.get_info(p) >> 5

    def box_id(self, p: Pos):
        return (self.get_info(p) >> 2) & 7

    def get_item_id(self, s: str):
        return list(Item.ITEM_TYPES.keys()).index(s) + 1

    def get_item_name(self, p: Pos):
        if self.is_item(p):
            return list(Item.ITEM_TYPES.keys())[self.item_id(p) - 1]
        return None

    def add_bomb(self, name, pos, power):
        self.bomb_dict[pos] = {"owner": name, "power": power}

    def bomb_count(self, name):
        return sum(1 for i in self.bomb_dict if name == self.bomb_dict[i]["owner"])

    def char_pos(self):
        return Pos(self.char_stat["x"], self.char_stat["y"])

    def boss_pos(self, live=False, inline=False):
        output = []
        for b in self.mob_dict["boss"]:
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

    def minion_pos(self, live=False):
        return [m["pos"] for m in self.mob_dict["minion"] if not (live and m["hp"] <= 0)]

    def player_name(self):
        return self.char_stat["name"]

    ###########################################################################

    def initialize(self):
        self.map_info = [[0 for i in range(self.map_size[0])] for j in range(self.map_size[1])]  # 맵 사이즈

        # 박스&빈 공간
        for i in range(self.map_size[1]):  # y
            for j in range(self.map_size[0]):  # x
                point_num = random.uniform(0, 1)  # 확률
                if point_num > 0.3:  # 70% 박스
                    if point_num <= 0.37:
                        self.map_info[i][j] = 28  # 부서지지 않는 박스 -1
                    elif 0.37 < point_num <= 0.5:
                        self.map_info[i][j] = 12  # 박스 체력 3
                        # self.map_info[i][j] = 4  # 박스 체력 3
                    elif 0.5 < point_num <= 0.7:
                        self.map_info[i][j] = 8  # 박스 체력 2
                        # self.map_info[i][j] = 4  # 박스 체력 2
                    else:
                        self.map_info[i][j] = 4  # 박스 체력 1
                else:  # 아니면 빈 공간
                    self.map_info[i][j] = 0

        # 구역 9개
        for i in range(3):
            for j in range(3):
                self.map_info[(self.map_size[1] // 2) - 1 + j][
                    (self.map_size[0] // 2) - 1 + i] = 0  # 중앙 고정 값(보스) [13][13]
                self.map_info[(self.map_size[1] - 4) + j][(self.map_size[1] - 4) + i] = 0  # 오른쪽 모서리 아래 [23][23]
                self.map_info[(self.map_size[1] - 4) + j][i + 1] = 0  # 왼쪽 모서리 아래 # [23][3]
                self.map_info[j + 1][(self.map_size[1] - 4) + i] = 0  # 오른쪽 모서리 위 [3][23]
                self.map_info[j + 1][i + 1] = 0  # 왼쪽 위 모서리 # [3][3]
                self.map_info[(self.map_size[1] - 4) + j][(self.map_size[0] // 2) - 1 + i] = 0  # 아래 중앙 # [23][13]
                self.map_info[j + 1][(self.map_size[0] // 2) - 1 + i] = 0  # 위 중앙 # [3][13]
                self.map_info[(self.map_size[0] // 2) - 1 + j][i + 1] = 0  # 왼쪽 중앙 # [13][3]
                self.map_info[(self.map_size[0] // 2) - 1 + j][(self.map_size[1] - 4) + i] = 0  # 오른쪽 중앙 # [13][23]

        # 맵 외곽은 부서지지 않는 박스
        for i in range(self.map_size[0]):
            for j in range(self.map_size[0]):
                self.map_info[0][i] = 28  # 윗줄
                self.map_info[-1][i] = 28  # 아랫줄
                self.map_info[j][0] = 28  # 왼쪽줄
                self.map_info[j][-1] = 28  # 오른쪽줄

        # map size 13 13
        # print(i, j)
        # 12 12

        # 각 구역 중앙 값
        A_point = Pos(self.map_size[0] // 2, self.map_size[1] // 2)  # 중앙 보스 [12][12]
        B_point = Pos(self.map_size[0] - 3, 2)  # 오른쪽 모서리 위 [24][0]
        C_point = Pos(self.map_size[0] // 2, 2)  # 위 중앙 [24][12]
        D_point = Pos(2, 2)  # 왼쪽 위 모서리 # [24][24]
        E_point = Pos(2, self.map_size[1] // 2)  # 왼쪽 중앙 [12][24]
        F_point = Pos(self.map_size[0] - 3, self.map_size[1] // 2)  # 오른쪽 중앙 [12][0]
        G_point = Pos(2, self.map_size[1] - 3)  # 왼쪽 모서리 아래 # [0][24]
        H_point = Pos(self.map_size[0] // 2, self.map_size[1] - 3)  # 아래 중앙 [0][12]
        I_point = Pos(self.map_size[0] - 3, self.map_size[1] - 3)  # 오른쪽 모서리 아래 [0][0]

        # point_list = [A_point, B_point, ...]

        ###########################################################################
        point_list = [B_point, C_point, D_point, E_point, F_point, G_point, H_point, I_point]
        for i in range(len(point_list) - 1):
            r = random.randrange(i + 1, len(point_list))
            point_list[i], point_list[r] = point_list[r], point_list[i]
        # print(point_list)

        self.current_tick = 0

        self.box_dict = {}
        for i in range(self.map_size[0]):
            for j in range(self.map_size[1]):
                p = Pos(j, i)
                if self.is_box(p):
                    self.box_dict[p] = {"hp": self.box_id(p), "hit": False}
                # print(self.map_info[i][j], end="\t")

        # 박스 id(1~7), 아이템(1~7), 0(없음), 1(물줄기), 2(물풍선)
        # 000 000 00 / 32 4 1
        # print([value["hp"] for _, value in self.box_dict.items()])
        Box.init([value["hp"] for _, value in self.box_dict.items()])

        # for i in range(self.map_size[0]):
        #     for j in range(self.map_size[1]):
        #         print(self.map_info[i][j], end="\t")
        #     print()

        # 캐릭터
        # 이름 입력받고
        n = input("이름: ")
        while n == "":
            n = input("이름: ")
        self.char_stat = Character.init(x=point_list[1].x, y=point_list[1].y, name=n)
        # print(self.char_stat)

        # 보스 초기화
        self.mob_dict = {"boss": [{"pos": A_point, "hp": -1, "hit": False}],
                         "minion": [{"pos": point_list[i], "hp": -1, "hit": False} for i in range(2, 7)]}
        mob_a, mob_b = Mob.init(boss_coords=[i["pos"].to_list() for i in self.mob_dict["boss"]],
                                minion_coords=[i["pos"].to_list() for i in self.mob_dict["minion"]])
        # print(self.minion_pos())
        # print("init mob_b", mob_b)
        for i in range(len(mob_a)):
            self.mob_dict["boss"][i]["hp"] = mob_a[i]["hp"]
        for i in range(len(mob_b)):
            self.mob_dict["minion"][i]["hp"] = mob_b[i]["hp"]

    ###########################################################################

    def play(self):
        self.display()
        last_tick = False
        mob_b = [{"move": [0, 0]} for _ in self.mob_dict["minion"]]
        while not last_tick:
            # last tick 체크
            last_tick = self.game_state() != 2
            if last_tick:
                print("게임 끝남")
                break

            self.current_tick += 1

            self.char_dict = {
                "movement": [],
                "movecheck": [],
                "dropped_item": [],
                "hit_count": 0,
                "bomb": False,

                "bomb_hit": False,
                "clear": False,
                "nowtick": self.current_tick,
            }
            # i = input("test: ")
            # 입력
            self.is_movable_(self.inp_user_act())

            # 직전 틱의 물줄기는 빈칸으로 초기화
            for p in self.all_pos():
                if self.is_water(p):
                    self.set_empty(p)

            # 박스 맞음 상태 false로 초기화
            for key in self.box_dict:
                self.box_dict[key]["hit"] = False
            # 몹 맞음 상태 false로 초기화
            for b in self.mob_dict["boss"]:
                b["hit"] = False
            for m in self.mob_dict["minion"]:
                m["hit"] = False

            # 적 실제 이동
            for i in range(len(self.mob_dict["minion"])):
                p = Pos.from_list(mob_b[i]["move"])
                if self.is_inside(p) and not (self.is_box(p) or self.is_bomb(p)) and not (
                        p in self.boss_pos(live=True, inline=True)):
                    self.mob_dict["minion"][i]["pos"] = p

            # 캐릭터 물풍선 리스트에 추가
            if self.char_dict["bomb"]:
                self.add_bomb(self.player_name(), self.char_pos(), self.char_stat["b_range"])

            # bomb tick
            bomb_a, bomb_b = Bomb.tick(self.bomb_dict)
            self.bomb_dict = bomb_b
            # print("bomb_dict", self.bomb_dict)

            # 맵에 물풍선 놓기
            for p in self.bomb_dict:
                if self.bomb_dict[p]["owner"] == "boss":
                    # self.set_boss_bomb(p)
                    pass
                else:
                    self.set_player_bomb(p)

            # 캐릭터 이동 (임시)
            r = -1 if self.char_stat["reverse"] else 1
            mv = {"w": Pos(0, -r), "a": Pos(-r, 0), "s": Pos(0, r), "d": Pos(r, 0)}
            p = self.char_pos()
            for i in range(len(self.char_dict["movecheck"])):
                if self.char_dict["movecheck"][i]:
                    p += mv[self.char_dict["movement"][i]]
            self.char_stat["x"] = p.x
            self.char_stat["y"] = p.y

            # 아이템 맞았나 체크
            if self.is_item(self.char_pos()):
                iname = self.get_item_name(self.char_pos())
                # print(iname, "먹음")
                del self.item_dict[self.char_pos()]
                self.char_dict["dropped_item"].append(iname)
                self.set_empty(self.char_pos())
            # 아이템 먹으면 다음 틱부터 능력치 적용

            # print("item_dict", self.item_dict)
            # 터짐
            for p in bomb_a:
                for q in self.bomb(p, bomb_a[p]["power"]):
                    if self.is_box(q):
                        self.box_dict[q]["hit"] = True
                    elif q in self.item_dict:  # 아이템이 맞았는지
                        # print("아이템 물에 맞음")
                        del self.item_dict[q]
                        self.set_water(q)
                    else:
                        self.set_water(q)
                    # 적이 맞았는지
                    for i in range(len(self.boss_pos())):
                        if q in self.boss_pos()[i]:
                            self.mob_dict["boss"][i]["hit"] = True

                    for m in self.mob_dict["minion"]:
                        if q == m["pos"]:
                            m["hit"] = True
                    # 플레이어가 맞았는지
                    if q == self.char_pos():
                        # print("플레이어 물에 맞음")
                        self.char_dict["bomb_hit"] = True
            # print("item_dict", self.item_dict)

            # 적이랑 맞았는지 체크
            for p in self.boss_pos(live=True, inline=True):
                if self.char_pos() == p:
                    self.char_dict["hit_count"] = 1  # 임시
                    # print("플레이어 보스에 맞음")
            for p in self.minion_pos(live=True):
                if self.char_pos() == p and not self.is_water(self.char_pos()):
                    self.char_dict["hit_count"] = 1  # 임시
                    # print("플레이어 미니언에 맞음")

            # print("char_dict", self.char_dict)

            # self.char_dict["clear"] = False

            # character tick
            # print("character tick")
            self.char_stat = Character.tick(self.char_dict)
            # print("char_stat", self.char_stat)

            # box tick
            # print("box tick")
            box_a = Box.box_tick(damage_flags=[value["hit"] for _, value in self.box_dict.items()])
            for i, p in enumerate(self.box_dict):
                self.box_dict[p]["hp"] = box_a[i]["remaining_hp"]
                if self.is_broken_box(p):
                    if box_a[i]["item"] is not None:
                        self.set_item(p, self.get_item_id(box_a[i]["item"]))
                        self.item_dict[p] = box_a[i]["item"]
                    else:
                        self.set_empty(p)

            # mob tick
            # print("mob_dict", self.mob_dict)
            # print("mob tick")
            mob_a, mob_b = Mob.monster_tick(tick=self.current_tick,
                                            damage_info={"boss": [{"pos": i["pos"].to_list(), "hit": i["hit"]} for i in
                                                                  self.mob_dict["boss"]],
                                                         "minion": [{"pos": i["pos"].to_list(), "hit": i["hit"]} for i
                                                                    in self.mob_dict["minion"]]})
            # print("pattern", mob_a[0]["pattern"])
            # print("mob_b", mob_b)

            # 적 체력 설정
            for i in range(len(mob_a)):
                self.mob_dict["boss"][i]["hp"] = mob_a[i]["hp"]
            for i in range(len(mob_b)):
                self.mob_dict["minion"][i]["hp"] = mob_b[i]["hp"]
                if mob_b[i]["hp"] == 0 and mob_b[i]["dropitem"] is not None:
                    self.set_item(self.mob_dict["minion"][i]["pos"], self.get_item_id(mob_b[i]["dropitem"]))

            # 보스 패턴 설치
            self.set_boss_pattern(mob_a[0]["pattern"])

            # print(Box.save_stats_to_csv())
            self.display()
        input("계속하려면 아무 키 입력")

    def statistics(self):
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
        self.rank.append({"name": self.player_name(), "key1": c["damage_count"], "key2": self.current_tick})
        self.rank.sort(key=lambda x: (-x["key1"], -x["key2"]), reverse=True)
        print("### 랭킹 ###")
        print("순위\t이름\t피격\t틱")
        print("\n".join([f"{i + 1}등\t{e['name']}\t{e['key1']}\t{e['key2']}" for i, e in enumerate(self.rank)]))
        print()
        input("계속하려면 아무 키 입력")

    def display(self):
        ch_box = {1: "\033[48;2;204;153;153;38;2;000;000;000m１\033[0m",
                  2: "\033[48;2;204;153;153;38;2;000;000;000m２\033[0m",
                  3: "\033[48;2;204;153;153;38;2;000;000;000m３\033[0m", 7: "\U0001F7EB"}
        ch_item = {1: "\U0001F9E8", 2: "\U0001F386", 3: "\U0001F608"}

        tmp = [["" for _ in range(self.map_size[0])] for _ in range(self.map_size[1])]
        stat = {
            0: "플레이어 체력",
            1: self.char_stat["hp"],
            3: "보스 체력",
            4: sum(i["hp"] for i in self.mob_dict["boss"]),
            6: "현재 틱 / 전체 틱",
            7: f"{self.current_tick} / {self.max_tick}",
            9: "아이템 리스트",
            10: f"개수 {self.char_stat['b_count']}",
            11: f"범위 {self.char_stat['b_range']}",
            12: f"악마 {self.char_stat['devil']}"
        }

        for i in range(self.map_size[0]):
            for j in range(self.map_size[1]):
                # 해당 좌표
                p = Pos(j, i)
                # 빈공간
                if self.is_empty(p):
                    tmp[i][j] = "　"
                elif self.is_box(p) and self.box_dict[p]["hp"] > 0:
                    if self.box_id(p) == 7:
                        tmp[i][j] = ch_box[self.box_id(p)]
                    else:
                        tmp[i][j] = ch_box[self.box_dict[p]["hp"]]
                elif self.is_player_bomb(p):
                    tmp[i][j] = "\U0001F4A3"
                elif self.is_boss_bomb(p):
                    # tmp[i][j] = "\U0001F525"
                    tmp[i][j] = "\u2622\uFE0F"
                elif self.is_item(p):
                    tmp[i][j] = ch_item[self.item_id(p)]
                elif self.is_water(p):
                    tmp[i][j] = "\U0001F525"
                else:
                    tmp[i][j] = self.get_info(p)

        # 보스
        for b in self.mob_dict["boss"]:
            if b["hp"] <= 0:
                continue
            p = Pos(b["pos"].x, b["pos"].y)
            for i in range(-1, 2):
                for j in range(-1, 2):
                    q = p + Pos(i, j)
                    tmp[q.y][q.x] = "\U0001FAA6"
            tmp[p.y][p.x] = "\U0001F47B"

        # 쫄몹
        for m in self.mob_dict["minion"]:
            if m["hp"] > 0:
                tmp[m["pos"].y][m["pos"].x] = "\U0001F47E"

        # 캐릭터
        if self.is_water(self.char_pos()) or self.char_pos() in self.minion_pos(
                live=True) or self.char_pos() in self.boss_pos(live=True, inline=True):
            tmp[self.char_stat["y"]][self.char_stat["x"]] = "\U0001F62D"
        else:
            tmp[self.char_stat["y"]][self.char_stat["x"]] = "\U0001F600"

        for i in range(self.map_size[1]):
            for j in range(self.map_size[0]):
                print(tmp[i][j], end="\t")
            if i in stat:
                print(stat[i], end="")
            print()

        print("──────────────────────────────────────────────────")

    def game_state(self):
        if all(i["hp"] <= 0 for i in self.mob_dict["boss"]):  # 보스가 죽었으면
            # print("game state", 0)
            return 0  # 클리어
        elif self.char_stat["hp"] <= 0 or self.current_tick >= self.max_tick:
            # print("game state", 1)
            return 1  # 게임오버
        # print("game state", 2)
        return 2  # 진행중

    def bomb(self, p: Pos, power, s=None, pl=None):
        if s is None:
            s = set()
        if pl is None:
            pl = []
        ls = [i for i in range(1, power + 1)]
        dr = [[-1, 0], [1, 0], [0, -1], [0, 1]]
        self.bomb_dict.pop(p, None)
        s.add(p)
        for d in dr:
            for l in ls:
                q = Pos(p.x + d[0] * l, p.y + d[1] * l)
                if not self.is_inside(q):
                    break
                s.add(q)
                if self.is_box(q) and not self.is_broken_box(q):
                    break
                if self.is_bomb(q) and q not in pl:
                    pl.append(q)
                    if q in self.bomb_dict:
                        s |= self.bomb(q, self.bomb_dict[q]["power"], s, pl)
                    break
        return s

    ###########################################################################
    # 유저 행동 선택 입력받기
    def inp_user_act(self):
        tmp_tick = 0
        # bomb_count = 0
        directions = []
        install_bomb = False

        while (tmp_tick != 1):
            _inp = input("입력>>")
            # print(self.bomb_count("player"))
            # 이동 # 시작이 wasd 중 하나 여야하고, 총 입력 길이가 0보다 크고 케릭터의 이동 가능한 크기보다 같거나 작아야함
            if _inp:
                if _inp[0] in "wasd" and 0 < len(_inp) <= self.char_stat["speed"]:
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
                    if not self.is_bomb(self.char_pos()) and not self.is_water(self.char_pos()) and self.bomb_count(
                            self.player_name()) < self.char_stat[
                        "b_count"] and install_bomb != True and self.char_pos() not in self.boss_pos(live=True,
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

        self.char_dict['bomb'] = install_bomb
        self.char_dict['movement'] = directions
        return directions

        # 이동가능여부

    def is_movable_(self, direction):  # is_moveable(inp_user_act()[0])
        c = self.char_pos()
        r = -1 if self.char_stat["reverse"] else 1
        key = {"w": Pos(0, -r), "a": Pos(-r, 0), "s": Pos(0, r), "d": Pos(r, 0)}
        self.char_dict["movecheck"] = [
            act in key and (self.is_movable(c + key[act]) or self.is_broken_box(c + key[act])) for act in direction]

    def game_start_screen(self):
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
