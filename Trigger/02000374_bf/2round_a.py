""" trigger/02000374_bf/2round_a.xml """
import common


class idle(common.Trigger):
    def on_tick(self) -> common.Trigger:
        if self.user_value(key='2Round_A', value=1):
            return Spawn_Start_Ready(self.ctx)


class Spawn_Start_Ready(common.Trigger):
    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=1000):
            return Spawn_Start(self.ctx)


class Spawn_Start(common.Trigger):
    def on_enter(self):
        self.set_effect(triggerIds=[7102], visible=True)

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=4000):
            return Round_Spawn_A_01_Ready2(self.ctx)


class Round_Spawn_A_01_Ready2(common.Trigger):
    def on_enter(self):
        self.set_effect(triggerIds=[7202], visible=True)
        self.set_effect(triggerIds=[7002], visible=False)

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=2300):
            return Round_Spawn_A_01_2(self.ctx)


class Round_Spawn_A_01_2(common.Trigger):
    def on_enter(self):
        self.create_monster(spawnIds=[102], animationEffect=False) # 파모칸 등장

    def on_tick(self) -> common.Trigger:
        if self.monster_dead(boxIds=[102]):
            return Round_Spawn_A_End2(self.ctx)


class Round_Spawn_A_End2(common.Trigger):
    def on_enter(self):
        self.move_npc(spawnId=110, patrolName='MS2PatrolData_2006')
        self.set_conversation(type=1, spawnId=110, script='$02000374_BF__2ROUND_A__0$', arg4=2, arg5=1)
        self.set_user_value(triggerId=2037401, key='2Round_A', value=1) # 파모칸 소환 장치


initial_state = idle
