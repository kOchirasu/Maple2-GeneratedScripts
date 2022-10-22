""" trigger/02010060_bf/main.xml """
from common import *
import state


class Ready(state.State):
    def on_enter(self):
        set_mesh(triggerIds=[6001], visible=False) # 몬스터는 밟을 수 있고 플레이어는 밟을 수 없는 투명벽 설정하기, 남쪽 넓게 설정
        set_mesh(triggerIds=[6002], visible=False) # 몬스터는 밟을 수 있고 플레이어는 밟을 수 없는 투명벽 설정하기, 10시쪽 끊어진 다리 지점
        set_mesh(triggerIds=[6003], visible=False) # 몬스터는 밟을 수 있고 플레이어는 밟을 수 없는 투명벽 설정하기, 2시쪽 끊어진 다리 지점

    def on_tick(self) -> state.State:
        if count_users(boxId=700, boxId=1):
            return Ready_Idle()


class Ready_Idle(state.State):
    def on_enter(self):
        set_timer(timerId='1', seconds=1, display=False)


