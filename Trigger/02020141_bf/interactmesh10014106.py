""" trigger/02020141_bf/interactmesh10014106.xml """
from common import *
import state


class 최초시작(state.State):
    def on_enter(self):
        set_interact_object(triggerIds=[10003151], state=2) # 3페이즈 인터렉트 오브젝트 대기,  arg2="0" 노말 상태 (툴벤치에서 상태 입력)      arg2="1" 반응가능 상태 (툴벤치에서 상태 입력)      arg2="2" 반응완료 상태 (actor일 경우 메시가 보이지 않는다.)

    def on_tick(self) -> state.State:
        if check_user():
            return 탈것_등장대기()


class 탈것_등장대기(state.State):
    def on_tick(self) -> state.State:
        if wait_tick(waitTick=1000):
            return 탈것_등장연출()


class 탈것_등장연출(state.State):
    def on_enter(self):
        create_monster(spawnIds=[914106], arg2=False) # 탑승 아르케온 등장(연출용) : 리젠 애니메이션 출력

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=4000):
            return 탈것_등장()


class 탈것_등장(state.State):
    def on_enter(self):
        set_interact_object(triggerIds=[10003151], state=1) # arg2="0" 노말 상태 (툴벤치에서 상태 입력)      arg2="1" 반응가능 상태 (툴벤치에서 상태 입력)      arg2="2" 반응완료 상태 (actor일 경우 메시가 보이지 않는다.)
        destroy_monster(spawnIds=[914106])

    def on_tick(self) -> state.State:
        if object_interacted(interactIds=[10003151], arg2=0):
            return 인터렉트_동작중()
        if user_value(key='RidingBattle', value=-1):
            return 종료()


class 인터렉트_동작중(state.State):
    def on_enter(self):
        set_interact_object(triggerIds=[10003151], state=2) # 3페이즈 인터렉트 오브젝트 대기,  arg2="0" 노말 상태 (툴벤치에서 상태 입력)      arg2="1" 반응가능 상태 (툴벤치에서 상태 입력)      arg2="2" 반응완료 상태 (actor일 경우 메시가 보이지 않는다.)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=30000):
            return 탈것_등장대기()
        if user_value(key='RidingBattle', value=-1):
            return 종료()


class 종료(state.State):
    def on_enter(self):
        set_interact_object(triggerIds=[10003151], state=2) # 3페이즈 인터렉트 오브젝트 대기,  arg2="0" 노말 상태 (툴벤치에서 상태 입력)      arg2="1" 반응가능 상태 (툴벤치에서 상태 입력)      arg2="2" 반응완료 상태 (actor일 경우 메시가 보이지 않는다.)


