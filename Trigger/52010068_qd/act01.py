""" trigger/52010068_qd/act01.xml """
from common import *
import state


class Wait(state.State):
    def on_tick(self) -> state.State:
        if quest_user_detected(boxIds=[9001], questIds=[91000074], questStates=[2]):
            return NPC리젠03_담당관과트리스탄_02()
        if quest_user_detected(boxIds=[9001], questIds=[91000050], questStates=[2]):
            return NPC리젠02_담당관과트리스탄()
        if quest_user_detected(boxIds=[9001], questIds=[91000037], questStates=[2]):
            return NPC리젠01_5대세력담당관()
        if quest_user_detected(boxIds=[9001], questIds=[91000075], questStates=[3]):
            return 종료()
        if quest_user_detected(boxIds=[9001], questIds=[91000074], questStates=[3]):
            return NPC리젠03_담당관과트리스탄_02()
        if quest_user_detected(boxIds=[9001], questIds=[91000063], questStates=[3]):
            return NPC리젠01_5대세력담당관()
        if quest_user_detected(boxIds=[9001], questIds=[91000058], questStates=[3]):
            return 종료()
        if quest_user_detected(boxIds=[9001], questIds=[91000057], questStates=[3]):
            return NPC리젠01_5대세력담당관()
        if quest_user_detected(boxIds=[9001], questIds=[91000050], questStates=[3]):
            return NPC리젠02_담당관과트리스탄()
        if quest_user_detected(boxIds=[9001], questIds=[91000043], questStates=[3]):
            return NPC리젠03_트리스탄솔로()
        if quest_user_detected(boxIds=[9001], questIds=[91000049], questStates=[3]):
            return NPC리젠02_담당관과트리스탄()
        if quest_user_detected(boxIds=[9001], questIds=[91000046], questStates=[3]):
            return NPC리젠01_5대세력담당관()
        if quest_user_detected(boxIds=[9001], questIds=[91000019], questStates=[3]):
            return 종료()


class NPC리젠03_트리스탄솔로(state.State):
    def on_enter(self):
        create_monster(spawnIds=[2005], arg2=False) # 트리스탄

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=1000):
            return 종료()


class NPC리젠01_5대세력담당관(state.State):
    def on_enter(self):
        create_monster(spawnIds=[2000], arg2=False) # 블리체
        create_monster(spawnIds=[2001], arg2=False) # 콘대르
        create_monster(spawnIds=[2002], arg2=False) # 메이슨
        create_monster(spawnIds=[2003], arg2=False) # 샤텐
        create_monster(spawnIds=[2004], arg2=False) # 네이린

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=1000):
            return 종료()


class NPC리젠02_담당관과트리스탄(state.State):
    def on_enter(self):
        create_monster(spawnIds=[2000], arg2=False) # 블리체
        create_monster(spawnIds=[2001], arg2=False) # 콘대르
        create_monster(spawnIds=[2002], arg2=False) # 메이슨
        create_monster(spawnIds=[2003], arg2=False) # 샤텐
        create_monster(spawnIds=[2004], arg2=False) # 네이린
        create_monster(spawnIds=[2005], arg2=False) # 트리스탄

    def on_tick(self) -> state.State:
        if quest_user_detected(boxIds=[9001], questIds=[91000057], questStates=[3]):
            return 트리스탄삐짐01()


class 트리스탄삐짐01(state.State):
    def on_enter(self):
        set_cinematic_ui(type=1)
        set_cinematic_ui(type=3)
        add_cinematic_talk(npcId=11003790, illustId='Tristan_normal', msg='$52010052_QD__ACT01__0$', duration=4000) # 11003790: 트리스탄
        move_npc(spawnId=2005, patrolName='MS2PatrolData_1001')

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=5000):
            return 트리스탄삐짐02()


class 트리스탄삐짐02(state.State):
    def on_enter(self):
        set_cinematic_ui(type=0)
        set_cinematic_ui(type=2)
        destroy_monster(spawnIds=[2005])

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=1000):
            return 종료()


class NPC리젠03_담당관과트리스탄_02(state.State):
    def on_enter(self):
        create_monster(spawnIds=[2000], arg2=False) # 블리체
        create_monster(spawnIds=[2001], arg2=False) # 콘대르
        create_monster(spawnIds=[2002], arg2=False) # 메이슨
        create_monster(spawnIds=[2003], arg2=False) # 샤텐
        create_monster(spawnIds=[2004], arg2=False) # 네이린
        create_monster(spawnIds=[2005], arg2=False) # 트리스탄

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=1000):
            return 종료()


class 종료(state.State):
    pass


