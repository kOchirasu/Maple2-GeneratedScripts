""" trigger/02100001_bf/01_mainmission.xml """
from common import *
import state

from dungeon_common.checkuser10_guildraid import *

#  아프렐라 오지 
class Wait(state.State):
    def on_enter(self):
        reset_timer(timerId='10000') # Red
        set_interact_object(triggerIds=[10001234], state=1) # Blue
        set_interact_object(triggerIds=[10001235], state=1) # Grey
        set_interact_object(triggerIds=[10001236], state=1) # Green
        set_interact_object(triggerIds=[10001237], state=1) # Yellow
        set_interact_object(triggerIds=[10001238], state=1) # 주민NPC
        destroy_monster(spawnIds=[101,102,103,104,105,106,107,108]) # 입구 포탈
        set_portal(portalId=1, visible=True, enabled=True, minimapVisible=True) # 출구 포탈 Cage
        set_portal(portalId=2, visible=False, enabled=False, minimapVisible=False) # 출구 포탈
        set_portal(portalId=3, visible=False, enabled=False, minimapVisible=False)

    def on_tick(self) -> state.State:
        if check_user():
            return LoadingDelay()


class LoadingDelay(state.State):
    def on_enter(self):
        create_monster(spawnIds=[101,102,103,104,105,106,107,108], arg2=False) # 주민NPC

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=1000):
            return CheckUser10_GuildRaid()


class DungeonStart(state.DungeonStart):
    def on_enter(self):
        select_camera(triggerId=903, enable=True)
        set_cinematic_intro()

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=2000):
            return ShowCaption01()

state.DungeonStart = DungeonStart


#  설명문 출력 
class ShowCaption01(state.State):
    def on_enter(self):
        set_cinematic_intro(text='$02100001_BF__01_MAINMISSION__0$')
        set_skip(state=ShowCaption01Skip)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=20000):
            return ShowCaption01Skip()


class ShowCaption01Skip(state.State):
    def on_enter(self):
        set_skip()

    def on_tick(self) -> state.State:
        if true():
            return ShowCaption02()


class ShowCaption02(state.State):
    def on_enter(self):
        set_cinematic_intro(text='$02100001_BF__01_MAINMISSION__1$')
        set_skip(state=ShowCaption02Skip)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=20000):
            return ShowCaption02Skip()


class ShowCaption02Skip(state.State):
    def on_enter(self):
        set_skip()

    def on_tick(self) -> state.State:
        if true():
            return CloseCaptionSetting()


class CloseCaptionSetting(state.State):
    def on_enter(self):
        close_cinematic()
        select_camera(triggerId=903, enable=False)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=1000):
            return DoorOpen()


class DoorOpen(state.State):
    def on_enter(self):
        set_user_value(triggerId=99, key='CageDoorOpen', value=1)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=2000):
            return TalkStart()


class TalkStart(state.State):
    def on_enter(self):
        set_cinematic_ui(type=1)
        set_cinematic_ui(type=3)
        select_camera(triggerId=900, enable=True)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=2000):
            return CinematicTalk01()


class CinematicTalk01(state.State):
    def on_enter(self):
        add_cinematic_talk(npcId=11003512, msg='$02100001_BF__01_MAINMISSION__2$', duration=5000, align='center', illustId='0')
        set_skip(state=CinematicTalk01Skip)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=5000):
            return CinematicTalk01Skip()


class CinematicTalk01Skip(state.State):
    def on_enter(self):
        set_skip()
        remove_cinematic_talk()

    def on_tick(self) -> state.State:
        if true():
            return CinematicTalk02()


class CinematicTalk02(state.State):
    def on_enter(self):
        add_cinematic_talk(npcId=11003512, msg='$02100001_BF__01_MAINMISSION__3$', duration=5000, align='center', illustId='0')
        set_skip(state=CinematicTalk02Skip)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=5000):
            return CinematicTalk02Skip()


class CinematicTalk02Skip(state.State):
    def on_enter(self):
        set_skip()
        remove_cinematic_talk()

    def on_tick(self) -> state.State:
        if true():
            return TalkEnd()


class TalkEnd(state.State):
    def on_enter(self):
        set_cinematic_ui(type=0)
        set_cinematic_ui(type=2)
        select_camera(triggerId=900, enable=False)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=1500):
            return TimmerStart()


class TimmerStart(state.State):
    def on_enter(self):
        set_user_value(triggerId=99, key='MissionStart', value=1)
        play_system_sound_in_box(sound='System_ShowGuideSummary_01') # 제한 시간 5분
        set_timer(timerId='10000', seconds=300, clearAtZero=True, display=True, arg5=0)

    def on_tick(self) -> state.State:
        if all_of():
            return MissionComplete()
        if time_expired(timerId='10000'):
            return MissionFail()

    def on_exit(self):
        set_user_value(triggerId=5, key='GiveBuffSlowly', value=2)


class MissionFail(state.State):
    def on_enter(self):
        reset_timer(timerId='10000')
        set_portal(portalId=1, visible=False, enabled=False, minimapVisible=False) # 입구 포탈
        set_event_ui(type=5, arg2='$02100001_BF__01_MAINMISSION__4$', arg3='3000')
        set_interact_object(triggerIds=[10001234], state=2) # Red
        set_interact_object(triggerIds=[10001235], state=2) # Blue
        set_interact_object(triggerIds=[10001236], state=2) # Grey
        set_interact_object(triggerIds=[10001237], state=2) # Green
        set_interact_object(triggerIds=[10001238], state=2) # Yellow

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=3000):
            return MoveToCage()


class MoveToCage(state.State):
    def on_enter(self):
        move_user(mapId=2100001, portalId=10)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=2000):
            return BadEndingStart()


#  BadEnding 연출 
class BadEndingStart(state.State):
    def on_enter(self):
        set_cinematic_ui(type=1)
        set_cinematic_ui(type=3)
        select_camera(triggerId=901, enable=True)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=1000):
            return BadEndingTalk01()


class BadEndingTalk01(state.State):
    def on_enter(self):
        add_cinematic_talk(npcId=11003517, msg='$02100001_BF__01_MAINMISSION__5$', duration=5000, align='center', illustId='0')
        set_skip(state=BadEndingTalk01Skip)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=5000):
            return BadEndingTalk01Skip()


class BadEndingTalk01Skip(state.State):
    def on_enter(self):
        set_skip()
        remove_cinematic_talk()

    def on_tick(self) -> state.State:
        if true():
            return BadEndingEnd()


class BadEndingEnd(state.State):
    def on_enter(self):
        set_cinematic_ui(type=0)
        set_cinematic_ui(type=2)
        select_camera(triggerId=901, enable=False)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=1000):
            return DungeonFail()


#  던전 실패 선언 
class DungeonFail(state.State):
    def on_enter(self):
        dungeon_fail()

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=1000):
            return BadEndingPortalOn()


class BadEndingPortalOn(state.State):
    def on_enter(self):
        set_portal(portalId=2, visible=True, enabled=True, minimapVisible=True) # 출구 포탈 Cage

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=1000):
            return Quit()


class MissionComplete(state.State):
    def on_enter(self):
        reset_timer(timerId='10000')
        set_portal(portalId=1, visible=False, enabled=False, minimapVisible=False) # 입구 포탈
        set_achievement(triggerId=9902, type='trigger', achieve='Find02100001')
        set_achievement(triggerId=9902, type='trigger', achieve='guildraid_clear_1') # CN 스탬프 이벤트 전용
        set_event_ui(type=7, arg2='$02100001_BF__01_MAINMISSION__6$', arg3='3000')
        set_user_value(triggerId=99, key='MissionComplete', value=1)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=3000):
            return HappyEndingStart()


#  HappyEnding 연출 
class HappyEndingStart(state.State):
    def on_enter(self):
        set_cinematic_ui(type=1)
        set_cinematic_ui(type=3)
        select_camera(triggerId=902, enable=True)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=1000):
            return HappyEndingTalk01()


class HappyEndingTalk01(state.State):
    def on_enter(self):
        add_cinematic_talk(npcId=11003512, msg='$02100001_BF__01_MAINMISSION__7$', duration=5000, align='center', illustId='0')
        set_skip(state=HappyEndingTalk01Skip)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=5000):
            return HappyEndingTalk01Skip()


class HappyEndingTalk01Skip(state.State):
    def on_enter(self):
        set_skip()
        remove_cinematic_talk()

    def on_tick(self) -> state.State:
        if true():
            return HappyEndingEnd()


class HappyEndingEnd(state.State):
    def on_enter(self):
        set_cinematic_ui(type=0)
        set_cinematic_ui(type=2)
        select_camera(triggerId=902, enable=False)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=1000):
            return DungeonSuccess()


#  던전 클리어 선언 
class DungeonSuccess(state.State):
    def on_enter(self):
        dungeon_clear()

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=1000):
            return HappyEndingPortalOn()


class HappyEndingPortalOn(state.State):
    def on_enter(self):
        set_portal(portalId=3, visible=True, enabled=True, minimapVisible=True) # 출구 포탈

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=1000):
            return Quit()


class Quit(state.State):
    pass


