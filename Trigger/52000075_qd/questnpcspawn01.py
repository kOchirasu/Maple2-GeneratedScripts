""" trigger/52000075_qd/questnpcspawn01.xml """
from common import *
import state


class Wait(state.State):
    def on_enter(self):
        set_agent(triggerIds=[8000,8001,8002,8003,8004,8005,8006,8007,8008,8009,8010,8011,8012,8013,8014,8015,8016,8017], visible=False)
        create_monster(spawnIds=[101,201], arg2=False) # 레이먼, 경비병
        set_onetime_effect(id=1, enable=False, path='BG/Common/ScreenMask/Eff_fadein_1sec.xml')

    def on_tick(self) -> state.State:
        if quest_user_detected(boxIds=[9900], questIds=[40002668], questStates=[3]):
            return RemoveNpc01()
        if quest_user_detected(boxIds=[9900], questIds=[40002668], questStates=[2]):
            return GuardDown01()
        if quest_user_detected(boxIds=[9900], questIds=[40002668], questStates=[1]):
            return GuardDown01()
        if quest_user_detected(boxIds=[9900], questIds=[40002667], questStates=[3]):
            return GuardDown01()
        if quest_user_detected(boxIds=[9900], questIds=[40002667], questStates=[2]):
            return GuardDown01()
        if quest_user_detected(boxIds=[9900], questIds=[40002667], questStates=[1]):
            return NpcChange01()


#  40002668 퀘스트 완료 상태 
class RemoveNpc01(state.State):
    def on_enter(self):
        destroy_monster(spawnIds=[101,201])


#  40002667 퀘스트 진행중 상태 
class NpcChange01(state.State):
    def on_enter(self):
        set_agent(triggerIds=[8000,8001,8002,8003,8004,8005,8006,8007,8008,8009,8010,8011,8012,8013,8014,8015,8016,8017], visible=True)
        destroy_monster(spawnIds=[101,201])
        create_monster(spawnIds=[202,900,901,902], arg2=False)

    def on_tick(self) -> state.State:
        if monster_dead(boxIds=[900,901,902]):
            return MobChange01()


class MobChange01(state.State):
    def on_enter(self):
        set_cinematic_ui(type=1)
        set_cinematic_ui(type=3)
        set_onetime_effect(id=1, enable=True, path='BG/Common/ScreenMask/Eff_fadein_1sec.xml')

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=1000):
            return MobChange02()


class MobChange02(state.State):
    def on_enter(self):
        move_user(mapId=52000075, portalId=10)
        create_monster(spawnIds=[301], arg2=False) # 어둠의 졸개

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=1000):
            return MobChange03()


class MobChange03(state.State):
    def on_tick(self) -> state.State:
        if wait_tick(waitTick=1000):
            return MobChange04()


class MobChange04(state.State):
    def on_enter(self):
        set_onetime_effect(id=1, enable=False, path='BG/Common/ScreenMask/Eff_fadein_1sec.xml')
        select_camera(triggerId=600, enable=True)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=1000):
            return MobTalk01()


class MobTalk01(state.State):
    def on_enter(self):
        set_cinematic_ui(type=1)
        set_cinematic_ui(type=3)
        set_conversation(type=2, spawnId=11001960, script='$52000075_QD__QUESTNPCSPAWN01__0$', arg4=4) # 어둠의 졸개
        set_skip(state=MobTalk02)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=4000):
            return MobTalk02()


class MobTalk02(state.State):
    def on_enter(self):
        remove_cinematic_talk()
        set_skip()
        set_cinematic_ui(type=0)
        set_cinematic_ui(type=2)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=1000):
            return MobTalk03()


class MobTalk03(state.State):
    def on_enter(self):
        select_camera(triggerId=600, enable=False)
        destroy_monster(spawnIds=[301])

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=1000):
            return QuestComplete01()


class QuestComplete01(state.State):
    def on_enter(self):
        set_achievement(triggerId=9900, type='trigger', achieve='abductedRamon')


#  40002667 퀘스트 완료 가능 상태 
class GuardDown01(state.State):
    def on_enter(self):
        destroy_monster(spawnIds=[101,201])
        create_monster(spawnIds=[202], arg2=False)


