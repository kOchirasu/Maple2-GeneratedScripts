""" trigger/02000213_bf/scene01.xml """
from common import *
import state


class 시작대기중(state.State):
    def on_enter(self):
        create_monster(spawnIds=[201])
        set_effect(triggerIds=[401], visible=False)
        set_effect(triggerIds=[601], visible=False) # 벨라 음성
        set_effect(triggerIds=[602], visible=False) # 벨라 음성
        set_effect(triggerIds=[603], visible=False) # 벨라 음성
        set_effect(triggerIds=[604], visible=False) # 벨라 음성
        set_effect(triggerIds=[605], visible=False) # 벨라 음성
        set_effect(triggerIds=[606], visible=False) # 레논 음성
        set_effect(triggerIds=[607], visible=False) # 알론 음성
        set_effect(triggerIds=[608], visible=False) # 알론 음성
        set_effect(triggerIds=[609], visible=False) # 알론 음성

    def on_tick(self) -> state.State:
        if monster_dead(boxIds=[201]):
            return 연출시작()


class 연출시작(state.State):
    def on_enter(self):
        set_cinematic_ui(type=1)
        set_cinematic_ui(type=3)
        select_camera(triggerId=301, enable=True)
        set_timer(timerId='1', seconds=1)

    def on_tick(self) -> state.State:
        if time_expired(timerId='1'):
            return 데보라크대사()


class 데보라크대사(state.State):
    def on_enter(self):
        set_timer(timerId='1', seconds=2)
        set_conversation(type=2, spawnId=23000007, script='$02000213_BF__SCENE01__0$', arg4=2)

    def on_tick(self) -> state.State:
        if time_expired(timerId='1'):
            return 레논등장()


class 레논등장(state.State):
    def on_enter(self):
        create_monster(spawnIds=[203])
        set_timer(timerId='1', seconds=2)

    def on_tick(self) -> state.State:
        if time_expired(timerId='1'):
            return 레논대사1()


class 레논대사1(state.State):
    def on_enter(self):
        set_timer(timerId='1', seconds=2)
        set_effect(triggerIds=[606], visible=True) # 2.33
        set_conversation(type=2, spawnId=11000064, script='$02000213_BF__SCENE01__1$', arg4=2)

    def on_tick(self) -> state.State:
        if time_expired(timerId='1'):
            return 벨라등장()


class 벨라등장(state.State):
    def on_enter(self):
        create_monster(spawnIds=[202])
        set_effect(triggerIds=[401], visible=True)
        set_timer(timerId='1', seconds=2)

    def on_tick(self) -> state.State:
        if time_expired(timerId='1'):
            return 벨라대사1()


class 벨라대사1(state.State):
    def on_enter(self):
        set_effect(triggerIds=[401], visible=False)
        set_timer(timerId='1', seconds=4)
        set_effect(triggerIds=[601], visible=True) # 3.40
        set_conversation(type=2, spawnId=11000057, script='$02000213_BF__SCENE01__2$', arg4=4)

    def on_tick(self) -> state.State:
        if time_expired(timerId='1'):
            return 벨라대사2()


class 벨라대사2(state.State):
    def on_enter(self):
        set_timer(timerId='1', seconds=3)
        set_effect(triggerIds=[602], visible=True) # 2.54
        set_conversation(type=2, spawnId=11000057, script='$02000213_BF__SCENE01__3$', arg4=3)

    def on_tick(self) -> state.State:
        if time_expired(timerId='1'):
            return 알론등장()


class 알론등장(state.State):
    def on_enter(self):
        create_monster(spawnIds=[204])
        set_timer(timerId='1', seconds=1)

    def on_tick(self) -> state.State:
        if time_expired(timerId='1'):
            return 알론대사1()


class 알론대사1(state.State):
    def on_enter(self):
        set_timer(timerId='1', seconds=4)
        set_effect(triggerIds=[607], visible=True) # 3.68
        set_conversation(type=2, spawnId=11000076, script='$02000213_BF__SCENE01__4$', arg4=4)

    def on_tick(self) -> state.State:
        if time_expired(timerId='1'):
            return 벨라대사3()


class 벨라대사3(state.State):
    def on_enter(self):
        set_timer(timerId='1', seconds=4)
        set_effect(triggerIds=[603], visible=True) # 4.10
        set_conversation(type=2, spawnId=11000057, script='$02000213_BF__SCENE01__5$', arg4=4)

    def on_tick(self) -> state.State:
        if time_expired(timerId='1'):
            return 벨라대사4()


class 벨라대사4(state.State):
    def on_enter(self):
        set_timer(timerId='1', seconds=4)
        set_effect(triggerIds=[604], visible=True) # 3.38
        set_conversation(type=2, spawnId=11000057, script='$02000213_BF__SCENE01__6$', arg4=4)

    def on_tick(self) -> state.State:
        if time_expired(timerId='1'):
            return 벨라대사5()


class 벨라대사5(state.State):
    def on_enter(self):
        set_timer(timerId='1', seconds=2)
        set_effect(triggerIds=[605], visible=True) # 2.10
        set_conversation(type=2, spawnId=11000057, script='$02000213_BF__SCENE01__7$', arg4=2)

    def on_tick(self) -> state.State:
        if time_expired(timerId='1'):
            return 벨라사라짐이펙트()


class 벨라사라짐이펙트(state.State):
    def on_enter(self):
        set_timer(timerId='1', seconds=1)
        set_effect(triggerIds=[407], visible=True)

    def on_tick(self) -> state.State:
        if time_expired(timerId='1'):
            return 벨라사라짐()


class 벨라사라짐(state.State):
    def on_enter(self):
        set_timer(timerId='1', seconds=1)
        set_cinematic_ui(type=0)
        set_cinematic_ui(type=2)
        select_camera_path(pathIds=[302], returnView=True)
        destroy_monster(spawnIds=[202])
        destroy_monster(spawnIds=[203])
        destroy_monster(spawnIds=[204])
        create_monster(spawnIds=[205])

    def on_tick(self) -> state.State:
        if time_expired(timerId='1'):
            return 알론대사2()


class 알론대사2(state.State):
    def on_enter(self):
        set_timer(timerId='1', seconds=4)
        set_effect(triggerIds=[608], visible=True) # 3.27
        set_conversation(type=1, spawnId=205, script='$02000213_BF__SCENE01__8$', arg4=4)

    def on_tick(self) -> state.State:
        if time_expired(timerId='1'):
            return 알론대사3()


class 알론대사3(state.State):
    def on_enter(self):
        set_timer(timerId='1', seconds=4)
        set_effect(triggerIds=[609], visible=True) # 3.33
        set_conversation(type=1, spawnId=205, script='$02000213_BF__SCENE01__9$', arg4=4)

    def on_tick(self) -> state.State:
        if time_expired(timerId='1'):
            return 연출끝()


class 연출끝(state.State):
    def on_enter(self):
        select_camera(triggerId=301, enable=False)
        set_timer(timerId='1', seconds=2)

    def on_tick(self) -> state.State:
        if time_expired(timerId='1'):
            return 끝()


class 끝(state.State):
    pass


