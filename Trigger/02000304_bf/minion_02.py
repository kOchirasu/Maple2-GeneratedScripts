""" trigger/02000304_bf/minion_02.xml """
from common import *
import state


class 대기(state.State):
    def on_tick(self) -> state.State:
        if user_detected(boxIds=[112]):
            create_monster(spawnIds=[1003,1004], arg2=False)
            return 종료체크()
        if monster_dead(boxIds=[2001]):
            return 종료체크()


class 종료체크(state.State):
    def on_tick(self) -> state.State:
        if monster_dead(boxIds=[1003,1004]):
            return 대기시간()
        if monster_dead(boxIds=[2001]):
            destroy_monster(spawnIds=[1003,1004])
            return 대기시간()


class 대기시간(state.State):
    def on_enter(self):
        set_timer(timerId='2', seconds=2)

    def on_tick(self) -> state.State:
        if time_expired(timerId='2'):
            move_user(mapId=2000304, portalId=10, boxId=112)
            return 대기()


