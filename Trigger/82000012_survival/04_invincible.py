""" trigger/82000012_survival/04_invincible.xml """
import trigger_api


class Wait(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.user_detected(boxIds=[9000]):
            return MakeInvincible(self.ctx)


class MakeInvincible(trigger_api.Trigger):
    def on_enter(self):
        self.add_buff(boxIds=[9000], skillId=71000049, level=1, isPlayer=False, isSkillSet=False) # 대기공간 무적

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=500):
            return MakeInvincible(self.ctx)
        if self.user_value(key='InvincibleOff', value=1):
            return Quit(self.ctx)


class Quit(trigger_api.Trigger):
    pass


initial_state = Wait
