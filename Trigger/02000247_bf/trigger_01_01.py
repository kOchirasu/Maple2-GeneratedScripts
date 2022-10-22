""" trigger/02000247_bf/trigger_01_01.xml """
from common import *
import state


class 대기(state.State):
    def on_enter(self):
        set_mesh(triggerIds=[705,706], visible=True)
        set_mesh(triggerIds=[711,712], visible=False)
        destroy_monster(spawnIds=[601,602])
        set_effect(triggerIds=[2004], visible=False)

    def on_tick(self) -> state.State:
        if count_users(boxId=201, boxId=1):
            return 몹생성()


class 몹생성(state.State):
    def on_enter(self):
        set_mesh(triggerIds=[711,712], visible=True)
        create_monster(spawnIds=[601,602], arg2=False)

    def on_tick(self) -> state.State:
        if monster_dead(boxIds=[601,602]):
            return 통과딜레이()


class 통과딜레이(state.State):
    def on_enter(self):
        set_achievement(triggerId=999, type='trigger', achieve='GoldenTower3rd')
        dungeon_clear()
        set_timer(timerId='3', seconds=3)
        set_mesh(triggerIds=[711,712], visible=False)
        set_mesh(triggerIds=[705,706], visible=False)

    def on_tick(self) -> state.State:
        if time_expired(timerId='3'):
            return 통과()


class 통과(state.State):
    def on_enter(self):
        set_effect(triggerIds=[2004], visible=True)


