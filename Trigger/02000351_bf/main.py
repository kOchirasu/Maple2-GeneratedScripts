""" trigger/02000351_bf/main.xml """
from common import *
import state

from dungeon_common.checkusercount import *

class idle(state.State):
    def on_enter(self):
        create_monster(spawnIds=[31,32], arg2=False)
        create_monster(spawnIds=[11,12,13,14,15,16,17], arg2=False) # 기본 배치 될 몬스터 등장
        create_monster(spawnIds=[21,22,23,24,25,26,27,28,29], arg2=False) # 기본 배치 될 몬스터 등장
        set_interact_object(triggerIds=[10000818], state=0)
        set_effect(triggerIds=[9000001], visible=False)
        set_effect(triggerIds=[9000002], visible=False)
        set_effect(triggerIds=[9000003], visible=False)
        set_effect(triggerIds=[9000004], visible=False)
        set_effect(triggerIds=[9000005], visible=False)
        set_effect(triggerIds=[9000006], visible=False)
        set_effect(triggerIds=[9000007], visible=False)
        set_effect(triggerIds=[9000008], visible=False)
        set_effect(triggerIds=[9000009], visible=False)
        set_effect(triggerIds=[9000010], visible=False)
        set_mesh(triggerIds=[6007], visible=False, arg4=0, arg5=10) # 화살표 표시 안함

    def on_tick(self) -> state.State:
        if count_users(boxId=701, boxId=1):
            return CheckUserCount()


class DungeonStart(state.DungeonStart):
    def on_enter(self):
        set_cinematic_ui(type=1)
        set_cinematic_ui(type=3)
        set_skip(state=Start)
        select_camera_path(pathIds=[80001,80002], returnView=True)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=5000):
            return Start()

    def on_exit(self):
        remove_cinematic_talk() # 레터박스, 플레이어 조작 불가능 해제
        set_cinematic_ui(type=0)
        set_cinematic_ui(type=2)
        set_cinematic_ui(type=7)

state.DungeonStart = DungeonStart


class Start(state.State):
    def on_enter(self):
        set_event_ui(type=1, arg2='$02000351_BF__MAIN__0$', arg3='3000')
        select_camera_path(pathIds=[80003], returnView=True)
        set_mesh(triggerIds=[6900], visible=False, arg4=0, arg5=10)

    def on_tick(self) -> state.State:
        if count_users(boxId=702, boxId=1):
            return 관문_01_개방()


class 관문_01_개방(state.State):
    def on_enter(self):
        set_interact_object(triggerIds=[10000818], state=1)

    def on_tick(self) -> state.State:
        if count_users(boxId=703, boxId=1):
            return 관문_02_개방()


class 관문_02_개방(state.State):
    def on_enter(self):
        play_system_sound_in_box(sound='System_ShowGuideSummary_01')
        show_guide_summary(entityId=111, textId=20000080) # 스위치를 정지하세요
        set_interact_object(triggerIds=[10000819], state=1)
        set_interact_object(triggerIds=[10000820], state=1)

    def on_tick(self) -> state.State:
        if count_users(boxId=704, boxId=1):
            return 관문_03_시작()

    def on_exit(self):
        hide_guide_summary(entityId=111)


class 관문_03_시작(state.State):
    def on_enter(self):
        create_monster(spawnIds=[33], arg2=False) # 기본 배치 될 몬스터 등장

    def on_tick(self) -> state.State:
        if monster_dead(boxIds=[31,32]):
            return 관문_03_개방()


class 관문_03_개방(state.State):
    def on_enter(self):
        play_system_sound_in_box(sound='System_ShowGuideSummary_01')
        show_guide_summary(entityId=112, textId=40009) # 포탈을 타세요
        set_mesh(triggerIds=[6006], visible=False, arg4=0, arg5=10)
        set_portal(portalId=11, visible=True, enabled=True, minimapVisible=True)

    def on_exit(self):
        hide_guide_summary(entityId=112)


