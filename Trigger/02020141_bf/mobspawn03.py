""" trigger/02020141_bf/mobspawn03.xml """
from common import *
import state


class 시작대기중(state.State):
    def on_tick(self) -> state.State:
        if check_user():
            return 보스등장때까지잠시대기()


class 보스등장때까지잠시대기(state.State):
    def on_tick(self) -> state.State:
        if wait_tick(waitTick=7000):
            return 트리거영역체크시작()


class 트리거영역체크시작(state.State):
    def on_tick(self) -> state.State:
        if user_value(key='MobSpawnStop', value=4):
            return 졸몬스터제거작업()
        if monster_dead(boxIds=[99]): # ##  보스가 죽으면 졸몹 등장 트리거 종료시키기 ##
            return 졸몬스터제거작업()
        if user_detected(boxIds=[10300]):
            return 졸몬스터등장대기중()


class 졸몬스터등장대기중(state.State):
    def on_tick(self) -> state.State:
        if wait_tick(waitTick=2000):
            return 트리거영역안플레이어최종체크()


class 트리거영역안플레이어최종체크(state.State):
    def on_tick(self) -> state.State:
        if user_value(key='MobSpawnStop', value=4):
            return 졸몬스터제거작업()
        if monster_dead(boxIds=[99]): # ##  보스가 죽으면 졸몹 등장 트리거 종료시키기 ##
            return 졸몬스터제거작업()
        if user_detected(boxIds=[10300]): # waitTick 후에도 플레이어가 트리거 박스 안에서 벗어났으면, 다시 처음단계로 돌아가기
            return 졸몬스터등장하기()
        if wait_tick(waitTick=500):
            return 트리거영역체크시작()


class 졸몬스터등장하기(state.State):
    def on_enter(self):
        create_monster(spawnIds=[10301,10302,10303,10304], arg2=False)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=2000):
            return 트리거영역에계속있는지체크()


class 트리거영역에계속있는지체크(state.State):
    def on_tick(self) -> state.State:
        if user_value(key='MobSpawnStop', value=4):
            return 졸몬스터제거작업()
        if monster_dead(boxIds=[99]): # ##  보스가 죽으면 졸몹 등장 트리거 종료시키기 ##
            return 졸몬스터제거작업()
        if user_detected(boxIds=[10300]):
            return 졸몬스터리젠단계시작()
        if not user_detected(boxIds=[10300]):
            return 졸몬스터제거작동대기()


class 졸몬스터리젠단계시작(state.State):
    def on_tick(self) -> state.State:
        if user_detected(boxIds=[10300]):
            return 졸몬스터리젠대기중()
        if not user_detected(boxIds=[10300]):
            return 졸몬스터제거작동대기()


class 졸몬스터리젠대기중(state.State):
    def on_tick(self) -> state.State:
        if user_value(key='MobSpawnStop', value=4):
            return 졸몬스터제거작업()
        if monster_dead(boxIds=[99]): # ##  보스가 죽으면 졸몹 등장 트리거 종료시키기 ##
            return 졸몬스터제거작업()
        if not user_detected(boxIds=[10300]):
            return 졸몬스터제거작동대기()
        if wait_tick(waitTick=15000):
            return 졸몬스터리젠YesNo()


class 졸몬스터리젠YesNo(state.State):
    def on_tick(self) -> state.State:
        if user_value(key='MobSpawnStop', value=4):
            return 졸몬스터제거작업()
        if monster_dead(boxIds=[99]): # ##  보스가 죽으면 졸몹 등장 트리거 종료시키기 ##
            return 졸몬스터제거작업()
        if user_detected(boxIds=[10300]):
            return 졸몬스터등장하기()
        if not user_detected(boxIds=[10300]):
            return 졸몬스터제거작동대기()


class 졸몬스터제거작동대기(state.State):
    def on_tick(self) -> state.State:
        if user_detected(boxIds=[10300]):
            return 트리거영역에계속있는지체크()
        if wait_tick(waitTick=7000):
            return 졸몬스터제거작업()


class 졸몬스터제거작업(state.State):
    def on_enter(self):
        destroy_monster(spawnIds=[10301,10302,10303,10304])

    def on_tick(self) -> state.State:
        if user_value(key='MobSpawnStop', value=4):
            return 종료()
        if monster_dead(boxIds=[99]): # ##  보스가 죽으면 졸몹 등장 트리거 종료시키기 ##
            return 종료()
        if wait_tick(waitTick=2000):
            return 트리거영역체크시작()


class 종료(state.State):
    pass


