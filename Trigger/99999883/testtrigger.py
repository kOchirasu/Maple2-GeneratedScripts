""" trigger/99999883/testtrigger.xml """
from common import *
import state


class 시작대기중(state.State):
    def on_enter(self):
        show_guide_summary(entityId=20000661, textId=20000661, duration=3000)

    def on_tick(self) -> state.State:
        if detect_liftable_object(boxIds=[100], itemId=0):
            return 보상테스트07()
        if user_value(key='TimeEvent', value=1):
            return 경험치구슬01()


#  Test State 
class 경험치구슬01(state.State):
    def on_enter(self):
        create_item(spawnIds=[1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16])
        debug_string(string='변수를 설정한다')
        set_user_value(key='TimeEvent', value=0)
        set_user_value(triggerId=2, key='test', value=1)
        give_exp(boxId=100, amount=36)

    def on_tick(self) -> state.State:
        if wait_seconds_user_value(key='TimeEventLifeTime', desc='타임이벤트로 유지시간을 받아 끝나면 다시 돌아갑니다.'):
            return 컷씬종료()


class 업적이벤트02(state.State):
    def on_enter(self):
        set_achievement(achieve='oxquiz_win')
        debug_string(string='업적이벤트테스트')

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=10000):
            return 컷씬종료()


class 컷씬03(state.State):
    def on_enter(self):
        set_cinematic_intro(text='텍스트 안녕하세요 한줄 \n두줄 테스트 입니다.')
        debug_string(string='컷씬테스트')

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=10000):
            return 컷씬종료()


class 그림자원정대게이지04(state.State):
    def on_enter(self):
        shadow_expedition(type='OpenBossGauge', title='$02000401_BF__MADRICANSIEGE_Gauge$', maxGaugePoint=1000)
        debug_string(string='그림자원정대게이지테스트')

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=10000):
            return 컷씬종료()


class PC이동테스트05(state.State):
    def on_enter(self):
        move_user_to_pos(pos=[907,758,151], rot=[0,0,315])
        move_npc_to_pos(spawnId=101, pos=[702,767,151], rot=[0,0,45])
        debug_string(string='05PC NPC이동테스트')

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=10000):
            return 컷씬종료()


class 요일테스트06(state.State):
    def on_enter(self):
        debug_string(string='06_요일테스트')

    def on_tick(self) -> state.State:
        if day_of_week(dayOfWeeks=[5], desc='1(일)-7(토)'):
            return 컷씬03()


class 보상테스트07(state.State):
    def on_enter(self):
        debug_string(string='07_보상테스트')
        give_reward_content(rewardId=31000003)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=10000):
            return 시작대기중()


#  End State 
class 컷씬종료(state.State):
    def on_enter(self):
        close_cinematic()

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=1000):
            return 시작대기중()


