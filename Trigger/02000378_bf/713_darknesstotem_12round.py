""" trigger/02000378_bf/713_darknesstotem_12round.xml """
import common


class Wait(common.Trigger):
    def on_enter(self):
        self.set_mesh(triggerIds=[3900,3901,3902,3903,3904,3905,3906,3907,3908,3909,3910,3911,3912,3913], visible=False, arg3=0, delay=0, scale=0) # TotemGround
        self.set_user_value(key='TotemApp', value=0)

    def on_tick(self) -> common.Trigger:
        if self.user_value(key='TotemApp', value=1):
            return TotemApp01(self.ctx)


class TotemApp01(common.Trigger):
    def on_enter(self):
        self.destroy_monster(spawnIds=[2212]) # Regen_A로 돌아갔던 준타
        self.create_monster(spawnIds=[2313], animationEffect=False) # 날아라 준타
        self.set_mesh(triggerIds=[3900,3901,3902,3903,3904,3905,3906,3907,3908,3909,3910,3911,3912,3913], visible=True, arg3=0, delay=0, scale=5) # TotemGround
        self.create_monster(spawnIds=[926], animationEffect=False) # 암흑 토템

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=4000):
            return JuntaReady01(self.ctx)


class JuntaReady01(common.Trigger):
    def on_enter(self):
        self.set_conversation(type=1, spawnId=2313, script='$02000378_BF__713_DARKNESSTOTEM_12ROUND__0$', arg4=3, arg5=0) # 전투중인 준타

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=3000):
            return JuntaGoUp01(self.ctx)


class JuntaGoUp01(common.Trigger):
    def on_enter(self):
        self.move_npc(spawnId=2313, patrolName='MS2PatrolData_2313')

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=2000):
            return DestoryTotem01(self.ctx)


class DestoryTotem01(common.Trigger):
    def on_enter(self):
        self.create_monster(spawnIds=[2113], animationEffect=False) # 토템 옆에 준타

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=5000):
            return JuntaReturn01(self.ctx)


class JuntaReturn01(common.Trigger):
    def on_enter(self):
        self.destroy_monster(spawnIds=[926]) # 암흑 토템
        self.destroy_monster(spawnIds=[2313]) # 날아라 준타
        self.destroy_monster(spawnIds=[2113]) # 토템 옆에 준타

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=1000):
            return JuntaReturn02(self.ctx)


class JuntaReturn02(common.Trigger):
    def on_enter(self):
        self.create_monster(spawnIds=[2213], animationEffect=False) # Regen_A 준타

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=2000):
            return Quit(self.ctx)


class Quit(common.Trigger):
    def on_enter(self):
        self.set_mesh(triggerIds=[3900,3901,3902,3903,3904,3905,3906,3907,3908,3909,3910,3911,3912,3913], visible=False, arg3=0, delay=0, scale=5) # TotemGround


initial_state = Wait
