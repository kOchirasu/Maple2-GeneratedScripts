""" trigger/02000336_bf/main.xml """
from common import *
import state


class 시작(state.State):
    def on_enter(self):
        set_mesh(triggerIds=[16003,16004], visible=False, arg4=0, arg5=0) # 벽 해제
        create_monster(spawnIds=[122,123,301,302], arg2=False) # 기본 배치 될 몬스터 등장
        create_monster(spawnIds=[110,111,112,113,114,116,117,120,121,124,125,126,127,128,129,131,132,133,134,135,137,139,141,142,144], arg2=False) # 기본 배치 될 몬스터 등장

    def on_tick(self) -> state.State:
        if count_users(boxId=703, boxId=1):
            return 관문_01_개방_준비()


class 관문_01_개방_준비(state.State):
    def on_enter(self):
        play_system_sound_in_box(sound='System_ShowGuideSummary_01')
        show_guide_summary(entityId=105, textId=20003361) # 키 몬스터를 처치하세요.
        create_monster(spawnIds=[309,311,313,172,173], arg2=False)

    def on_tick(self) -> state.State:
        if monster_dead(boxIds=[127]):
            return 관문_01_개방()

    def on_exit(self):
        hide_guide_summary(entityId=105)


class 관문_01_개방(state.State):
    def on_enter(self):
        play_system_sound_in_box(sound='System_ShowGuideSummary_01')
        show_guide_summary(entityId=106, textId=20003362, duration=3000) # 다음 구역으로 이동할 수 있습니다.
        set_mesh(triggerIds=[8010,8011,8012,8013,8014], visible=False, arg4=0, arg5=10) # 벽 해제
        set_timer(timerId='3', seconds=3, display=False)

    def on_tick(self) -> state.State:
        if monster_dead(boxIds=[125]):
            return 관문_02_개방()


class 관문_02_개방_준비(state.State):
    def on_tick(self) -> state.State:
        if monster_dead(boxIds=[127]):
            return 관문_01_개방()

    def on_exit(self):
        hide_guide_summary(entityId=113)


class 관문_02_개방(state.State):
    def on_enter(self):
        set_mesh(triggerIds=[16017,16018], visible=False, arg4=0, arg5=10) # 벽 해제


