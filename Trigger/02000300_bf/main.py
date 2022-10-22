""" trigger/02000300_bf/main.xml """
from common import *
import state


class 대기(state.State):
    def on_enter(self):
        set_interact_object(triggerIds=[10000585], state=0)
        set_effect(triggerIds=[601], visible=False)
        set_mesh(triggerIds=[3001,3002,3003,3004,3005], visible=False, arg3=0, arg4=0, arg5=0)
        create_monster(spawnIds=[1001,1002,1003,1004], arg2=False)
        create_monster(spawnIds=[1099], arg2=False)

    def on_tick(self) -> state.State:
        if user_detected(boxIds=[101]):
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
        set_conversation(type=2, spawnId=11000144, script='$02000300_BF__MAIN__0$', arg4=4)
        set_skip(state=연출종료)

    def on_tick(self) -> state.State:
        if time_expired(timerId='5'):
            return 연출종료()


class 연출종료(state.State):
    def on_enter(self):
        select_camera_path(pathIds=[301], returnView=True)

    def on_tick(self) -> state.State:
        if true():
            return 완료체크()


class 완료체크(state.State):
    def on_enter(self):
        set_cinematic_ui(type=0)
        set_cinematic_ui(type=2)
        select_camera(triggerId=301, enable=False)

    def on_tick(self) -> state.State:
        if monster_dead(boxIds=[1099]):
            return 또다른연출시작()


class 또다른연출시작(state.State):
    def on_enter(self):
        set_cinematic_ui(type=1)
        set_cinematic_ui(type=3)
        set_timer(timerId='1', seconds=1)
        set_skip(state=또다른연출종료)

    def on_tick(self) -> state.State:
        if time_expired(timerId='1'):
            return 트리스탄마무리()


class 트리스탄마무리(state.State):
    def on_enter(self):
        set_timer(timerId='5', seconds=5)
        set_conversation(type=2, spawnId=11000144, script='$02000300_BF__MAIN__1$', arg4=4)
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

    def on_tick(self) -> state.State:
        if object_interacted(interactIds=[10000585], arg2=0):
            hide_guide_summary(entityId=20002999)
            return 이동()


class 이동(state.State):
    def on_enter(self):
        set_effect(triggerIds=[601], visible=True)
        set_timer(timerId='4', seconds=4)
        show_count_ui(text='$02000300_BF__MAIN__3$', stage=1, count=3)

    def on_tick(self) -> state.State:
        if time_expired(timerId='4'):
            move_user(mapId=2000299, portalId=2, boxId=101)
            return 이동대기()


class 종료(state.State):
    def on_enter(self):
        set_timer(timerId='1800000', seconds=1800000)

    def on_tick(self) -> state.State:
        if time_expired(timerId='1800000'):
            return None # Missing State: 종료2


