""" trigger/84000006_wd/84000006_wd_object.xml """
from common import *
import state


# 반응 오브젝트 올리기
class Staging(state.State):
    def on_enter(self):
        set_mesh(triggerIds=[800,801,802,803,804,805,806,807,808,809,810,811,812,813,814,815,816,817,818,819,820,821,822,823,824,825,826,827,828,829,830,831,832,833,834,835,836,837,838,839,840,841,842,843,844,845,846,847], visible=True) # 경기 대기. 상호작용 off 메쉬 on
        set_interact_object(triggerIds=[10001442], state=2) # 난이도 조절용 1
        set_interact_object(triggerIds=[10001443], state=2) # 난이도 조절용 2
        set_interact_object(triggerIds=[10001444], state=2) # 난이도 조절용 3
        set_interact_object(triggerIds=[10001445], state=2) # 테스트용 1개

    def on_tick(self) -> state.State:
        if user_value(key='Interaction', value=1):
            return UserCount()


# 경기 준비 : 유저카운트
class UserCount(state.State):
    def on_tick(self) -> state.State:
        if count_users(boxId=9001, boxId=50, operator='GreaterEqual'):
            return Over50()
        if count_users(boxId=9001, boxId=30, operator='GreaterEqual'):
            return Over30()
        if count_users(boxId=9001, boxId=30, operator='Less'):
            return Under30()


# 경기 준비 : 50명 이상 유저 수에 따라 난이도 3단계 구분
class Over50(state.State):
    def on_enter(self):
        set_timer(timerId='2', seconds=60, display=False) # 테스트 수정 가능 지점
        set_interact_object(triggerIds=[10001442], state=1) # 상호작용 on 메쉬 off
        set_interact_object(triggerIds=[10001443], state=1)
        set_interact_object(triggerIds=[10001444], state=1)
        set_interact_object(triggerIds=[10001445], state=1)
        set_mesh(triggerIds=[800,801,802,803,804,805,806,807,808,809,810,811,812,813,814,815,816,817,818,819,820,821,822,823,824,825,826,827,828,829,830,831,832,833,834,835,836,837,838,839,840,841,842,843,844,845,846,847], visible=False)

    def on_tick(self) -> state.State:
        if all_of():
            add_buff(boxIds=[9002], skillId=99940046, level=1, arg4=False, arg5=True)
            set_user_value(triggerId=1001, key='Steal', value=1)
            return Standby()
        if time_expired(timerId='2'):
            add_buff(boxIds=[9002], skillId=99940046, level=1, arg4=False, arg5=True)
            set_user_value(triggerId=1001, key='Steal', value=1)
            return Standby()


# 경기 준비: 30명 이상
class Over30(state.State):
    def on_enter(self):
        set_timer(timerId='2', seconds=60, display=False) # 테스트 수정 가능 지점
        set_interact_object(triggerIds=[10001442], state=1)
        set_interact_object(triggerIds=[10001443], state=1) # action name="오브젝트반응설정한다" arg1="10001444" arg2="1"/
        set_interact_object(triggerIds=[10001445], state=1) # 테스트용 1개
        set_mesh(triggerIds=[800,801,802,803,804,805,806,807,808,809,810,811,812,813,814,815,816,817,818,819,820,821,822,823,824,825,826,827,828,829,830,831,832,833,834,835,836,837,838,839,840,841,842,843,844,845,846,847], visible=False)

    def on_tick(self) -> state.State:
        if all_of():
            add_buff(boxIds=[9002], skillId=99940045, level=1, arg4=False, arg5=True)
            set_user_value(triggerId=1001, key='Steal', value=1)
            return Standby()
        if time_expired(timerId='2'):
            add_buff(boxIds=[9002], skillId=99940045, level=1, arg4=False, arg5=True)
            set_user_value(triggerId=1001, key='Steal', value=1)
            return Standby()


# 경기 준비: 30명 미만
class Under30(state.State):
    def on_enter(self):
        set_timer(timerId='2', seconds=60, display=False) # 테스트 수정 가능 지점
        set_interact_object(triggerIds=[10001442], state=1) # action name="오브젝트반응설정한다" arg1="10001443" arg2="1"/
        set_interact_object(triggerIds=[10001445], state=1) # 테스트용 꼬다리 1개
        set_mesh(triggerIds=[800,801,802,803,804,805,806,807,808,809,810,811,812,813,814,815,816,817,818,819,820,821,822,823,824,825,826,827,828,829,830,831,832,833,834,835,836,837,838,839,840,841,842,843,844,845,846,847], visible=False)

    def on_tick(self) -> state.State:
        if all_of():
            add_buff(boxIds=[9002], skillId=99940043, level=1, arg4=False, arg5=True)
            set_user_value(triggerId=1001, key='Steal', value=1)
            return Standby()
        if time_expired(timerId='2'):
            add_buff(boxIds=[9002], skillId=99940043, level=1, arg4=False, arg5=True)
            set_user_value(triggerId=1001, key='Steal', value=1)
            return Standby()


# 경기 종료 준비
class Standby(state.State):
    def on_tick(self) -> state.State:
        if user_value(key='Interaction', value=2):
            return Interaction_Off()


# 경기 종료 후 상호작용 오브젝트 off
class Interaction_Off(state.State):
    def on_enter(self):
        set_mesh(triggerIds=[812,813,814,815,816,817,818,819,820,821,822,823,824,825,826,827,828,829,830,831,832,833,834,835,836,837,838,839,840,841,842,843,844,845,846,847], visible=True) # IntObj off 처리
        set_interact_object(triggerIds=[10001442], state=2) # 웨딩댄스스탑과 보상 수령 밸런스 유지
        set_interact_object(triggerIds=[10001443], state=2)
        set_interact_object(triggerIds=[10001444], state=2)
        set_interact_object(triggerIds=[10001445], state=2)


