""" trigger/82000003_survival/04_invincible.xml """
import common


class Wait(common.Trigger):
    def on_tick(self) -> common.Trigger:
        if self.user_detected(boxIds=[9000]):
            return MakeInvincible(self.ctx)


class MakeInvincible(common.Trigger):
    def on_enter(self):
        self.add_buff(boxIds=[9000], skillId=71000049, level=1, isPlayer=False, isSkillSet=False) # 대기공간 무적

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=500):
            return MakeInvincible(self.ctx)
        if self.user_value(key='InvincibleOff', value=1):
            return Quit(self.ctx)


class Quit(common.Trigger):
    pass


initial_state = Wait
