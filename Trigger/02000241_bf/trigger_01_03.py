""" trigger/02000241_bf/trigger_01_03.xml """
import trigger_api


class 대기(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_mesh(triggerIds=[302], visible=True, arg3=0, delay=0, scale=0)
        self.set_mesh(triggerIds=[701,702], visible=True)
        self.set_actor(triggerId=501, visible=True, initialSequence='Closed')
        self.set_actor(triggerId=502, visible=True, initialSequence='Closed')
        self.set_actor(triggerId=503, visible=True, initialSequence='Closed')
        self.set_actor(triggerId=504, visible=True, initialSequence='Closed')
        self.set_actor(triggerId=505, visible=True, initialSequence='Closed')
        self.set_actor(triggerId=506, visible=True, initialSequence='Closed')
        self.destroy_monster(spawnIds=[601,602,603,604,605,606])

    def on_tick(self) -> trigger_api.Trigger:
        if self.user_detected(boxIds=[402]):
            return 버튼눌림(self.ctx)


class 버튼눌림(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_mesh(triggerIds=[302], visible=False, arg3=0, delay=0, scale=0)
        self.set_actor(triggerId=503, visible=True, initialSequence='Opened')
        self.set_actor(triggerId=504, visible=True, initialSequence='Opened')
        self.create_monster(spawnIds=[603,604], animationEffect=False)
        self.move_npc(spawnId=603, patrolName='MS2PatrolData_603')
        self.move_npc(spawnId=604, patrolName='MS2PatrolData_604')


initial_state = 대기
