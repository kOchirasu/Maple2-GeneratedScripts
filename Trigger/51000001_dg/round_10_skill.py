""" trigger/51000001_dg/round_10_skill.xml """
import trigger_api


class 시작대기중(trigger_api.Trigger):
    def on_enter(self):
        self.set_mesh(triggerIds=[31001], visible=False, arg3=0, delay=0, scale=0)
        self.set_mesh(triggerIds=[31002], visible=False, arg3=0, delay=0, scale=0)
        self.set_mesh(triggerIds=[31003], visible=False, arg3=0, delay=0, scale=0)
        self.set_mesh(triggerIds=[31004], visible=False, arg3=0, delay=0, scale=0)
        self.set_mesh(triggerIds=[31005], visible=False, arg3=0, delay=0, scale=0)

    def on_tick(self) -> trigger_api.Trigger:
        if self.user_detected(boxIds=[110]):
            return 지역랜덤(self.ctx)


class 지역랜덤(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if not self.user_detected(boxIds=[110]):
            return 종료(self.ctx)
        if self.random_condition(rate=20):
            self.set_mesh(triggerIds=[31001], visible=True, arg3=0, delay=0, scale=0)
            return A지역(self.ctx)
        if self.random_condition(rate=20):
            self.set_mesh(triggerIds=[31002], visible=True, arg3=0, delay=0, scale=0)
            return B지역(self.ctx)
        if self.random_condition(rate=20):
            self.set_mesh(triggerIds=[31003], visible=True, arg3=0, delay=0, scale=0)
            return C지역(self.ctx)
        if self.random_condition(rate=20):
            self.set_mesh(triggerIds=[31004], visible=True, arg3=0, delay=0, scale=0)
            return D지역(self.ctx)
        if self.random_condition(rate=20):
            self.set_mesh(triggerIds=[31005], visible=True, arg3=0, delay=0, scale=0)
            return E지역(self.ctx)


class A지역(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.user_detected(boxIds=[11001]):
            return 스킬랜덤(self.ctx)


class B지역(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.user_detected(boxIds=[11002]):
            return 스킬랜덤(self.ctx)


class C지역(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.user_detected(boxIds=[11003]):
            return 스킬랜덤(self.ctx)


class D지역(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.user_detected(boxIds=[11004]):
            return 스킬랜덤(self.ctx)


class E지역(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.user_detected(boxIds=[11005]):
            return 스킬랜덤(self.ctx)


class 스킬랜덤(trigger_api.Trigger):
    def on_enter(self):
        self.set_achievement(triggerId=199, type='trigger', achieve='random_buff_box')

    def on_tick(self) -> trigger_api.Trigger:
        if not self.user_detected(boxIds=[110]):
            return 종료(self.ctx)
        if self.random_condition(rate=40):
            self.add_buff(boxIds=[199], skillId=49179051, level=1, isPlayer=False, isSkillSet=False)
            return 대기시간(self.ctx)
        """
        <condition name="랜덤조건" arg1="20">    소형화 사용 안함
                    <action name="버프를걸어준다" arg1="199" arg2="49179081" arg3="1" arg4="0" arg5="0"/>
                    <transition state="대기시간" />
                </condition>
        """
        if self.random_condition(rate=30):
            self.add_buff(boxIds=[199], skillId=70000085, level=1, isSkillSet=False)
            return 대기시간(self.ctx)
        if self.random_condition(rate=15):
            self.add_buff(boxIds=[199], skillId=49179061, level=1, isPlayer=False, isSkillSet=False)
            return 대기시간(self.ctx)
        if self.random_condition(rate=15):
            self.add_buff(boxIds=[199], skillId=49179071, level=1, isPlayer=False, isSkillSet=False)
            return 대기시간(self.ctx)


class 대기시간(trigger_api.Trigger):
    def on_enter(self):
        self.set_mesh(triggerIds=[31001], visible=False, arg3=0, delay=0, scale=0)
        self.set_mesh(triggerIds=[31002], visible=False, arg3=0, delay=0, scale=0)
        self.set_mesh(triggerIds=[31003], visible=False, arg3=0, delay=0, scale=0)
        self.set_mesh(triggerIds=[31004], visible=False, arg3=0, delay=0, scale=0)
        self.set_mesh(triggerIds=[31005], visible=False, arg3=0, delay=0, scale=0)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=30000):
            return 시작대기중(self.ctx)


class 종료(trigger_api.Trigger):
    pass


initial_state = 시작대기중
