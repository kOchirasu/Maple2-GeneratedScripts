""" trigger/52000072_qd/questnpcspawn01.xml """
from common import *
import state


class Wait(state.State):
    def on_enter(self):
        set_onetime_effect(id=1, enable=False, path='BG/Common/ScreenMask/Eff_fadein_1sec.xml')

    def on_tick(self) -> state.State:
        if quest_user_detected(boxIds=[9900], questIds=[40002684], questStates=[2]):
            return None # Missing State: NpcRemove01
        if quest_user_detected(boxIds=[9900], questIds=[40002684], questStates=[1]):
            return NpcChange01()
        if quest_user_detected(boxIds=[9900], questIds=[40002683], questStates=[3]):
            return NpcChange01()
        if quest_user_detected(boxIds=[9900], questIds=[40002683], questStates=[2]):
            return NpcChange01()
        if quest_user_detected(boxIds=[9900], questIds=[40002683], questStates=[1]): # 레논이 있던 자리
            return NpcChange01()
        if quest_user_detected(boxIds=[9900], questIds=[40002682], questStates=[3]):
            return NpcChange02()
        if quest_user_detected(boxIds=[9900], questIds=[40002682], questStates=[2]):
            return NpcChange02()
        if quest_user_detected(boxIds=[9900], questIds=[40002682], questStates=[1]):
            return NpcChange02()
        if quest_user_detected(boxIds=[9900], questIds=[40002681], questStates=[3]):
            return NpcChange02()
        if quest_user_detected(boxIds=[9900], questIds=[40002681], questStates=[2]):
            return NpcChange02()
        if quest_user_detected(boxIds=[9900], questIds=[40002681], questStates=[1]):
            return SetCamera01()


class NpcChange01(state.State):
    def on_enter(self):
        create_monster(spawnIds=[201], arg2=False)


class NpcChange02(state.State):
    def on_enter(self):
        create_monster(spawnIds=[101], arg2=False)


#  NPC 패트롤 연출 
class SetCamera01(state.State):
    def on_enter(self):
        set_scene_skip(state=ActEnd01, arg2='exit')
        set_cinematic_ui(type=1)
        set_cinematic_ui(type=3)
        set_onetime_effect(id=1, enable=True, path='BG/Common/ScreenMask/Eff_fadein_1sec.xml')

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=1000):
            return SetCamera02()


class SetCamera02(state.State):
    def on_enter(self):
        select_camera(triggerId=600, enable=True)
        create_monster(spawnIds=[102,301,401], arg2=False)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=2000):
            return ActStart01()


class ActStart01(state.State):
    def on_enter(self):
        set_cinematic_ui(type=1)
        set_cinematic_ui(type=3)
        set_onetime_effect(id=1, enable=False, path='BG/Common/ScreenMask/Eff_fadein_1sec.xml')
        move_npc(spawnId=301, patrolName='MS2PatrolData_301')
        move_npc(spawnId=401, patrolName='MS2PatrolData_401')

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=1000):
            return ActStart02()


class ActStart02(state.State):
    def on_enter(self):
        move_npc(spawnId=102, patrolName='MS2PatrolData_102')

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=1000):
            return ActStart03()


class ActStart03(state.State):
    def on_enter(self):
        select_camera(triggerId=601, enable=True)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=3000):
            return ActEnd01()


class ActEnd01(state.State):
    def on_enter(self):
        set_scene_skip()
        set_onetime_effect(id=1, enable=True, path='BG/Common/ScreenMask/Eff_fadein_1sec.xml')
        destroy_monster(spawnIds=[301,401])

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=500):
            return ActEnd02()


class ActEnd02(state.State):
    def on_enter(self):
        destroy_monster(spawnIds=[102])
        create_monster(spawnIds=[101], arg2=False)
        reset_camera(interpolationTime=1)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=1500):
            return ActEnd03()


class ActEnd03(state.State):
    def on_enter(self):
        set_onetime_effect(id=1, enable=False, path='BG/Common/ScreenMask/Eff_fadein_1sec.xml')
        set_cinematic_ui(type=0)
        set_cinematic_ui(type=2)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=1000):
            return QuestComplete()


class QuestComplete(state.State):
    def on_enter(self):
        set_achievement(triggerId=9900, type='trigger', achieve='triangularRelation')


