""" trigger/50000006_dl/checkusercount.xml """
from common import *
import state


class CheckUserCount(state.State):
    def on_enter(self):
        set_user_value(key='DungeonRoomOpened', value=0)
        set_actor(triggerId=4002, visible=True, initialSequence='Interaction_vrmachine_A01_off')
        set_actor(triggerId=4001, visible=True, initialSequence='Interaction_vrmachine_A01_off')
        set_actor(triggerId=4003, visible=True, initialSequence='Interaction_vrmachine_A01_off')

    def on_tick(self) -> state.State:
        if check_dungeon_lobby_user_count():
            return state.DungeonStart()
        if not check_dungeon_lobby_user_count():
            return WaitDungeon01()


#  던전 최대 인원수가 충족되면 
class DungeonStart(state.DungeonStart):
    def on_enter(self):
        set_user_value(triggerId=3, key='machineon', value=1)
        set_actor(triggerId=4002, visible=True, initialSequence='Interaction_vrmachine_A01_on')

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=800):
            return DungeonStart01()

state.DungeonStart = DungeonStart


class DungeonStart01(state.State):
    def on_enter(self):
        play_system_sound_in_box(sound='GuildRaid_Laboratory_DungeonOpen_01')
        show_guide_summary(entityId=25100206, textId=25100206, duration=3000)
        set_actor(triggerId=4002, visible=False, initialSequence='Interaction_vrmachine_A01_on')

    def on_tick(self) -> state.State:
        if user_value(key='DungeonRoomOpened', value=1):
            return DungeonStart02()


class DungeonStart02(state.State):
    def on_enter(self):
        set_user_value(triggerId=2, key='machineon', value=1)
        set_user_value(triggerId=4, key='machineon', value=1)
        set_actor(triggerId=4001, visible=True, initialSequence='Interaction_vrmachine_A01_on')
        set_actor(triggerId=4003, visible=True, initialSequence='Interaction_vrmachine_A01_on')

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=800):
            return DungeonStart03()


class DungeonStart03(state.State):
    def on_enter(self):
        set_actor(triggerId=4001, visible=False, initialSequence='Interaction_vrmachine_A01_on')
        set_actor(triggerId=4003, visible=False, initialSequence='Interaction_vrmachine_A01_on')

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=1000):
            return DungeonStart04()


class DungeonStart04(state.State):
    def on_enter(self):
        play_system_sound_in_box(sound='GuildRaid_Laboratory_DungeonOpen_01')
        show_guide_summary(entityId=25100206, textId=25100206, duration=3000)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=5000):
            return DungeonStart04()


#  던전 로비에서 생성할 던전 인원수가 부족하면 대기
class WaitDungeon01(state.State):
    def on_enter(self):
        show_guide_summary(entityId=25100204, textId=25100204, duration=3000)

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
        show_guide_summary(entityId=25100205, textId=25100205, duration=3000)

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
        show_guide_summary(entityId=25100204, textId=25100204, duration=3000)

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
        show_guide_summary(entityId=25100205, textId=25100205, duration=3000)

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
        show_guide_summary(entityId=25100204, textId=25100204, duration=3000)

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
        show_guide_summary(entityId=25100205, textId=25100205, duration=3000)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=5000):
            return state.DungeonStart()


