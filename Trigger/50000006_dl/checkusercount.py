""" trigger/50000006_dl/checkusercount.xml """
import common


class CheckUserCount(common.Trigger):
    def on_enter(self):
        self.set_user_value(key='DungeonRoomOpened', value=0)
        self.set_actor(triggerId=4002, visible=True, initialSequence='Interaction_vrmachine_A01_off')
        self.set_actor(triggerId=4001, visible=True, initialSequence='Interaction_vrmachine_A01_off')
        self.set_actor(triggerId=4003, visible=True, initialSequence='Interaction_vrmachine_A01_off')

    def on_tick(self) -> common.Trigger:
        if self.check_dungeon_lobby_user_count():
            return DungeonStart(self.ctx)
        if not self.check_dungeon_lobby_user_count():
            return WaitDungeon01(self.ctx)


# 던전 최대 인원수가 충족되면
class DungeonStart(common.Trigger):
    def on_enter(self):
        self.set_user_value(triggerId=3, key='machineon', value=1)
        self.set_actor(triggerId=4002, visible=True, initialSequence='Interaction_vrmachine_A01_on')

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=800):
            return DungeonStart01(self.ctx)


class DungeonStart01(common.Trigger):
    def on_enter(self):
        self.play_system_sound_in_box(sound='GuildRaid_Laboratory_DungeonOpen_01')
        self.show_guide_summary(entityId=25100206, textId=25100206, duration=3000)
        self.set_actor(triggerId=4002, visible=False, initialSequence='Interaction_vrmachine_A01_on')

    def on_tick(self) -> common.Trigger:
        if self.user_value(key='DungeonRoomOpened', value=1):
            return DungeonStart02(self.ctx)


class DungeonStart02(common.Trigger):
    def on_enter(self):
        self.set_user_value(triggerId=2, key='machineon', value=1)
        self.set_user_value(triggerId=4, key='machineon', value=1)
        self.set_actor(triggerId=4001, visible=True, initialSequence='Interaction_vrmachine_A01_on')
        self.set_actor(triggerId=4003, visible=True, initialSequence='Interaction_vrmachine_A01_on')

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=800):
            return DungeonStart03(self.ctx)


class DungeonStart03(common.Trigger):
    def on_enter(self):
        self.set_actor(triggerId=4001, visible=False, initialSequence='Interaction_vrmachine_A01_on')
        self.set_actor(triggerId=4003, visible=False, initialSequence='Interaction_vrmachine_A01_on')

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=1000):
            return DungeonStart04(self.ctx)


class DungeonStart04(common.Trigger):
    def on_enter(self):
        self.play_system_sound_in_box(sound='GuildRaid_Laboratory_DungeonOpen_01')
        self.show_guide_summary(entityId=25100206, textId=25100206, duration=3000)

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=5000):
            return DungeonStart04(self.ctx)


# 던전 로비에서 생성할 던전 인원수가 부족하면 대기
class WaitDungeon01(common.Trigger):
    def on_enter(self):
        self.show_guide_summary(entityId=25100204, textId=25100204, duration=3000)

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
        self.show_guide_summary(entityId=25100205, textId=25100205, duration=3000)

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
        self.show_guide_summary(entityId=25100204, textId=25100204, duration=3000)

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
        self.show_guide_summary(entityId=25100205, textId=25100205, duration=3000)

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
        self.show_guide_summary(entityId=25100204, textId=25100204, duration=3000)

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
        self.show_guide_summary(entityId=25100205, textId=25100205, duration=3000)

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=5000):
            return DungeonStart(self.ctx)


initial_state = CheckUserCount
