""" trigger/50000009_dl/checkusercount.xml """
from common import *
import state


class CheckUserCount(state.State):
    def on_enter(self):
        set_portal(portalId=2, visible=False, enabled=False, minimapVisible=False)

    def on_tick(self) -> state.State:
        if check_dungeon_lobby_user_count():
            return state.DungeonStart()
        if not check_dungeon_lobby_user_count():
            return WaitDungeon01()


#  던전 최대 인원수가 충족되면 
class DungeonStart(state.DungeonStart):
    def on_enter(self):
        set_portal(portalId=2, visible=True, enabled=True, minimapVisible=True)
        show_guide_summary(entityId=25100203, textId=25100203)

state.DungeonStart = DungeonStart


#  던전 로비에서 생성할 던전 인원수가 부족하면 대기
class WaitDungeon01(state.State):
    def on_enter(self):
        show_guide_summary(entityId=25100201, textId=25100201, duration=3000)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=5000):
            return WaitDungeon02()


class WaitDungeon02(state.State):
    def on_tick(self) -> state.State:
        if check_dungeon_lobby_user_count():
            return state.DungeonStart()
        if not check_dungeon_lobby_user_count():
            return WaitDungeon03()


class WaitDungeon03(state.State):
    def on_enter(self):
        show_guide_summary(entityId=25100202, textId=25100202, duration=3000)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=5000):
            return WaitDungeon04()


class WaitDungeon04(state.State):
    def on_tick(self) -> state.State:
        if check_dungeon_lobby_user_count():
            return state.DungeonStart()
        if not check_dungeon_lobby_user_count():
            return WaitDungeon05()


class WaitDungeon05(state.State):
    def on_enter(self):
        show_guide_summary(entityId=25100201, textId=25100201, duration=3000)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=5000):
            return WaitDungeon06()


class WaitDungeon06(state.State):
    def on_tick(self) -> state.State:
        if check_dungeon_lobby_user_count():
            return state.DungeonStart()
        if not check_dungeon_lobby_user_count():
            return WaitDungeon07()


class WaitDungeon07(state.State):
    def on_enter(self):
        show_guide_summary(entityId=25100202, textId=25100202, duration=3000)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=5000):
            return WaitDungeon08()


class WaitDungeon08(state.State):
    def on_tick(self) -> state.State:
        if check_dungeon_lobby_user_count():
            return state.DungeonStart()
        if not check_dungeon_lobby_user_count():
            return WaitDungeon09()


class WaitDungeon09(state.State):
    def on_enter(self):
        show_guide_summary(entityId=25100201, textId=25100201, duration=3000)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=5000):
            return WaitDungeon10()


class WaitDungeon10(state.State):
    def on_tick(self) -> state.State:
        if check_dungeon_lobby_user_count():
            return state.DungeonStart()
        if not check_dungeon_lobby_user_count():
            return WaitDungeon11()


class WaitDungeon11(state.State):
    def on_enter(self):
        show_guide_summary(entityId=25100202, textId=25100202, duration=3000)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=5000):
            return state.DungeonStart()


