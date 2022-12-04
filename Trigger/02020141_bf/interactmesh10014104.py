""" trigger/02020141_bf/interactmesh10014104.xml """
import trigger_api


class 최초시작(trigger_api.Trigger):
    def on_enter(self):
        self.set_interact_object(triggerIds=[10003150], state=2) # 3페이즈 인터렉트 오브젝트 대기,  arg2="0" 노말 상태 (툴벤치에서 상태 입력)      arg2="1" 반응가능 상태 (툴벤치에서 상태 입력)      arg2="2" 반응완료 상태 (actor일 경우 메시가 보이지 않는다.)

    def on_tick(self) -> trigger_api.Trigger:
        if self.check_user():
            return 탈것_등장대기(self.ctx)


class 탈것_등장대기(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=1000):
            return 탈것_등장연출(self.ctx)


class 탈것_등장연출(trigger_api.Trigger):
    def on_enter(self):
        self.create_monster(spawnIds=[14104], animationEffect=False) # 탑승 아르케온 등장(연출용) : 리젠 애니메이션 출력

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=4000):
            return 탈것_등장(self.ctx)


class 탈것_등장(trigger_api.Trigger):
    def on_enter(self):
        self.set_interact_object(triggerIds=[10003150], state=1) # arg2="0" 노말 상태 (툴벤치에서 상태 입력)      arg2="1" 반응가능 상태 (툴벤치에서 상태 입력)      arg2="2" 반응완료 상태 (actor일 경우 메시가 보이지 않는다.)
        self.destroy_monster(spawnIds=[14104])

    def on_tick(self) -> trigger_api.Trigger:
        if self.object_interacted(interactIds=[10003150], stateValue=0):
            return 인터렉트_동작중(self.ctx)
        if self.user_value(key='RidingBattle', value=-1):
            return 종료(self.ctx)


class 인터렉트_동작중(trigger_api.Trigger):
    def on_enter(self):
        self.set_interact_object(triggerIds=[10003150], state=2) # 3페이즈 인터렉트 오브젝트 대기,  arg2="0" 노말 상태 (툴벤치에서 상태 입력)      arg2="1" 반응가능 상태 (툴벤치에서 상태 입력)      arg2="2" 반응완료 상태 (actor일 경우 메시가 보이지 않는다.)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=30000):
            return 탈것_등장대기(self.ctx)
        if self.user_value(key='RidingBattle', value=-1):
            return 종료(self.ctx)


class 종료(trigger_api.Trigger):
    def on_enter(self):
        self.set_interact_object(triggerIds=[10003150], state=2) # 3페이즈 인터렉트 오브젝트 대기,  arg2="0" 노말 상태 (툴벤치에서 상태 입력)      arg2="1" 반응가능 상태 (툴벤치에서 상태 입력)      arg2="2" 반응완료 상태 (actor일 경우 메시가 보이지 않는다.)


initial_state = 최초시작
