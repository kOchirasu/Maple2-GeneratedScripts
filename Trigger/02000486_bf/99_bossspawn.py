""" trigger/02000486_bf/99_bossspawn.xml """
import common


class Wait(common.Trigger):
    def on_enter(self):
        self.set_portal(portalId=2, visible=False, enable=False, minimapVisible=False)

    def on_tick(self) -> common.Trigger:
        if self.check_user():
            return 던전시작(self.ctx)


class 룸체크(common.Trigger):
    def on_tick(self) -> common.Trigger:
        if self.is_dungeon_room():
            return 던전시작(self.ctx)


class 던전시작(common.Trigger):
    def on_enter(self):
        self.create_monster(spawnIds=[900,901], animationEffect=False)

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=1000):
            return BossBattle01(self.ctx)


class BossBattle01(common.Trigger):
    def on_enter(self):
        self.set_user_value(triggerId=100, key='CheckDualKill', value=1)

    def on_tick(self) -> common.Trigger:
        if self.monster_dead(boxIds=[900,901]):
            return BossBattle02(self.ctx)


class BossBattle02(common.Trigger):
    def on_enter(self):
        self.destroy_monster(spawnIds=[900,901])
        self.set_achievement(triggerId=9900, type='trigger', achieve='Madracan02')
        self.set_achievement(triggerId=9900, type='trigger', achieve='Madracan_Q02')

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=2000):
            return Quit(self.ctx)


class QuestClear(common.Trigger):
    def on_enter(self):
        self.set_achievement(triggerId=9900, type='trigger', achieve='Madracan_Q02')

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=2000):
            return Quit(self.ctx)


class Quit(common.Trigger):
    def on_enter(self):
        self.dungeon_clear()
        self.set_portal(portalId=2, visible=True, enable=True, minimapVisible=True)


initial_state = Wait
