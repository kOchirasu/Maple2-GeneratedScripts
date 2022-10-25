""" trigger/52100056_qd/99_bossspawn.xml """
import common


class Wait(common.Trigger):
    def on_enter(self):
        self.set_portal(portalId=2, visible=False, enable=False, minimapVisible=False)

    def on_tick(self) -> common.Trigger:
        if self.check_user():
            return 룸체크(self.ctx)


class 룸체크(common.Trigger):
    def on_tick(self) -> common.Trigger:
        if self.is_dungeon_room():
            return 던전시작(self.ctx)
        if not self.is_dungeon_room():
            return 퀘스트던전시작(self.ctx)


class 던전시작(common.Trigger):
    def on_enter(self):
        self.create_monster(spawnIds=[900,901], animationEffect=False)

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=1000):
            return BossBattle01(self.ctx)


class 퀘스트던전시작(common.Trigger):
    def on_enter(self):
        self.create_monster(spawnIds=[910,911], animationEffect=False)

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=1000):
            return 종료체크(self.ctx)


class 종료체크(common.Trigger):
    def on_tick(self) -> common.Trigger:
        if self.monster_dead(boxIds=[910,911]):
            return QuestClear(self.ctx)


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
        self.move_user(mapId=2000402, portalId=1)
        # <action name="포탈을설정한다" arg1="2" arg2="1" arg3="1" arg4="1"/>


initial_state = Wait
