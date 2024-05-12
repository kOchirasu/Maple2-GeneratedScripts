""" trigger/84000006_wd/84000006_wd_object.xml """
import trigger_api


# 반응 오브젝트 올리기
class Staging(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_mesh(triggerIds=[800,801,802,803,804,805,806,807,808,809,810,811,812,813,814,815,816,817,818,819,820,821,822,823,824,825,826,827,828,829,830,831,832,833,834,835,836,837,838,839,840,841,842,843,844,845,846,847], visible=True) # 경기 대기. 상호작용 off 메쉬 on
        self.set_interact_object(triggerIds=[10001442], state=2) # 난이도 조절용 1
        self.set_interact_object(triggerIds=[10001443], state=2) # 난이도 조절용 2
        self.set_interact_object(triggerIds=[10001444], state=2) # 난이도 조절용 3
        self.set_interact_object(triggerIds=[10001445], state=2) # 테스트용 1개

    def on_tick(self) -> trigger_api.Trigger:
        if self.user_value(key='Interaction', value=1):
            # 경기 준비되면 작동 시작
            return UserCount(self.ctx)


# 경기 준비 : 유저카운트
class UserCount(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.count_users(boxId=9001, minUsers='50', operator='GreaterEqual'):
            # 50인이상
            return Over50(self.ctx)
        if self.count_users(boxId=9001, minUsers='30', operator='GreaterEqual'):
            # 30인이상
            return Over30(self.ctx)
        if self.count_users(boxId=9001, minUsers='30', operator='Less'):
            # 30인미만
            return Under30(self.ctx)


# 경기 준비 : 50명 이상 유저 수에 따라 난이도 3단계 구분
class Over50(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_timer(timerId='2', seconds=60, interval=0) # 테스트 수정 가능 지점
        self.set_interact_object(triggerIds=[10001442], state=1) # 상호작용 on 메쉬 off
        self.set_interact_object(triggerIds=[10001443], state=1)
        self.set_interact_object(triggerIds=[10001444], state=1)
        self.set_interact_object(triggerIds=[10001445], state=1)
        self.set_mesh(triggerIds=[800,801,802,803,804,805,806,807,808,809,810,811,812,813,814,815,816,817,818,819,820,821,822,823,824,825,826,827,828,829,830,831,832,833,834,835,836,837,838,839,840,841,842,843,844,845,846,847], visible=False)

    def on_tick(self) -> trigger_api.Trigger:
        if self.object_interacted(interactIds=[10001442], ar2='2') and self.object_interacted(interactIds=[10001443], ar2='2') and self.object_interacted(interactIds=[10001444], ar2='2') and self.object_interacted(interactIds=[10001445], ar2='2'):
            # 종료조건: 시간경과 or 전부훔쳐먹음
            self.add_buff(boxIds=[9002], skillId=99940046, level=1, isPlayer=False, isSkillSet=True) # 달팽이 스킬셋 50인용 제공
            self.set_user_value(triggerId=1001, key='Steal', value=1) # 전투 페이즈2 이동 UV발사
            return Standby(self.ctx)
        if self.time_expired(timerId='2'):
            self.add_buff(boxIds=[9002], skillId=99940046, level=1, isPlayer=False, isSkillSet=True) # 달팽이 스킬셋 50인용 제공
            self.set_user_value(triggerId=1001, key='Steal', value=1) # 전투 페이즈2 이동 UV발사
            return Standby(self.ctx)


# 경기 준비: 30명 이상
class Over30(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_timer(timerId='2', seconds=60, interval=0) # 테스트 수정 가능 지점
        self.set_interact_object(triggerIds=[10001442], state=1)
        self.set_interact_object(triggerIds=[10001443], state=1)
        # self.set_interact_object(triggerIds=[10001444], state=1)
        # 난이도 조절로 꺼둠
        self.set_interact_object(triggerIds=[10001445], state=1) # 테스트용 1개
        self.set_mesh(triggerIds=[800,801,802,803,804,805,806,807,808,809,810,811,812,813,814,815,816,817,818,819,820,821,822,823,824,825,826,827,828,829,830,831,832,833,834,835,836,837,838,839,840,841,842,843,844,845,846,847], visible=False)

    def on_tick(self) -> trigger_api.Trigger:
        # all_of: condition name="오브젝트가반응했으면" arg1="10001444" ar2="2" /
        # all_of: 난이도 조절로 꺼둠
        # all_of: 테스트용 1개
        if self.object_interacted(interactIds=[10001442], ar2='2') and self.object_interacted(interactIds=[10001443], ar2='2') and self.object_interacted(interactIds=[10001445], ar2='2'):
            self.add_buff(boxIds=[9002], skillId=99940045, level=1, isPlayer=False, isSkillSet=True) # 달팽이 스킬셋 30Up 제공
            self.set_user_value(triggerId=1001, key='Steal', value=1) # 전투 페이즈2 이동 UV발사
            return Standby(self.ctx)
        if self.time_expired(timerId='2'):
            self.add_buff(boxIds=[9002], skillId=99940045, level=1, isPlayer=False, isSkillSet=True) # 달팽이 스킬셋 30Up 제공
            self.set_user_value(triggerId=1001, key='Steal', value=1) # 전투 페이즈2 이동 UV발사
            return Standby(self.ctx)


# 경기 준비: 30명 미만
class Under30(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_timer(timerId='2', seconds=60, interval=0) # 테스트 수정 가능 지점
        self.set_interact_object(triggerIds=[10001442], state=1)
        # self.set_interact_object(triggerIds=[10001443], state=1)
        # 난이도 조절로 꺼둠
        # self.set_interact_object(triggerIds=[10001444], state=1)
        # 난이도 조절로 꺼둠
        self.set_interact_object(triggerIds=[10001445], state=1) # 테스트용 꼬다리 1개
        self.set_mesh(triggerIds=[800,801,802,803,804,805,806,807,808,809,810,811,812,813,814,815,816,817,818,819,820,821,822,823,824,825,826,827,828,829,830,831,832,833,834,835,836,837,838,839,840,841,842,843,844,845,846,847], visible=False)

    def on_tick(self) -> trigger_api.Trigger:
        # all_of: condition name="오브젝트가반응했으면" arg1="10001443" ar2="2" /
        # all_of: 난이도 조절로 꺼둠
        # all_of: condition name="오브젝트가반응했으면" arg1="10001444" ar2="2" /
        # all_of: 난이도 조절로 꺼둠
        # all_of: 테스트용 꼬다리 1개
        if self.object_interacted(interactIds=[10001442], ar2='2') and self.object_interacted(interactIds=[10001445], ar2='2'):
            self.add_buff(boxIds=[9002], skillId=99940043, level=1, isPlayer=False, isSkillSet=True) # 달팽이 스킬셋 30Under 제공
            self.set_user_value(triggerId=1001, key='Steal', value=1) # 전투 페이즈2 이동 UV발사
            return Standby(self.ctx)
        if self.time_expired(timerId='2'):
            self.add_buff(boxIds=[9002], skillId=99940043, level=1, isPlayer=False, isSkillSet=True) # 달팽이 스킬셋 제공
            self.set_user_value(triggerId=1001, key='Steal', value=1) # 전투 페이즈2 이동 UV발사
            return Standby(self.ctx)


# 경기 종료 준비
class Standby(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.user_value(key='Interaction', value=2):
            # OFF 신호 수신
            return Interaction_Off(self.ctx)


# 경기 종료 후 상호작용 오브젝트 off
class Interaction_Off(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_mesh(triggerIds=[812,813,814,815,816,817,818,819,820,821,822,823,824,825,826,827,828,829,830,831,832,833,834,835,836,837,838,839,840,841,842,843,844,845,846,847], visible=True) # IntObj off 처리
        self.set_interact_object(triggerIds=[10001442], state=2) # 웨딩댄스스탑과 보상 수령 밸런스 유지
        self.set_interact_object(triggerIds=[10001443], state=2)
        self.set_interact_object(triggerIds=[10001444], state=2)
        self.set_interact_object(triggerIds=[10001445], state=2)


initial_state = Staging
