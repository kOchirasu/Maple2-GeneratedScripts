""" trigger/dungeon_common/checkusercount.xml """
import common


class CheckUserCount(common.Trigger):
    def on_tick(self) -> common.Trigger:
        if self.dungeon_max_user_count(value=4):
            return MaxCount04_Wait01(self.ctx)
        if self.dungeon_max_user_count(value=3):
            return MaxCount03_Wait01(self.ctx)
        if self.dungeon_max_user_count(value=2):
            return MaxCount02_Wait01(self.ctx)
        if self.dungeon_max_user_count(value=1):
            return MaxCount01_Wait01(self.ctx)
        if not self.is_dungeon_room():
            return DungeonStart(self.ctx)


# 던전 최대 인원수가 4이면
class MaxCount04_Wait01(common.Trigger):
    def on_tick(self) -> common.Trigger:
        if self.check_user_count(checkCount=4):
            return DungeonStart(self.ctx)
        if self.wait_tick(waitTick=1000):
            return MaxCount04_Wait02(self.ctx)


class MaxCount04_Wait02(common.Trigger):
    def on_enter(self):
        self.show_guide_summary(entityId=40012, textId=40012, duration=4000)

    def on_tick(self) -> common.Trigger:
        if self.check_user_count(checkCount=4):
            return DungeonStart(self.ctx)
        if self.wait_tick(waitTick=5000):
            return MaxCount04_Wait03(self.ctx)


class MaxCount04_Wait03(common.Trigger):
    def on_enter(self):
        self.show_guide_summary(entityId=40012, textId=40012, duration=4000)

    def on_tick(self) -> common.Trigger:
        if self.check_user_count(checkCount=4):
            return DungeonStart(self.ctx)
        if self.wait_tick(waitTick=5000):
            return MaxCount04_Wait04(self.ctx)


class MaxCount04_Wait04(common.Trigger):
    def on_enter(self):
        self.show_guide_summary(entityId=40012, textId=40012, duration=4000)

    def on_tick(self) -> common.Trigger:
        if self.check_user_count(checkCount=4):
            return DungeonStart(self.ctx)
        if self.wait_tick(waitTick=5000):
            return DungeonStart(self.ctx)


# 던전 최대 인원수가 3이면
class MaxCount03_Wait01(common.Trigger):
    def on_tick(self) -> common.Trigger:
        if self.check_user_count(checkCount=3):
            return DungeonStart(self.ctx)
        if self.wait_tick(waitTick=1000):
            return MaxCount03_Wait02(self.ctx)


class MaxCount03_Wait02(common.Trigger):
    def on_enter(self):
        self.show_guide_summary(entityId=40012, textId=40012, duration=4000)

    def on_tick(self) -> common.Trigger:
        if self.check_user_count(checkCount=3):
            return DungeonStart(self.ctx)
        if self.wait_tick(waitTick=5000):
            return MaxCount03_Wait03(self.ctx)


class MaxCount03_Wait03(common.Trigger):
    def on_enter(self):
        self.show_guide_summary(entityId=40012, textId=40012, duration=4000)

    def on_tick(self) -> common.Trigger:
        if self.check_user_count(checkCount=3):
            return DungeonStart(self.ctx)
        if self.wait_tick(waitTick=5000):
            return MaxCount03_Wait04(self.ctx)


class MaxCount03_Wait04(common.Trigger):
    def on_enter(self):
        self.show_guide_summary(entityId=40012, textId=40012, duration=4000)

    def on_tick(self) -> common.Trigger:
        if self.check_user_count(checkCount=3):
            return DungeonStart(self.ctx)
        if self.wait_tick(waitTick=5000):
            return DungeonStart(self.ctx)


# 던전 최대 인원수가 2이면
class MaxCount02_Wait01(common.Trigger):
    def on_tick(self) -> common.Trigger:
        if self.check_user_count(checkCount=2):
            return DungeonStart(self.ctx)
        if self.wait_tick(waitTick=1000):
            return MaxCount02_Wait02(self.ctx)


class MaxCount02_Wait02(common.Trigger):
    def on_enter(self):
        self.show_guide_summary(entityId=40012, textId=40012, duration=4000)

    def on_tick(self) -> common.Trigger:
        if self.check_user_count(checkCount=2):
            return DungeonStart(self.ctx)
        if self.wait_tick(waitTick=5000):
            return MaxCount02_Wait03(self.ctx)


class MaxCount02_Wait03(common.Trigger):
    def on_enter(self):
        self.show_guide_summary(entityId=40012, textId=40012, duration=4000)

    def on_tick(self) -> common.Trigger:
        if self.check_user_count(checkCount=2):
            return DungeonStart(self.ctx)
        if self.wait_tick(waitTick=5000):
            return MaxCount02_Wait04(self.ctx)


class MaxCount02_Wait04(common.Trigger):
    def on_enter(self):
        self.show_guide_summary(entityId=40012, textId=40012, duration=4000)

    def on_tick(self) -> common.Trigger:
        if self.check_user_count(checkCount=2):
            return DungeonStart(self.ctx)
        if self.wait_tick(waitTick=5000):
            return DungeonStart(self.ctx)


# 던전 최대 인원수가 1이면 바로 시작
class MaxCount01_Wait01(common.Trigger):
    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=1000):
            return DungeonStart(self.ctx)


