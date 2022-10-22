""" trigger/52010009_qd/main.xml """
from common import *
import state


class idle(state.State):
    def on_enter(self):
        set_interact_object(triggerIds=[10000866], state=0) # 컨테이너를 반응 가능한 상태로 변경
        set_interact_object(triggerIds=[10000880], state=0) # 컨테이너를 반응 가능한 상태로 변경
        set_interact_object(triggerIds=[10000915], state=0) # 컨테이너를 반응 가능한 상태로 변경

    def on_tick(self) -> state.State:
        if quest_user_detected(boxIds=[701], questIds=[20002091], questStates=[1]):
            return Event_01_Idle()


class Event_01_Idle(state.State):
    def on_enter(self):
        set_timer(timerId='1', seconds=1)

    def on_tick(self) -> state.State:
        if time_expired(timerId='1'):
            return Event_01()


class Event_01(state.State):
    def on_enter(self):
        play_system_sound_in_box(sound='System_Space_PopUp_01')
        show_guide_summary(entityId=110, textId=40010) # 적을 모두 처치하세요
        create_monster(spawnIds=[101], arg2=False)

    def on_tick(self) -> state.State:
        if monster_dead(boxIds=[101]):
            return Event_02()

    def on_exit(self):
        hide_guide_summary(entityId=110)
        set_interact_object(triggerIds=[10000866], state=1) # 컨테이너를 반응 가능한 상태로 변경


class Event_02(state.State):
    def on_enter(self):
        play_system_sound_in_box(sound='System_Space_PopUp_01')
        show_guide_summary(entityId=111, textId=25201901) # 수리공이 숨어있는 컨테이너를 찾으세요.

    def on_tick(self) -> state.State:
        if object_interacted(interactIds=[10000866], arg2=0):
            return Event_03()

    def on_exit(self):
        hide_guide_summary(entityId=111)
        create_monster(spawnIds=[111], arg2=False) # 그 안에 숨어있던 수리공 NPC들이 리젠
        set_conversation(type=1, spawnId=111, script='$52010009_QD__MAIN__0$', arg4=3, arg5=1)
        move_npc(spawnId=111, patrolName='MS2PatrolData0_1001')


class Event_03(state.State):
    def on_enter(self):
        play_system_sound_in_box(sound='System_Space_PopUp_01')
        show_guide_summary(entityId=110, textId=40010) # 적을 모두 처치하세요
        create_monster(spawnIds=[102], arg2=False)

    def on_tick(self) -> state.State:
        if monster_dead(boxIds=[102]):
            return Event_04()

    def on_exit(self):
        hide_guide_summary(entityId=110)
        set_interact_object(triggerIds=[10000880], state=1) # 컨테이너를 반응 가능한 상태로 변경


class Event_04(state.State):
    def on_enter(self):
        play_system_sound_in_box(sound='System_Space_PopUp_01')
        show_guide_summary(entityId=111, textId=25201901) # 수리공이 숨어있는 컨테이너를 찾으세요.

    def on_tick(self) -> state.State:
        if object_interacted(interactIds=[10000880], arg2=0):
            return Event_05()

    def on_exit(self):
        hide_guide_summary(entityId=111)
        create_monster(spawnIds=[112], arg2=False) # 그 안에 숨어있던 수리공 NPC들이 리젠
        set_conversation(type=1, spawnId=112, script='$52010009_QD__MAIN__1$', arg4=3, arg5=1)
        move_npc(spawnId=112, patrolName='MS2PatrolData0_1001')


class Event_05(state.State):
    def on_enter(self):
        play_system_sound_in_box(sound='System_Space_PopUp_01')
        show_guide_summary(entityId=110, textId=40010) # 적을 모두 처치하세요
        create_monster(spawnIds=[103], arg2=False)

    def on_tick(self) -> state.State:
        if monster_dead(boxIds=[103]):
            return Event_06()

    def on_exit(self):
        hide_guide_summary(entityId=110)
        set_interact_object(triggerIds=[10000915], state=1) # 컨테이너를 반응 가능한 상태로 변경


class Event_06(state.State):
    def on_enter(self):
        play_system_sound_in_box(sound='System_Space_PopUp_01')
        show_guide_summary(entityId=111, textId=25201901) # 수리공이 숨어있는 컨테이너를 찾으세요.

    def on_tick(self) -> state.State:
        if object_interacted(interactIds=[10000915], arg2=0):
            return End()

    def on_exit(self):
        hide_guide_summary(entityId=111)
        create_monster(spawnIds=[113], arg2=False) # 그 안에 숨어있던 수리공 NPC들이 리젠
        set_conversation(type=1, spawnId=113, script='$52010009_QD__MAIN__2$', arg4=3, arg5=1)
        move_npc(spawnId=113, patrolName='MS2PatrolData0_1001')


class End(state.State):
    def on_enter(self):
        set_achievement(triggerId=701, type='trigger', achieve='findrepairman') # findrepairman


