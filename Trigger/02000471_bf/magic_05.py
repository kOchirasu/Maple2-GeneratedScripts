""" trigger/02000471_bf/magic_05.xml """
import common


class idle(common.Trigger):
    def on_enter(self):
        self.set_user_value(triggerId=2040315, key='10002023clear', value=0)
        self.set_user_value(triggerId=2040320, key='10002023clear', value=0)
        self.set_user_value(triggerId=2040322, key='10002023clear', value=0)

    def on_tick(self) -> common.Trigger:
        if self.object_interacted(interactIds=[10002023], stateValue=0):
            return Ready(self.ctx)


class Ready(common.Trigger):
    def on_enter(self):
        self.set_effect(triggerIds=[7005], visible=False)
        self.set_mesh(triggerIds=[1105], visible=False, arg3=0, delay=200, scale=15)
        self.set_mesh(triggerIds=[1205], visible=True, arg3=0, delay=200, scale=15)
        self.create_monster(spawnIds=[205], animationEffect=False)
        self.add_buff(boxIds=[205], skillId=70002041, level=1, isPlayer=True, isSkillSet=False)

    def on_tick(self) -> common.Trigger:
        if self.monster_dead(boxIds=[205]):
            return Event_05(self.ctx)


class Event_05(common.Trigger):
    def on_enter(self):
        self.set_user_value(triggerId=2040315, key='10002023clear', value=1)
        self.set_user_value(triggerId=2040320, key='10002023clear', value=1)
        self.set_user_value(triggerId=2040322, key='10002023clear', value=1)
        self.set_achievement(triggerId=715, type='trigger', achieve='Hauntedmansion')
        self.create_monster(spawnIds=[145,146,147], animationEffect=False)

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=1000):
            return Event_05_b(self.ctx)


class Event_05_b(common.Trigger):
    def on_enter(self):
        self.move_npc(spawnId=147, patrolName='MS2PatrolData_2136')
        self.set_conversation(type=1, spawnId=147, script='$02000471_BF__MAGIC_05__0$', arg4=2, arg5=2)
        self.set_conversation(type=1, spawnId=145, script='$02000471_BF__MAGIC_05__1$', arg4=3, arg5=4)
        self.set_conversation(type=1, spawnId=146, script='$02000471_BF__MAGIC_05__1$', arg4=3, arg5=5)
        self.set_conversation(type=1, spawnId=147, script='$02000471_BF__MAGIC_05__3$', arg4=3, arg5=6)

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=2000):
            return Event_05_c(self.ctx)


class Event_05_c(common.Trigger):
    def on_enter(self):
        self.create_monster(spawnIds=[148], animationEffect=False)

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=6000):
            return Event_05_d(self.ctx)


class Event_05_d(common.Trigger):
    def on_enter(self):
        self.move_npc(spawnId=148, patrolName='MS2PatrolData_2137')

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=3000):
            return Event_05_e(self.ctx)


class Event_05_e(common.Trigger):
    def on_enter(self):
        self.destroy_monster(spawnIds=[145,146,147])

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=3000):
            return Event_05_f(self.ctx)


class Event_05_f(common.Trigger):
    def on_enter(self):
        self.destroy_monster(spawnIds=[148])


initial_state = idle
