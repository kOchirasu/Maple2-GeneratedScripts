""" trigger/02020142_bf/2phaseplayercheck.xml """
import common


class 시작대기중(common.Trigger):
    def on_tick(self) -> common.Trigger:
        if self.check_user():
            return 안잡힌플레이어체크(self.ctx)


class 안잡힌플레이어체크(common.Trigger):
    def on_tick(self) -> common.Trigger:
        if self.user_value(key='2PhasePlayerCheckStart', value=1):
            return 페이즈지점체크하기1(self.ctx)


class 페이즈지점체크하기1(common.Trigger):
    def on_tick(self) -> common.Trigger:
        if self.user_detected(boxIds=[98]):
            return 종료(self.ctx)
        if self.wait_tick(waitTick=900):
            return 추가로최초시작지점체크하기(self.ctx)


class 추가로최초시작지점체크하기(common.Trigger):
    def on_tick(self) -> common.Trigger:
        if self.user_detected(boxIds=[99]):
            return 종료(self.ctx)
        if self.wait_tick(waitTick=900):
            return 안잡힌플레이어없음확인(self.ctx)


class 안잡힌플레이어없음확인(common.Trigger):
    def on_enter(self):
        self.set_ai_extra_data(key='TwoPhaseMainBattle', value=1)

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=500):
            return 페이즈복격진행_안내메시지출력2(self.ctx)


class 페이즈복격진행_안내메시지출력2(common.Trigger):
    def on_enter(self):
        self.set_skill(triggerIds=[91], enable=True) # CubeBreak ,  MS2TriggerSkill = 91 스킬코드 70000105(레벨1) 발동시켜 마법구슬 지점에 계단을 막고 있는 큐브 제거함
        self.show_guide_summary(entityId=29200003, textId=29200003)

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=6500):
            return 종료(self.ctx)

    def on_exit(self):
        self.hide_guide_summary(entityId=29200003)


class 종료(common.Trigger):
    pass


initial_state = 시작대기중
