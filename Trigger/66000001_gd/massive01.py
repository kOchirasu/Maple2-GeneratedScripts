""" trigger/66000001_gd/massive01.xml """
import common


# 파이널서바이버
class 대기(common.Trigger):
    def on_tick(self) -> common.Trigger:
        if self.user_detected(boxIds=[301]):
            return 퍼즐대기중(self.ctx)


class 퍼즐대기중(common.Trigger):
    def on_enter(self):
        self.set_mesh(triggerIds=[201,202,203,204,205,206,207,208,209,210,211], visible=True)
        self.set_actor(triggerId=251, visible=True, initialSequence='Eff_MassiveEvent_Stair_Opened')
        self.set_actor(triggerId=252, visible=True, initialSequence='Eff_MassiveEvent_Stair_Opened')
        self.set_actor(triggerId=253, visible=True, initialSequence='Eff_MassiveEvent_Stair_Opened')
        self.set_actor(triggerId=254, visible=True, initialSequence='Eff_MassiveEvent_Stair_Opened')
        self.set_actor(triggerId=255, visible=True, initialSequence='Eff_MassiveEvent_Stair_Opened')
        self.set_actor(triggerId=256, visible=True, initialSequence='Eff_MassiveEvent_Stair_Opened')
        self.set_actor(triggerId=257, visible=True, initialSequence='Eff_MassiveEvent_Stair_Opened')
        self.set_actor(triggerId=258, visible=True, initialSequence='Eff_MassiveEvent_Stair_Opened')
        self.set_actor(triggerId=259, visible=True, initialSequence='Eff_MassiveEvent_Stair_Opened')
        self.set_actor(triggerId=260, visible=True, initialSequence='Eff_MassiveEvent_Stair_Opened')
        self.set_actor(triggerId=261, visible=True, initialSequence='Eff_MassiveEvent_Door_Opened')
        self.set_mesh(triggerIds=[1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36,37,38,39,40,41,42,43,44,45,46,47,48,49,50,51,52,53,54,55,56,57,58,59,60,61,62,63,64,65,66,67,68,69,70,71,72,73,74,75,76,77,78,79,80,81,82,83,84,85,86,87,88,89,90,91,92,93,94,95,96,97,98,99,100], visible=True)
        self.set_portal(portalId=777, visible=False, enable=True, minimapVisible=False)
        self.set_portal(portalId=778, visible=True, enable=True, minimapVisible=True)
        self.set_portal(portalId=779, visible=True, enable=True, minimapVisible=True)

    def on_tick(self) -> common.Trigger:
        if self.count_users(boxId=301, boxId=50):
            return 계단없애기(self.ctx)
        if self.wait_tick(waitTick=30000):
            return 계단없애기(self.ctx)

    def on_exit(self):
        self.set_actor(triggerId=261, visible=True, initialSequence='Eff_MassiveEvent_Door_Vanished')
        self.set_portal(portalId=777, visible=False, enable=False, minimapVisible=False)


class 계단없애기(common.Trigger):
    def on_enter(self):
        self.set_mini_game_area_for_hack(boxId=301) # 해킹 보안용 시작 box 설정
        self.set_timer(timerId='1', seconds=1)

    def on_tick(self) -> common.Trigger:
        if self.time_expired(timerId='1'):
            return 계단없애기2(self.ctx)

    def on_exit(self):
        self.set_mesh(triggerIds=[206,207,208,209,210,211], visible=False)
        self.set_actor(triggerId=256, visible=True, initialSequence='Eff_MassiveEvent_Stair_Closed')
        self.set_actor(triggerId=257, visible=True, initialSequence='Eff_MassiveEvent_Stair_Closed')
        self.set_actor(triggerId=258, visible=True, initialSequence='Eff_MassiveEvent_Stair_Closed')
        self.set_actor(triggerId=259, visible=True, initialSequence='Eff_MassiveEvent_Stair_Closed')
        self.set_actor(triggerId=260, visible=True, initialSequence='Eff_MassiveEvent_Stair_Closed')
        self.set_actor(triggerId=261, visible=False, initialSequence='Eff_MassiveEvent_Door_Vanished')
        self.reset_timer(timerId='1')


class 계단없애기2(common.Trigger):
    def on_enter(self):
        self.set_timer(timerId='1', seconds=1)

    def on_tick(self) -> common.Trigger:
        if self.time_expired(timerId='1'):
            return 시작대기(self.ctx)

    def on_exit(self):
        self.set_mesh(triggerIds=[201,202,203,204,205], visible=False)
        self.set_actor(triggerId=251, visible=True, initialSequence='Eff_MassiveEvent_Stair_Closed')
        self.set_actor(triggerId=252, visible=True, initialSequence='Eff_MassiveEvent_Stair_Closed')
        self.set_actor(triggerId=253, visible=True, initialSequence='Eff_MassiveEvent_Stair_Closed')
        self.set_actor(triggerId=254, visible=True, initialSequence='Eff_MassiveEvent_Stair_Closed')
        self.set_actor(triggerId=255, visible=True, initialSequence='Eff_MassiveEvent_Stair_Closed')
        self.set_actor(triggerId=256, visible=False, initialSequence='Eff_MassiveEvent_Stair_Closed')
        self.set_actor(triggerId=257, visible=False, initialSequence='Eff_MassiveEvent_Stair_Closed')
        self.set_actor(triggerId=258, visible=False, initialSequence='Eff_MassiveEvent_Stair_Closed')
        self.set_actor(triggerId=259, visible=False, initialSequence='Eff_MassiveEvent_Stair_Closed')
        self.set_actor(triggerId=260, visible=False, initialSequence='Eff_MassiveEvent_Stair_Closed')
        self.reset_timer(timerId='1')


class 시작대기(common.Trigger):
    def on_enter(self):
        self.set_timer(timerId='1', seconds=5)

    def on_tick(self) -> common.Trigger:
        if self.time_expired(timerId='1'):
            return 멘트0(self.ctx)

    def on_exit(self):
        self.reset_timer(timerId='1')


class 멘트0(common.Trigger):
    def on_enter(self):
        self.set_timer(timerId='1', seconds=5)
        self.set_event_ui(type=1, arg2='$61000002_ME_002__MASSIVE01__0$', arg3='6000') # 로그에서 해당 이벤트에 참여한 사람을 체크하기 위한 명령어 / 1=미니게임 이름, 2=타겟박스 id

    def on_tick(self) -> common.Trigger:
        if self.time_expired(timerId='1'):
            return 멘트1(self.ctx)

    def on_exit(self):
        self.reset_timer(timerId='1')


class 멘트1(common.Trigger):
    def on_enter(self):
        self.set_timer(timerId='1', seconds=4)
        self.set_event_ui(type=1, arg2='$66000001_GD__MASSIVE01__0$', arg3='4000')

    def on_tick(self) -> common.Trigger:
        if self.time_expired(timerId='1'):
            return 멘트2(self.ctx)

    def on_exit(self):
        self.reset_timer(timerId='1')


class 멘트2(common.Trigger):
    def on_enter(self):
        self.set_timer(timerId='1', seconds=5)
        self.set_event_ui(type=1, arg2='$61000002_ME_002__MASSIVE01__2$', arg3='6000')

    def on_tick(self) -> common.Trigger:
        if self.time_expired(timerId='1'):
            return 멘트3(self.ctx)

    def on_exit(self):
        self.reset_timer(timerId='1')


class 멘트3(common.Trigger):
    def on_enter(self):
        self.set_timer(timerId='1', seconds=6)
        self.set_event_ui(type=0, arg2='1,4')
        self.show_count_ui(text='$61000002_ME_002__MASSIVE01__3$', stage=1, count=5)

    def on_tick(self) -> common.Trigger:
        if self.time_expired(timerId='1'):
            return 퍼즐단계1대기(self.ctx)

    def on_exit(self):
        self.reset_timer(timerId='1')


class 퍼즐단계1대기(common.Trigger):
    def on_enter(self):
        self.set_timer(timerId='1', seconds=2)

    def on_tick(self) -> common.Trigger:
        if self.time_expired(timerId='1'):
            return 퍼즐단계1(self.ctx)

    def on_exit(self):
        self.reset_timer(timerId='1')


class 퍼즐단계1(common.Trigger):
    def on_enter(self):
        self.set_timer(timerId='1', seconds=40)
        self.set_random_mesh(triggerIds=[1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36,37,38,39,40,41,42,43,44,45,46,47,48,49,50,51,52,53,54,55,56,57,58,59,60,61,62,63,64,65,66,67,68,69,70,71,72,73,74,75,76,77,78,79,80,81,82,83,84,85,86,87,88,89,90,91,92,93,94,95,96,97,98,99,100], visible=False, meshCount=20, arg4=0, delay=2000)

    def on_tick(self) -> common.Trigger:
        if self.time_expired(timerId='1'):
            return 퍼즐단계1정리(self.ctx)

    def on_exit(self):
        self.reset_timer(timerId='1')


class 퍼즐단계1정리(common.Trigger):
    def on_enter(self):
        self.set_timer(timerId='1', seconds=3)

    def on_tick(self) -> common.Trigger:
        if self.time_expired(timerId='1'):
            return 퍼즐단계1정리2(self.ctx)

    def on_exit(self):
        self.reset_timer(timerId='1')


class 퍼즐단계1정리2(common.Trigger):
    def on_tick(self) -> common.Trigger:
        if self.user_detected(boxIds=[301]):
            self.set_event_ui(type=0, arg2='2,4')
            self.show_count_ui(text='$61000002_ME_002__MASSIVE01__4$', stage=2, count=5)
            return 퍼즐단계2대기(self.ctx)
        if not self.user_detected(boxIds=[301]):
            return 실패(self.ctx)


class 퍼즐단계2대기(common.Trigger):
    def on_enter(self):
        self.set_timer(timerId='1', seconds=6)

    def on_tick(self) -> common.Trigger:
        if self.time_expired(timerId='1'):
            return 퍼즐단계2(self.ctx)

    def on_exit(self):
        self.reset_timer(timerId='1')


class 퍼즐단계2(common.Trigger):
    def on_enter(self):
        self.set_timer(timerId='1', seconds=30)
        self.set_random_mesh(triggerIds=[1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36,37,38,39,40,41,42,43,44,45,46,47,48,49,50,51,52,53,54,55,56,57,58,59,60,61,62,63,64,65,66,67,68,69,70,71,72,73,74,75,76,77,78,79,80,81,82,83,84,85,86,87,88,89,90,91,92,93,94,95,96,97,98,99,100], visible=False, meshCount=30, arg4=0, delay=1000)

    def on_tick(self) -> common.Trigger:
        if self.time_expired(timerId='1'):
            return 퍼즐단계2정리(self.ctx)

    def on_exit(self):
        self.reset_timer(timerId='1')


class 퍼즐단계2정리(common.Trigger):
    def on_enter(self):
        self.set_timer(timerId='1', seconds=3)

    def on_tick(self) -> common.Trigger:
        if self.time_expired(timerId='1'):
            return 퍼즐단계2정리2(self.ctx)

    def on_exit(self):
        self.reset_timer(timerId='1')


class 퍼즐단계2정리2(common.Trigger):
    def on_tick(self) -> common.Trigger:
        if self.user_detected(boxIds=[301]):
            self.set_event_ui(type=0, arg2='3,4')
            self.show_count_ui(text='$61000002_ME_002__MASSIVE01__5$', stage=3, count=5)
            return 퍼즐단계3대기(self.ctx)
        if not self.user_detected(boxIds=[301]):
            return 실패(self.ctx)


class 퍼즐단계3대기(common.Trigger):
    def on_enter(self):
        self.set_timer(timerId='1', seconds=6)

    def on_tick(self) -> common.Trigger:
        if self.time_expired(timerId='1'):
            return 퍼즐단계3(self.ctx)

    def on_exit(self):
        self.reset_timer(timerId='1')


class 퍼즐단계3(common.Trigger):
    def on_enter(self):
        self.set_timer(timerId='1', seconds=15)
        self.set_random_mesh(triggerIds=[1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36,37,38,39,40,41,42,43,44,45,46,47,48,49,50,51,52,53,54,55,56,57,58,59,60,61,62,63,64,65,66,67,68,69,70,71,72,73,74,75,76,77,78,79,80,81,82,83,84,85,86,87,88,89,90,91,92,93,94,95,96,97,98,99,100], visible=False, meshCount=30, arg4=0, delay=500)

    def on_tick(self) -> common.Trigger:
        if self.time_expired(timerId='1'):
            return 퍼즐단계3정리(self.ctx)

    def on_exit(self):
        self.reset_timer(timerId='1')


class 퍼즐단계3정리(common.Trigger):
    def on_enter(self):
        self.set_timer(timerId='1', seconds=3)

    def on_tick(self) -> common.Trigger:
        if self.time_expired(timerId='1'):
            return 퍼즐단계3정리2(self.ctx)

    def on_exit(self):
        self.reset_timer(timerId='1')


class 퍼즐단계3정리2(common.Trigger):
    def on_tick(self) -> common.Trigger:
        if self.user_detected(boxIds=[301]):
            self.set_event_ui(type=0, arg2='4,4')
            self.show_count_ui(text='$61000002_ME_002__MASSIVE01__6$', stage=4, count=5)
            return 퍼즐단계4대기(self.ctx)
        if not self.user_detected(boxIds=[301]):
            return 실패(self.ctx)


class 퍼즐단계4대기(common.Trigger):
    def on_enter(self):
        self.set_timer(timerId='1', seconds=6)

    def on_tick(self) -> common.Trigger:
        if self.time_expired(timerId='1'):
            return 퍼즐단계4(self.ctx)

    def on_exit(self):
        self.reset_timer(timerId='1')


class 퍼즐단계4(common.Trigger):
    def on_enter(self):
        self.set_timer(timerId='1', seconds=5)
        self.set_random_mesh(triggerIds=[1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36,37,38,39,40,41,42,43,44,45,46,47,48,49,50,51,52,53,54,55,56,57,58,59,60,61,62,63,64,65,66,67,68,69,70,71,72,73,74,75,76,77,78,79,80,81,82,83,84,85,86,87,88,89,90,91,92,93,94,95,96,97,98,99,100], visible=False, meshCount=15, arg4=0, delay=200)

    def on_tick(self) -> common.Trigger:
        if self.time_expired(timerId='1'):
            return 퍼즐단계4정리(self.ctx)

    def on_exit(self):
        self.reset_timer(timerId='1')


class 퍼즐단계4정리(common.Trigger):
    def on_enter(self):
        self.set_timer(timerId='1', seconds=1)

    def on_tick(self) -> common.Trigger:
        if self.time_expired(timerId='1'):
            return 퍼즐단계4정리2(self.ctx)

    def on_exit(self):
        self.reset_timer(timerId='1')


class 퍼즐단계4정리2(common.Trigger):
    def on_tick(self) -> common.Trigger:
        if self.user_detected(boxIds=[301]):
            self.set_mesh(triggerIds=[1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36,37,38,39,40,41,42,43,44,45,46,47,48,49,50,51,52,53,54,55,56,57,58,59,60,61,62,63,64,65,66,67,68,69,70,71,72,73,74,75,76,77,78,79,80,81,82,83,84,85,86,87,88,89,90,91,92,93,94,95,96,97,98,99,100], visible=True)
            return 보상단계(self.ctx)
        if not self.user_detected(boxIds=[301]):
            return 실패(self.ctx)


class 보상단계(common.Trigger):
    def on_enter(self):
        self.set_timer(timerId='1', seconds=7)
        self.set_event_ui(type=0, arg2='0,0')
        self.set_event_ui(type=3, arg2='$61000002_ME_002__MASSIVE01__7$', arg3='7000', arg4='301')
        self.set_event_ui(type=6, arg2='$61000002_ME_002__MASSIVE01__8$', arg3='7000', arg4='!301') # 로그에서 해당 이벤트에서 우승한 사람을 체크하기 위한 명령어 / 1=미니게임 이름, 2=타겟박스 id

    def on_tick(self) -> common.Trigger:
        if self.time_expired(timerId='1'):
            return 경험치지급(self.ctx)

    def on_exit(self):
        self.reset_timer(timerId='1')


class 경험치지급(common.Trigger):
    def on_enter(self):
        self.set_timer(timerId='2', seconds=2)

    def on_tick(self) -> common.Trigger:
        if self.time_expired(timerId='2'):
            return 버프걸기(self.ctx)


class 버프걸기(common.Trigger):
    def on_enter(self):
        self.set_timer(timerId='1', seconds=7)
        self.set_event_ui(type=0, arg2='0,0')
        # action name="버프를걸어준다" arg1="301" arg2="70000019" arg3="1"/

    def on_tick(self) -> common.Trigger:
        if self.time_expired(timerId='1'):
            return 퍼즐종료계단보이기(self.ctx)

    def on_exit(self):
        self.reset_timer(timerId='1')


class 퍼즐종료계단보이기(common.Trigger):
    def on_enter(self):
        self.set_event_ui(type=0, arg2='0,0')
        self.set_mesh(triggerIds=[1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36,37,38,39,40,41,42,43,44,45,46,47,48,49,50,51,52,53,54,55,56,57,58,59,60,61,62,63,64,65,66,67,68,69,70,71,72,73,74,75,76,77,78,79,80,81,82,83,84,85,86,87,88,89,90,91,92,93,94,95,96,97,98,99,100], visible=True)
        self.set_mesh(triggerIds=[201,202,203,204,205], visible=True)
        self.set_actor(triggerId=251, visible=True, initialSequence='Eff_MassiveEvent_Stair_Opened')
        self.set_actor(triggerId=252, visible=True, initialSequence='Eff_MassiveEvent_Stair_Opened')
        self.set_actor(triggerId=253, visible=True, initialSequence='Eff_MassiveEvent_Stair_Opened')
        self.set_actor(triggerId=254, visible=True, initialSequence='Eff_MassiveEvent_Stair_Opened')
        self.set_actor(triggerId=255, visible=True, initialSequence='Eff_MassiveEvent_Stair_Opened')
        self.set_timer(timerId='1', seconds=1)

    def on_tick(self) -> common.Trigger:
        if self.time_expired(timerId='1'):
            return 퍼즐종료계단보이기2(self.ctx)

    def on_exit(self):
        self.reset_timer(timerId='1')


class 퍼즐종료계단보이기2(common.Trigger):
    def on_enter(self):
        self.set_mesh(triggerIds=[206,207,208,209,210], visible=True)
        self.set_actor(triggerId=256, visible=True, initialSequence='Eff_MassiveEvent_Stair_Opened')
        self.set_actor(triggerId=257, visible=True, initialSequence='Eff_MassiveEvent_Stair_Opened')
        self.set_actor(triggerId=258, visible=True, initialSequence='Eff_MassiveEvent_Stair_Opened')
        self.set_actor(triggerId=259, visible=True, initialSequence='Eff_MassiveEvent_Stair_Opened')
        self.set_actor(triggerId=260, visible=True, initialSequence='Eff_MassiveEvent_Stair_Opened')
        self.set_timer(timerId='1', seconds=1)

    def on_tick(self) -> common.Trigger:
        if self.time_expired(timerId='1'):
            return 퍼즐종료(self.ctx)

    def on_exit(self):
        self.set_mesh(triggerIds=[211], visible=True)
        self.set_actor(triggerId=261, visible=True, initialSequence='Eff_MassiveEvent_Door_Opened')
        self.reset_timer(timerId='1')


class 퍼즐종료(common.Trigger):
    def on_enter(self):
        self.unset_mini_game_area_for_hack() # 해킹 보안 종료
        self.set_event_ui(type=0, arg2='0,0')
        self.set_portal(portalId=777, visible=False, enable=True, minimapVisible=False)

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=1000):
            return 유저이동(self.ctx)


class 실패(common.Trigger):
    def on_enter(self):
        self.unset_mini_game_area_for_hack() # 해킹 보안 종료
        self.set_event_ui(type=0, arg2='0,0')
        self.set_event_ui(type=5, arg2='$61000002_ME_002__MASSIVE01__13$', arg3='5000')
        self.set_mesh(triggerIds=[1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36,37,38,39,40,41,42,43,44,45,46,47,48,49,50,51,52,53,54,55,56,57,58,59,60,61,62,63,64,65,66,67,68,69,70,71,72,73,74,75,76,77,78,79,80,81,82,83,84,85,86,87,88,89,90,91,92,93,94,95,96,97,98,99,100], visible=True)
        self.set_portal(portalId=777, visible=False, enable=True, minimapVisible=False)
        self.set_mesh(triggerIds=[201,202,203,204,205], visible=True)
        self.set_actor(triggerId=251, visible=True, initialSequence='Eff_MassiveEvent_Stair_Opened')
        self.set_actor(triggerId=252, visible=True, initialSequence='Eff_MassiveEvent_Stair_Opened')
        self.set_actor(triggerId=253, visible=True, initialSequence='Eff_MassiveEvent_Stair_Opened')
        self.set_actor(triggerId=254, visible=True, initialSequence='Eff_MassiveEvent_Stair_Opened')
        self.set_actor(triggerId=255, visible=True, initialSequence='Eff_MassiveEvent_Stair_Opened')
        self.set_timer(timerId='1', seconds=1)

    def on_tick(self) -> common.Trigger:
        if self.time_expired(timerId='1'):
            return 실패계단보이기2(self.ctx)

    def on_exit(self):
        self.reset_timer(timerId='1')


class 실패계단보이기2(common.Trigger):
    def on_enter(self):
        self.set_mesh(triggerIds=[206,207,208,209,210], visible=True)
        self.set_actor(triggerId=256, visible=True, initialSequence='Eff_MassiveEvent_Stair_Opened')
        self.set_actor(triggerId=257, visible=True, initialSequence='Eff_MassiveEvent_Stair_Opened')
        self.set_actor(triggerId=258, visible=True, initialSequence='Eff_MassiveEvent_Stair_Opened')
        self.set_actor(triggerId=259, visible=True, initialSequence='Eff_MassiveEvent_Stair_Opened')
        self.set_actor(triggerId=260, visible=True, initialSequence='Eff_MassiveEvent_Stair_Opened')
        self.set_timer(timerId='1', seconds=1)

    def on_tick(self) -> common.Trigger:
        if self.time_expired(timerId='1'):
            return 유저이동(self.ctx)

    def on_exit(self):
        self.set_mesh(triggerIds=[211], visible=True)
        self.set_actor(triggerId=261, visible=True, initialSequence='Eff_MassiveEvent_Door_Opened')
        self.reset_timer(timerId='1')


class 유저이동(common.Trigger):
    def on_enter(self):
        self.set_event_ui(type=1, arg2='$61000007_ME__MAINPROCESS_SPRINGBEACH__23$', arg3='5000', arg4='0')

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=120000):
            self.move_user(mapId=0, portalId=0)
            return 종료(self.ctx)


class 종료(common.Trigger):
    pass


initial_state = 대기
