""" trigger/02020300_bf/laser_01.xml """
from common import *
import state


class 레이저_01_생성(state.State):
    def on_tick(self) -> state.State:
        if user_value(key='Laser', value=1):
            create_monster(spawnIds=[902], arg2=True)
            return 레이저_01_소멸()


class 레이저_01_소멸(state.State):
    def on_tick(self) -> state.State:
        if monster_dead(boxIds=[101,102,103]):
            destroy_monster(spawnIds=[902])
            return 레이저_02_생성()


class 레이저_02_생성(state.State):
    def on_tick(self) -> state.State:
        if count_users(boxId=711, boxId=1):
            create_monster(spawnIds=[711], arg2=True)
            return 레이저_02_소멸()


class 레이저_02_소멸(state.State):
    def on_tick(self) -> state.State:
        if count_users(boxId=712, boxId=1):
            destroy_monster(spawnIds=[711])
            return 레이저_03_생성()


class 레이저_03_생성(state.State):
    def on_tick(self) -> state.State:
        if count_users(boxId=712, boxId=1):
            create_monster(spawnIds=[712], arg2=True)
            return 레이저_03_소멸()


class 레이저_03_소멸(state.State):
    def on_tick(self) -> state.State:
        if count_users(boxId=713, boxId=1):
            destroy_monster(spawnIds=[712])
            create_monster(spawnIds=[713], arg2=True)
            return 레이저_04()


class 레이저_04(state.State):
    def on_tick(self) -> state.State:
        if user_value(key='Laser', value=0):
            destroy_monster(spawnIds=[713])
            return None


