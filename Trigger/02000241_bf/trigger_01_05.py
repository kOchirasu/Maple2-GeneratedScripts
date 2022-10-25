""" trigger/02000241_bf/trigger_01_05.xml """
import common


class 대기(common.Trigger):
    def on_enter(self):
        self.set_mesh(triggerIds=[304], visible=True, arg3=0, delay=0, scale=0)
        self.set_mesh(triggerIds=[701,702], visible=True)
        self.set_actor(triggerId=501, visible=True, initialSequence='Closed')
        self.set_actor(triggerId=502, visible=True, initialSequence='Closed')
        self.set_actor(triggerId=503, visible=True, initialSequence='Closed')
        self.set_actor(triggerId=504, visible=True, initialSequence='Closed')
        self.set_actor(triggerId=505, visible=True, initialSequence='Closed')
        self.set_actor(triggerId=506, visible=True, initialSequence='Closed')
        self.destroy_monster(spawnIds=[601,602,603,604,605,606])

    def on_tick(self) -> common.Trigger:
        if self.user_detected(boxIds=[404]):
            return 버튼눌림(self.ctx)


class 버튼눌림(common.Trigger):
    def on_enter(self):
        self.set_mesh(triggerIds=[304], visible=False, arg3=0, delay=0, scale=0)
        self.set_actor(triggerId=505, visible=True, initialSequence='Opened')
        self.set_actor(triggerId=506, visible=True, initialSequence='Opened')
        self.create_monster(spawnIds=[605,606], animationEffect=False)
        self.move_npc(spawnId=605, patrolName='MS2PatrolData_605')
        self.move_npc(spawnId=606, patrolName='MS2PatrolData_606')


initial_state = 대기
