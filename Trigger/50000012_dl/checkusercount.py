""" trigger/50000012_dl/checkusercount.xml """
import common


class CheckUserCount(common.Trigger):
    def on_enter(self):
        self.set_portal(portalId=2, visible=False, enable=False, minimapVisible=False)

    def on_tick(self) -> common.Trigger:
        if self.check_dungeon_lobby_user_count():
            return DungeonStart(self.ctx)
        if not self.check_dungeon_lobby_user_count():
            return WaitDungeon01(self.ctx)


# 던전 최대 인원수가 충족되면
class DungeonStart(common.Trigger):
    def on_enter(self):
        self.set_portal(portalId=2, visible=True, enable=True, minimapVisible=True)
        self.show_guide_summary(entityId=25100203, textId=25100203)


# 던전 로비에서 생성할 던전 인원수가 부족하면 대기
class WaitDungeon01(common.Trigger):
    def on_enter(self):
        self.show_guide_summary(entityId=25100201, textId=25100201, duration=3000)

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=5000):
            return WaitDungeon02(self.ctx)


class WaitDungeon02(common.Trigger):
    def on_tick(self) -> common.Trigger:
        if self.check_dungeon_lobby_user_count():
            return DungeonStart(self.ctx)
        if not self.check_dungeon_lobby_user_count():
            return WaitDungeon03(self.ctx)


class WaitDungeon03(common.Trigger):
    def on_enter(self):
        self.show_guide_summary(entityId=25100202, textId=25100202, duration=3000)

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=5000):
            return WaitDungeon04(self.ctx)


class WaitDungeon04(common.Trigger):
    def on_tick(self) -> common.Trigger:
        if self.check_dungeon_lobby_user_count():
            return DungeonStart(self.ctx)
        if not self.check_dungeon_lobby_user_count():
            return WaitDungeon05(self.ctx)


class WaitDungeon05(common.Trigger):
    def on_enter(self):
        self.show_guide_summary(entityId=25100201, textId=25100201, duration=3000)

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=5000):
            return WaitDungeon06(self.ctx)


class WaitDungeon06(common.Trigger):
    def on_tick(self) -> common.Trigger:
        if self.check_dungeon_lobby_user_count():
            return DungeonStart(self.ctx)
        if not self.check_dungeon_lobby_user_count():
            return WaitDungeon07(self.ctx)


class WaitDungeon07(common.Trigger):
    def on_enter(self):
        self.show_guide_summary(entityId=25100202, textId=25100202, duration=3000)

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=5000):
            return WaitDungeon08(self.ctx)


class WaitDungeon08(common.Trigger):
    def on_tick(self) -> common.Trigger:
        if self.check_dungeon_lobby_user_count():
            return DungeonStart(self.ctx)
        if not self.check_dungeon_lobby_user_count():
            return WaitDungeon09(self.ctx)


class WaitDungeon09(common.Trigger):
    def on_enter(self):
        self.show_guide_summary(entityId=25100201, textId=25100201, duration=3000)

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=5000):
            return WaitDungeon10(self.ctx)


class WaitDungeon10(common.Trigger):
    def on_tick(self) -> common.Trigger:
        if self.check_dungeon_lobby_user_count():
            return DungeonStart(self.ctx)
        if not self.check_dungeon_lobby_user_count():
            return WaitDungeon11(self.ctx)


class WaitDungeon11(common.Trigger):
    def on_enter(self):
        self.show_guide_summary(entityId=25100202, textId=25100202, duration=3000)

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=5000):
            return DungeonStart(self.ctx)


initial_state = CheckUserCount
