""" trigger/51000001_dg/round_07_skill.xml """
import trigger_api


class 시작대기중(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_mesh(trigger_ids=[3701])
        self.set_mesh(trigger_ids=[3702])
        self.set_mesh(trigger_ids=[3703])
        self.set_mesh(trigger_ids=[3704])

    def on_tick(self) -> trigger_api.Trigger:
        if self.user_detected(box_ids=[107]):
            return 지역랜덤(self.ctx)


class 지역랜덤(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if not self.user_detected(box_ids=[107]):
            return 종료(self.ctx)
        if self.random_condition(weight=25.0):
            self.set_mesh(trigger_ids=[3701], visible=True)
            return A지역(self.ctx)
        if self.random_condition(weight=25.0):
            self.set_mesh(trigger_ids=[3702], visible=True)
            return B지역(self.ctx)
        if self.random_condition(weight=25.0):
            self.set_mesh(trigger_ids=[3703], visible=True)
            return C지역(self.ctx)
        if self.random_condition(weight=25.0):
            self.set_mesh(trigger_ids=[3704], visible=True)
            return D지역(self.ctx)


class A지역(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.user_detected(box_ids=[10701]):
            return 스킬랜덤(self.ctx)


class B지역(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.user_detected(box_ids=[10702]):
            return 스킬랜덤(self.ctx)


class C지역(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.user_detected(box_ids=[10703]):
            return 스킬랜덤(self.ctx)


class D지역(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.user_detected(box_ids=[10704]):
            return 스킬랜덤(self.ctx)


class 스킬랜덤(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_achievement(trigger_id=199, type='trigger', achieve='random_buff_box')

    def on_tick(self) -> trigger_api.Trigger:
        if not self.user_detected(box_ids=[107]):
            return 종료(self.ctx)
        """
        if self.random_condition(weight=20.0): # 소형화 사용 안함
            self.add_buff(box_ids=[199], skill_id=49179081, level=1, is_player=False, is_skill_set=False)
            return 대기시간(self.ctx)
        """
        if self.random_condition(weight=40.0):
            # 이속증가
            self.add_buff(box_ids=[199], skill_id=49179051, level=1, is_player=False, is_skill_set=False)
            return 대기시간(self.ctx)
        if self.random_condition(weight=30.0):
            # 무적 20
            self.add_buff(box_ids=[199], skill_id=70000085, level=1, is_skill_set=False)
            return 대기시간(self.ctx)
        if self.random_condition(weight=15.0):
            # 이속감소 10
            self.add_buff(box_ids=[199], skill_id=49179061, level=1, is_player=False, is_skill_set=False)
            return 대기시간(self.ctx)
        if self.random_condition(weight=15.0):
            # 혼란 10
            self.add_buff(box_ids=[199], skill_id=49179071, level=1, is_player=False, is_skill_set=False)
            return 대기시간(self.ctx)


class 대기시간(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_mesh(trigger_ids=[3701])
        self.set_mesh(trigger_ids=[3702])
        self.set_mesh(trigger_ids=[3703])
        self.set_mesh(trigger_ids=[3704])

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=20000):
            return 시작대기중(self.ctx)


class 종료(trigger_api.Trigger):
    pass


initial_state = 시작대기중
