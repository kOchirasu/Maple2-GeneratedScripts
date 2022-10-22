""" trigger/02010086_bf/laser_01.xml """
from common import *
import state


class 레이저_01_소멸(state.State):
    def on_tick(self) -> state.State:
        if count_users(boxId=712, boxId=1):
            return 레이저_02()

    def on_exit(self):
        destroy_monster(spawnIds=[999])


class 레이저_02(state.State):
    def on_tick(self) -> state.State:
        if count_users(boxId=707, boxId=1):
            return 레이저_02_생성()


class 레이저_02_생성(state.State):
    def on_enter(self):
        create_monster(spawnIds=[998], arg2=True) # 몬스터 등장

    def on_tick(self) -> state.State:
        if count_users(boxId=708, boxId=1):
            return 레이저_03_생성()


class 레이저_03_생성(state.State):
    def on_enter(self):
        create_monster(spawnIds=[995], arg2=True) # 몬스터 등장


