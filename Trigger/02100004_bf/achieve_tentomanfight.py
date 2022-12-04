""" trigger/02100004_bf/achieve_tentomanfight.xml """
import trigger_api


class Wait(trigger_api.Trigger):
    def on_enter(self):
        self.set_user_value(key='LastRoundStart', value=0)
        self.set_user_value(key='LastRoundEnd', value=0)

    def on_tick(self) -> trigger_api.Trigger:
        if self.user_value(key='LastRoundStart', value=1):
            return MobCheck01(self.ctx)


class MobCheck01(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.npc_detected(boxId=102, spawnIds=[2000]):
            return MobCheck02(self.ctx)


class MobCheck02(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.all_of():
            return CheckSuccess(self.ctx)
        if self.user_value(key='LastRoundEnd', value=1):
            return Quit(self.ctx)


class CheckSuccess(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.monster_dead(boxIds=[2000]):
            return MemberCheck(self.ctx)
        if self.user_value(key='LastRoundEnd', value=1):
            return Quit(self.ctx)


class MemberCheck(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.count_users(boxId=102, boxId=10, operator='Equal'):
            return Achieve(self.ctx)
        if self.user_value(key='LastRoundEnd', value=1):
            return Quit(self.ctx)


class Achieve(trigger_api.Trigger):
    def on_enter(self):
        self.set_achievement(triggerId=102, type='trigger', achieve='TenToOneFight')

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=1000):
            return Quit(self.ctx)


class Quit(trigger_api.Trigger):
    pass


initial_state = Wait
