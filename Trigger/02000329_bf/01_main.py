""" trigger/02000329_bf/01_main.xml """
from common import *
import state

from dungeon_common.checkusercount import *

class idle(state.State):
    def on_enter(self):
        create_monster(spawnIds=[701], arg2=False)
        set_effect(triggerIds=[6701], visible=True)
        create_monster(spawnIds=[5001,5002,1301,1302,1303,1304], arg2=False) # 보스 소환

    def on_tick(self) -> state.State:
        if count_users(boxId=101, boxId=1):
            return CheckUserCount()


class DungeonStart(state.DungeonStart):
    def on_enter(self):
        set_cinematic_ui(type=1)
        set_cinematic_ui(type=3)
        set_skip(state=scene_02)
        select_camera_path(pathIds=[80001,80002,80003,80004], returnView=True)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=3000):
            return scene_01()

state.DungeonStart = DungeonStart


class scene_01(state.State):
    def on_enter(self):
        set_skip(state=scene_02)
        set_conversation(type=1, spawnId=1301, script='$02000329_BF__01_MAIN__0$', arg4=2, arg5=0)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=3000):
            return scene_02()

    def on_exit(self):
        set_cinematic_ui(type=0)
        set_cinematic_ui(type=2)
        set_cinematic_ui(type=7)


class scene_02(state.State):
    def on_enter(self):
        set_cinematic_ui(type=0)
        set_cinematic_ui(type=2)
        set_cinematic_ui(type=7)
        select_camera_path(pathIds=[80005], returnView=True)
        set_event_ui(type=1, arg2='$02000329_BF__01_MAIN__1$', arg3='3000', arg4='0')
        create_monster(spawnIds=[2001,2002,2003,2004,2005], arg2=False)
        set_mesh(triggerIds=[10000,11001,11002,11003,19999], visible=False)

    def on_tick(self) -> state.State:
        if count_users(boxId=105, boxId=1):
            return npc_talk()


class npc_talk(state.State):
    def on_enter(self):
        set_npc_emotion_sequence(spawnId=1301, sequenceName='Talk_A')
        play_system_sound_in_box(sound='System_ShowGuideSummary_01')
        show_guide_summary(entityId=101, textId=20000051, duration=5000) # 닭들을 찾아주세요
        set_conversation(type=1, spawnId=1301, script='$02000329_BF__01_MAIN__2$', arg4=2, arg5=0)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=3000):
            return npc_talk_02()


class npc_talk_02(state.State):
    def on_enter(self):
        set_npc_emotion_sequence(spawnId=1301, sequenceName='Talk_A')
        set_conversation(type=1, spawnId=1301, script='$02000329_BF__01_MAIN__3$', arg4=2, arg5=0)


