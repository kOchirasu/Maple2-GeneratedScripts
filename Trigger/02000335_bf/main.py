""" trigger/02000335_bf/main.xml """
from common import *
import state

from dungeon_common.checkusercount import *

class idle(state.State):
    def on_enter(self):
        set_mesh(triggerIds=[6901,6902,6903,6904,6905,6906,6907,6908], visible=False, arg4=0, arg5=10) # 벽 해제
        create_monster(spawnIds=[101,102,103,104,106,107,111,120,121,124,125,131,132,133,134,135,140,143,144,145,147,148], arg2=False) # 기본 배치 될 몬스터 등장
        create_monster(spawnIds=[201,202,203,204,205,206,207,208,209,210,211,212,213,214,215,216,217], arg2=False) # 기본 배치 될 NPC 등장
        set_effect(triggerIds=[6901], visible=False)
        set_effect(triggerIds=[6902], visible=False)
        set_effect(triggerIds=[6903], visible=False)
        set_effect(triggerIds=[6904], visible=False)
        set_effect(triggerIds=[6905], visible=False)
        set_effect(triggerIds=[6906], visible=False)
        enable_spawn_point_pc(spawnId=0, isEnable=True)
        enable_spawn_point_pc(spawnId=991, isEnable=False)
        enable_spawn_point_pc(spawnId=992, isEnable=False)

    def on_tick(self) -> state.State:
        if count_users(boxId=700, boxId=1):
            return CheckUserCount()


class DungeonStart(state.DungeonStart):
    def on_tick(self) -> state.State:
        if wait_tick(waitTick=3000):
            return 시작_02()

state.DungeonStart = DungeonStart


class 시작_02(state.State):
    def on_enter(self):
        set_cinematic_ui(type=1)
        set_cinematic_ui(type=3)
        set_skip(state=시작_03)
        set_conversation(type=1, spawnId=203, script='$02000335_BF__MAIN__0$', arg4=2, arg5=0)
        select_camera_path(pathIds=[80001,80002,80003,80004], returnView=False)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=7000):
            return 시작_03()

    def on_exit(self):
        set_cinematic_ui(type=0)
        set_cinematic_ui(type=2)
        set_cinematic_ui(type=7)


class 시작_03(state.State):
    def on_enter(self):
        reset_camera(interpolationTime=1)
        set_event_ui(type=1, arg2='$02000335_BF__MAIN__1$', arg3='3000', arg4='0')
        set_timer(timerId='3', seconds=3, display=False)

    def on_tick(self) -> state.State:
        if time_expired(timerId='3'):
            return 시작_04()

    def on_exit(self):
        set_mesh(triggerIds=[6401,6402,6403,6404], visible=False, arg4=0, arg5=10) # 벽 해제


class 시작_04(state.State):
    def on_enter(self):
        play_system_sound_in_box(sound='System_ShowGuideSummary_01')
        show_guide_summary(entityId=105, textId=20003361) # 키 몬스터를 처치하세요.

    def on_tick(self) -> state.State:
        if monster_dead(boxIds=[107]):
            return 관문_01_개방()

    def on_exit(self):
        hide_guide_summary(entityId=105)


class 관문_01_개방(state.State):
    def on_enter(self):
        play_system_sound_in_box(sound='System_ShowGuideSummary_01')
        show_guide_summary(entityId=106, textId=20003362) # 다음 구역으로 이동할 수 있습니다.
        set_mesh(triggerIds=[6101,6102,6103,6104,6105,6106,6107,6108], visible=False, arg4=0, arg5=10) # 벽 해제
        set_timer(timerId='3', seconds=3, display=False)

    def on_tick(self) -> state.State:
        if time_expired(timerId='3'):
            return 관문_01_개방_02()
        if monster_dead(boxIds=[106]):
            return 관문_02_개방()

    def on_exit(self):
        hide_guide_summary(entityId=106)


class 관문_01_개방_02(state.State):
    def on_tick(self) -> state.State:
        if monster_dead(boxIds=[106]):
            return 관문_02_개방()
        if count_users(boxId=702, boxId=1):
            return 관문_01_개방_03()


class 관문_01_개방_03(state.State):
    def on_enter(self):
        play_system_sound_in_box(sound='System_ShowGuideSummary_01')
        show_guide_summary(entityId=105, textId=20003361) # 키 몬스터를 처치하세요.

    def on_tick(self) -> state.State:
        if monster_dead(boxIds=[106]):
            return 관문_02_개방()

    def on_exit(self):
        hide_guide_summary(entityId=105)


class 관문_02_개방(state.State):
    def on_enter(self):
        enable_spawn_point_pc(spawnId=0, isEnable=False)
        enable_spawn_point_pc(spawnId=991, isEnable=True)
        play_system_sound_in_box(sound='System_ShowGuideSummary_01')
        show_guide_summary(entityId=106, textId=20003362) # 다음 구역으로 이동할 수 있습니다.
        set_mesh(triggerIds=[6111,6112,6113,6114,6115,6116,6117,6118], visible=False, arg4=0, arg5=10) # 벽 해제
        set_timer(timerId='3', seconds=3, display=False)

    def on_tick(self) -> state.State:
        if time_expired(timerId='3'):
            return 관문_02_개방_02()

    def on_exit(self):
        hide_guide_summary(entityId=106)


class 관문_02_개방_02(state.State):
    pass


