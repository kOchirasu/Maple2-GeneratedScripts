""" trigger/02000251_bf/trigger_01_01.xml """
from common import *
import state


class 대기(state.State):
    def on_enter(self):
        set_mesh(triggerIds=[705,706], visible=True)
        set_mesh(triggerIds=[711,712], visible=False)
        destroy_monster(spawnIds=[601,602,603,604])
        set_effect(triggerIds=[3004], visible=False)

    def on_tick(self) -> state.State:
        if count_users(boxId=201, boxId=1):
            return 몹생성()


class 몹생성(state.State):
    def on_enter(self):
        set_mesh(triggerIds=[711,712], visible=True)
        create_monster(spawnIds=[601,602,603,604], arg2=False)

    def on_tick(self) -> state.State:
        if monster_dead(boxIds=[601,602,603,604]):
            return 통과딜레이()


class 통과딜레이(state.State):
    def on_enter(self):
        set_timer(timerId='3', seconds=3)
        # <action name="이벤트UI를설정한다" arg1="7" arg2="$02000251_BF__TRIGGER_01_01__0$" arg3="3000" arg4="0" />
        set_achievement(triggerId=1000, type='trigger', achieve='goldenTower')
        # <action name="아이템을생성한다" arg1="9001" arg2="998" />
        dungeon_clear()
        set_mesh(triggerIds=[705,706], visible=False)
        set_mesh(triggerIds=[711,712], visible=False)

    def on_tick(self) -> state.State:
        if time_expired(timerId='3'):
            return 통과()


class 통과(state.State):
    def on_enter(self):
        set_effect(triggerIds=[3004], visible=True)


