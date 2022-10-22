""" trigger/52000003_qd/katvan_01.xml """
from common import *
import state


class 시작대기중(state.State):
    def on_tick(self) -> state.State:
        if quest_user_detected(boxIds=[100], questIds=[50001743], questStates=[1]):
            return 카트반생성()


class 카트반생성(state.State):
    def on_enter(self):
        create_monster(spawnIds=[102]) # 카트반

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=1000):
            return 연출시작딜레이()


class 연출시작딜레이(state.State):
    def on_enter(self):
        set_cinematic_ui(type=1)
        set_cinematic_ui(type=3)
        select_camera(triggerId=101, enable=True)
        set_timer(timerId='1', seconds=1)
        set_scene_skip(state=Skip_1, arg2='nextState')

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=2000):
            return 대화시작()


class 대화시작(state.State):
    def on_enter(self):
        set_effect(triggerIds=[601], visible=True) # 2.33
        set_conversation(type=2, spawnId=11000064, script='$52000003_QD__KATVAN_01__0$', arg4=3)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=3000):
            return 카트반대사1()


class 카트반대사1(state.State):
    def on_enter(self):
        set_effect(triggerIds=[603], visible=True) # 2.33
        set_conversation(type=2, spawnId=11001024, script='$52000003_QD__KATVAN_01__1$', arg4=5)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=5000):
            return 카트반대사2()


class 카트반대사2(state.State):
    def on_enter(self):
        set_effect(triggerIds=[604], visible=True) # 2.33
        set_conversation(type=2, spawnId=11001024, script='$52000003_QD__KATVAN_01__2$', arg4=5)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=5000):
            return 레논대사1()

    def on_exit(self):
        destroy_monster(spawnIds=[102])


class 레논대사1(state.State):
    def on_enter(self):
        set_effect(triggerIds=[602], visible=True) # 2.33
        set_conversation(type=2, spawnId=11000064, script='$52000003_QD__KATVAN_01__3$', arg4=2)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=2000):
            return 카메라원위치()


class 카메라원위치(state.State):
    def on_enter(self):
        reset_camera(interpolationTime=0.5)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=1000):
            return 카메라원위치_1()


class 카메라원위치_1(state.State):
    def on_enter(self):
        set_scene_skip()

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=1000):
            return 끝()


class Skip_1(state.State):
    def on_enter(self):
        set_cinematic_ui(type=4)
        reset_camera(interpolationTime=0.5)
        destroy_monster(spawnIds=[102]) # 카트반

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=1000):
            return 끝()


class 끝(state.State):
    def on_enter(self):
        set_achievement(triggerId=100, type='trigger', achieve='Katvan')
        set_cinematic_ui(type=0)
        set_cinematic_ui(type=2)


