""" trigger/52010002_qd/main.xml """
from common import *
import state


class idle(state.State):
    def on_tick(self) -> state.State:
        if quest_user_detected(boxIds=[701], questIds=[10002789], questStates=[1]): # 유치장에 같혀있는 NPC 들
            return Event_01()
        if not quest_user_detected(boxIds=[701], questIds=[10002789], questStates=[1]):
            return Event_02()


class Event_01(state.State):
    def on_enter(self):
        play_system_sound_in_box(sound='System_Space_PopUp_01')
        show_guide_summary(entityId=110, textId=40010) # 적을 모두 처치하세요
        set_mesh(triggerIds=[1001,1002], visible=False, arg3=0, arg4=0, arg5=0)
        set_mesh(triggerIds=[1003,1004], visible=True, arg3=0, arg4=0, arg5=0)
        create_monster(spawnIds=[101,102,103], arg2=False)

    def on_tick(self) -> state.State:
        if monster_dead(boxIds=[101,102,103]):
            return Event_03()

    def on_exit(self):
        hide_guide_summary(entityId=110)


class Event_02(state.State):
    def on_enter(self):
        set_mesh(triggerIds=[1001,1002], visible=True, arg3=0, arg4=0, arg5=0)
        set_mesh(triggerIds=[1003,1004], visible=False, arg3=0, arg4=0, arg5=0)
        create_monster(spawnIds=[111,112,113], arg2=False)


class Event_03(state.State):
    def on_enter(self):
        set_achievement(triggerId=701, type='trigger', achieve='Clearbadman') # Clearbadman
        set_mesh(triggerIds=[1001,1002], visible=True, arg3=0, arg4=0, arg5=0)
        set_mesh(triggerIds=[1003,1004], visible=False, arg3=0, arg4=0, arg5=0)


class End(state.State):
    pass


