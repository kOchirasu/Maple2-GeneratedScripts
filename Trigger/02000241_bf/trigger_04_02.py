""" trigger/02000241_bf/trigger_04_02.xml """
import trigger_api


class 대기(trigger_api.Trigger):
    def on_enter(self):
        self.set_mesh(triggerIds=[305], visible=True, arg3=0, delay=0, scale=0)
        self.set_mesh(triggerIds=[707,708], visible=True)
        self.set_mesh(triggerIds=[309,310,311,312,313,314,315,316,317,318,319,320,321,322,323,324], visible=False)
        self.set_actor(triggerId=507, visible=True, initialSequence='Closed')
        self.set_actor(triggerId=508, visible=True, initialSequence='Closed')
        self.set_actor(triggerId=509, visible=True, initialSequence='Closed')
        self.set_actor(triggerId=510, visible=True, initialSequence='Closed')
        self.set_actor(triggerId=511, visible=True, initialSequence='Closed')
        self.set_actor(triggerId=512, visible=True, initialSequence='Closed')
        self.destroy_monster(spawnIds=[607,608,609,610,611,612])

    def on_tick(self) -> trigger_api.Trigger:
        if self.user_detected(boxIds=[405]):
            return 버튼눌림(self.ctx)


class 버튼눌림(trigger_api.Trigger):
    def on_enter(self):
        self.set_mesh(triggerIds=[305], visible=False, arg3=0, delay=0, scale=0)
        self.set_actor(triggerId=507, visible=True, initialSequence='Opened')
        self.set_actor(triggerId=508, visible=True, initialSequence='Opened')
        self.set_mesh(triggerIds=[309,310,311,312,313,314,315,316,317,318,319,320,321,322,323,324], visible=True)
        self.create_monster(spawnIds=[607,608], animationEffect=False)
        self.move_npc(spawnId=607, patrolName='MS2PatrolData_607')
        self.move_npc(spawnId=608, patrolName='MS2PatrolData_608')


initial_state = 대기
