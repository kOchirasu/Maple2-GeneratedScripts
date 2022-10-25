""" trigger/02000428_bf/dropdebuff.xml """
import common


class Ready(common.Trigger):
    def on_tick(self) -> common.Trigger:
        if self.count_users(boxId=750, boxId=1):
            return 드랍어뷰징디버프_작동시작(self.ctx)


class 드랍어뷰징디버프_작동시작(common.Trigger):
    def on_tick(self) -> common.Trigger:
        if self.count_users(boxId=780, boxId=1):
            return 전투판에떨어지면디버프걸기(self.ctx)


class 전투판에떨어지면디버프걸기(common.Trigger):
    def on_enter(self):
        self.add_buff(boxIds=[780], skillId=50000512, level=1, isPlayer=False, isSkillSet=False) # MS2TriggerBox   TriggerObjectID = 780, 이 트리거 박스 안에 있는 플레이어 Sp 0 상태이상 걸리게 하기

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=300):
            return 드랍어뷰징디버프_작동시작(self.ctx)


initial_state = Ready
