""" trigger/02000086_bf/03_wave.xml """
import trigger_api


class 대기(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_interact_object(triggerIds=[10000159], state=1)
        self.set_effect(triggerIds=[301,302,303,304,305,306,307,308,309,310,311,312,313,314,315,316,317,318,319,320,321,322,323,324,325,326], visible=False)
        self.set_mesh(triggerIds=[201,202,203,204,205,206,207,208,209,210,211,212,213,214,215,216,217,218,219,220,221,222,223,224,225,226], visible=False)
        self.set_actor(triggerId=501, visible=True, initialSequence='Closed')
        self.set_actor(triggerId=502, visible=True, initialSequence='Closed')
        self.set_actor(triggerId=503, visible=True, initialSequence='Closed')
        self.set_actor(triggerId=504, visible=True, initialSequence='Closed')
        self.set_actor(triggerId=505, visible=True, initialSequence='Closed')
        self.set_actor(triggerId=506, visible=True, initialSequence='Closed')

    def on_tick(self) -> trigger_api.Trigger:
        if self.object_interacted(interactIds=[10000159], stateValue=0):
            return 딜레이1(self.ctx)


class 딜레이1(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_effect(triggerIds=[301,302,303,304,305,306,307,308,309,310,311,312,313,314,315,316,317,318,319,320,321,322,323,324,325,326], visible=True)
        self.set_mesh(triggerIds=[201,202,203,204,205,206,207,208,209,210,211,212,213,214,215,216,217,218,219,220,221,222,223,224,225,226], visible=True)
        self.set_timer(timerId='3', seconds=2)
        self.set_actor(triggerId=501, visible=True, initialSequence='Opened')
        self.set_actor(triggerId=502, visible=True, initialSequence='Opened')
        self.set_actor(triggerId=503, visible=True, initialSequence='Opened')
        self.set_actor(triggerId=504, visible=True, initialSequence='Opened')
        self.set_actor(triggerId=505, visible=True, initialSequence='Opened')
        self.set_actor(triggerId=506, visible=True, initialSequence='Opened')

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timerId='3'):
            return 웨이브1(self.ctx)


class 웨이브1(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_event_ui(type=1, arg2='$02000086_BF__03_WAVE__0$', arg3='3000', arg4='401')
        self.create_monster(spawnIds=[101,102,103,104,105,106], animationEffect=False)
        self.move_npc(spawnId=101, patrolName='MS2PatrolData_601')
        self.move_npc(spawnId=102, patrolName='MS2PatrolData_602')
        self.move_npc(spawnId=103, patrolName='MS2PatrolData_603')
        self.move_npc(spawnId=104, patrolName='MS2PatrolData_604')
        self.move_npc(spawnId=105, patrolName='MS2PatrolData_605')
        self.move_npc(spawnId=106, patrolName='MS2PatrolData_606')

    def on_tick(self) -> trigger_api.Trigger:
        if self.monster_dead(boxIds=[101,102,103,104,105,106]):
            return 대기(self.ctx)


class 딜레이2(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_timer(timerId='3', seconds=2)

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timerId='3'):
            return 웨이브2(self.ctx)


class 웨이브2(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.create_monster(spawnIds=[101,102,103,104,105,106], animationEffect=True)
        self.move_npc(spawnId=101, patrolName='MS2PatrolData_601')
        self.move_npc(spawnId=102, patrolName='MS2PatrolData_602')
        self.move_npc(spawnId=103, patrolName='MS2PatrolData_603')
        self.move_npc(spawnId=104, patrolName='MS2PatrolData_604')
        self.move_npc(spawnId=105, patrolName='MS2PatrolData_605')
        self.move_npc(spawnId=106, patrolName='MS2PatrolData_606')
        self.set_timer(timerId='3', seconds=120)

    def on_tick(self) -> trigger_api.Trigger:
        if self.monster_dead(boxIds=[101,102,103,104,105,106]):
            return 딜레이4(self.ctx)
        if self.time_expired(timerId='3'):
            return 대기(self.ctx)


class 딜레이3(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_timer(timerId='3', seconds=2)

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timerId='3'):
            return 웨이브3(self.ctx)


class 웨이브3(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_event_ui(type=1, arg2='$02000086_BF__03_WAVE__1$', arg3='3000', arg4='401')
        self.create_monster(spawnIds=[101,102,103,104,105,106], animationEffect=True)
        self.move_npc(spawnId=101, patrolName='MS2PatrolData_601')
        self.move_npc(spawnId=102, patrolName='MS2PatrolData_602')
        self.move_npc(spawnId=103, patrolName='MS2PatrolData_603')
        self.move_npc(spawnId=104, patrolName='MS2PatrolData_604')
        self.move_npc(spawnId=105, patrolName='MS2PatrolData_605')
        self.move_npc(spawnId=106, patrolName='MS2PatrolData_606')
        self.set_timer(timerId='3', seconds=120)

    def on_tick(self) -> trigger_api.Trigger:
        if self.monster_dead(boxIds=[101,102,103,104,105,106]):
            return 딜레이4(self.ctx)
        if self.time_expired(timerId='3'):
            return 대기(self.ctx)


class 딜레이4(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_timer(timerId='3', seconds=1)

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timerId='3'):
            return 딜레이5(self.ctx)


class 딜레이5(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_interact_object(triggerIds=[10000159], state=1)
        self.set_effect(triggerIds=[301,302,303,304,305,306,307,308,309,310,311,312,313,314,315,316,317,318,319,320,321,322,323,324,325,326], visible=False)
        self.set_mesh(triggerIds=[201,202,203,204,205,206,207,208,209,210,211,212,213,214,215,216,217,218,219,220,221,222,223,224,225,226], visible=False)
        self.set_actor(triggerId=501, visible=True, initialSequence='Closed')
        self.set_actor(triggerId=502, visible=True, initialSequence='Closed')
        self.set_actor(triggerId=503, visible=True, initialSequence='Closed')
        self.set_actor(triggerId=504, visible=True, initialSequence='Closed')
        self.set_actor(triggerId=505, visible=True, initialSequence='Closed')
        self.set_actor(triggerId=506, visible=True, initialSequence='Closed')
        self.set_timer(timerId='3', seconds=2)

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timerId='3'):
            return 딜레이6(self.ctx)


class 딜레이6(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_timer(timerId='3', seconds=2)

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timerId='3'):
            return 대기(self.ctx)


initial_state = 대기
