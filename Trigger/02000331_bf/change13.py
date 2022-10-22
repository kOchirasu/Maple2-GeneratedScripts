""" trigger/02000331_bf/change13.xml """
from common import *
import state


class 대기(state.State):
    def on_tick(self) -> state.State:
        if npc_detected(boxId=9024, spawnIds=[604]):
            return 시작()


class 시작(state.State):
    def on_tick(self) -> state.State:
        if npc_detected(boxId=9030, spawnIds=[990]):
            return 분기점()


#  자코 몬스터 웨이브 중 꼬마가 사망했는지 체크 
class 분기점(state.State):
    def on_tick(self) -> state.State:
        if npc_detected(boxId=9030, spawnIds=[999]):
            return 보스전투()
        if monster_dead(boxIds=[604]):
            return 교체딜레이()


#  보스 몬스터 웨이브 중 꼬마가 사망했는지 체크 
class 보스전투(state.State):
    def on_tick(self) -> state.State:
        if monster_dead(boxIds=[999]):
            return 전투종료()
        if monster_dead(boxIds=[604]):
            return 교체딜레이()


#  보스 몬스터가 죽을 때 까지 꼬마 NPC가 살아 있는지 체크 
class 전투종료(state.State):
    def on_tick(self) -> state.State:
        if npc_detected(boxId=9024, spawnIds=[604]):
            return 디펜스성공()


#  모든 전투가 끝날 때 까지 꼬마 NPC가 살아 있으면 교체 없이 종료 
class 디펜스성공(state.State):
    pass


#  자코 또는 보스 몬스터와 전투 중 꼬마가 쓰러졌을 때 교체 진행 
class 교체딜레이(state.State):
    def on_tick(self) -> state.State:
        if wait_tick(waitTick=1000):
            return 교체쓰러짐()


class 교체쓰러짐(state.State):
    def on_enter(self):
        create_monster(spawnIds=[614])

    def on_tick(self) -> state.State:
        if npc_detected(boxId=9020, spawnIds=[600]):
            return 교체일어남()


class 교체일어남(state.State):
    def on_enter(self):
        change_monster(removeSpawnId=614, addSpawnId=410)


