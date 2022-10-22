""" trigger/02000303_bf/main.xml """
from common import *
import state


class 대기(state.State):
    def on_enter(self):
        set_mesh(triggerIds=[3005], visible=False, arg3=0, arg4=0, arg5=0)
        set_interact_object(triggerIds=[13000008], state=2)
        set_effect(triggerIds=[601], visible=False)
        set_effect(triggerIds=[602], visible=False)
        set_interact_object(triggerIds=[10000585], state=0)
        set_interact_object(triggerIds=[10000575,10000576,10000577,10000578], state=1)
        create_monster(spawnIds=[2001], arg2=False)

    def on_tick(self) -> state.State:
        if user_detected(boxIds=[101]):
            return 연출시작딜레이()


class 연출시작딜레이(state.State):
    def on_tick(self) -> state.State:
        if wait_tick(waitTick=2000):
            return 연출시작()


class 연출시작(state.State):
    def on_enter(self):
        set_cinematic_ui(type=1)
        set_cinematic_ui(type=3)
        set_timer(timerId='5', seconds=5)
        set_conversation(type=2, spawnId=11000145, script='$02000303_BF__MAIN__0$', arg4=4)
        set_skip(state=연출종료)

    def on_tick(self) -> state.State:
        if time_expired(timerId='5'):
            return 연출종료()


class 연출종료(state.State):
    def on_enter(self):
        set_cinematic_ui(type=0)
        set_cinematic_ui(type=2)
        create_monster(spawnIds=[1001,1002,1003,1004,1005,1006,1007], arg2=False)
        show_guide_summary(entityId=20003031, textId=20003031, duration=5000)
        play_system_sound_in_box(sound='System_ShowGuideSummary_01')

    def on_tick(self) -> state.State:
        if object_interacted(interactIds=[10000575,10000576,10000577,10000578], arg2=0):
            return 또다른연출시작()


class 또다른연출시작(state.State):
    def on_enter(self):
        set_cinematic_ui(type=1)
        set_cinematic_ui(type=3)
        select_camera(triggerId=301, enable=True)
        set_skip(state=또다른연출종료)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=1500):
            return 연출이펙트()


class 연출이펙트(state.State):
    def on_enter(self):
        set_mesh(triggerIds=[3005], visible=True, arg3=0, arg4=0, arg5=2)
        set_effect(triggerIds=[602], visible=True)
        set_skip(state=또다른연출종료)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=2500):
            return 카메라이동2()


class 카메라이동2(state.State):
    def on_enter(self):
        select_camera(triggerId=302, enable=True)
        set_skip(state=또다른연출종료)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=2500):
            return NPC대사()


class NPC대사(state.State):
    def on_enter(self):
        move_npc(spawnId=2001, patrolName='MS2PatrolData_2001_A')
        set_conversation(type=2, spawnId=11000145, script='$02000303_BF__MAIN__1$', arg4=4)
        set_skip(state=또다른연출종료)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=4000):
            return 또다른연출종료()


class 또다른연출종료(state.State):
    def on_enter(self):
        destroy_monster(spawnIds=[2001])
        select_camera(triggerId=302, enable=False)
        set_mesh(triggerIds=[3005], visible=True, arg3=0, arg4=0, arg5=0)
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

    def on_tick(self) -> state.State:
        if object_interacted(interactIds=[10000585], arg2=0):
            hide_guide_summary(entityId=20002999)
            return 이동()


class 이동(state.State):
    def on_enter(self):
        set_effect(triggerIds=[601], visible=True)
        set_timer(timerId='4', seconds=4)
        show_count_ui(text='$02000303_BF__MAIN__3$', stage=1, count=3)

    def on_tick(self) -> state.State:
        if time_expired(timerId='4'):
            move_user(mapId=2000299, portalId=2, boxId=101)
            return 이동대기()


class 종료(state.State):
    pass


