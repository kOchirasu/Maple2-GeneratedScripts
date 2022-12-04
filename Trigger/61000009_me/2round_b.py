""" trigger/61000009_me/2round_b.xml """
import trigger_api


class idle(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.user_value(key='2Round_B', value=1):
            return Spawn_Start_Ready(self.ctx)


class Spawn_Start_Ready(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=1000):
            return Spawn_Start(self.ctx)


class Spawn_Start(trigger_api.Trigger):
    def on_enter(self):
        self.set_effect(triggerIds=[7103], visible=True)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=4000):
            return Round_Spawn_B_01_Ready2(self.ctx)


class Round_Spawn_B_01_Ready2(trigger_api.Trigger):
    def on_enter(self):
        self.set_effect(triggerIds=[7203], visible=True)
        self.set_effect(triggerIds=[7003], visible=False)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=2300):
            return Round_Spawn_B_01_2(self.ctx)


class Round_Spawn_B_01_2(trigger_api.Trigger):
    def on_enter(self):
        self.create_monster(spawnIds=[103], animationEffect=False) # 캡틴 모크 등장

    def on_tick(self) -> trigger_api.Trigger:
        if self.monster_dead(boxIds=[103]):
            return Round_Spawn_B_End2(self.ctx)


class Round_Spawn_B_End2(trigger_api.Trigger):
    def on_enter(self):
        self.move_npc(spawnId=110, patrolName='MS2PatrolData_2007')
        self.set_conversation(type=1, spawnId=110, script='$02000374_BF__2ROUND_B__0$', arg4=2, arg5=1)
        self.set_user_value(triggerId=2037401, key='2Round_B', value=1) # 캡틴 모크  소환 장치


initial_state = idle
