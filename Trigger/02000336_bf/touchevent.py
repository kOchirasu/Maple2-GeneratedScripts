""" trigger/02000336_bf/touchevent.xml """
from common import *
import state


class 시작(state.State):
    def on_tick(self) -> state.State:
        if count_users(boxId=702, boxId=1):
            return 몬스터생성()


class 몬스터생성(state.State):
    def on_enter(self):
        create_monster(spawnIds=[118,119], arg2=False) # 기본 배치 될 몬스터 등장


