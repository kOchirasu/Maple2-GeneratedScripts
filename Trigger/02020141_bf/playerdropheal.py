""" trigger/02020141_bf/playerdropheal.xml """
import common


class 시작대기중(common.Trigger):
    def on_tick(self) -> common.Trigger:
        if self.check_user():
            return 트리거시작(self.ctx)


class 트리거시작(common.Trigger):
    def on_tick(self) -> common.Trigger:
        if self.user_detected(boxIds=[102]):
            return 드랍지점회복(self.ctx)


class 드랍지점회복(common.Trigger):
    def on_enter(self):
        self.add_buff(boxIds=[102], skillId=50000554, level=1, isPlayer=False, isSkillSet=False) # MS2TriggerBox   TriggerObjectID = 102, 이 트리거 박스 안의 플레이어에게 애디셔널 50000554(레벨1) 회복 버프 부여하기, 이 맵은 추락하면서 시작하는데 추락 대미지에 의해 죽을 수있기 때문에 시작하자마자 무조건 HP회복 버프 부여함

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=1000):
            return 트리거시작(self.ctx)


initial_state = 시작대기중
