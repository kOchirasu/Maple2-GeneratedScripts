""" trigger/52000074_qd/questnpcspawn01.xml """
from common import *
import state


class Wait(state.State):
    def on_enter(self):
        create_monster(spawnIds=[101,201], arg2=False)

    def on_tick(self) -> state.State:
        if quest_user_detected(boxIds=[9900], questIds=[40002679], questStates=[3]):
            return NpcRemove01()
        if quest_user_detected(boxIds=[9900], questIds=[40002679], questStates=[2]):
            return NpcChange01()
        if quest_user_detected(boxIds=[9900], questIds=[40002679], questStates=[1]):
            return NpcChange01()
        if quest_user_detected(boxIds=[9900], questIds=[40002678], questStates=[3]):
            return NpcChange01()
        if quest_user_detected(boxIds=[9900], questIds=[40002678], questStates=[2]):
            return NpcChange01()
        if quest_user_detected(boxIds=[9900], questIds=[40002678], questStates=[1]):
            return NpcChange01()
        if quest_user_detected(boxIds=[9900], questIds=[40002677], questStates=[3]):
            return NpcChange01()
        if quest_user_detected(boxIds=[9900], questIds=[40002677], questStates=[2]):
            return NpcChange01()
        if quest_user_detected(boxIds=[9900], questIds=[40002677], questStates=[1]):
            return NpcChange01()
        if quest_user_detected(boxIds=[9900], questIds=[40002676], questStates=[3]):
            return NpcChange01()
        if quest_user_detected(boxIds=[9900], questIds=[40002676], questStates=[2]):
            return NpcChange01()
        if quest_user_detected(boxIds=[9900], questIds=[40002676], questStates=[1]):
            return NpcChange01()
        if quest_user_detected(boxIds=[9900], questIds=[40002675], questStates=[3]):
            return NpcChange01()
        if quest_user_detected(boxIds=[9900], questIds=[40002675], questStates=[2]):
            return NpcChange01()
        if quest_user_detected(boxIds=[9900], questIds=[40002675], questStates=[1]):
            return NpcChange01()
        if quest_user_detected(boxIds=[9900], questIds=[40002674], questStates=[3]):
            return NpcChange01()
        if quest_user_detected(boxIds=[9900], questIds=[40002674], questStates=[2]):
            return NpcChange01()
        if quest_user_detected(boxIds=[9900], questIds=[40002674], questStates=[1]):
            return NpcChange01()
        if quest_user_detected(boxIds=[9900], questIds=[40002673], questStates=[3]):
            return NpcChange01()
        if quest_user_detected(boxIds=[9900], questIds=[40002673], questStates=[2]):
            return NpcTalk01()


class NpcRemove01(state.State):
    def on_enter(self):
        destroy_monster(spawnIds=[101,201])


class NpcChange01(state.State):
    def on_enter(self):
        destroy_monster(spawnIds=[101])
        create_monster(spawnIds=[102], arg2=False)


class NpcTalk01(state.State):
    def on_enter(self):
        destroy_monster(spawnIds=[101])
        create_monster(spawnIds=[102], arg2=False)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=1000):
            return CameraSet01()


class CameraSet01(state.State):
    def on_enter(self):
        set_scene_skip(state=TalkEnd01, arg2='exit')
        set_cinematic_ui(type=1)
        set_cinematic_ui(type=3)
        select_camera(triggerId=600, enable=True)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=2000):
            return EveTalk01()


class EveTalk01(state.State):
    def on_enter(self):
        set_npc_emotion_sequence(spawnId=201, sequenceName='Talk_A')
        set_conversation(type=2, spawnId=11001962, script='$52000074_QD__QUESTNPCSPAWN01__0$', arg4=5) # 이브

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=5000):
            return EveTalk01Skip()


class EveTalk01Skip(state.State):
    def on_enter(self):
        set_npc_emotion_sequence(spawnId=201, sequenceName='Idle_A')
        remove_cinematic_talk()
        # <action name="스킵을설정한다" arg1=""/>

    def on_tick(self) -> state.State:
        if true():
            return LennonTalk01()


class LennonTalk01(state.State):
    def on_enter(self):
        set_npc_emotion_sequence(spawnId=102, sequenceName='Talk_A')
        set_conversation(type=2, spawnId=11001961, script='$52000074_QD__QUESTNPCSPAWN01__1$', arg4=5) # 레논

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=5000):
            return LennonTalk01Skip()


class LennonTalk01Skip(state.State):
    def on_enter(self):
        set_npc_emotion_sequence(spawnId=102, sequenceName='Idle_A')
        remove_cinematic_talk()
        # <action name="스킵을설정한다" arg1=""/>

    def on_tick(self) -> state.State:
        if true():
            return EveTalk02()


class EveTalk02(state.State):
    def on_enter(self):
        set_npc_emotion_sequence(spawnId=201, sequenceName='Talk_A')
        set_conversation(type=2, spawnId=11001962, script='$52000074_QD__QUESTNPCSPAWN01__2$', arg4=3) # 이브

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=3000):
            return EveTalk02Skip()


class EveTalk02Skip(state.State):
    def on_enter(self):
        set_npc_emotion_sequence(spawnId=201, sequenceName='Idle_A')
        remove_cinematic_talk()
        # <action name="스킵을설정한다" arg1=""/>

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=1000):
            return TalkEnd01()


class TalkEnd01(state.State):
    def on_enter(self):
        set_scene_skip()
        select_camera(triggerId=600, enable=False)
        set_cinematic_ui(type=2)
        set_cinematic_ui(type=0)


