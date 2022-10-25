""" trigger/02000471_bf/respawn.xml """
import common


class idle(common.Trigger):
    def on_tick(self) -> common.Trigger:
        if self.user_value(key='respawn', value=1):
            return respawn_timer1(self.ctx)


class respawn_timer1(common.Trigger):
    def on_enter(self):
        self.set_timer(timerId='respawntimer1', seconds=120, startDelay=1, interval=0, vOffset=0)

    def on_tick(self) -> common.Trigger:
        if self.user_value(key='respawn', value=2):
            return end(self.ctx)
        if self.time_expired(timerId='respawntimer1'):
            return respawn1(self.ctx)


class respawn1(common.Trigger):
    def on_enter(self):
        self.reset_timer(timerId='respawntimer1')
        self.create_monster(spawnIds=[301,302,303,304,305,306], animationEffect=False)

    def on_tick(self) -> common.Trigger:
        if self.user_value(key='respawn', value=2):
            return end(self.ctx)
        if not self.monster_dead(boxIds=[1999]):
            return respawn_timer2(self.ctx)


class respawn_timer2(common.Trigger):
    def on_enter(self):
        self.set_timer(timerId='respawntimer2', seconds=120, startDelay=1, interval=0, vOffset=0)

    def on_tick(self) -> common.Trigger:
        if self.user_value(key='respawn', value=2):
            return end(self.ctx)
        if self.time_expired(timerId='respawntimer2'):
            return respawn2(self.ctx)


class respawn2(common.Trigger):
    def on_enter(self):
        self.reset_timer(timerId='respawntimer2')
        self.create_monster(spawnIds=[301,302,303,304,305,306], animationEffect=False)

    def on_tick(self) -> common.Trigger:
        if self.user_value(key='respawn', value=2):
            return end(self.ctx)
        if not self.monster_dead(boxIds=[1999]):
            return respawn_timer3(self.ctx)


class respawn_timer3(common.Trigger):
    def on_enter(self):
        self.set_timer(timerId='respawntimer3', seconds=120, startDelay=1, interval=0, vOffset=0)

    def on_tick(self) -> common.Trigger:
        if self.user_value(key='respawn', value=2):
            return end(self.ctx)
        if self.time_expired(timerId='respawntimer3'):
            return respawn3(self.ctx)


class respawn3(common.Trigger):
    def on_enter(self):
        self.reset_timer(timerId='respawntimer3')
        self.create_monster(spawnIds=[301,302,303,304,305,306], animationEffect=False)

    def on_tick(self) -> common.Trigger:
        if self.user_value(key='respawn', value=2):
            return end(self.ctx)
        if not self.monster_dead(boxIds=[1999]):
            return respawn_timer4(self.ctx)


class respawn_timer4(common.Trigger):
    def on_enter(self):
        self.set_timer(timerId='respawntimer4', seconds=120, startDelay=1, interval=0, vOffset=0)

    def on_tick(self) -> common.Trigger:
        if self.user_value(key='respawn', value=2):
            return end(self.ctx)
        if self.time_expired(timerId='respawntimer4'):
            return respawn4(self.ctx)


class respawn4(common.Trigger):
    def on_enter(self):
        self.reset_timer(timerId='respawntimer4')
        self.create_monster(spawnIds=[301,302,303,304,305,306], animationEffect=False)

    def on_tick(self) -> common.Trigger:
        if self.user_value(key='respawn', value=2):
            return end(self.ctx)
        if not self.monster_dead(boxIds=[1999]):
            return respawn_timer5(self.ctx)


class respawn_timer5(common.Trigger):
    def on_enter(self):
        self.set_timer(timerId='respawntimer5', seconds=120, startDelay=1, interval=0, vOffset=0)

    def on_tick(self) -> common.Trigger:
        if self.user_value(key='respawn', value=2):
            return end(self.ctx)
        if self.time_expired(timerId='respawntimer5'):
            return respawn5(self.ctx)


class respawn5(common.Trigger):
    def on_enter(self):
        self.reset_timer(timerId='respawntimer5')
        self.create_monster(spawnIds=[301,302,303,304,305,306], animationEffect=False)

    def on_tick(self) -> common.Trigger:
        if self.true():
            return end(self.ctx)


class end(common.Trigger):
    pass


initial_state = idle
