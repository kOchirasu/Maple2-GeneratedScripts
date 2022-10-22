""" trigger/80000021_bonus/80000021_main.xml """
from common import *
import state


class 입장(state.State):
    def on_enter(self):
        set_mesh(triggerIds=[180,181,182,183,184,185,186,187,188,189,190,191,192,193,194,195,196,197,198], visible=True) # 뒷문준비 / 막힌 상태
        create_monster(spawnIds=[101,102,103,104,105], arg2=False) # 101-4: 용병 우르자들 / 105:연출용 핑크빈
        set_portal(portalId=1, visible=False, enabled=False, minimapVisible=False) # 출구포털준비 / 꺼놓은 상태

    def on_tick(self) -> state.State:
        if user_detected(boxIds=[9000]):
            return 안내()


class 안내(state.State):
    def on_enter(self):
        show_guide_summary(entityId=1, textId=26300734, duration=10)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=500):
            return 몬스터체크()


class 몬스터체크(state.State):
    def on_enter(self):
        show_guide_summary(entityId=1, textId=26300734, duration=10000) # 가이드 텍스트 ON : 슈퍼파워 핑크빈의 용병, 험상궂은 우르자들을 처치하세요!

    def on_tick(self) -> state.State:
        if monster_dead(boxIds=[101,102,103,104]):
            return 길을열어라()


class 길을열어라(state.State):
    def on_enter(self):
        set_npc_emotion_sequence(spawnId=105, sequenceName='Dead_A') # 핑크빈 빠잉
        set_portal(portalId=1, visible=True, enabled=True, minimapVisible=True) # 출구포털 / 활성화
        create_item(spawnIds=[5001]) # 초록코인

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=1500):
            return 문열기00()


class 문열기00(state.State):
    def on_enter(self):
        show_guide_summary(entityId=2, textId=26300735, duration=10000) # 가이드 텍스트 ON : 문이 열렸어요. 출구에 있는 초록 코인을 주운 후 이동하세요.
        set_mesh(triggerIds=[198], visible=False) # 뒷문 / 열기

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=800):
            return 문열기01()


class 문열기01(state.State):
    def on_enter(self):
        set_mesh(triggerIds=[180,182,184], visible=False) # 뒷문 / 열기

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=800):
            return 문열기02()


class 문열기02(state.State):
    def on_enter(self):
        set_mesh(triggerIds=[181,183,185], visible=False) # 뒷문 / 열기

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=800):
            return 문열기03()


class 문열기03(state.State):
    def on_enter(self):
        set_mesh(triggerIds=[186,188,190], visible=False) # 뒷문 / 열기

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=800):
            return 문열기04()


class 문열기04(state.State):
    def on_enter(self):
        set_mesh(triggerIds=[187,189,191], visible=False) # 뒷문 / 열기

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=800):
            return 문열기05()


class 문열기05(state.State):
    def on_enter(self):
        set_mesh(triggerIds=[192,194,196], visible=False) # 뒷문 / 열기

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=800):
            return 문열기06()


class 문열기06(state.State):
    def on_enter(self):
        set_mesh(triggerIds=[193,195,197], visible=False) # 뒷문 / 열기
        destroy_monster(spawnIds=[105]) # 핑크빈 소멸

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=1500):
            return 완료()


class 완료(state.State):
    pass


