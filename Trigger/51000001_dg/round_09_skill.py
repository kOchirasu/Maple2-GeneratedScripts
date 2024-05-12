""" trigger/51000001_dg/round_09_skill.xml """
import trigger_api


class 시작대기중(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_mesh(trigger_ids=[3901], visible=False, start_delay=0, interval=0, fade=0)
        self.set_mesh(trigger_ids=[3902], visible=False, start_delay=0, interval=0, fade=0)
        self.set_mesh(trigger_ids=[3903], visible=False, start_delay=0, interval=0, fade=0)
        self.set_mesh(trigger_ids=[3904], visible=False, start_delay=0, interval=0, fade=0)
        self.set_mesh(trigger_ids=[3905], visible=False, start_delay=0, interval=0, fade=0)

    def on_tick(self) -> trigger_api.Trigger:
        if self.user_detected(box_ids=[109]):
            return 지역랜덤(self.ctx)


class 지역랜덤(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if not self.user_detected(box_ids=[109]):
            return 종료(self.ctx)
        if self.random_condition(weight=20):
            self.set_mesh(trigger_ids=[3901], visible=True, start_delay=0, interval=0, fade=0)
            return A지역(self.ctx)
        if self.random_condition(weight=20):
            self.set_mesh(trigger_ids=[3902], visible=True, start_delay=0, interval=0, fade=0)
            return B지역(self.ctx)
        if self.random_condition(weight=20):
            self.set_mesh(trigger_ids=[3903], visible=True, start_delay=0, interval=0, fade=0)
            return C지역(self.ctx)
        if self.random_condition(weight=20):
            self.set_mesh(trigger_ids=[3904], visible=True, start_delay=0, interval=0, fade=0)
            return D지역(self.ctx)
        if self.random_condition(weight=20):
            self.set_mesh(trigger_ids=[3905], visible=True, start_delay=0, interval=0, fade=0)
            return E지역(self.ctx)


class A지역(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.user_detected(box_ids=[10901]):
            return 스킬랜덤(self.ctx)


class B지역(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.user_detected(box_ids=[10902]):
            return 스킬랜덤(self.ctx)


class C지역(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.user_detected(box_ids=[10903]):
            return 스킬랜덤(self.ctx)


class D지역(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.user_detected(box_ids=[10904]):
            return 스킬랜덤(self.ctx)


class E지역(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.user_detected(box_ids=[10905]):
            return 스킬랜덤(self.ctx)


class 스킬랜덤(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_achievement(trigger_id=199, type='trigger', achieve='random_buff_box')

    def on_tick(self) -> trigger_api.Trigger:
        if not self.user_detected(box_ids=[109]):
            return 종료(self.ctx)
        """
        if self.random_condition(weight=20): # 소형화 사용 안함
            self.add_buff(box_ids=[199], skill_id=49179081, level=1, is_player=False, is_skill_set=False)
            return 대기시간(self.ctx)
        """
        if self.random_condition(weight=40):
            # 이속증가
            self.add_buff(box_ids=[199], skill_id=49179051, level=1, is_player=False, is_skill_set=False)
            return 대기시간(self.ctx)
        if self.random_condition(weight=30):
            # 무적 20
            self.add_buff(box_ids=[199], skill_id=70000085, level=1, is_skill_set=False)
            return 대기시간(self.ctx)
        if self.random_condition(weight=15):
            # 이속감소 10
            self.add_buff(box_ids=[199], skill_id=49179061, level=1, is_player=False, is_skill_set=False)
            return 대기시간(self.ctx)
        if self.random_condition(weight=15):
            # 혼란 10
            self.add_buff(box_ids=[199], skill_id=49179071, level=1, is_player=False, is_skill_set=False)
            return 대기시간(self.ctx)


class 대기시간(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_mesh(trigger_ids=[3901], visible=False, start_delay=0, interval=0, fade=0)
        self.set_mesh(trigger_ids=[3902], visible=False, start_delay=0, interval=0, fade=0)
        self.set_mesh(trigger_ids=[3903], visible=False, start_delay=0, interval=0, fade=0)
        self.set_mesh(trigger_ids=[3904], visible=False, start_delay=0, interval=0, fade=0)
        self.set_mesh(trigger_ids=[3905], visible=False, start_delay=0, interval=0, fade=0)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=20000):
            return 시작대기중(self.ctx)


class 종료(trigger_api.Trigger):
    pass


initial_state = 시작대기중
