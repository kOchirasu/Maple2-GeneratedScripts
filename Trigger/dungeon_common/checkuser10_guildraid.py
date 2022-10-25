""" trigger/dungeon_common/checkuser10_guildraid.xml """
import common


class CheckUser10_GuildRaid(common.Trigger):
    def on_enter(self):
        self.set_timer(timerId='1', seconds=30, startDelay=1, interval=0, vOffset=0) # 최대 30초 대기

    def on_tick(self) -> common.Trigger:
        if self.count_users(boxId=9900, boxId=10, operator='GreaterEqual'):
            return MaxCount10_Start(self.ctx)
        if self.count_users(boxId=9900, boxId=10, operator='Less'):
            return MaxCount10_Wait(self.ctx)


class MaxCount10_Wait(common.Trigger):
    def on_enter(self):
        self.show_guide_summary(entityId=40012, textId=40012, duration=3000)

    def on_tick(self) -> common.Trigger:
        if self.count_users(boxId=9900, boxId=10, operator='GreaterEqual'):
            return MaxCount10_Start(self.ctx)
        if self.time_expired(timerId='1'):
            return MaxCount10_Start(self.ctx)
        if self.wait_tick(waitTick=6000):
            return MaxCount10_Wait(self.ctx)


class MaxCount10_Start(common.Trigger):
    def on_enter(self):
        self.reset_timer(timerId='1')

    def on_tick(self) -> common.Trigger:
        if self.true():
            return DungeonStart(self.ctx)


