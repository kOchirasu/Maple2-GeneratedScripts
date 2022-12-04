""" trigger/02020130_bf/debuff_ishurarenduebianyuperia.xml """
import trigger_api


class Ready(trigger_api.Trigger):
    def on_enter(self):
        self.set_user_value(key='IshuraFirstSetEnd', value=0)
        self.set_user_value(key='RenduebianFirstSetEnd', value=0)
        self.set_user_value(key='YuperiaFirstSetEnd', value=0)

    def on_tick(self) -> trigger_api.Trigger:
        if self.count_users(boxId=601, boxId=1):
            return 셋트전투판스킬트리거셋팅1(self.ctx)


class 셋트전투판스킬트리거셋팅1(trigger_api.Trigger):
    def on_enter(self):
        self.set_skill(triggerIds=[1301], enable=True) # 이슈라 전투판 디버프 스킬 On으로 초기 셋팅하기
        self.set_skill(triggerIds=[1302], enable=True) # 렌듀비앙 전투판 디버프 스킬 On으로 초기 셋팅하기
        self.set_skill(triggerIds=[1303], enable=True) # 유페리아 전투판 디버프 스킬 On으로 초기 셋팅하기

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=310):
            return 셋트전투판마무리신호대기1(self.ctx)


class 셋트전투판마무리신호대기1(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.user_value(key='IshuraFirstSetEnd', value=1): # 레듀비앙 보스 AI에게 변수 신호 받을때까지 대기하기
            return 이슈라_디버프스킬끄기(self.ctx)
        if self.user_value(key='RenduebianFirstSetEnd', value=1): # 유페리아 보스 AI에게 변수 신호 받을때까지 대기하기
            return 렌듀비앙_디버프스킬끄기(self.ctx)
        if self.user_value(key='YuperiaFirstSetEnd', value=1):
            return 유페리아_디버프스킬끄기(self.ctx)


class 이슈라_디버프스킬끄기(trigger_api.Trigger):
    def on_enter(self):
        self.set_user_value(key='IshuraFirstSetEnd', value=0) # IshuraFirstSetEnd 변수 0으로 초기화
        self.set_skill(triggerIds=[1301], enable=False) # 이슈라 전투판 디버프 스킬 끄기

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=370):
            return 셋트전투판마무리신호대기1(self.ctx)


class 렌듀비앙_디버프스킬끄기(trigger_api.Trigger):
    def on_enter(self):
        self.set_user_value(key='RenduebianFirstSetEnd', value=0) # RenduebianFirstSetEnd 변수 0으로 초기화
        self.set_skill(triggerIds=[1302], enable=False) # 렌듀비앙 전투판 디버프 스킬 끄기

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=370):
            return 셋트전투판마무리신호대기1(self.ctx)


class 유페리아_디버프스킬끄기(trigger_api.Trigger):
    def on_enter(self):
        self.set_user_value(key='YuperiaFirstSetEnd', value=0) # YuperiaFirstSetEnd 변수 0으로 초기화
        self.set_skill(triggerIds=[1303], enable=False) # 유페리아 전투판 디버프 스킬 끄기

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=370):
            return 셋트전투판마무리신호대기1(self.ctx)


class 종료(trigger_api.Trigger):
    pass


initial_state = Ready
