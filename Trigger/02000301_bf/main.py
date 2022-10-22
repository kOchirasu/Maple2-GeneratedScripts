""" trigger/02000301_bf/main.xml """
from common import *
import state


class 대기(state.State):
    def on_enter(self):
        set_interact_object(triggerIds=[10000585], state=0)
        set_interact_object(triggerIds=[11000004], state=2)
        set_interact_object(triggerIds=[13000006], state=2)
        set_effect(triggerIds=[604], visible=False)
        create_monster(spawnIds=[1007,1008], arg2=False)
        create_monster(spawnIds=[2099], arg2=False)
        set_mesh(triggerIds=[4998,4999], visible=True, arg3=0, arg4=0, arg5=0)

    def on_tick(self) -> state.State:
        if user_detected(boxIds=[199]):
            return 연출시작딜레이()


class 연출시작딜레이(state.State):
    def on_enter(self):
        set_timer(timerId='2', seconds=2)

    def on_tick(self) -> state.State:
        if time_expired(timerId='2'):
            return 연출시작()


class 연출시작(state.State):
    def on_enter(self):
        set_cinematic_ui(type=1)
        set_cinematic_ui(type=3)
        select_camera(triggerId=301, enable=True)
        set_timer(timerId='3', seconds=3)
        set_skip(state=연출종료)

    def on_tick(self) -> state.State:
        if time_expired(timerId='3'):
            return 트리스탄01()


class 트리스탄01(state.State):
    def on_enter(self):
        set_timer(timerId='5', seconds=5)
        set_conversation(type=2, spawnId=11000252, script='$02000301_BF__MAIN__0$', arg4=4)
        set_skip(state=연출종료)

    def on_tick(self) -> state.State:
        if time_expired(timerId='5'):
            return 연출종료()


class 연출종료(state.State):
    def on_enter(self):
        select_camera_path(pathIds=[301], returnView=True)

    def on_tick(self) -> state.State:
        if true():
            return 몬스터전투()


class 몬스터전투(state.State):
    def on_enter(self):
        set_cinematic_ui(type=0)
        set_cinematic_ui(type=2)
        select_camera(triggerId=301, enable=False)

    def on_tick(self) -> state.State:
        if monster_in_combat(boxIds=[1007,1008]):
            return 골두스이동()


class 골두스이동(state.State):
    def on_enter(self):
        move_npc(spawnId=2099, patrolName='MS2PatrolData_2098')
        set_conversation(type=1, spawnId=2099, script='$02000301_BF__MAIN__1$', arg4=3)

    def on_tick(self) -> state.State:
        if monster_dead(boxIds=[1007,1008]):
            return 또다른연출시작()

    def on_exit(self):
        set_mesh(triggerIds=[4998,4999], visible=False, arg3=0, arg4=0, arg5=0)


class 또다른연출시작(state.State):
    def on_enter(self):
        set_cinematic_ui(type=1)
        set_cinematic_ui(type=3)
        set_timer(timerId='1', seconds=1)
        set_skip(state=또다른연출종료)

    def on_tick(self) -> state.State:
        if time_expired(timerId='1'):
            return 골두스마무리()


class 골두스마무리(state.State):
    def on_enter(self):
        set_timer(timerId='5', seconds=5)
        set_conversation(type=2, spawnId=11000252, script='$02000301_BF__MAIN__2$', arg4=4)
        set_skip(state=또다른연출종료)

    def on_tick(self) -> state.State:
        if time_expired(timerId='5'):
            return 또다른연출종료()


class 또다른연출종료(state.State):
    def on_enter(self):
        set_cinematic_ui(type=0)
        set_cinematic_ui(type=2)

    def on_tick(self) -> state.State:
        if true():
            return 이동대기()


class 이동대기(state.State):
    def on_enter(self):
        set_interact_object(triggerIds=[10000585], state=1)
        show_guide_summary(entityId=20002999, textId=20002999)
        play_system_sound_in_box(sound='System_ShowGuideSummary_01')
        move_npc(spawnId=2099, patrolName='MS2PatrolData_2099')

    def on_tick(self) -> state.State:
        if object_interacted(interactIds=[10000585], arg2=0):
            hide_guide_summary(entityId=20002999)
            return 이동()


class 이동(state.State):
    def on_enter(self):
        set_effect(triggerIds=[601], visible=True)
        set_timer(timerId='4', seconds=4)
        show_count_ui(text='$02000301_BF__MAIN__4$', stage=1, count=3)

    def on_tick(self) -> state.State:
        if time_expired(timerId='4'):
            move_user(mapId=2000299, portalId=2, boxId=199)
            return 이동대기()


class 종료(state.State):
    def on_enter(self):
        set_timer(timerId='1800000', seconds=1800000)

    def on_tick(self) -> state.State:
        if time_expired(timerId='1800000'):
            return None # Missing State: 종료2


