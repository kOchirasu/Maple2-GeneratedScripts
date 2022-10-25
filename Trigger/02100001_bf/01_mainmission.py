""" trigger/02100001_bf/01_mainmission.xml """
import common

#include dungeon_common/checkuser10_guildraid.py
from dungeon_common.checkuser10_guildraid import *


# 아프렐라 오지
class Wait(common.Trigger):
    def on_enter(self):
        self.reset_timer(timerId='10000') # Red
        self.set_interact_object(triggerIds=[10001234], state=1) # Blue
        self.set_interact_object(triggerIds=[10001235], state=1) # Grey
        self.set_interact_object(triggerIds=[10001236], state=1) # Green
        self.set_interact_object(triggerIds=[10001237], state=1) # Yellow
        self.set_interact_object(triggerIds=[10001238], state=1) # 주민NPC
        self.destroy_monster(spawnIds=[101,102,103,104,105,106,107,108]) # 입구 포탈
        self.set_portal(portalId=1, visible=True, enable=True, minimapVisible=True) # 출구 포탈 Cage
        self.set_portal(portalId=2, visible=False, enable=False, minimapVisible=False) # 출구 포탈
        self.set_portal(portalId=3, visible=False, enable=False, minimapVisible=False)

    def on_tick(self) -> common.Trigger:
        if self.check_user():
            return LoadingDelay(self.ctx)


class LoadingDelay(common.Trigger):
    def on_enter(self):
        self.create_monster(spawnIds=[101,102,103,104,105,106,107,108], animationEffect=False) # 주민NPC

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=1000):
            return CheckUser10_GuildRaid(self.ctx)


class DungeonStart(common.Trigger):
    def on_enter(self):
        self.select_camera(triggerId=903, enable=True)
        self.set_cinematic_intro()

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=2000):
            return ShowCaption01(self.ctx)


# 설명문 출력
class ShowCaption01(common.Trigger):
    def on_enter(self):
        self.set_cinematic_intro(text='$02100001_BF__01_MAINMISSION__0$')
        self.set_skip(state=ShowCaption01Skip)

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=20000):
            return ShowCaption01Skip(self.ctx)


class ShowCaption01Skip(common.Trigger):
    def on_enter(self):
        self.set_skip()

    def on_tick(self) -> common.Trigger:
        if self.true():
            return ShowCaption02(self.ctx)


class ShowCaption02(common.Trigger):
    def on_enter(self):
        self.set_cinematic_intro(text='$02100001_BF__01_MAINMISSION__1$')
        self.set_skip(state=ShowCaption02Skip)

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=20000):
            return ShowCaption02Skip(self.ctx)


class ShowCaption02Skip(common.Trigger):
    def on_enter(self):
        self.set_skip()

    def on_tick(self) -> common.Trigger:
        if self.true():
            return CloseCaptionSetting(self.ctx)


class CloseCaptionSetting(common.Trigger):
    def on_enter(self):
        self.close_cinematic()
        self.select_camera(triggerId=903, enable=False)

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=1000):
            return DoorOpen(self.ctx)


class DoorOpen(common.Trigger):
    def on_enter(self):
        self.set_user_value(triggerId=99, key='CageDoorOpen', value=1)

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=2000):
            return TalkStart(self.ctx)


class TalkStart(common.Trigger):
    def on_enter(self):
        self.set_cinematic_ui(type=1)
        self.set_cinematic_ui(type=3)
        self.select_camera(triggerId=900, enable=True)

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=2000):
            return CinematicTalk01(self.ctx)


class CinematicTalk01(common.Trigger):
    def on_enter(self):
        self.add_cinematic_talk(npcId=11003512, msg='$02100001_BF__01_MAINMISSION__2$', duration=5000, align='center', illustId='0')
        self.set_skip(state=CinematicTalk01Skip)

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=5000):
            return CinematicTalk01Skip(self.ctx)


class CinematicTalk01Skip(common.Trigger):
    def on_enter(self):
        self.set_skip()
        self.remove_cinematic_talk()

    def on_tick(self) -> common.Trigger:
        if self.true():
            return CinematicTalk02(self.ctx)


class CinematicTalk02(common.Trigger):
    def on_enter(self):
        self.add_cinematic_talk(npcId=11003512, msg='$02100001_BF__01_MAINMISSION__3$', duration=5000, align='center', illustId='0')
        self.set_skip(state=CinematicTalk02Skip)

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=5000):
            return CinematicTalk02Skip(self.ctx)


class CinematicTalk02Skip(common.Trigger):
    def on_enter(self):
        self.set_skip()
        self.remove_cinematic_talk()

    def on_tick(self) -> common.Trigger:
        if self.true():
            return TalkEnd(self.ctx)


class TalkEnd(common.Trigger):
    def on_enter(self):
        self.set_cinematic_ui(type=0)
        self.set_cinematic_ui(type=2)
        self.select_camera(triggerId=900, enable=False)

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=1500):
            return TimmerStart(self.ctx)


class TimmerStart(common.Trigger):
    def on_enter(self):
        self.set_user_value(triggerId=99, key='MissionStart', value=1)
        self.play_system_sound_in_box(sound='System_ShowGuideSummary_01') # 제한 시간 5분
        self.set_timer(timerId='10000', seconds=300, startDelay=1, interval=1, vOffset=0)

    def on_tick(self) -> common.Trigger:
        if self.all_of():
            return MissionComplete(self.ctx)
        if self.time_expired(timerId='10000'):
            return MissionFail(self.ctx)

    def on_exit(self):
        self.set_user_value(triggerId=5, key='GiveBuffSlowly', value=2)


class MissionFail(common.Trigger):
    def on_enter(self):
        self.reset_timer(timerId='10000')
        self.set_portal(portalId=1, visible=False, enable=False, minimapVisible=False) # 입구 포탈
        self.set_event_ui(type=5, arg2='$02100001_BF__01_MAINMISSION__4$', arg3='3000')
        self.set_interact_object(triggerIds=[10001234], state=2) # Red
        self.set_interact_object(triggerIds=[10001235], state=2) # Blue
        self.set_interact_object(triggerIds=[10001236], state=2) # Grey
        self.set_interact_object(triggerIds=[10001237], state=2) # Green
        self.set_interact_object(triggerIds=[10001238], state=2) # Yellow

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=3000):
            return MoveToCage(self.ctx)


class MoveToCage(common.Trigger):
    def on_enter(self):
        self.move_user(mapId=2100001, portalId=10)

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=2000):
            return BadEndingStart(self.ctx)


# BadEnding 연출
class BadEndingStart(common.Trigger):
    def on_enter(self):
        self.set_cinematic_ui(type=1)
        self.set_cinematic_ui(type=3)
        self.select_camera(triggerId=901, enable=True)

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=1000):
            return BadEndingTalk01(self.ctx)


class BadEndingTalk01(common.Trigger):
    def on_enter(self):
        self.add_cinematic_talk(npcId=11003517, msg='$02100001_BF__01_MAINMISSION__5$', duration=5000, align='center', illustId='0')
        self.set_skip(state=BadEndingTalk01Skip)

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=5000):
            return BadEndingTalk01Skip(self.ctx)


class BadEndingTalk01Skip(common.Trigger):
    def on_enter(self):
        self.set_skip()
        self.remove_cinematic_talk()

    def on_tick(self) -> common.Trigger:
        if self.true():
            return BadEndingEnd(self.ctx)


class BadEndingEnd(common.Trigger):
    def on_enter(self):
        self.set_cinematic_ui(type=0)
        self.set_cinematic_ui(type=2)
        self.select_camera(triggerId=901, enable=False)

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=1000):
            return DungeonFail(self.ctx)


# 던전 실패 선언
class DungeonFail(common.Trigger):
    def on_enter(self):
        self.dungeon_fail()

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=1000):
            return BadEndingPortalOn(self.ctx)


class BadEndingPortalOn(common.Trigger):
    def on_enter(self):
        self.set_portal(portalId=2, visible=True, enable=True, minimapVisible=True) # 출구 포탈 Cage

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=1000):
            return Quit(self.ctx)


class MissionComplete(common.Trigger):
    def on_enter(self):
        self.reset_timer(timerId='10000')
        self.set_portal(portalId=1, visible=False, enable=False, minimapVisible=False) # 입구 포탈
        self.set_achievement(triggerId=9902, type='trigger', achieve='Find02100001')
        self.set_achievement(triggerId=9902, type='trigger', achieve='guildraid_clear_1') # CN 스탬프 이벤트 전용
        self.set_event_ui(type=7, arg2='$02100001_BF__01_MAINMISSION__6$', arg3='3000')
        self.set_user_value(triggerId=99, key='MissionComplete', value=1)

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=3000):
            return HappyEndingStart(self.ctx)


# HappyEnding 연출
class HappyEndingStart(common.Trigger):
    def on_enter(self):
        self.set_cinematic_ui(type=1)
        self.set_cinematic_ui(type=3)
        self.select_camera(triggerId=902, enable=True)

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=1000):
            return HappyEndingTalk01(self.ctx)


class HappyEndingTalk01(common.Trigger):
    def on_enter(self):
        self.add_cinematic_talk(npcId=11003512, msg='$02100001_BF__01_MAINMISSION__7$', duration=5000, align='center', illustId='0')
        self.set_skip(state=HappyEndingTalk01Skip)

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=5000):
            return HappyEndingTalk01Skip(self.ctx)


class HappyEndingTalk01Skip(common.Trigger):
    def on_enter(self):
        self.set_skip()
        self.remove_cinematic_talk()

    def on_tick(self) -> common.Trigger:
        if self.true():
            return HappyEndingEnd(self.ctx)


class HappyEndingEnd(common.Trigger):
    def on_enter(self):
        self.set_cinematic_ui(type=0)
        self.set_cinematic_ui(type=2)
        self.select_camera(triggerId=902, enable=False)

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=1000):
            return DungeonSuccess(self.ctx)


# 던전 클리어 선언
class DungeonSuccess(common.Trigger):
    def on_enter(self):
        self.dungeon_clear()

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=1000):
            return HappyEndingPortalOn(self.ctx)


class HappyEndingPortalOn(common.Trigger):
    def on_enter(self):
        self.set_portal(portalId=3, visible=True, enable=True, minimapVisible=True) # 출구 포탈

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=1000):
            return Quit(self.ctx)


class Quit(common.Trigger):
    pass


initial_state = Wait
