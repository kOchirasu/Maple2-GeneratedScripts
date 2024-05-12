""" trigger/02000329_bf/01_main.xml """
import trigger_api

#include dungeon_common/checkusercount.py
from dungeon_common.checkusercount import *


class idle(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.create_monster(spawnIds=[701], animationEffect=False)
        self.set_effect(triggerIds=[6701], visible=True)
        self.create_monster(spawnIds=[5001,5002,1301,1302,1303,1304], animationEffect=False) # 보스 소환

    def on_tick(self) -> trigger_api.Trigger:
        if self.count_users(boxId=101, minUsers='1'):
            return CheckUserCount(self.ctx)


class DungeonStart(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_cinematic_ui(type=1)
        self.set_cinematic_ui(type=3)
        self.set_skip(state=scene_02)
        self.select_camera_path(pathIds=[80001,80002,80003,80004], returnView=True)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=3000):
            return scene_01(self.ctx)


class scene_01(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_skip(state=scene_02)
        self.set_conversation(type=1, spawnId=1301, script='$02000329_BF__01_MAIN__0$', arg4=2, arg5=0)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=3000):
            return scene_02(self.ctx)

    def on_exit(self) -> None:
        # 레터박스, 플레이어 조작 불가능 해제
        self.set_cinematic_ui(type=0)
        self.set_cinematic_ui(type=2)
        self.set_cinematic_ui(type=7)


class scene_02(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        # 레터박스, 플레이어 조작 불가능 해제
        self.set_cinematic_ui(type=0)
        self.set_cinematic_ui(type=2)
        self.set_cinematic_ui(type=7)
        self.select_camera_path(pathIds=[80005], returnView=True)
        self.set_event_ui(type=1, arg2='$02000329_BF__01_MAIN__1$', arg3='3000', arg4='0')
        self.create_monster(spawnIds=[2001,2002,2003,2004,2005], animationEffect=False)
        self.set_mesh(triggerIds=[10000,11001,11002,11003,19999], visible=False)

    def on_tick(self) -> trigger_api.Trigger:
        if self.count_users(boxId=105, minUsers='1'):
            return npc_talk(self.ctx)


class npc_talk(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_npc_emotion_sequence(spawnId=1301, sequenceName='Talk_A')
        self.play_system_sound_in_box(sound='System_ShowGuideSummary_01')
        self.show_guide_summary(entityId=101, textId=20000051, duration=5000) # 닭들을 찾아주세요
        self.set_conversation(type=1, spawnId=1301, script='$02000329_BF__01_MAIN__2$', arg4=2, arg5=0)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=3000):
            return npc_talk_02(self.ctx)


class npc_talk_02(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_npc_emotion_sequence(spawnId=1301, sequenceName='Talk_A')
        self.set_conversation(type=1, spawnId=1301, script='$02000329_BF__01_MAIN__3$', arg4=2, arg5=0)


initial_state = idle
