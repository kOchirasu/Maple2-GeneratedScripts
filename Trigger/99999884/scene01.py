""" trigger/99999884/scene01.xml """
from common import *
import state


class 시작대기중(state.State):
    def on_enter(self):
        set_effect(triggerIds=[401], visible=False)
        set_effect(triggerIds=[402], visible=False)
        set_effect(triggerIds=[403], visible=False)
        set_effect(triggerIds=[404], visible=False)
        set_actor(triggerId=405, visible=False)
        set_effect(triggerIds=[406], visible=False)

    def on_tick(self) -> state.State:
        if user_detected(boxIds=[199]):
            return 연출시작()


class 연출시작(state.State):
    def on_enter(self):
        set_cinematic_ui(type=1)
        set_cinematic_ui(type=3)
        select_camera(triggerId=301, enable=True)
        set_timer(timerId='1', seconds=1)

    def on_tick(self) -> state.State:
        if time_expired(timerId='1'):
            return 벨라등장()


class 벨라등장(state.State):
    def on_enter(self):
        create_monster(spawnIds=[202])
        set_effect(triggerIds=[401], visible=True)
        set_timer(timerId='1', seconds=4)

    def on_tick(self) -> state.State:
        if time_expired(timerId='1'):
            return 벨라대사1()


class 벨라대사1(state.State):
    def on_enter(self):
        set_effect(triggerIds=[401], visible=False)
        set_timer(timerId='1', seconds=2)
        set_conversation(type=2, spawnId=11000057, script='$99999884__SCENE01__0$', arg4=2)

    def on_tick(self) -> state.State:
        if time_expired(timerId='1'):
            return 벨라대사2()


class 벨라대사2(state.State):
    def on_enter(self):
        set_timer(timerId='1', seconds=2)
        set_conversation(type=1, spawnId=202, script='$99999884__SCENE01__1$', arg4=2)

    def on_tick(self) -> state.State:
        if time_expired(timerId='1'):
            return 프레이와오스칼등장()


class 프레이와오스칼등장(state.State):
    def on_enter(self):
        create_monster(spawnIds=[203])
        create_monster(spawnIds=[204])
        set_effect(triggerIds=[402], visible=True)
        set_timer(timerId='1', seconds=1)

    def on_tick(self) -> state.State:
        if time_expired(timerId='1'):
            return 프레이대사1()


class 프레이대사1(state.State):
    def on_enter(self):
        set_timer(timerId='1', seconds=2)
        set_conversation(type=2, spawnId=11000119, script='$99999884__SCENE01__2$', arg4=2)

    def on_tick(self) -> state.State:
        if time_expired(timerId='1'):
            return 벨라대사3()


class 벨라대사3(state.State):
    def on_enter(self):
        set_timer(timerId='1', seconds=2)
        set_effect(triggerIds=[402], visible=False)
        move_npc(spawnId=202, patrolName='202_MS2PatrolData_Bella_TurnToFrey')
        set_conversation(type=1, spawnId=202, script='$99999884__SCENE01__3$', arg4=2)

    def on_tick(self) -> state.State:
        if time_expired(timerId='1'):
            return 벨라대사4()


class 벨라대사4(state.State):
    def on_enter(self):
        set_timer(timerId='1', seconds=1)
        move_npc(spawnId=202, patrolName='202_MS2PatrolData_Bella_TurnToDevorak')
        set_conversation(type=1, spawnId=202, script='$99999884__SCENE01__4$', arg4=2)

    def on_tick(self) -> state.State:
        if time_expired(timerId='1'):
            return 이펙트지연()


class 이펙트지연(state.State):
    def on_enter(self):
        set_timer(timerId='1', seconds=1)
        set_effect(triggerIds=[402], visible=True)

    def on_tick(self) -> state.State:
        if time_expired(timerId='1'):
            return 프레이대사2()


class 프레이대사2(state.State):
    def on_enter(self):
        set_timer(timerId='1', seconds=2)
        move_npc(spawnId=203, patrolName='203_MS2PatrolData_Frey_MoveToBella')
        set_conversation(type=1, spawnId=203, script='$99999884__SCENE01__5$', arg4=2)

    def on_tick(self) -> state.State:
        if time_expired(timerId='1'):
            return 벨라대사5()


class 벨라대사5(state.State):
    def on_enter(self):
        set_timer(timerId='1', seconds=1)
        set_effect(triggerIds=[402], visible=False)
        set_effect(triggerIds=[403], visible=True)
        move_npc(spawnId=202, patrolName='202_MS2PatrolData_Bella_TurnToFrey')
        set_conversation(type=1, spawnId=202, script='$99999884__SCENE01__6$', arg4=2)

    def on_tick(self) -> state.State:
        if time_expired(timerId='1'):
            return 프레이피격()


class 프레이피격(state.State):
    def on_enter(self):
        set_timer(timerId='1', seconds=1)
        move_npc(spawnId=203, patrolName='203_MS2PatrolData_Frey_HitByBella')

    def on_tick(self) -> state.State:
        if time_expired(timerId='1'):
            return 오스칼대사1()


class 오스칼대사1(state.State):
    def on_enter(self):
        set_timer(timerId='1', seconds=2)
        destroy_monster(spawnIds=[203])
        set_effect(triggerIds=[403], visible=False)
        set_effect(triggerIds=[406], visible=True)
        set_actor(triggerId=405, visible=True, initialSequence='Down_Idle_A')
        move_npc(spawnId=204, patrolName='204_MS2PatrolData_Oskhal_MoveToFrey')
        set_conversation(type=2, spawnId=11000015, script='$99999884__SCENE01__7$', arg4=2)

    def on_tick(self) -> state.State:
        if time_expired(timerId='1'):
            return 오스칼대사2()


class 오스칼대사2(state.State):
    def on_enter(self):
        set_timer(timerId='1', seconds=1)
        set_conversation(type=1, spawnId=204, script='$99999884__SCENE01__8$', arg4=2)

    def on_tick(self) -> state.State:
        if time_expired(timerId='1'):
            return 오스칼돌격()


class 오스칼돌격(state.State):
    def on_enter(self):
        set_timer(timerId='1', seconds=1)
        move_npc(spawnId=204, patrolName='204_MS2PatrolData_Oskhal_MoveToBella')

    def on_tick(self) -> state.State:
        if time_expired(timerId='1'):
            return 연출끝()


class 연출끝(state.State):
    def on_enter(self):
        set_cinematic_ui(type=0)
        set_cinematic_ui(type=2)
        select_camera_path(pathIds=[302], returnView=True)
        set_timer(timerId='1', seconds=1)

    def on_tick(self) -> state.State:
        if time_expired(timerId='1'):
            return 끝()


class 끝(state.State):
    pass


