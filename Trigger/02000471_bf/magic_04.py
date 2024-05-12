""" trigger/02000471_bf/magic_04.xml """
import trigger_api


class idle(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_user_value(triggerId=2040315, key='10002022clear', value=0)
        self.set_user_value(triggerId=2040319, key='10002022clear', value=0)
        self.set_user_value(triggerId=2040322, key='10002022clear', value=0)

    def on_tick(self) -> trigger_api.Trigger:
        if self.object_interacted(interactIds=[10002022], stateValue=0):
            return Ready(self.ctx)


class Ready(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_effect(triggerIds=[7004], visible=False)
        self.set_mesh(triggerIds=[1104], visible=False, arg3=0, delay=200, scale=15)
        self.set_mesh(triggerIds=[1204], visible=True, arg3=0, delay=200, scale=15)
        self.create_monster(spawnIds=[204], animationEffect=False)
        self.add_buff(boxIds=[204], skillId=70002031, level=1, isPlayer=True, isSkillSet=False)

    def on_tick(self) -> trigger_api.Trigger:
        if self.monster_dead(boxIds=[204]):
            return Event_04(self.ctx)


class Event_04(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_user_value(triggerId=2040315, key='10002022clear', value=1)
        self.set_user_value(triggerId=2040319, key='10002022clear', value=1)
        self.set_user_value(triggerId=2040322, key='10002022clear', value=1)
        self.set_achievement(triggerId=714, type='trigger', achieve='Hauntedmansion')
        self.create_monster(spawnIds=[144], animationEffect=False)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=1000):
            return Event_04_b(self.ctx)


class Event_04_b(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_conversation(type=1, spawnId=144, script='$02000471_BF__MAGIC_04__0$', arg4=2, arg5=2)
        self.set_conversation(type=1, spawnId=144, script='$02000471_BF__MAGIC_04__1$', arg4=4, arg5=5)
        self.move_npc(spawnId=144, patrolName='MS2PatrolData_2134')

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=7000):
            return Event_04_c(self.ctx)


class Event_04_c(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_conversation(type=1, spawnId=144, script='$02000471_BF__MAGIC_04__2$', arg4=3, arg5=1)
        self.set_conversation(type=1, spawnId=144, script='$02000471_BF__MAGIC_04__3$', arg4=3, arg5=4)
        self.move_npc(spawnId=144, patrolName='MS2PatrolData_2135')

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=7000):
            return Event_04_d(self.ctx)


class Event_04_d(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.destroy_monster(spawnIds=[144])


initial_state = idle
