""" trigger/02020141_bf/interactmesh10014100.xml """
import common


class 최초시작(common.Trigger):
    def on_enter(self):
        self.set_interact_object(triggerIds=[10003154], state=2) # 3페이즈 인터렉트 오브젝트 대기,  arg2="0" 노말 상태 (툴벤치에서 상태 입력)      arg2="1" 반응가능 상태 (툴벤치에서 상태 입력)      arg2="2" 반응완료 상태 (actor일 경우 메시가 보이지 않는다.)

    def on_tick(self) -> common.Trigger:
        if self.check_user():
            return 탈것_등장대기(self.ctx)


class 탈것_등장대기(common.Trigger):
    def on_tick(self) -> common.Trigger:
        if self.random_condition(rate=3):
            return WaitTick후에결정01(self.ctx)
        if self.random_condition(rate=3):
            return WaitTick후에결정02(self.ctx)
        if self.random_condition(rate=3):
            return WaitTick후에결정03(self.ctx)


class WaitTick후에결정01(common.Trigger):
    def on_tick(self) -> common.Trigger:
        if self.user_value(key='RidingBattle', value=-1):
            return 종료(self.ctx)
        if self.wait_tick(waitTick=110000):
            return 탈것_확률결정(self.ctx)


class WaitTick후에결정02(common.Trigger):
    def on_tick(self) -> common.Trigger:
        if self.user_value(key='RidingBattle', value=-1):
            return 종료(self.ctx)
        if self.wait_tick(waitTick=135000):
            return 탈것_확률결정(self.ctx)


class WaitTick후에결정03(common.Trigger):
    def on_tick(self) -> common.Trigger:
        if self.user_value(key='RidingBattle', value=-1):
            return 종료(self.ctx)
        if self.wait_tick(waitTick=150000):
            return 탈것_확률결정(self.ctx)


class 탈것_확률결정(common.Trigger):
    def on_tick(self) -> common.Trigger:
        if self.random_condition(rate=85):
            return 탈것등장_실패(self.ctx)
        if self.random_condition(rate=15):
            return 탈것등장_성공(self.ctx)


class 탈것등장_성공(common.Trigger):
    def on_enter(self):
        self.create_monster(spawnIds=[914100], animationEffect=False) # 탑승 거대 아르케온 등장(연출용) : 리젠 애니메이션 출력

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=4000):
            return 탈것_등장(self.ctx)


class 탈것_등장(common.Trigger):
    def on_enter(self):
        self.set_event_ui(type=1, arg2='$02020141_BF__INTERACTMESH_PHASE_3_INTERECT_01__0$', arg3='5000') # 거대 로봇탈것 등장을 알리는 메시지 출력
        self.set_interact_object(triggerIds=[10003154], state=1) # arg2="0" 노말 상태 (툴벤치에서 상태 입력)      arg2="1" 반응가능 상태 (툴벤치에서 상태 입력)      arg2="2" 반응완료 상태 (actor일 경우 메시가 보이지 않는다.)
        self.destroy_monster(spawnIds=[914100]) # 탑승 거대 아르케온 등장(연출용) : 리젠 애니메이션 출력용 몬스터 리젠 애니만 나오고 바로 제거하기

    def on_tick(self) -> common.Trigger:
        if self.object_interacted(interactIds=[10003154], stateValue=0):
            return 종료(self.ctx)
        if self.user_value(key='RidingBattle', value=-1):
            return 종료(self.ctx)


class 종료(common.Trigger):
    def on_enter(self):
        self.set_interact_object(triggerIds=[10003154], state=2) # 3페이즈 인터렉트 오브젝트 대기,  arg2="0" 노말 상태 (툴벤치에서 상태 입력)      arg2="1" 반응가능 상태 (툴벤치에서 상태 입력)      arg2="2" 반응완료 상태 (actor일 경우 메시가 보이지 않는다.)


class 탈것등장_실패(common.Trigger):
    def on_enter(self):
        self.create_monster(spawnIds=[914100], animationEffect=False) # 탑승 거대 아르케온 등장(연출용) : 리젠 애니메이션 출력, 그리고 가만히 내버려 두면 AI에서 스스로 자살하면서 사라짐(AI_ArcheonMaceRegenEvent_TypeB.xml)

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=13000):
            return 탈것등장_실패_최종종료처리(self.ctx)


class 탈것등장_실패_최종종료처리(common.Trigger):
    def on_enter(self):
        self.destroy_monster(spawnIds=[914100])
        # 혹시 <action name="몬스터를생성한다" arg1="914100" arg2="0" /> 로 인해 생성한 몬스터가 주변에 적대적 몬스터가 없어서 스스로 자살 스킬 사용하지 않을 경우를 대비해, WaitTick = 13초 후에 스스로 사라지도록 설정함


initial_state = 최초시작
