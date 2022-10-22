""" trigger/02000318_bf/mobspawn_01.xml """
from common import *
import state

from dungeon_common.checkusercount import *

class Setting(state.State):
    def on_enter(self):
        set_mesh(triggerIds=[3000], visible=True, arg3=0, arg4=0, arg5=0) # EnteranceBarrier
        set_mesh(triggerIds=[3001], visible=True, arg3=0, arg4=0, arg5=0) # 1stBarrier
        set_mesh(triggerIds=[3002], visible=True, arg3=0, arg4=0, arg5=0) # 2ndBarrier
        set_mesh(triggerIds=[3100,3101,3102,3103,3104,3105,3106,3107,3108,3109,3110,3111,3112,3113,3114,3115,3116,3117,3118,3119,3120,3121,3122,3123,3124,3125,3126,3127,3128], visible=True, arg3=0, arg4=0, arg5=0) # EnteranceBarrier
        set_user_value(key='ShipMove', value=0)

    def on_tick(self) -> state.State:
        if check_user():
            return LoadingDelay()


class LoadingDelay(state.State):
    def on_enter(self):
        create_monster(spawnIds=[301,302,303,304,305], arg2=False)
        create_monster(spawnIds=[201,202,203,204,205], arg2=False)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=1000):
            return CheckUserCount()


class DungeonStart(state.DungeonStart):
    def on_enter(self):
        play_system_sound_in_box(boxIds=[102], sound='System_ShowGuideSummary_01')
        set_cinematic_ui(type=1)
        set_cinematic_ui(type=3)
        select_camera(triggerId=600, enable=True)
        set_skip(state=CameraWalk01)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=5000):
            return CameraWalk01()

state.DungeonStart = DungeonStart


class CameraWalk01(state.State):
    def on_enter(self):
        select_camera(triggerId=600, enable=False)
        set_skip()

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=1000):
            return CameraWalk02()


class CameraWalk02(state.State):
    def on_enter(self):
        set_cinematic_ui(type=0)
        set_cinematic_ui(type=2)
        play_system_sound_in_box(boxIds=[102], sound='System_ShowGuideSummary_01')
        set_event_ui(type=1, arg2='$02000318_BF__MOBSPAWN_01__0$', arg3='3000', arg4='0')
        set_mesh(triggerIds=[3000], visible=False, arg3=0, arg4=0, arg5=0) # EnteranceBarrier
        set_random_mesh(triggerIds=[3100,3101,3102,3103,3104,3105,3106,3107,3108,3109,3110,3111,3112,3113,3114,3115,3116,3117,3118,3119,3120,3121,3122,3123,3124,3125,3126,3127,3128], visible=False, meshCount=29, arg4=500, delay=30) # EnteranceBarrier

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=5000):
            return Battle01()


class Battle01(state.State):
    def on_enter(self):
        play_system_sound_in_box(boxIds=[102], sound='System_ShowGuideSummary_01')
        show_guide_summary(entityId=20031801, textId=20031801) # 몬스터를 모두 처치하세요

    def on_tick(self) -> state.State:
        if monster_dead(boxIds=[301,302,303,304,305]):
            return Battle02()

    def on_exit(self):
        destroy_monster(spawnIds=[301,302,303,304,305])


class Battle02(state.State):
    def on_enter(self):
        create_monster(spawnIds=[111,112,113,114,115,116,501], arg2=False)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=4000):
            return Battle03()


class Battle03(state.State):
    def on_enter(self):
        hide_guide_summary(entityId=20031801)
        play_system_sound_in_box(boxIds=[102], sound='System_ShowGuideSummary_01')
        show_guide_summary(entityId=20031802, textId=20031802) # 대포를 이용해 올라갈 수 없는 지형 위의 몬스터를 처치하세요

    def on_tick(self) -> state.State:
        if monster_dead(boxIds=[111,112,113,114,115,116]):
            return MoveShip01()

    def on_exit(self):
        destroy_monster(spawnIds=[111,112,113,114,115,116,501])


class MoveShip01(state.State):
    def on_enter(self):
        hide_guide_summary(entityId=20031802)
        set_user_value(triggerId=2, key='ShipSet', value=1)
        set_mesh(triggerIds=[3001], visible=False, arg3=0, arg4=0, arg5=0) # 1stBarrier

    def on_tick(self) -> state.State:
        if user_value(key='ShipMove', value=1):
            return MoveShip02()


class MoveShip02(state.State):
    def on_tick(self) -> state.State:
        if user_detected(boxIds=[103]):
            return Battle11()


class Battle11(state.State):
    def on_enter(self):
        play_system_sound_in_box(boxIds=[102], sound='System_ShowGuideSummary_01')
        show_guide_summary(entityId=20031801, textId=20031801) # 몬스터를 모두 처치하세요

    def on_tick(self) -> state.State:
        if monster_dead(boxIds=[201,202,203,204,205]):
            return Battle12()

    def on_exit(self):
        destroy_monster(spawnIds=[201,202,203,204,205])


class Battle12(state.State):
    def on_enter(self):
        create_monster(spawnIds=[211,212,213,214,215,216,217,218,219,502,503], arg2=False)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=4000):
            return Battle13()


class Battle13(state.State):
    def on_enter(self):
        hide_guide_summary(entityId=20031801)
        play_system_sound_in_box(boxIds=[102], sound='System_ShowGuideSummary_01')
        show_guide_summary(entityId=20031802, textId=20031802) # 대포를 이용해 올라갈 수 없는 지형 위의 몬스터를 처치하세요

    def on_tick(self) -> state.State:
        if monster_dead(boxIds=[211,212,213,214,215,216,217,218,219]):
            return CannonSpawn01()

    def on_exit(self):
        destroy_monster(spawnIds=[211,212,213,214,215,216,217,218,219,502,503])


class CannonSpawn01(state.State):
    def on_enter(self):
        create_monster(spawnIds=[401], arg2=False)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=2000):
            return CannonSpawn02()


class CannonSpawn02(state.State):
    def on_enter(self):
        hide_guide_summary(entityId=20031802)
        play_system_sound_in_box(boxIds=[102], sound='System_ShowGuideSummary_01')
        show_guide_summary(entityId=20031804, textId=20031804) # 대포를 이용해 다음 지역으로 이동하세요
        set_mesh(triggerIds=[3002], visible=False, arg3=0, arg4=0, arg5=0) # 2ndBarrier

    def on_tick(self) -> state.State:
        if user_detected(boxIds=[104]):
            return Quit()


class Quit(state.State):
    def on_enter(self):
        hide_guide_summary(entityId=20031804)


