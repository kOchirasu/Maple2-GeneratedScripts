""" trigger/80000014_bonus/main.xml """
from common import *
import state


class 대기(state.State):
    def on_enter(self):
        set_interact_object(triggerIds=[10001337], state=1)
        set_interact_object(triggerIds=[10001338], state=2)
        set_portal(portalId=2, visible=False, enabled=False, minimapVisible=False)
        set_mesh(triggerIds=[3000,3001], visible=True, arg3=0, arg4=0, arg5=0)
        set_mesh(triggerIds=[3002,3003,3004], visible=False, arg3=0, arg4=0, arg5=0)
        set_mesh(triggerIds=[3101,3102,3201,3202,3301,3302,3401,3402,3601,3602,3603,3604], visible=False, arg3=0, arg4=0, arg5=0)

    def on_tick(self) -> state.State:
        if user_detected(boxIds=[199]):
            return 랜덤A()


class 랜덤A(state.State):
    def on_tick(self) -> state.State:
        if random_condition(rate=50):
            set_mesh(triggerIds=[3101], visible=True, arg3=0, arg4=0, arg5=0)
            return 랜덤B()
        if random_condition(rate=50):
            set_mesh(triggerIds=[3102], visible=True, arg3=0, arg4=0, arg5=0)
            return 랜덤B()


class 랜덤B(state.State):
    def on_tick(self) -> state.State:
        if random_condition(rate=50):
            set_mesh(triggerIds=[3201], visible=True, arg3=0, arg4=0, arg5=0)
            return 랜덤C()
        if random_condition(rate=50):
            set_mesh(triggerIds=[3202], visible=True, arg3=0, arg4=0, arg5=0)
            return 랜덤C()


class 랜덤C(state.State):
    def on_tick(self) -> state.State:
        if random_condition(rate=50):
            set_mesh(triggerIds=[3301], visible=True, arg3=0, arg4=0, arg5=0)
            return 랜덤D()
        if random_condition(rate=50):
            set_mesh(triggerIds=[3302], visible=True, arg3=0, arg4=0, arg5=0)
            return 랜덤D()


class 랜덤D(state.State):
    def on_tick(self) -> state.State:
        if random_condition(rate=50):
            set_mesh(triggerIds=[3401], visible=True, arg3=0, arg4=0, arg5=0)
            return 랜덤E()
        if random_condition(rate=50):
            set_mesh(triggerIds=[3402], visible=True, arg3=0, arg4=0, arg5=0)
            return 랜덤E()


class 랜덤E(state.State):
    def on_tick(self) -> state.State:
        if random_condition(rate=50):
            set_mesh(triggerIds=[3601,3602], visible=True, arg3=0, arg4=0, arg5=0)
            return 시작()
        if random_condition(rate=50):
            set_mesh(triggerIds=[3603,3604], visible=True, arg3=0, arg4=0, arg5=0)
            return 시작()


class 시작(state.State):
    def on_enter(self):
        set_event_ui(type=1, arg2='$80000014_bonus__main__0$', arg3='5000')
        score_board_create(type='ScoreBoardTopCenter', maxScore=0)
        score_board_set_score(score=0)
        spawn_item_range(rangeIds=[9001,9002,9003,9004,9005,9006,9007,9008,9009,9010,9011,9012,9013,9014,9015,9016,9017,9018,9019], randomPickCount=10)

    def on_tick(self) -> state.State:
        if user_detected(boxIds=[102]):
            return 보스등장()


class 보스등장(state.State):
    def on_enter(self):
        spawn_npc_range(rangeIds=[2001], isAutoTargeting=False, score=1500)

    def on_tick(self) -> state.State:
        if monster_dead(boxIds=[2001]):
            return 딜레이()


class 딜레이(state.State):
    def on_enter(self):
        destroy_monster(spawnIds=[0])

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=1500):
            set_mesh(triggerIds=[3000,3001], visible=False, arg3=0, arg4=0, arg5=0)
            set_mesh(triggerIds=[3002,3003,3004], visible=True, arg3=0, arg4=0, arg5=0)
            return 정산()


class 정산(state.State):
    def on_tick(self) -> state.State:
        if score_board_compare(compareOp='GreaterEqual', score=18000):
            debug_string(value='18000 이상')
            set_achievement(triggerId=199, type='trigger', achieve='HighScoreTreasureMap01')
            set_achievement(triggerId=199, type='trigger', achieve='TimerunTreasureMap01')
            return 반응대기()
        if score_board_compare(compareOp='Less', score=18000):
            debug_string(value='18000 미만')
            set_achievement(triggerId=199, type='trigger', achieve='TimerunTreasureMap01')
            return 반응대기()
        if wait_tick(waitTick=500):
            return 반응대기()


class 반응대기(state.State):
    def on_enter(self):
        set_interact_object(triggerIds=[10001338], state=1)

    def on_tick(self) -> state.State:
        if object_interacted(interactIds=[10001338], arg2=0):
            set_achievement(triggerId=199, type='trigger', achieve='TreasureMap01')
            dungeon_clear()
            score_board_remove()
            set_portal(portalId=2, visible=True, enabled=True, minimapVisible=True)
            return 종료()


class 종료(state.State):
    pass


