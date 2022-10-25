""" trigger/02020097_bf/message.xml """
import common


class 시작대기중(common.Trigger):
    def on_tick(self) -> common.Trigger:
        if self.user_detected(boxIds=[10]):
            return 대기상태(self.ctx)


class 대기상태(common.Trigger):
    def on_tick(self) -> common.Trigger:
        if self.user_detected(boxIds=[12]): # 2페이즈 전투 다 끝나고 , AI_Balrog_Kritias.xml 발록에게   StairsOk2nd = 1 신호를 받으면 이 부분 실행, 2페이즈 건너띄기가 되었기 때문에 경비병 도움 메시지 출력 안함
            return 경비병도움안내(self.ctx)
        if self.user_value(key='StairsOk2nd', value=1):
            return 트리거종료(self.ctx)


class 경비병도움안내(common.Trigger):
    def on_enter(self):
        self.show_guide_summary(entityId=29200001, textId=29200001)

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=7000):
            return 트리거종료(self.ctx)

    def on_exit(self):
        self.hide_guide_summary(entityId=29200001)


class 트리거종료(common.Trigger):
    pass


initial_state = 시작대기중
