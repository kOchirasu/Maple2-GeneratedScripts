""" trigger/99999904/main.xml """
import common


class 대기(common.Trigger):
    def on_enter(self):
        self.set_interact_object(triggerIds=[12000084], state=2)

    def on_tick(self) -> common.Trigger:
        if self.user_detected(boxIds=[902]):
            return 딜레이(self.ctx)


class 딜레이(common.Trigger):
    def on_enter(self):
        self.set_interact_object(triggerIds=[12000084], state=1)
        # <action name="이벤트UI를설정한다" arg1="1" arg2="5초 후에 인터렉트 오브젝트를 비활성화 합니다." arg3="5000"/>


class 비활성화(common.Trigger):
    def on_enter(self):
        self.set_interact_object(triggerIds=[12000084], state=2, arg3=True)


initial_state = 대기
