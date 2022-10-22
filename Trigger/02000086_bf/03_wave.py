""" trigger/02000086_bf/03_wave.xml """
from common import *
import state


class 대기(state.State):
    def on_enter(self):
        set_interact_object(triggerIds=[10000159], state=1)
        set_effect(triggerIds=[301,302,303,304,305,306,307,308,309,310,311,312,313,314,315,316,317,318,319,320,321,322,323,324,325,326], visible=False)
        set_mesh(triggerIds=[201,202,203,204,205,206,207,208,209,210,211,212,213,214,215,216,217,218,219,220,221,222,223,224,225,226], visible=False)
        set_actor(triggerId=501, visible=True, initialSequence='Closed')
        set_actor(triggerId=502, visible=True, initialSequence='Closed')
        set_actor(triggerId=503, visible=True, initialSequence='Closed')
        set_actor(triggerId=504, visible=True, initialSequence='Closed')
        set_actor(triggerId=505, visible=True, initialSequence='Closed')
        set_actor(triggerId=506, visible=True, initialSequence='Closed')

    def on_tick(self) -> state.State:
        if object_interacted(interactIds=[10000159], arg2=0):
            return 딜레이1()


class 딜레이1(state.State):
    def on_enter(self):
        set_effect(triggerIds=[301,302,303,304,305,306,307,308,309,310,311,312,313,314,315,316,317,318,319,320,321,322,323,324,325,326], visible=True)
        set_mesh(triggerIds=[201,202,203,204,205,206,207,208,209,210,211,212,213,214,215,216,217,218,219,220,221,222,223,224,225,226], visible=True)
        set_timer(timerId='3', seconds=2)
        set_actor(triggerId=501, visible=True, initialSequence='Opened')
        set_actor(triggerId=502, visible=True, initialSequence='Opened')
        set_actor(triggerId=503, visible=True, initialSequence='Opened')
        set_actor(triggerId=504, visible=True, initialSequence='Opened')
        set_actor(triggerId=505, visible=True, initialSequence='Opened')
        set_actor(triggerId=506, visible=True, initialSequence='Opened')

    def on_tick(self) -> state.State:
        if time_expired(timerId='3'):
            return 웨이브1()


class 웨이브1(state.State):
    def on_enter(self):
        set_event_ui(type=1, arg2='$02000086_BF__03_WAVE__0$', arg3='3000', arg4='401')
        create_monster(spawnIds=[101,102,103,104,105,106], arg2=False)
        move_npc(spawnId=101, patrolName='MS2PatrolData_601')
        move_npc(spawnId=102, patrolName='MS2PatrolData_602')
        move_npc(spawnId=103, patrolName='MS2PatrolData_603')
        move_npc(spawnId=104, patrolName='MS2PatrolData_604')
        move_npc(spawnId=105, patrolName='MS2PatrolData_605')
        move_npc(spawnId=106, patrolName='MS2PatrolData_606')

    def on_tick(self) -> state.State:
        if monster_dead(boxIds=[101,102,103,104,105,106]):
            return 대기()


class 딜레이2(state.State):
    def on_enter(self):
        set_timer(timerId='3', seconds=2)

    def on_tick(self) -> state.State:
        if time_expired(timerId='3'):
            return 웨이브2()


class 웨이브2(state.State):
    def on_enter(self):
        create_monster(spawnIds=[101,102,103,104,105,106], arg2=True)
        move_npc(spawnId=101, patrolName='MS2PatrolData_601')
        move_npc(spawnId=102, patrolName='MS2PatrolData_602')
        move_npc(spawnId=103, patrolName='MS2PatrolData_603')
        move_npc(spawnId=104, patrolName='MS2PatrolData_604')
        move_npc(spawnId=105, patrolName='MS2PatrolData_605')
        move_npc(spawnId=106, patrolName='MS2PatrolData_606')
        set_timer(timerId='3', seconds=120)

    def on_tick(self) -> state.State:
        if monster_dead(boxIds=[101,102,103,104,105,106]):
            return 딜레이4()
        if time_expired(timerId='3'):
            return 대기()


class 딜레이3(state.State):
    def on_enter(self):
        set_timer(timerId='3', seconds=2)

    def on_tick(self) -> state.State:
        if time_expired(timerId='3'):
            return 웨이브3()


class 웨이브3(state.State):
    def on_enter(self):
        set_event_ui(type=1, arg2='$02000086_BF__03_WAVE__1$', arg3='3000', arg4='401')
        create_monster(spawnIds=[101,102,103,104,105,106], arg2=True)
        move_npc(spawnId=101, patrolName='MS2PatrolData_601')
        move_npc(spawnId=102, patrolName='MS2PatrolData_602')
        move_npc(spawnId=103, patrolName='MS2PatrolData_603')
        move_npc(spawnId=104, patrolName='MS2PatrolData_604')
        move_npc(spawnId=105, patrolName='MS2PatrolData_605')
        move_npc(spawnId=106, patrolName='MS2PatrolData_606')
        set_timer(timerId='3', seconds=120)

    def on_tick(self) -> state.State:
        if monster_dead(boxIds=[101,102,103,104,105,106]):
            return 딜레이4()
        if time_expired(timerId='3'):
            return 대기()


class 딜레이4(state.State):
    def on_enter(self):
        set_timer(timerId='3', seconds=1)

    def on_tick(self) -> state.State:
        if time_expired(timerId='3'):
            return 딜레이5()


class 딜레이5(state.State):
    def on_enter(self):
        set_interact_object(triggerIds=[10000159], state=1)
        set_effect(triggerIds=[301,302,303,304,305,306,307,308,309,310,311,312,313,314,315,316,317,318,319,320,321,322,323,324,325,326], visible=False)
        set_mesh(triggerIds=[201,202,203,204,205,206,207,208,209,210,211,212,213,214,215,216,217,218,219,220,221,222,223,224,225,226], visible=False)
        set_actor(triggerId=501, visible=True, initialSequence='Closed')
        set_actor(triggerId=502, visible=True, initialSequence='Closed')
        set_actor(triggerId=503, visible=True, initialSequence='Closed')
        set_actor(triggerId=504, visible=True, initialSequence='Closed')
        set_actor(triggerId=505, visible=True, initialSequence='Closed')
        set_actor(triggerId=506, visible=True, initialSequence='Closed')
        set_timer(timerId='3', seconds=2)

    def on_tick(self) -> state.State:
        if time_expired(timerId='3'):
            return 딜레이6()


class 딜레이6(state.State):
    def on_enter(self):
        set_timer(timerId='3', seconds=2)

    def on_tick(self) -> state.State:
        if time_expired(timerId='3'):
            return 대기()


