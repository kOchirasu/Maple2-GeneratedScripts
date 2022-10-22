""" trigger/02010052_bf/torchlight_04.xml """
from common import *
import state


class start(state.State):
    def on_enter(self):
        set_mesh(triggerIds=[6051,6052,6053,6054,6055,6056,6057,6058,6059,6060,6061,6062,6063,6064,6065,6066], visible=False, arg3=800, arg4=100, arg5=8) # 벽 해제
        set_effect(triggerIds=[7004], visible=False) # 횃불에 불이 붙는 이펙트

    def on_tick(self) -> state.State:
        if count_users(boxId=707, boxId=1):
            return Event_04()


class Event_04(state.State):
    def on_enter(self):
        create_monster(spawnIds=[104], arg2=True) # 화로 104 생성
        show_guide_summary(entityId=200, textId=20105204) # 길이 막혔습니다. [b:화로]를 찾아보세요.
        set_effect(triggerIds=[7541], visible=True) # 얼음이 어는 소리
        set_mesh(triggerIds=[6051,6052,6053,6054,6055,6056,6057,6058,6059,6060,6061,6062,6063,6064,6065,6066], visible=True, arg3=80, arg4=100, arg5=8) # 얼음!
        move_npc(spawnId=994, patrolName='MS2PatrolData_1006') # 카나의 분신 994 (이동)
        set_conversation(type=1, spawnId=994, script='$02010052_BF__MAIN__6$', arg4=3) # 카나 말풍선 대사

    def on_tick(self) -> state.State:
        if monster_dead(boxIds=[104]):
            return burn_state()


class burn_state(state.State):
    def on_enter(self):
        set_effect(triggerIds=[7504], visible=True) # 얼음 녹는 소리
        set_mesh(triggerIds=[6051,6052,6053,6054,6055,6056,6057,6058,6059,6060,6061,6062,6063,6064,6065,6066], visible=False, arg3=800, arg4=100, arg5=8) # 벽 해제
        set_event_ui(type=1, arg2='$02010052_BF__TORCHLIGHT_04__0$', arg3='3000')
        set_effect(triggerIds=[7004], visible=True) # 횃불에 불이 붙는 이펙트
        set_timer(timerId='1', seconds=1, display=False)

    def on_tick(self) -> state.State:
        if time_expired(timerId='1'):
            return spawn_state()


class spawn_state(state.State):
    def on_enter(self):
        hide_guide_summary(entityId=200)
        set_cinematic_ui(type=1)
        set_cinematic_ui(type=3)
        select_camera(triggerId=80003, enable=True)
        set_conversation(type=2, spawnId=21800073, script='$02010052_BF__TORCHLIGHT_04__1$', arg4=2) # 카나 대사
        set_timer(timerId='2', seconds=2)
        set_skip(state=run)

    def on_tick(self) -> state.State:
        if time_expired(timerId='2'):
            return run()

    def on_exit(self):
        remove_cinematic_talk() # 레터박스, 플레이어 조작 불가능 해제
        set_cinematic_ui(type=0)
        set_cinematic_ui(type=2)
        set_cinematic_ui(type=7)
        select_camera(triggerId=80003, enable=False)


class run(state.State):
    def on_tick(self) -> state.State:
        if count_users(boxId=707, boxId=1):
            return run_01()


class run_01(state.State):
    def on_enter(self):
        show_guide_summary(entityId=200, textId=20105202) # 카나를 쫓아가세요
        set_conversation(type=1, spawnId=994, script='$02010052_BF__TORCHLIGHT_04__2$', arg4=3) # 카나 말풍선 대사
        move_npc(spawnId=994, patrolName='MS2PatrolData_1005') # 카나의 분신 994 (이동)
        create_monster(spawnIds=[501,502,503,504,505,506], arg2=True) # 카나 정령 몬스터 등장


