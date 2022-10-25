""" trigger/02000400_bf/100_dualkill.xml """
import common


class 룸체크(common.Trigger):
    def on_tick(self) -> common.Trigger:
        if self.is_dungeon_room():
            return Wait(self.ctx)


class Wait(common.Trigger):
    def on_enter(self):
        self.set_user_value(key='CheckDualKill', value=0)

    def on_tick(self) -> common.Trigger:
        if self.user_value(key='CheckDualKill', value=1):
            return CheckDualKill(self.ctx)


class CheckDualKill(common.Trigger):
    def on_tick(self) -> common.Trigger:
        if self.monster_dead(boxIds=[900]):
            return LionBlueDead(self.ctx)
        if self.monster_dead(boxIds=[901]):
            return LionRedDead(self.ctx)


class LionBlueDead(common.Trigger):
    def on_tick(self) -> common.Trigger:
        if self.monster_dead(boxIds=[901]):
            self.set_achievement(triggerId=9900, type='trigger', achieve='ChangeLionDualKill')
            return Quit(self.ctx)
        if self.wait_tick(waitTick=2000):
            return Quit(self.ctx)


class LionRedDead(common.Trigger):
    def on_tick(self) -> common.Trigger:
        if self.monster_dead(boxIds=[900]):
            self.set_achievement(triggerId=9900, type='trigger', achieve='ChangeLionDualKill')
            return Quit(self.ctx)
        if self.wait_tick(waitTick=2000):
            return Quit(self.ctx)


class Quit(common.Trigger):
    pass


initial_state = 룸체크
