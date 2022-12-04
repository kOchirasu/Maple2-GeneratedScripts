""" trigger/61000002_me_002/massive01.xml """
import trigger_api


# 파이널서바이버
class 대기(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.user_detected(boxIds=[301]):
            return 퍼즐대기중(self.ctx)


class 퍼즐대기중(trigger_api.Trigger):
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

    def on_tick(self) -> trigger_api.Trigger:
        if self.count_users(boxId=301, boxId=50):
            return 계단없애기(self.ctx)
        if self.wait_tick(waitTick=60000):
            return 계단없애기(self.ctx)

    def on_exit(self):
        self.set_actor(triggerId=261, visible=True, initialSequence='Eff_MassiveEvent_Door_Vanished')
        self.set_portal(portalId=777, visible=False, enable=False, minimapVisible=False)


class 계단없애기(trigger_api.Trigger):
    def on_enter(self):
        self.set_mini_game_area_for_hack(boxId=301) # 해킹 보안용 시작 box 설정
        self.set_timer(timerId='1', seconds=1)

    def on_tick(self) -> trigger_api.Trigger:
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


class 계단없애기2(trigger_api.Trigger):
    def on_enter(self):
        self.set_timer(timerId='1', seconds=1)

    def on_tick(self) -> trigger_api.Trigger:
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


class 시작대기(trigger_api.Trigger):
    def on_enter(self):
        self.set_timer(timerId='1', seconds=5)

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timerId='1'):
            return 멘트0(self.ctx)

    def on_exit(self):
        self.reset_timer(timerId='1')


class 멘트0(trigger_api.Trigger):
    def on_enter(self):
        self.set_timer(timerId='1', seconds=5)
        self.play_system_sound_in_box(sound='ME_002_Massive01_00')
        self.set_event_ui(type=1, arg2='$61000002_ME_002__MASSIVE01__0$', arg3='6000') # 로그에서 해당 이벤트에 참여한 사람을 체크하기 위한 명령어 / 1=미니게임 이름, 2=타겟박스 id
        self.start_mini_game(boxId=301, round=4, gameName='finalsurvivor') # 트로피 / 1=타겟박스 id, 2=achieveType, 3=code에 들어갈 값
        self.set_achievement(triggerId=301, type='trigger', achieve='finalsurvivor_start')
        self.set_achievement(triggerId=301, type='trigger', achieve='dailyquest_start') # 길드 경험치 지급 / boxID="타겟박스id", 0이면 맵전체, type="GuildGainExp의 id" 2가 매시브이벤트
        self.give_guild_exp(boxId=0, type=2)

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timerId='1'):
            return 멘트1(self.ctx)

    def on_exit(self):
        self.reset_timer(timerId='1')


class 멘트1(trigger_api.Trigger):
    def on_enter(self):
        self.set_timer(timerId='1', seconds=11)
        self.play_system_sound_in_box(sound='ME_002_Massive01_01')
        self.set_event_ui(type=1, arg2='$61000002_ME_002__MASSIVE01__1$', arg3='11000')

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timerId='1'):
            return 멘트2(self.ctx)

    def on_exit(self):
        self.reset_timer(timerId='1')


class 멘트2(trigger_api.Trigger):
    def on_enter(self):
        self.set_timer(timerId='1', seconds=9)
        self.play_system_sound_in_box(sound='ME_002_Massive01_02')
        self.set_event_ui(type=1, arg2='$61000002_ME_002__MASSIVE01__2$', arg3='9000')

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timerId='1'):
            return 멘트3(self.ctx)

    def on_exit(self):
        self.reset_timer(timerId='1')


class 멘트3(trigger_api.Trigger):
    def on_enter(self):
        self.set_timer(timerId='1', seconds=6)
        self.set_event_ui(type=0, arg2='1,4')
        self.show_count_ui(text='$61000002_ME_002__MASSIVE01__3$', stage=1, count=5)

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timerId='1'):
            return 퍼즐단계1대기(self.ctx)

    def on_exit(self):
        self.reset_timer(timerId='1')


class 퍼즐단계1대기(trigger_api.Trigger):
    def on_enter(self):
        self.set_timer(timerId='1', seconds=2)

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timerId='1'):
            return 퍼즐단계1(self.ctx)

    def on_exit(self):
        self.reset_timer(timerId='1')


class 퍼즐단계1(trigger_api.Trigger):
    def on_enter(self):
        self.start_mini_game_round(boxId=301, round=1)
        self.set_timer(timerId='1', seconds=40)
        self.set_random_mesh(triggerIds=[1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36,37,38,39,40,41,42,43,44,45,46,47,48,49,50,51,52,53,54,55,56,57,58,59,60,61,62,63,64,65,66,67,68,69,70,71,72,73,74,75,76,77,78,79,80,81,82,83,84,85,86,87,88,89,90,91,92,93,94,95,96,97,98,99,100], visible=False, meshCount=20, arg4=0, delay=2000)

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timerId='1'):
            return 퍼즐단계1정리(self.ctx)

    def on_exit(self):
        self.reset_timer(timerId='1')


class 퍼즐단계1정리(trigger_api.Trigger):
    def on_enter(self):
        self.end_mini_game_round(winnerBoxId=301, expRate=0.25)
        self.set_timer(timerId='1', seconds=3)

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timerId='1'):
            return 퍼즐단계1정리2(self.ctx)

    def on_exit(self):
        self.reset_timer(timerId='1')


class 퍼즐단계1정리2(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.user_detected(boxIds=[301]):
            self.set_event_ui(type=0, arg2='2,4')
            self.show_count_ui(text='$61000002_ME_002__MASSIVE01__4$', stage=2, count=5)
            return 퍼즐단계2대기(self.ctx)
        if not self.user_detected(boxIds=[301]):
            return 실패(self.ctx)


class 퍼즐단계2대기(trigger_api.Trigger):
    def on_enter(self):
        self.set_timer(timerId='1', seconds=6)

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timerId='1'):
            return 퍼즐단계2(self.ctx)

    def on_exit(self):
        self.reset_timer(timerId='1')


class 퍼즐단계2(trigger_api.Trigger):
    def on_enter(self):
        self.start_mini_game_round(boxId=301, round=2)
        self.set_timer(timerId='1', seconds=30)
        self.set_random_mesh(triggerIds=[1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36,37,38,39,40,41,42,43,44,45,46,47,48,49,50,51,52,53,54,55,56,57,58,59,60,61,62,63,64,65,66,67,68,69,70,71,72,73,74,75,76,77,78,79,80,81,82,83,84,85,86,87,88,89,90,91,92,93,94,95,96,97,98,99,100], visible=False, meshCount=30, arg4=0, delay=1000)

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timerId='1'):
            return 퍼즐단계2정리(self.ctx)

    def on_exit(self):
        self.reset_timer(timerId='1')


class 퍼즐단계2정리(trigger_api.Trigger):
    def on_enter(self):
        self.end_mini_game_round(winnerBoxId=301, expRate=0.25)
        self.set_timer(timerId='1', seconds=3)

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timerId='1'):
            return 퍼즐단계2정리2(self.ctx)

    def on_exit(self):
        self.reset_timer(timerId='1')


class 퍼즐단계2정리2(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.user_detected(boxIds=[301]):
            self.set_event_ui(type=0, arg2='3,4')
            self.show_count_ui(text='$61000002_ME_002__MASSIVE01__5$', stage=3, count=5)
            return 퍼즐단계3대기(self.ctx)
        if not self.user_detected(boxIds=[301]):
            return 실패(self.ctx)


class 퍼즐단계3대기(trigger_api.Trigger):
    def on_enter(self):
        self.set_timer(timerId='1', seconds=6)

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timerId='1'):
            return 퍼즐단계3(self.ctx)

    def on_exit(self):
        self.reset_timer(timerId='1')


class 퍼즐단계3(trigger_api.Trigger):
    def on_enter(self):
        self.start_mini_game_round(boxId=301, round=3)
        self.set_timer(timerId='1', seconds=15)
        self.set_random_mesh(triggerIds=[1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36,37,38,39,40,41,42,43,44,45,46,47,48,49,50,51,52,53,54,55,56,57,58,59,60,61,62,63,64,65,66,67,68,69,70,71,72,73,74,75,76,77,78,79,80,81,82,83,84,85,86,87,88,89,90,91,92,93,94,95,96,97,98,99,100], visible=False, meshCount=30, arg4=0, delay=500)

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timerId='1'):
            return 퍼즐단계3정리(self.ctx)

    def on_exit(self):
        self.reset_timer(timerId='1')


class 퍼즐단계3정리(trigger_api.Trigger):
    def on_enter(self):
        self.end_mini_game_round(winnerBoxId=301, expRate=0.25)
        self.set_timer(timerId='1', seconds=3)

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timerId='1'):
            return 퍼즐단계3정리2(self.ctx)

    def on_exit(self):
        self.reset_timer(timerId='1')


class 퍼즐단계3정리2(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.user_detected(boxIds=[301]):
            self.set_event_ui(type=0, arg2='4,4')
            self.show_count_ui(text='$61000002_ME_002__MASSIVE01__6$', stage=4, count=5)
            return 퍼즐단계4대기(self.ctx)
        if not self.user_detected(boxIds=[301]):
            return 실패(self.ctx)


class 퍼즐단계4대기(trigger_api.Trigger):
    def on_enter(self):
        self.set_timer(timerId='1', seconds=6)

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timerId='1'):
            return 퍼즐단계4(self.ctx)

    def on_exit(self):
        self.reset_timer(timerId='1')


class 퍼즐단계4(trigger_api.Trigger):
    def on_enter(self):
        self.start_mini_game_round(boxId=301, round=4)
        self.set_timer(timerId='1', seconds=5)
        self.set_random_mesh(triggerIds=[1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36,37,38,39,40,41,42,43,44,45,46,47,48,49,50,51,52,53,54,55,56,57,58,59,60,61,62,63,64,65,66,67,68,69,70,71,72,73,74,75,76,77,78,79,80,81,82,83,84,85,86,87,88,89,90,91,92,93,94,95,96,97,98,99,100], visible=False, meshCount=15, arg4=0, delay=200)

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timerId='1'):
            return 퍼즐단계4정리(self.ctx)

    def on_exit(self):
        self.reset_timer(timerId='1')


class 퍼즐단계4정리(trigger_api.Trigger):
    def on_enter(self):
        self.end_mini_game_round(winnerBoxId=301, expRate=0.25)
        self.set_timer(timerId='1', seconds=1)

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timerId='1'):
            return 퍼즐단계4정리2(self.ctx)

    def on_exit(self):
        self.reset_timer(timerId='1')


class 퍼즐단계4정리2(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.user_detected(boxIds=[301]):
            self.set_mesh(triggerIds=[1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36,37,38,39,40,41,42,43,44,45,46,47,48,49,50,51,52,53,54,55,56,57,58,59,60,61,62,63,64,65,66,67,68,69,70,71,72,73,74,75,76,77,78,79,80,81,82,83,84,85,86,87,88,89,90,91,92,93,94,95,96,97,98,99,100], visible=True)
            return 우승자카메라연출(self.ctx)
        if not self.user_detected(boxIds=[301]):
            return 실패(self.ctx)


class 우승자카메라연출(trigger_api.Trigger):
    def on_enter(self):
        self.mini_game_camera_direction(boxId=301, cameraId=901)
        self.set_event_ui(type=0, arg2='0,0')
        self.play_system_sound_in_box(sound='ME_002_Massive01_07')
        self.set_event_ui(type=3, arg2='$61000002_ME_002__MASSIVE01__7$', arg3='7000', arg4='301')
        self.set_event_ui(type=6, arg2='$61000002_ME_002__MASSIVE01__8$', arg3='7000', arg4='!301')

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=6000):
            self.set_local_camera(cameraId=901, enable=False)
            return 보상단계(self.ctx)


class 보상단계(trigger_api.Trigger):
    def on_enter(self):
        self.play_system_sound_in_box(boxIds=[301], sound='ME_001_Massive00_10')
        self.set_event_ui(type=3, arg2='$61000002_ME_002__MASSIVE01__9$', arg3='5000', arg4='301')
        self.set_event_ui(type=6, arg2='$61000002_ME_002__MASSIVE01__10$', arg3='5000', arg4='!301')
        self.add_buff(boxIds=[301], skillId=70000019, level=1) # 로그에서 해당 이벤트에서 우승한 사람을 체크하기 위한 명령어 / 1=미니게임 이름, 2=타겟박스 id
        self.mini_game_give_reward(winnerBoxId=301, contentType='miniGame')
        self.end_mini_game(winnerBoxId=301, gameName='finalsurvivor') # 트로피 / 1=타겟박스 id, 2=achieveType, 3=code에 들어갈 값
        self.set_achievement(triggerId=301, type='trigger', achieve='finalsurvivor_win')

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=3000):
            return 퍼즐종료계단보이기(self.ctx)


class 퍼즐종료계단보이기(trigger_api.Trigger):
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

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timerId='1'):
            return 퍼즐종료계단보이기2(self.ctx)

    def on_exit(self):
        self.reset_timer(timerId='1')


class 퍼즐종료계단보이기2(trigger_api.Trigger):
    def on_enter(self):
        self.set_mesh(triggerIds=[206,207,208,209,210], visible=True)
        self.set_actor(triggerId=256, visible=True, initialSequence='Eff_MassiveEvent_Stair_Opened')
        self.set_actor(triggerId=257, visible=True, initialSequence='Eff_MassiveEvent_Stair_Opened')
        self.set_actor(triggerId=258, visible=True, initialSequence='Eff_MassiveEvent_Stair_Opened')
        self.set_actor(triggerId=259, visible=True, initialSequence='Eff_MassiveEvent_Stair_Opened')
        self.set_actor(triggerId=260, visible=True, initialSequence='Eff_MassiveEvent_Stair_Opened')
        self.set_timer(timerId='1', seconds=1)

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timerId='1'):
            return 퍼즐종료(self.ctx)

    def on_exit(self):
        self.set_mesh(triggerIds=[211], visible=True)
        self.set_actor(triggerId=261, visible=True, initialSequence='Eff_MassiveEvent_Door_Opened')
        self.reset_timer(timerId='1')


class 퍼즐종료(trigger_api.Trigger):
    def on_enter(self):
        self.unset_mini_game_area_for_hack() # 해킹 보안 종료
        self.set_event_ui(type=0, arg2='0,0')
        self.set_portal(portalId=777, visible=False, enable=True, minimapVisible=False)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=1000):
            return 유저이동(self.ctx)


class 실패(trigger_api.Trigger):
    def on_enter(self):
        self.end_mini_game_round(winnerBoxId=301)
        self.end_mini_game(winnerBoxId=301, gameName='finalsurvivor')
        self.unset_mini_game_area_for_hack() # 해킹 보안 종료
        self.set_event_ui(type=0, arg2='0,0')
        self.play_system_sound_in_box(boxIds=[301], sound='ME_001_Massive00_14')
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

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timerId='1'):
            return 실패계단보이기2(self.ctx)

    def on_exit(self):
        self.reset_timer(timerId='1')


class 실패계단보이기2(trigger_api.Trigger):
    def on_enter(self):
        self.set_mesh(triggerIds=[206,207,208,209,210], visible=True)
        self.set_actor(triggerId=256, visible=True, initialSequence='Eff_MassiveEvent_Stair_Opened')
        self.set_actor(triggerId=257, visible=True, initialSequence='Eff_MassiveEvent_Stair_Opened')
        self.set_actor(triggerId=258, visible=True, initialSequence='Eff_MassiveEvent_Stair_Opened')
        self.set_actor(triggerId=259, visible=True, initialSequence='Eff_MassiveEvent_Stair_Opened')
        self.set_actor(triggerId=260, visible=True, initialSequence='Eff_MassiveEvent_Stair_Opened')
        self.set_timer(timerId='1', seconds=1)

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timerId='1'):
            return 유저이동(self.ctx)

    def on_exit(self):
        self.set_mesh(triggerIds=[211], visible=True)
        self.set_actor(triggerId=261, visible=True, initialSequence='Eff_MassiveEvent_Door_Opened')
        self.reset_timer(timerId='1')


class 유저이동(trigger_api.Trigger):
    def on_enter(self):
        self.set_event_ui(type=1, arg2='$61000007_ME__MAINPROCESS_SPRINGBEACH__23$', arg3='5000', arg4='0')

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=120000):
            self.move_user(mapId=0, portalId=0)
            return 종료(self.ctx)


class 종료(trigger_api.Trigger):
    pass


initial_state = 대기
