""" trigger/66000001_gd/massive01.xml """
from common import *
import state


# 파이널서바이버
class 대기(state.State):
    def on_tick(self) -> state.State:
        if user_detected(boxIds=[301]):
            return 퍼즐대기중()


class 퍼즐대기중(state.State):
    def on_enter(self):
        set_mesh(triggerIds=[201,202,203,204,205,206,207,208,209,210,211], visible=True)
        set_actor(triggerId=251, visible=True, initialSequence='Eff_MassiveEvent_Stair_Opened')
        set_actor(triggerId=252, visible=True, initialSequence='Eff_MassiveEvent_Stair_Opened')
        set_actor(triggerId=253, visible=True, initialSequence='Eff_MassiveEvent_Stair_Opened')
        set_actor(triggerId=254, visible=True, initialSequence='Eff_MassiveEvent_Stair_Opened')
        set_actor(triggerId=255, visible=True, initialSequence='Eff_MassiveEvent_Stair_Opened')
        set_actor(triggerId=256, visible=True, initialSequence='Eff_MassiveEvent_Stair_Opened')
        set_actor(triggerId=257, visible=True, initialSequence='Eff_MassiveEvent_Stair_Opened')
        set_actor(triggerId=258, visible=True, initialSequence='Eff_MassiveEvent_Stair_Opened')
        set_actor(triggerId=259, visible=True, initialSequence='Eff_MassiveEvent_Stair_Opened')
        set_actor(triggerId=260, visible=True, initialSequence='Eff_MassiveEvent_Stair_Opened')
        set_actor(triggerId=261, visible=True, initialSequence='Eff_MassiveEvent_Door_Opened')
        set_mesh(triggerIds=[1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36,37,38,39,40,41,42,43,44,45,46,47,48,49,50,51,52,53,54,55,56,57,58,59,60,61,62,63,64,65,66,67,68,69,70,71,72,73,74,75,76,77,78,79,80,81,82,83,84,85,86,87,88,89,90,91,92,93,94,95,96,97,98,99,100], visible=True)
        set_portal(portalId=777, visible=False, enabled=True, minimapVisible=False)
        set_portal(portalId=778, visible=True, enabled=True, minimapVisible=True)
        set_portal(portalId=779, visible=True, enabled=True, minimapVisible=True)

    def on_tick(self) -> state.State:
        if count_users(boxId=301, boxId=50):
            return 계단없애기()
        if wait_tick(waitTick=30000):
            return 계단없애기()

    def on_exit(self):
        set_actor(triggerId=261, visible=True, initialSequence='Eff_MassiveEvent_Door_Vanished')
        set_portal(portalId=777, visible=False, enabled=False, minimapVisible=False)


class 계단없애기(state.State):
    def on_enter(self):
        set_mini_game_area_for_hack(boxId=301) # 해킹 보안용 시작 box 설정
        set_timer(timerId='1', seconds=1)

    def on_tick(self) -> state.State:
        if time_expired(timerId='1'):
            return 계단없애기2()

    def on_exit(self):
        set_mesh(triggerIds=[206,207,208,209,210,211], visible=False)
        set_actor(triggerId=256, visible=True, initialSequence='Eff_MassiveEvent_Stair_Closed')
        set_actor(triggerId=257, visible=True, initialSequence='Eff_MassiveEvent_Stair_Closed')
        set_actor(triggerId=258, visible=True, initialSequence='Eff_MassiveEvent_Stair_Closed')
        set_actor(triggerId=259, visible=True, initialSequence='Eff_MassiveEvent_Stair_Closed')
        set_actor(triggerId=260, visible=True, initialSequence='Eff_MassiveEvent_Stair_Closed')
        set_actor(triggerId=261, visible=False, initialSequence='Eff_MassiveEvent_Door_Vanished')
        reset_timer(timerId='1')


class 계단없애기2(state.State):
    def on_enter(self):
        set_timer(timerId='1', seconds=1)

    def on_tick(self) -> state.State:
        if time_expired(timerId='1'):
            return 시작대기()

    def on_exit(self):
        set_mesh(triggerIds=[201,202,203,204,205], visible=False)
        set_actor(triggerId=251, visible=True, initialSequence='Eff_MassiveEvent_Stair_Closed')
        set_actor(triggerId=252, visible=True, initialSequence='Eff_MassiveEvent_Stair_Closed')
        set_actor(triggerId=253, visible=True, initialSequence='Eff_MassiveEvent_Stair_Closed')
        set_actor(triggerId=254, visible=True, initialSequence='Eff_MassiveEvent_Stair_Closed')
        set_actor(triggerId=255, visible=True, initialSequence='Eff_MassiveEvent_Stair_Closed')
        set_actor(triggerId=256, visible=False, initialSequence='Eff_MassiveEvent_Stair_Closed')
        set_actor(triggerId=257, visible=False, initialSequence='Eff_MassiveEvent_Stair_Closed')
        set_actor(triggerId=258, visible=False, initialSequence='Eff_MassiveEvent_Stair_Closed')
        set_actor(triggerId=259, visible=False, initialSequence='Eff_MassiveEvent_Stair_Closed')
        set_actor(triggerId=260, visible=False, initialSequence='Eff_MassiveEvent_Stair_Closed')
        reset_timer(timerId='1')


class 시작대기(state.State):
    def on_enter(self):
        set_timer(timerId='1', seconds=5)

    def on_tick(self) -> state.State:
        if time_expired(timerId='1'):
            return 멘트0()

    def on_exit(self):
        reset_timer(timerId='1')


class 멘트0(state.State):
    def on_enter(self):
        set_timer(timerId='1', seconds=5)
        set_event_ui(type=1, arg2='$61000002_ME_002__MASSIVE01__0$', arg3='6000') # 로그에서 해당 이벤트에 참여한 사람을 체크하기 위한 명령어 / 1=미니게임 이름, 2=타겟박스 id

    def on_tick(self) -> state.State:
        if time_expired(timerId='1'):
            return 멘트1()

    def on_exit(self):
        reset_timer(timerId='1')


class 멘트1(state.State):
    def on_enter(self):
        set_timer(timerId='1', seconds=4)
        set_event_ui(type=1, arg2='$66000001_GD__MASSIVE01__0$', arg3='4000')

    def on_tick(self) -> state.State:
        if time_expired(timerId='1'):
            return 멘트2()

    def on_exit(self):
        reset_timer(timerId='1')


class 멘트2(state.State):
    def on_enter(self):
        set_timer(timerId='1', seconds=5)
        set_event_ui(type=1, arg2='$61000002_ME_002__MASSIVE01__2$', arg3='6000')

    def on_tick(self) -> state.State:
        if time_expired(timerId='1'):
            return 멘트3()

    def on_exit(self):
        reset_timer(timerId='1')


class 멘트3(state.State):
    def on_enter(self):
        set_timer(timerId='1', seconds=6)
        set_event_ui(type=0, arg2='1,4')
        show_count_ui(text='$61000002_ME_002__MASSIVE01__3$', stage=1, count=5)

    def on_tick(self) -> state.State:
        if time_expired(timerId='1'):
            return 퍼즐단계1대기()

    def on_exit(self):
        reset_timer(timerId='1')


class 퍼즐단계1대기(state.State):
    def on_enter(self):
        set_timer(timerId='1', seconds=2)

    def on_tick(self) -> state.State:
        if time_expired(timerId='1'):
            return 퍼즐단계1()

    def on_exit(self):
        reset_timer(timerId='1')


class 퍼즐단계1(state.State):
    def on_enter(self):
        set_timer(timerId='1', seconds=40)
        set_random_mesh(triggerIds=[1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36,37,38,39,40,41,42,43,44,45,46,47,48,49,50,51,52,53,54,55,56,57,58,59,60,61,62,63,64,65,66,67,68,69,70,71,72,73,74,75,76,77,78,79,80,81,82,83,84,85,86,87,88,89,90,91,92,93,94,95,96,97,98,99,100], visible=False, meshCount=20, arg4=0, delay=2000)

    def on_tick(self) -> state.State:
        if time_expired(timerId='1'):
            return 퍼즐단계1정리()

    def on_exit(self):
        reset_timer(timerId='1')


class 퍼즐단계1정리(state.State):
    def on_enter(self):
        set_timer(timerId='1', seconds=3)

    def on_tick(self) -> state.State:
        if time_expired(timerId='1'):
            return 퍼즐단계1정리2()

    def on_exit(self):
        reset_timer(timerId='1')


class 퍼즐단계1정리2(state.State):
    def on_tick(self) -> state.State:
        if user_detected(boxIds=[301]):
            set_event_ui(type=0, arg2='2,4')
            show_count_ui(text='$61000002_ME_002__MASSIVE01__4$', stage=2, count=5)
            return 퍼즐단계2대기()
        if not user_detected(boxIds=[301]):
            return 실패()


class 퍼즐단계2대기(state.State):
    def on_enter(self):
        set_timer(timerId='1', seconds=6)

    def on_tick(self) -> state.State:
        if time_expired(timerId='1'):
            return 퍼즐단계2()

    def on_exit(self):
        reset_timer(timerId='1')


class 퍼즐단계2(state.State):
    def on_enter(self):
        set_timer(timerId='1', seconds=30)
        set_random_mesh(triggerIds=[1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36,37,38,39,40,41,42,43,44,45,46,47,48,49,50,51,52,53,54,55,56,57,58,59,60,61,62,63,64,65,66,67,68,69,70,71,72,73,74,75,76,77,78,79,80,81,82,83,84,85,86,87,88,89,90,91,92,93,94,95,96,97,98,99,100], visible=False, meshCount=30, arg4=0, delay=1000)

    def on_tick(self) -> state.State:
        if time_expired(timerId='1'):
            return 퍼즐단계2정리()

    def on_exit(self):
        reset_timer(timerId='1')


class 퍼즐단계2정리(state.State):
    def on_enter(self):
        set_timer(timerId='1', seconds=3)

    def on_tick(self) -> state.State:
        if time_expired(timerId='1'):
            return 퍼즐단계2정리2()

    def on_exit(self):
        reset_timer(timerId='1')


class 퍼즐단계2정리2(state.State):
    def on_tick(self) -> state.State:
        if user_detected(boxIds=[301]):
            set_event_ui(type=0, arg2='3,4')
            show_count_ui(text='$61000002_ME_002__MASSIVE01__5$', stage=3, count=5)
            return 퍼즐단계3대기()
        if not user_detected(boxIds=[301]):
            return 실패()


class 퍼즐단계3대기(state.State):
    def on_enter(self):
        set_timer(timerId='1', seconds=6)

    def on_tick(self) -> state.State:
        if time_expired(timerId='1'):
            return 퍼즐단계3()

    def on_exit(self):
        reset_timer(timerId='1')


class 퍼즐단계3(state.State):
    def on_enter(self):
        set_timer(timerId='1', seconds=15)
        set_random_mesh(triggerIds=[1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36,37,38,39,40,41,42,43,44,45,46,47,48,49,50,51,52,53,54,55,56,57,58,59,60,61,62,63,64,65,66,67,68,69,70,71,72,73,74,75,76,77,78,79,80,81,82,83,84,85,86,87,88,89,90,91,92,93,94,95,96,97,98,99,100], visible=False, meshCount=30, arg4=0, delay=500)

    def on_tick(self) -> state.State:
        if time_expired(timerId='1'):
            return 퍼즐단계3정리()

    def on_exit(self):
        reset_timer(timerId='1')


class 퍼즐단계3정리(state.State):
    def on_enter(self):
        set_timer(timerId='1', seconds=3)

    def on_tick(self) -> state.State:
        if time_expired(timerId='1'):
            return 퍼즐단계3정리2()

    def on_exit(self):
        reset_timer(timerId='1')


class 퍼즐단계3정리2(state.State):
    def on_tick(self) -> state.State:
        if user_detected(boxIds=[301]):
            set_event_ui(type=0, arg2='4,4')
            show_count_ui(text='$61000002_ME_002__MASSIVE01__6$', stage=4, count=5)
            return 퍼즐단계4대기()
        if not user_detected(boxIds=[301]):
            return 실패()


class 퍼즐단계4대기(state.State):
    def on_enter(self):
        set_timer(timerId='1', seconds=6)

    def on_tick(self) -> state.State:
        if time_expired(timerId='1'):
            return 퍼즐단계4()

    def on_exit(self):
        reset_timer(timerId='1')


class 퍼즐단계4(state.State):
    def on_enter(self):
        set_timer(timerId='1', seconds=5)
        set_random_mesh(triggerIds=[1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36,37,38,39,40,41,42,43,44,45,46,47,48,49,50,51,52,53,54,55,56,57,58,59,60,61,62,63,64,65,66,67,68,69,70,71,72,73,74,75,76,77,78,79,80,81,82,83,84,85,86,87,88,89,90,91,92,93,94,95,96,97,98,99,100], visible=False, meshCount=15, arg4=0, delay=200)

    def on_tick(self) -> state.State:
        if time_expired(timerId='1'):
            return 퍼즐단계4정리()

    def on_exit(self):
        reset_timer(timerId='1')


class 퍼즐단계4정리(state.State):
    def on_enter(self):
        set_timer(timerId='1', seconds=1)

    def on_tick(self) -> state.State:
        if time_expired(timerId='1'):
            return 퍼즐단계4정리2()

    def on_exit(self):
        reset_timer(timerId='1')


class 퍼즐단계4정리2(state.State):
    def on_tick(self) -> state.State:
        if user_detected(boxIds=[301]):
            set_mesh(triggerIds=[1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36,37,38,39,40,41,42,43,44,45,46,47,48,49,50,51,52,53,54,55,56,57,58,59,60,61,62,63,64,65,66,67,68,69,70,71,72,73,74,75,76,77,78,79,80,81,82,83,84,85,86,87,88,89,90,91,92,93,94,95,96,97,98,99,100], visible=True)
            return 보상단계()
        if not user_detected(boxIds=[301]):
            return 실패()


class 보상단계(state.State):
    def on_enter(self):
        set_timer(timerId='1', seconds=7)
        set_event_ui(type=0, arg2='0,0')
        set_event_ui(type=3, arg2='$61000002_ME_002__MASSIVE01__7$', arg3='7000', arg4='301')
        set_event_ui(type=6, arg2='$61000002_ME_002__MASSIVE01__8$', arg3='7000', arg4='!301') # 로그에서 해당 이벤트에서 우승한 사람을 체크하기 위한 명령어 / 1=미니게임 이름, 2=타겟박스 id

    def on_tick(self) -> state.State:
        if time_expired(timerId='1'):
            return 경험치지급()

    def on_exit(self):
        reset_timer(timerId='1')


class 경험치지급(state.State):
    def on_enter(self):
        set_timer(timerId='2', seconds=2)

    def on_tick(self) -> state.State:
        if time_expired(timerId='2'):
            return 버프걸기()


class 버프걸기(state.State):
    def on_enter(self):
        set_timer(timerId='1', seconds=7)
        set_event_ui(type=0, arg2='0,0') # action name="버프를걸어준다" arg1="301" arg2="70000019" arg3="1"/

    def on_tick(self) -> state.State:
        if time_expired(timerId='1'):
            return 퍼즐종료계단보이기()

    def on_exit(self):
        reset_timer(timerId='1')


class 퍼즐종료계단보이기(state.State):
    def on_enter(self):
        set_event_ui(type=0, arg2='0,0')
        set_mesh(triggerIds=[1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36,37,38,39,40,41,42,43,44,45,46,47,48,49,50,51,52,53,54,55,56,57,58,59,60,61,62,63,64,65,66,67,68,69,70,71,72,73,74,75,76,77,78,79,80,81,82,83,84,85,86,87,88,89,90,91,92,93,94,95,96,97,98,99,100], visible=True)
        set_mesh(triggerIds=[201,202,203,204,205], visible=True)
        set_actor(triggerId=251, visible=True, initialSequence='Eff_MassiveEvent_Stair_Opened')
        set_actor(triggerId=252, visible=True, initialSequence='Eff_MassiveEvent_Stair_Opened')
        set_actor(triggerId=253, visible=True, initialSequence='Eff_MassiveEvent_Stair_Opened')
        set_actor(triggerId=254, visible=True, initialSequence='Eff_MassiveEvent_Stair_Opened')
        set_actor(triggerId=255, visible=True, initialSequence='Eff_MassiveEvent_Stair_Opened')
        set_timer(timerId='1', seconds=1)

    def on_tick(self) -> state.State:
        if time_expired(timerId='1'):
            return 퍼즐종료계단보이기2()

    def on_exit(self):
        reset_timer(timerId='1')


class 퍼즐종료계단보이기2(state.State):
    def on_enter(self):
        set_mesh(triggerIds=[206,207,208,209,210], visible=True)
        set_actor(triggerId=256, visible=True, initialSequence='Eff_MassiveEvent_Stair_Opened')
        set_actor(triggerId=257, visible=True, initialSequence='Eff_MassiveEvent_Stair_Opened')
        set_actor(triggerId=258, visible=True, initialSequence='Eff_MassiveEvent_Stair_Opened')
        set_actor(triggerId=259, visible=True, initialSequence='Eff_MassiveEvent_Stair_Opened')
        set_actor(triggerId=260, visible=True, initialSequence='Eff_MassiveEvent_Stair_Opened')
        set_timer(timerId='1', seconds=1)

    def on_tick(self) -> state.State:
        if time_expired(timerId='1'):
            return 퍼즐종료()

    def on_exit(self):
        set_mesh(triggerIds=[211], visible=True)
        set_actor(triggerId=261, visible=True, initialSequence='Eff_MassiveEvent_Door_Opened')
        reset_timer(timerId='1')


class 퍼즐종료(state.State):
    def on_enter(self):
        unset_mini_game_area_for_hack() # 해킹 보안 종료
        set_event_ui(type=0, arg2='0,0')
        set_portal(portalId=777, visible=False, enabled=True, minimapVisible=False)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=1000):
            return 유저이동()


class 실패(state.State):
    def on_enter(self):
        unset_mini_game_area_for_hack() # 해킹 보안 종료
        set_event_ui(type=0, arg2='0,0')
        set_event_ui(type=5, arg2='$61000002_ME_002__MASSIVE01__13$', arg3='5000')
        set_mesh(triggerIds=[1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36,37,38,39,40,41,42,43,44,45,46,47,48,49,50,51,52,53,54,55,56,57,58,59,60,61,62,63,64,65,66,67,68,69,70,71,72,73,74,75,76,77,78,79,80,81,82,83,84,85,86,87,88,89,90,91,92,93,94,95,96,97,98,99,100], visible=True)
        set_portal(portalId=777, visible=False, enabled=True, minimapVisible=False)
        set_mesh(triggerIds=[201,202,203,204,205], visible=True)
        set_actor(triggerId=251, visible=True, initialSequence='Eff_MassiveEvent_Stair_Opened')
        set_actor(triggerId=252, visible=True, initialSequence='Eff_MassiveEvent_Stair_Opened')
        set_actor(triggerId=253, visible=True, initialSequence='Eff_MassiveEvent_Stair_Opened')
        set_actor(triggerId=254, visible=True, initialSequence='Eff_MassiveEvent_Stair_Opened')
        set_actor(triggerId=255, visible=True, initialSequence='Eff_MassiveEvent_Stair_Opened')
        set_timer(timerId='1', seconds=1)

    def on_tick(self) -> state.State:
        if time_expired(timerId='1'):
            return 실패계단보이기2()

    def on_exit(self):
        reset_timer(timerId='1')


class 실패계단보이기2(state.State):
    def on_enter(self):
        set_mesh(triggerIds=[206,207,208,209,210], visible=True)
        set_actor(triggerId=256, visible=True, initialSequence='Eff_MassiveEvent_Stair_Opened')
        set_actor(triggerId=257, visible=True, initialSequence='Eff_MassiveEvent_Stair_Opened')
        set_actor(triggerId=258, visible=True, initialSequence='Eff_MassiveEvent_Stair_Opened')
        set_actor(triggerId=259, visible=True, initialSequence='Eff_MassiveEvent_Stair_Opened')
        set_actor(triggerId=260, visible=True, initialSequence='Eff_MassiveEvent_Stair_Opened')
        set_timer(timerId='1', seconds=1)

    def on_tick(self) -> state.State:
        if time_expired(timerId='1'):
            return 유저이동()

    def on_exit(self):
        set_mesh(triggerIds=[211], visible=True)
        set_actor(triggerId=261, visible=True, initialSequence='Eff_MassiveEvent_Door_Opened')
        reset_timer(timerId='1')


class 유저이동(state.State):
    def on_enter(self):
        set_event_ui(type=1, arg2='$61000007_ME__MAINPROCESS_SPRINGBEACH__23$', arg3='5000', arg4='0')

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=120000):
            move_user(mapId=0, portalId=0)
            return 종료()


class 종료(state.State):
    pass


