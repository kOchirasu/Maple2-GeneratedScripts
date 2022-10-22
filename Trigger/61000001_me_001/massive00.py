""" trigger/61000001_me_001/massive00.xml """
from common import *
import state


# 트랩마스터
class 대기(state.State):
    def on_tick(self) -> state.State:
        if user_detected(boxIds=[301]):
            return 퍼즐대기중()


class 퍼즐대기중(state.State):
    def on_enter(self):
        set_state(arg1=1, arg2=['퍼즐패턴10','퍼즐패턴11','퍼즐패턴12','퍼즐패턴13','퍼즐패턴14','퍼즐패턴15','퍼즐패턴16','퍼즐패턴17','퍼즐패턴18','퍼즐패턴19','퍼즐패턴20','퍼즐패턴21','퍼즐패턴22','퍼즐패턴23','퍼즐패턴24','퍼즐패턴25','퍼즐패턴26','퍼즐패턴27','퍼즐패턴28','퍼즐패턴29','퍼즐패턴30','퍼즐패턴31','퍼즐패턴32','퍼즐패턴33','퍼즐패턴34','퍼즐패턴35','퍼즐패턴36','퍼즐패턴37','퍼즐패턴38','퍼즐패턴39','퍼즐패턴40','퍼즐패턴41','퍼즐패턴42','퍼즐패턴43','퍼즐패턴44','퍼즐패턴45','퍼즐패턴46','퍼즐패턴47','퍼즐패턴48','퍼즐패턴49','퍼즐패턴50','퍼즐패턴51','퍼즐패턴52','퍼즐패턴53','퍼즐패턴54','퍼즐패턴55','퍼즐패턴56','퍼즐패턴57','퍼즐패턴58','퍼즐패턴59','퍼즐패턴60'], arg3=True)
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
        set_portal(portalId=777, visible=False, enabled=True, minimapVisible=True)
        set_portal(portalId=778, visible=True, enabled=True, minimapVisible=True)
        set_portal(portalId=779, visible=True, enabled=True, minimapVisible=True)

    def on_tick(self) -> state.State:
        if count_users(boxId=301, boxId=50):
            return 계단없애기()
        if wait_tick(waitTick=60000):
            return 계단없애기()


class 계단없애기(state.State):
    def on_enter(self):
        set_mini_game_area_for_hack(boxId=301) # 해킹 보안용 시작 box 설정
        set_actor(triggerId=261, visible=True, initialSequence='Eff_MassiveEvent_Door_Vanished')
        set_portal(portalId=777, visible=False, enabled=False, minimapVisible=False)
        set_timer(timerId='1', seconds=1)

    def on_tick(self) -> state.State:
        if time_expired(timerId='1'):
            return 계단없애기2()

    def on_exit(self):
        reset_timer(timerId='1')


class 계단없애기2(state.State):
    def on_enter(self):
        set_mesh(triggerIds=[206,207,208,209,210,211], visible=False)
        set_actor(triggerId=256, visible=True, initialSequence='Eff_MassiveEvent_Stair_Closed')
        set_actor(triggerId=257, visible=True, initialSequence='Eff_MassiveEvent_Stair_Closed')
        set_actor(triggerId=258, visible=True, initialSequence='Eff_MassiveEvent_Stair_Closed')
        set_actor(triggerId=259, visible=True, initialSequence='Eff_MassiveEvent_Stair_Closed')
        set_actor(triggerId=260, visible=True, initialSequence='Eff_MassiveEvent_Stair_Closed')
        set_actor(triggerId=261, visible=False, initialSequence='Eff_MassiveEvent_Door_Vanished')
        set_timer(timerId='1', seconds=1)

    def on_tick(self) -> state.State:
        if time_expired(timerId='1'):
            return 시작대기()

    def on_exit(self):
        reset_timer(timerId='1')


class 시작대기(state.State):
    def on_enter(self):
        set_state(arg1=1, arg2=['퍼즐패턴10','퍼즐패턴11','퍼즐패턴12','퍼즐패턴13','퍼즐패턴14','퍼즐패턴15','퍼즐패턴16','퍼즐패턴17','퍼즐패턴18','퍼즐패턴19','퍼즐패턴20','퍼즐패턴21','퍼즐패턴22','퍼즐패턴23','퍼즐패턴24','퍼즐패턴25','퍼즐패턴26','퍼즐패턴27','퍼즐패턴28','퍼즐패턴29','퍼즐패턴30','퍼즐패턴31','퍼즐패턴32','퍼즐패턴33','퍼즐패턴34','퍼즐패턴35','퍼즐패턴36','퍼즐패턴37','퍼즐패턴38','퍼즐패턴39','퍼즐패턴40','퍼즐패턴41','퍼즐패턴42','퍼즐패턴43','퍼즐패턴44','퍼즐패턴45','퍼즐패턴46','퍼즐패턴47','퍼즐패턴48','퍼즐패턴49','퍼즐패턴50','퍼즐패턴51','퍼즐패턴52','퍼즐패턴53','퍼즐패턴54','퍼즐패턴55','퍼즐패턴56','퍼즐패턴57','퍼즐패턴58','퍼즐패턴59','퍼즐패턴60'], arg3=True) # 퍼즐 패턴 섞기 종료
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
        set_timer(timerId='1', seconds=5)

    def on_tick(self) -> state.State:
        if time_expired(timerId='1'):
            return 멘트0()

    def on_exit(self):
        reset_timer(timerId='1')


class 멘트0(state.State):
    def on_enter(self):
        set_timer(timerId='1', seconds=5)
        play_system_sound_in_box(sound='ME_001_Massive00_00')
        set_event_ui(type=1, arg2='$61000001_ME_001__MASSIVE00__0$', arg3='6000') # 로그에서 해당 이벤트에 참여한 사람을 체크하기 위한 명령어 / 1=미니게임 이름, 2=타겟박스 id
        start_mini_game(boxId=301, round=5, gameName='trapmaster') # 트로피 / 1=타겟박스 id, 2=achieveType, 3=code에 들어갈 값
        set_achievement(triggerId=301, type='trigger', achieve='trapmaster_start')
        set_achievement(triggerId=301, type='trigger', achieve='dailyquest_start') # 길드 경험치 지급 / boxID="타겟박스id", 0이면 맵전체, type="GuildGainExp의 id" 2가 매시브이벤트
        give_guild_exp(boxId=0, type=2)

    def on_tick(self) -> state.State:
        if time_expired(timerId='1'):
            return 멘트1()

    def on_exit(self):
        reset_timer(timerId='1')


class 멘트1(state.State):
    def on_enter(self):
        set_timer(timerId='1', seconds=11)
        play_system_sound_in_box(sound='ME_001_Massive00_01')
        set_event_ui(type=1, arg2='$61000001_ME_001__MASSIVE00__1$', arg3='11000')

    def on_tick(self) -> state.State:
        if time_expired(timerId='1'):
            return 멘트2()

    def on_exit(self):
        reset_timer(timerId='1')


class 멘트2(state.State):
    def on_enter(self):
        set_timer(timerId='1', seconds=10)
        play_system_sound_in_box(sound='ME_001_Massive00_02')
        set_event_ui(type=1, arg2='$61000001_ME_001__MASSIVE00__2$', arg3='10000')

    def on_tick(self) -> state.State:
        if time_expired(timerId='1'):
            return 멘트3()

    def on_exit(self):
        reset_timer(timerId='1')


class 멘트3(state.State):
    def on_enter(self):
        set_timer(timerId='1', seconds=6)
        set_event_ui(type=0, arg2='1,5') # action name="PlaySystemSoundInBox" arg2="ME_001_Massive00_03"/
        show_count_ui(text='$61000001_ME_001__MASSIVE00__3$', stage=1, count=5)

    def on_tick(self) -> state.State:
        if time_expired(timerId='1'):
            return 퍼즐단계1()

    def on_exit(self):
        reset_timer(timerId='1')


class 퍼즐단계1(state.State):
    def on_enter(self):
        set_timer(timerId='99', seconds=14)
        use_state(arg1='1', arg2=False)
        start_mini_game_round(boxId=301, round=1)

    def on_tick(self) -> state.State:
        if time_expired(timerId='99'):
            return 퍼즐단계1정리()

    def on_exit(self):
        reset_timer(timerId='99')


class 퍼즐단계1정리(state.State):
    def on_enter(self):
        end_mini_game_round(winnerBoxId=301, expRate=0.2)
        set_timer(timerId='1', seconds=3)
        set_mesh(triggerIds=[1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36,37,38,39,40,41,42,43,44,45,46,47,48,49,50,51,52,53,54,55,56,57,58,59,60,61,62,63,64,65,66,67,68,69,70,71,72,73,74,75,76,77,78,79,80,81,82,83,84,85,86,87,88,89,90,91,92,93,94,95,96,97,98,99,100], visible=True)

    def on_tick(self) -> state.State:
        if time_expired(timerId='1'):
            return 퍼즐단계1종료()
        if not user_detected(boxIds=[301]):
            return 실패계단보이기()

    def on_exit(self):
        reset_timer(timerId='1')


class 퍼즐단계1종료(state.State):
    def on_tick(self) -> state.State:
        if user_detected(boxIds=[301]):
            set_event_ui(type=0, arg2='2,5')
            show_count_ui(text='$61000001_ME_001__MASSIVE00__4$', stage=2, count=5)
            return 퍼즐단계2대기()


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
        start_mini_game_round(boxId=301, round=2)
        set_timer(timerId='99', seconds=14)
        use_state(arg1='1', arg2=False)

    def on_tick(self) -> state.State:
        if time_expired(timerId='99'):
            return 퍼즐단계2정리()

    def on_exit(self):
        reset_timer(timerId='99')


class 퍼즐단계2정리(state.State):
    def on_enter(self):
        end_mini_game_round(winnerBoxId=301, expRate=0.2)
        set_timer(timerId='1', seconds=1)
        set_mesh(triggerIds=[1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36,37,38,39,40,41,42,43,44,45,46,47,48,49,50,51,52,53,54,55,56,57,58,59,60,61,62,63,64,65,66,67,68,69,70,71,72,73,74,75,76,77,78,79,80,81,82,83,84,85,86,87,88,89,90,91,92,93,94,95,96,97,98,99,100], visible=True)

    def on_tick(self) -> state.State:
        if time_expired(timerId='1'):
            return 퍼즐단계2종료()
        if not user_detected(boxIds=[301]):
            return 실패계단보이기()

    def on_exit(self):
        reset_timer(timerId='1')


class 퍼즐단계2종료(state.State):
    def on_tick(self) -> state.State:
        if user_detected(boxIds=[301]):
            set_event_ui(type=0, arg2='3,5')
            show_count_ui(text='$61000001_ME_001__MASSIVE00__5$', stage=3, count=5)
            return 퍼즐단계3대기()


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
        start_mini_game_round(boxId=301, round=3)
        set_timer(timerId='99', seconds=14)
        use_state(arg1='1', arg2=False)

    def on_tick(self) -> state.State:
        if time_expired(timerId='99'):
            return 퍼즐단계3정리()

    def on_exit(self):
        reset_timer(timerId='99')


class 퍼즐단계3정리(state.State):
    def on_enter(self):
        end_mini_game_round(winnerBoxId=301, expRate=0.2)
        set_timer(timerId='1', seconds=1)
        set_mesh(triggerIds=[1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36,37,38,39,40,41,42,43,44,45,46,47,48,49,50,51,52,53,54,55,56,57,58,59,60,61,62,63,64,65,66,67,68,69,70,71,72,73,74,75,76,77,78,79,80,81,82,83,84,85,86,87,88,89,90,91,92,93,94,95,96,97,98,99,100], visible=True)

    def on_tick(self) -> state.State:
        if time_expired(timerId='1'):
            return 퍼즐단계3종료()
        if not user_detected(boxIds=[301]):
            return 실패계단보이기()

    def on_exit(self):
        reset_timer(timerId='1')


class 퍼즐단계3종료(state.State):
    def on_tick(self) -> state.State:
        if user_detected(boxIds=[301]):
            set_event_ui(type=0, arg2='4,5')
            show_count_ui(text='$61000001_ME_001__MASSIVE00__6$', stage=4, count=5)
            return 퍼즐단계4대기()


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
        start_mini_game_round(boxId=301, round=4)
        set_timer(timerId='99', seconds=14)
        use_state(arg1='1', arg2=False)

    def on_tick(self) -> state.State:
        if time_expired(timerId='99'):
            return 퍼즐단계4정리()

    def on_exit(self):
        reset_timer(timerId='99')


class 퍼즐단계4정리(state.State):
    def on_enter(self):
        end_mini_game_round(winnerBoxId=301, expRate=0.2)
        set_timer(timerId='1', seconds=1)
        set_mesh(triggerIds=[1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36,37,38,39,40,41,42,43,44,45,46,47,48,49,50,51,52,53,54,55,56,57,58,59,60,61,62,63,64,65,66,67,68,69,70,71,72,73,74,75,76,77,78,79,80,81,82,83,84,85,86,87,88,89,90,91,92,93,94,95,96,97,98,99,100], visible=True)

    def on_tick(self) -> state.State:
        if time_expired(timerId='1'):
            return 퍼즐단계4종료()
        if not user_detected(boxIds=[301]):
            return 실패계단보이기()

    def on_exit(self):
        reset_timer(timerId='1')


class 퍼즐단계4종료(state.State):
    def on_tick(self) -> state.State:
        if user_detected(boxIds=[301]):
            set_event_ui(type=0, arg2='5,5')
            show_count_ui(text='$61000001_ME_001__MASSIVE00__7$', stage=5, count=5)
            return 퍼즐단계5대기()


class 퍼즐단계5대기(state.State):
    def on_enter(self):
        set_timer(timerId='1', seconds=6)

    def on_tick(self) -> state.State:
        if time_expired(timerId='1'):
            return 퍼즐단계5()

    def on_exit(self):
        reset_timer(timerId='1')


class 퍼즐단계5(state.State):
    def on_enter(self):
        start_mini_game_round(boxId=301, round=5)
        set_timer(timerId='99', seconds=14)
        use_state(arg1='1', arg2=False)

    def on_tick(self) -> state.State:
        if time_expired(timerId='99'):
            return 퍼즐단계5정리()

    def on_exit(self):
        reset_timer(timerId='99')


class 퍼즐단계5정리(state.State):
    def on_enter(self):
        end_mini_game_round(winnerBoxId=301, expRate=0.2)
        set_timer(timerId='1', seconds=1)

    def on_tick(self) -> state.State:
        if time_expired(timerId='1'):
            return 퍼즐단계5종료()
        if not user_detected(boxIds=[301]):
            return 실패계단보이기()

    def on_exit(self):
        reset_timer(timerId='1')


class 퍼즐단계5종료(state.State):
    def on_tick(self) -> state.State:
        if user_detected(boxIds=[301]):
            set_mesh(triggerIds=[1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36,37,38,39,40,41,42,43,44,45,46,47,48,49,50,51,52,53,54,55,56,57,58,59,60,61,62,63,64,65,66,67,68,69,70,71,72,73,74,75,76,77,78,79,80,81,82,83,84,85,86,87,88,89,90,91,92,93,94,95,96,97,98,99,100], visible=True)
            return 우승자카메라연출()
        if not user_detected(boxIds=[301]):
            return 실패계단보이기()


class 우승자카메라연출(state.State):
    def on_enter(self):
        mini_game_camera_direction(boxId=301, cameraId=901)
        set_event_ui(type=0, arg2='0,0')
        play_system_sound_in_box(boxIds=[301], sound='ME_001_Massive00_08')
        set_event_ui(type=3, arg2='$61000001_ME_001__MASSIVE00__8$', arg3='7000', arg4='301')
        set_event_ui(type=6, arg2='$61000001_ME_001__MASSIVE00__9$', arg3='7000', arg4='!301')

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=6000):
            set_local_camera(cameraId=901, enable=False)
            return 보상단계()


class 보상단계(state.State):
    def on_enter(self):
        add_buff(boxIds=[301], skillId=70000019, level=1)
        play_system_sound_in_box(boxIds=[301], sound='ME_001_Massive00_10')
        set_event_ui(type=3, arg2='$61000001_ME_001__MASSIVE00__10$', arg3='5000', arg4='301')
        set_event_ui(type=6, arg2='$61000001_ME_001__MASSIVE00__11$', arg3='5000', arg4='!301') # 로그에서 해당 이벤트에서 우승한 사람을 체크하기 위한 명령어 / 1=미니게임 이름, 2=타겟박스 id
        mini_game_give_reward(winnerBoxId=301, contentType='miniGame')
        end_mini_game(winnerBoxId=301, gameName='trapmaster') # 트로피 / 1=타겟박스 id, 2=achieveType, 3=code에 들어갈 값
        set_achievement(triggerId=301, type='trigger', achieve='trapmaster_win')

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=3000):
            return 퍼즐종료계단보이기()


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
        reset_timer(timerId='1')


class 퍼즐종료(state.State):
    def on_enter(self):
        unset_mini_game_area_for_hack() # 해킹 보안 종료
        set_mesh(triggerIds=[211], visible=True)
        set_actor(triggerId=261, visible=True, initialSequence='Eff_MassiveEvent_Door_Opened')
        set_event_ui(type=0, arg2='0,0')
        set_portal(portalId=777, visible=False, enabled=True, minimapVisible=True)

    def on_tick(self) -> state.State:
        if true(arg1=True):
            return 퍼즐종료2()


class 퍼즐종료2(state.State):
    def on_enter(self):
        set_timer(timerId='1', seconds=1)

    def on_tick(self) -> state.State:
        if time_expired(timerId='1'):
            return 유저이동()


# 퍼즐 패턴 시작
#  9시->12시 방향 패턴 
#  9시->12시 방향, 한줄씩 사라지는 패턴 
class 퍼즐패턴10(state.State):
    def on_enter(self):
        set_timer(timerId='1', seconds=14)
        set_mesh(triggerIds=[1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36,37,38,39,40,41,42,43,44,45,46,47,48,49,50,51,52,53,54,55,56,57,58,59,60,61,62,63,64,65,66,67,68,69,70,71,72,73,74,75,76,77,78,79,80,81,82,83,84,85,86,87,88,89,90], visible=False, arg3=0, arg4=100)


#  9시->12시 방향, 바깥에서 소용돌이로 빠지는 패턴 
class 퍼즐패턴11(state.State):
    def on_enter(self):
        set_timer(timerId='1', seconds=14)
        set_mesh(triggerIds=[1,2,3,4,5,6,7,8,9,10,20,30,40,50,60,70,80,90,100,99,98,97,96,95,94,93,92,91,81,71,61,51,41,31,21,11,12,13,14,15,16,17,18,19,29,39,49,59,69,79,89,88,87,86,85,84,83,82,72,62,52,42,32,22,23,24,25,26,27,28,38,48,58,68,78,77,76,75,74,73,63,53,43,33,34,35,36,37,47,57,67,66,65,64,54,44], visible=False, arg3=0, arg4=100)


#  9시->12시 방향, 숫자 2 모양으로 한줄씩 남기고 사라지는 패턴 
class 퍼즐패턴12(state.State):
    def on_enter(self):
        set_timer(timerId='1', seconds=14)
        set_mesh(triggerIds=[1,2,3,4,5,6,7,8,9,10,20,30,29,28,27,26,25,24,23,22,21,31,41,42,43,44,45,46,47,48,49,50,60,70,69,68,67,66,65,64,63,62,61,71,81,82,83,84,85,86,87,88,89,90,100], visible=False, arg3=0, arg4=100)


#  9시->12시 방향, 3시->6시 방향, 각각 한 방향에서 한줄씩 사라짐.
class 퍼즐패턴13(state.State):
    def on_enter(self):
        set_timer(timerId='1', seconds=14)
        set_mesh(triggerIds=[1,2,3,4,5,6,7,8,9,10,100,99,98,97,96,95,94,93,92,91,11,12,13,14,15,16,17,18,19,20,90,89,88,87,86,85,84,83,82,81,21,22,23,24,25,26,27,28,29,30,80,79,78,77,76,75,74,73,72,71,31,32,33,34,35,36,37,38,39,40,70,69,68,67,66,65,64,63,62,61], visible=False, arg3=0, arg4=100)


#  9시->12시 방향, 3시->6시 방향, 각각 한 방향에서 한줄씩 건너띄면서 한줄 씩 사라짐
class 퍼즐패턴14(state.State):
    def on_enter(self):
        set_timer(timerId='1', seconds=14)
        set_mesh(triggerIds=[1,2,3,4,5,6,7,8,9,10,100,99,98,97,96,95,94,93,92,91,21,22,23,24,25,26,27,28,29,30,80,79,78,77,76,75,74,73,72,71,41,42,43,44,45,46,47,48,49,50,60,59,58,57,56,55,54,53,52,51], visible=False, arg3=0, arg4=100)


#  9시->12시 방향, 바깥쪽에서 원 1개씩 사라짐, 중간에 1줄씩 건너뛰면서 원을 그리며 사라짐
class 퍼즐패턴15(state.State):
    def on_enter(self):
        set_timer(timerId='1', seconds=14)
        set_mesh(triggerIds=[1,2,3,4,5,6,7,8,9,10,20,30,40,50,60,70,80,90,100,99,98,97,96,95,94,93,92,91,81,71,61,51,41,31,21,11], visible=False, arg3=0, arg4=100)
        set_mesh(triggerIds=[23,24,25,26,27,28,38,48,58,68,78,77,76,75,74,73,63,53,43,33], visible=False, arg3=3600, arg4=100)
        set_mesh(triggerIds=[45,46,55,56], visible=False, arg3=5600, arg4=100)


#  9시->12시 방향, 12시->6시방향, 6시->3시 방향, 3시->9시 방향, 9시->6시방향, 그 후 시계 반대방향으로 원을 그림
class 퍼즐패턴16(state.State):
    def on_enter(self):
        set_timer(timerId='1', seconds=14)
        set_mesh(triggerIds=[1,2,3,4,5,6,7,8,9,10,19,28,37,46,55,64,73,82,91,92,93,94,95,96,97,98,99,100,89,78,67,56,45,34,23,12,11,21,31,41,51,61,71,81,83,84,85,86,87,88,90,80,70,60,50,40,30,20,18,17,16,15,14,13,22,32,42,52,62,72,74,75,76,77,79,69,59,49,39,29,27,26,25,24], visible=False, arg3=0, arg4=100)


#  9시->12시 방향, 12시->6시방향, 6시->3시 방향, Z형태가 된 후 안쪽으로 원을 그리며 사라짐
class 퍼즐패턴17(state.State):
    def on_enter(self):
        set_timer(timerId='1', seconds=14)
        set_mesh(triggerIds=[1,2,3,4,5,6,7,8,9,10,19,28,37,46,55,64,73,82,91,92,93,94,95,96,97,98,99,100,90,80,70,60,50,40,30,20,18,17,16,15,14,13,12,11,21,31,41,51,61,71,81,83,84,85,86,87,88,89,79,69,59,49,39,29,27,26,25,24,23,22,32,42,52,62,72,74,75,76,77,78,68,58,48,38,36,35,34,33,43,53,63,65,66,67], visible=False, arg3=0, arg4=100)


#  9시->12시 방향, 순서대로 S자로 사라지다가 다시 생겨남
class 퍼즐패턴18(state.State):
    def on_enter(self):
        set_timer(timerId='1', seconds=14)
        set_mesh(triggerIds=[1,2,3,4,5,6,7,8,9,10,20,19,18,17,16,15,14,13,12,11,21,22,23,24,25,26,27,28,29,30,40,39,38,37,36,35,34,33,32,31,41,42,43,44,45,46,47,48,49,50,60,59,58,57,56,55,54,53,52,51,61,62,63,64,65,66,67,68,69,70,80,79,78,77,76,75,74,73,72,71,81,82,83,84,85,86,87,88,89,90,91,92,93,94,95,96,97,98,99,100], visible=False, arg3=0, arg4=100)
        set_mesh(triggerIds=[10,9,8,7,6,5,4,3,2,1,11,12,13,14,15,16,17,18,19,20,30,29,28,27,26,25,24,23,22,21,31,32,33,34,35,36,37,38,39,40,50,49,48,47,46,45,44,43,42,41,51,52,53,54,55,56,57,58,59,60,70,69,68,67,66,65,64,63,62,61,71,72,73,74,75,76,77,78,79,80,90,89,88,87,86,85,84,83,82,81,91,92,93,94,95,96,97,98,99,100], visible=True, arg3=1200, arg4=100)


#  9시->12시 방향과 12시->9시방향 중앙 동시 패턴 
#  9시->12시 방향과 12시->9시방향 중앙 동시, 중앙 두 줄부터 S자로 차례대로 사라지는 패턴 
class 퍼즐패턴19(state.State):
    def on_enter(self):
        set_timer(timerId='1', seconds=14)
        set_mesh(triggerIds=[41,42,43,44,45,46,47,48,49,50,40,39,38,37,36,35,34,33,32,31,21,22,23,24,25,26,27,28,29,30,20,19,18,17,16,15,14,13,12,11], visible=False, arg3=0, arg4=100)
        set_mesh(triggerIds=[60,59,58,57,56,55,54,53,52,51,61,62,63,64,65,66,67,68,69,70,80,79,78,77,76,75,74,73,72,71,81,82,83,84,85,86,87,88,89,90], visible=False, arg3=0, arg4=100)


#  9시->12시 방향과 12시->9시방향 중앙 동시, 중앙 두 줄부터 서로 원을 그리며 사라지는 패턴
class 퍼즐패턴20(state.State):
    def on_enter(self):
        set_timer(timerId='1', seconds=14)
        set_mesh(triggerIds=[41,42,43,44,45,46,47,48,49,50,40,30,20,10,9,8,7,6,5,4,3,2,1,11,21,31,32,33,34,35,36,37,38,39,29,19,18,17,16,15,14,13,12,22], visible=False, arg3=0, arg4=100)
        set_mesh(triggerIds=[60,59,58,57,56,55,54,53,52,51,61,71,81,91,92,93,94,95,96,97,98,99,100,90,80,70,69,68,67,66,65,64,63,62,72,82,83,84,85,86,87,88,89,79], visible=False, arg3=0, arg4=100)


#  9시->12시 방향과 12시->9시방향 중앙 동시, 중앙 두 줄부터 각각 12시, 3시 방향으로 반으로 나뉜 공간을 작은 S자 형태로 없앰 
class 퍼즐패턴21(state.State):
    def on_enter(self):
        set_timer(timerId='1', seconds=14)
        set_mesh(triggerIds=[41,42,43,44,45,46,47,48,49,50,40,30,20,10,9,19,29,39,38,28,18,8,7,17,27,37,36,26,16,6,5,15,25,35,34,24,14,4,3,13,23,33,32,22,12,2], visible=False, arg3=0, arg4=100)
        set_mesh(triggerIds=[60,59,58,57,56,55,54,53,52,51,61,71,81,91,92,82,72,62,63,73,83,93,94,84,74,64,65,75,85,95,96,86,76,66,67,77,87,97,98,88,78,68,69,79,89,99], visible=False, arg3=0, arg4=100)


#  9시->12시 방향과 12시->9시방향 중앙 동시, 중앙 두 줄부터 각각 12시, 3시 방향으로 반으로 나뉜 공간을 큰 S자 형태로 없앰 
class 퍼즐패턴22(state.State):
    def on_enter(self):
        set_timer(timerId='1', seconds=14)
        set_mesh(triggerIds=[41,42,43,44,45,46,47,48,49,50,40,30,20,10,9,8,7,6,5,4,3,2,1,11,12,13,14,15,16,17,18,19,29,28,27,26,25,24,23,22,21,31], visible=False, arg3=0, arg4=100)
        set_mesh(triggerIds=[60,59,58,57,56,55,54,53,52,51,61,71,81,91,92,93,94,95,96,97,98,99,100,90,89,88,87,86,85,84,83,82,72,73,74,75,76,77,78,79,80,70], visible=False, arg3=0, arg4=100)


#  9시->12시 방향과 12시->9시방향 중앙 동시, 중앙 두 줄부터 각각 끝과 안쪽이 차례대로 한줄씩 사라짐 
class 퍼즐패턴23(state.State):
    def on_enter(self):
        set_timer(timerId='1', seconds=14)
        set_mesh(triggerIds=[41,42,43,44,45,46,47,48,49,50,1,2,3,4,5,6,7,8,9,10,31,32,33,34,35,36,37,38,39,40,11,12,13,14,15,16,17,18,19,20], visible=False, arg3=0, arg4=100)
        set_mesh(triggerIds=[60,59,58,57,56,55,54,53,52,51,100,99,98,97,96,95,94,93,92,91,70,69,68,67,66,65,64,63,62,61,90,89,88,87,86,85,84,83,82,81], visible=False, arg3=0, arg4=100)


#  9시->12시 방향과 12시->9시방향 중앙 동시, 한줄씩 사라지면서 다시 생성됨 
class 퍼즐패턴24(state.State):
    def on_enter(self):
        set_timer(timerId='1', seconds=14)
        set_mesh(triggerIds=[41,42,43,44,45,46,47,48,49,50,31,32,33,34,35,36,37,38,39,40,21,22,23,24,25,26,27,28,29,30,11,12,13,14,15,16,17,18,19,20,1,2,3,4,5,6,7,8,9,10], visible=False, arg3=0, arg4=100)
        set_mesh(triggerIds=[50,49,48,47,46,45,44,43,42,41,40,39,38,37,36,35,34,33,32,31,30,29,28,27,26,25,24,23,22,21,20,19,18,17,16,15,14,13,12,11,10,9,8,7,6,5,4,3,2,1], visible=True, arg3=1200, arg4=100)
        set_mesh(triggerIds=[60,59,58,57,56,55,54,53,52,51,70,69,68,67,66,65,64,63,62,61,80,79,78,77,76,75,74,73,72,71,90,89,88,87,86,85,84,83,82,81,100,99,98,97,96,95,94,93,92,91], visible=False, arg3=0, arg4=100)
        set_mesh(triggerIds=[51,52,53,54,55,56,57,58,59,60,61,62,63,64,65,66,67,68,69,70,71,72,73,74,75,76,77,78,79,80,81,82,83,84,85,86,87,88,89,90,91,92,93,94,95,96,97,98,99,100], visible=True, arg3=1200, arg4=100)


# 같은 색상 별로 띄엄띄엄 사라짐 패턴 
#  같은 색상 별로 띄엄띄엄 사라짐, 12시 방향에서 6시 방향으로 노란색이 사라짐 
class 퍼즐패턴25(state.State):
    def on_enter(self):
        set_timer(timerId='1', seconds=14)
        set_timer(timerId='1', seconds=10)
        set_mesh(triggerIds=[10], visible=False, arg3=0, arg4=0)
        set_mesh(triggerIds=[8,19,30], visible=False, arg3=500, arg4=0)
        set_mesh(triggerIds=[6,17,28,39,50], visible=False, arg3=1000, arg4=0)
        set_mesh(triggerIds=[4,15,26,37,48,59,70], visible=False, arg3=1500, arg4=0)
        set_mesh(triggerIds=[2,13,24,35,46,57,68,79,90], visible=False, arg3=2000, arg4=0)
        set_mesh(triggerIds=[11,22,33,44,55,66,77,88,99], visible=False, arg3=2500, arg4=0)
        set_mesh(triggerIds=[31,42,53,64,75,86,97], visible=False, arg3=3000, arg4=0)
        set_mesh(triggerIds=[51,62,73,84,95], visible=False, arg3=3500, arg4=0)
        set_mesh(triggerIds=[71,82,93], visible=False, arg3=4000, arg4=0)
        set_mesh(triggerIds=[91], visible=False, arg3=4500, arg4=0)


#  같은 색상 별로 띄엄띄엄 사라짐, 12시->3시 방향의 가로가 사라짐, 노란색이 사라지다가, 중간부터 반대편의 흰색이 사라짐 
class 퍼즐패턴26(state.State):
    def on_enter(self):
        set_timer(timerId='1', seconds=14)
        set_mesh(triggerIds=[10,30,50,70,90], visible=False, arg3=0, arg4=0)
        set_mesh(triggerIds=[19,39,59,79,99], visible=False, arg3=500, arg4=0)
        set_mesh(triggerIds=[8,28,48,68,88], visible=False, arg3=1000, arg4=0)
        set_mesh(triggerIds=[17,37,57,77,97], visible=False, arg3=1500, arg4=0)
        set_mesh(triggerIds=[6,26,46,66,86], visible=False, arg3=2000, arg4=0)
        set_mesh(triggerIds=[1,21,41,61,81], visible=False, arg3=2500, arg4=0)
        set_mesh(triggerIds=[12,32,52,72,92], visible=False, arg3=3000, arg4=0)
        set_mesh(triggerIds=[3,23,43,63,83], visible=False, arg3=3500, arg4=0)
        set_mesh(triggerIds=[14,34,54,74,94], visible=False, arg3=4000, arg4=0)
        set_mesh(triggerIds=[5,25,45,65,85], visible=False, arg3=4500, arg4=0)


#  같은 색상 별로 띄엄띄엄 사라짐, 12시->3시 방향의 가로가 사라짐, 노란색이 차례대로 계속 사라짐 
class 퍼즐패턴27(state.State):
    def on_enter(self):
        set_timer(timerId='1', seconds=14)
        set_mesh(triggerIds=[10,30,50,70,90], visible=False, arg3=0, arg4=0)
        set_mesh(triggerIds=[19,39,59,79,99], visible=False, arg3=500, arg4=0)
        set_mesh(triggerIds=[8,28,48,68,88], visible=False, arg3=1000, arg4=0)
        set_mesh(triggerIds=[17,37,57,77,97], visible=False, arg3=1500, arg4=0)
        set_mesh(triggerIds=[6,26,46,66,86], visible=False, arg3=2000, arg4=0)
        set_mesh(triggerIds=[15,35,55,75,95], visible=False, arg3=2500, arg4=0)
        set_mesh(triggerIds=[4,24,44,64,84], visible=False, arg3=3000, arg4=0)
        set_mesh(triggerIds=[13,33,53,73,93], visible=False, arg3=3500, arg4=0)
        set_mesh(triggerIds=[2,22,42,62,82], visible=False, arg3=4000, arg4=0)
        set_mesh(triggerIds=[11,31,51,71,91], visible=False, arg3=4500, arg4=0)


# 12시 방향에서 쭉 내려오는 패턴
#  12시 방향에서 쭉 내려오는 패턴, 한 줄로 사라지면서 다시 나타나는 패턴 
class 퍼즐패턴28(state.State):
    def on_enter(self):
        set_timer(timerId='1', seconds=14)
        set_mesh(triggerIds=[10], visible=False, arg3=0, arg4=0)
        set_mesh(triggerIds=[9,20], visible=False, arg3=500, arg4=0)
        set_mesh(triggerIds=[8,19,30], visible=False, arg3=1000, arg4=0)
        set_mesh(triggerIds=[7,18,29,40], visible=False, arg3=1500, arg4=0)
        set_mesh(triggerIds=[6,17,28,39,50], visible=False, arg3=2000, arg4=0)
        set_mesh(triggerIds=[5,16,27,38,49,60], visible=False, arg3=2500, arg4=0)
        set_mesh(triggerIds=[4,15,26,37,48,59,70], visible=False, arg3=3000, arg4=0)
        set_mesh(triggerIds=[3,14,25,36,47,58,69,80], visible=False, arg3=3500, arg4=0)
        set_mesh(triggerIds=[2,13,24,35,46,57,68,79,90], visible=False, arg3=4000, arg4=0)
        set_mesh(triggerIds=[1,12,23,34,45,56,67,78,89,100], visible=False, arg3=4500, arg4=0)
        set_mesh(triggerIds=[11,22,33,44,55,66,77,88,99], visible=False, arg3=5000, arg4=0)
        set_mesh(triggerIds=[21,32,43,54,65,76,87,98], visible=False, arg3=5500, arg4=0)
        set_mesh(triggerIds=[31,42,53,64,75,86,97], visible=False, arg3=6000, arg4=0)
        set_mesh(triggerIds=[41,52,63,74,85,96], visible=False, arg3=6500, arg4=0)
        set_mesh(triggerIds=[51,62,73,84,95], visible=False, arg3=7000, arg4=0)
        set_mesh(triggerIds=[61,72,83,94], visible=False, arg3=7500, arg4=0)
        set_mesh(triggerIds=[71,82,93], visible=False, arg3=8000, arg4=0)
        set_mesh(triggerIds=[81,92], visible=False, arg3=8500, arg4=0)
        set_mesh(triggerIds=[91], visible=False, arg3=9000, arg4=0)
        set_mesh(triggerIds=[10], visible=True, arg3=1500, arg4=0)
        set_mesh(triggerIds=[9,20], visible=True, arg3=2000, arg4=0)
        set_mesh(triggerIds=[8,19,30], visible=True, arg3=2500, arg4=0)
        set_mesh(triggerIds=[7,18,29,40], visible=True, arg3=3000, arg4=0)
        set_mesh(triggerIds=[6,17,28,39,50], visible=True, arg3=3500, arg4=0)
        set_mesh(triggerIds=[5,16,27,38,49,60], visible=True, arg3=4000, arg4=0)
        set_mesh(triggerIds=[4,15,26,37,48,59,70], visible=True, arg3=4500, arg4=0)
        set_mesh(triggerIds=[3,14,25,36,47,58,69,80], visible=True, arg3=5000, arg4=0)
        set_mesh(triggerIds=[2,13,24,35,46,57,68,79,90], visible=True, arg3=5500, arg4=0)
        set_mesh(triggerIds=[1,12,23,34,45,56,67,78,89,100], visible=True, arg3=6000, arg4=0)
        set_mesh(triggerIds=[11,22,33,44,55,66,77,88,99], visible=True, arg3=6500, arg4=0)
        set_mesh(triggerIds=[21,32,43,54,65,76,87,98], visible=True, arg3=7000, arg4=0)
        set_mesh(triggerIds=[31,42,53,64,75,86,97], visible=True, arg3=7500, arg4=0)
        set_mesh(triggerIds=[41,52,63,74,85,96], visible=True, arg3=8000, arg4=0)
        set_mesh(triggerIds=[51,62,73,84,95], visible=True, arg3=8500, arg4=0)
        set_mesh(triggerIds=[61,72,83,94], visible=True, arg3=9000, arg4=0)
        set_mesh(triggerIds=[71,82,93], visible=True, arg3=9500, arg4=0)
        set_mesh(triggerIds=[81,92], visible=True, arg3=10000, arg4=0)
        set_mesh(triggerIds=[91], visible=True, arg3=10500, arg4=0)


#  12시 방향에서 쭉 내려오는 패턴, 12시 방향에서 내려오고 동시에 6시 방향에서 올라오면서 가운데 대각선만 남기는 패턴 
class 퍼즐패턴29(state.State):
    def on_enter(self):
        set_timer(timerId='1', seconds=14)
        set_mesh(triggerIds=[10], visible=False, arg3=0, arg4=0)
        set_mesh(triggerIds=[9,20], visible=False, arg3=500, arg4=0)
        set_mesh(triggerIds=[8,19,30], visible=False, arg3=1000, arg4=0)
        set_mesh(triggerIds=[7,18,29,40], visible=False, arg3=1500, arg4=0)
        set_mesh(triggerIds=[6,17,28,39,50], visible=False, arg3=2000, arg4=0)
        set_mesh(triggerIds=[5,16,27,38,49,60], visible=False, arg3=2500, arg4=0)
        set_mesh(triggerIds=[4,15,26,37,48,59,70], visible=False, arg3=3000, arg4=0)
        set_mesh(triggerIds=[3,14,25,36,47,58,69,80], visible=False, arg3=3500, arg4=0)
        set_mesh(triggerIds=[2,13,24,35,46,57,68,79,90], visible=False, arg3=4000, arg4=0)
        set_mesh(triggerIds=[11,22,33,44,55,66,77,88,99], visible=False, arg3=4000, arg4=0)
        set_mesh(triggerIds=[21,32,43,54,65,76,87,98], visible=False, arg3=3500, arg4=0)
        set_mesh(triggerIds=[31,42,53,64,75,86,97], visible=False, arg3=3000, arg4=0)
        set_mesh(triggerIds=[41,52,63,74,85,96], visible=False, arg3=2500, arg4=0)
        set_mesh(triggerIds=[51,62,73,84,95], visible=False, arg3=2000, arg4=0)
        set_mesh(triggerIds=[61,72,83,94], visible=False, arg3=1500, arg4=0)
        set_mesh(triggerIds=[71,82,93], visible=False, arg3=1000, arg4=0)
        set_mesh(triggerIds=[81,92], visible=False, arg3=500, arg4=0)
        set_mesh(triggerIds=[91], visible=False, arg3=0, arg4=0)


#  12시 방향에서 쭉 내려오는 패턴, ㅅ자 형태로 사라짐	 
class 퍼즐패턴30(state.State):
    def on_enter(self):
        set_timer(timerId='1', seconds=14)
        set_mesh(triggerIds=[10], visible=False, arg3=0, arg4=0)
        set_mesh(triggerIds=[9,8,7,6,5,4,3,2,1], visible=False, arg3=100, arg4=100)
        set_mesh(triggerIds=[20,30,40,50,60,70,80,90,100], visible=False, arg3=100, arg4=100)
        set_mesh(triggerIds=[19], visible=False, arg3=900, arg4=0)
        set_mesh(triggerIds=[18,17,16,15,14,13,12,11], visible=False, arg3=1000, arg4=100)
        set_mesh(triggerIds=[29,39,49,59,69,79,89,99], visible=False, arg3=1000, arg4=100)
        set_mesh(triggerIds=[28], visible=False, arg3=1700, arg4=0)
        set_mesh(triggerIds=[27,26,25,24,23,22,21], visible=False, arg3=1800, arg4=100)
        set_mesh(triggerIds=[38,48,58,68,78,88,98], visible=False, arg3=1800, arg4=100)
        set_mesh(triggerIds=[37], visible=False, arg3=2400, arg4=0)
        set_mesh(triggerIds=[36,35,34,33,32,31], visible=False, arg3=2500, arg4=100)
        set_mesh(triggerIds=[47,57,67,77,87,97], visible=False, arg3=2500, arg4=100)
        set_mesh(triggerIds=[46], visible=False, arg3=3000, arg4=0)
        set_mesh(triggerIds=[45,44,43,42,41], visible=False, arg3=3100, arg4=100)
        set_mesh(triggerIds=[56,66,76,86,96], visible=False, arg3=3100, arg4=100)
        set_mesh(triggerIds=[55], visible=False, arg3=3500, arg4=0)
        set_mesh(triggerIds=[54,53,52,51], visible=False, arg3=3600, arg4=100)
        set_mesh(triggerIds=[65,75,85,95], visible=False, arg3=3600, arg4=100)
        set_mesh(triggerIds=[64], visible=False, arg3=3900, arg4=0)
        set_mesh(triggerIds=[63,62,61], visible=False, arg3=4000, arg4=100)
        set_mesh(triggerIds=[74,84,94], visible=False, arg3=4000, arg4=100)
        set_mesh(triggerIds=[73], visible=False, arg3=4200, arg4=0)
        set_mesh(triggerIds=[72,71], visible=False, arg3=4300, arg4=100)
        set_mesh(triggerIds=[83,93], visible=False, arg3=4300, arg4=100)


#  12시 방향에서 쭉 내려오는 패턴, 12시 방향 및 6시 방향에서 번갈아서 ㅅ자 형태로 사라짐	 
class 퍼즐패턴31(state.State):
    def on_enter(self):
        set_timer(timerId='1', seconds=14)
        set_mesh(triggerIds=[10], visible=False, arg3=0, arg4=0)
        set_mesh(triggerIds=[9,8,7,6,5,4,3,2,1], visible=False, arg3=100, arg4=100)
        set_mesh(triggerIds=[20,30,40,50,60,70,80,90,100], visible=False, arg3=100, arg4=100)
        set_mesh(triggerIds=[91], visible=False, arg3=900, arg4=0)
        set_mesh(triggerIds=[81,71,61,51,41,31,21,11], visible=False, arg3=1000, arg4=100)
        set_mesh(triggerIds=[92,93,94,95,96,97,98,99], visible=False, arg3=1000, arg4=100)
        set_mesh(triggerIds=[19], visible=False, arg3=1700, arg4=0)
        set_mesh(triggerIds=[18,17,16,15,14,13,12], visible=False, arg3=1800, arg4=100)
        set_mesh(triggerIds=[29,39,49,59,69,79,89], visible=False, arg3=1800, arg4=100)
        set_mesh(triggerIds=[82], visible=False, arg3=2400, arg4=0)
        set_mesh(triggerIds=[72,62,52,42,32,22], visible=False, arg3=2500, arg4=100)
        set_mesh(triggerIds=[83,84,85,86,87,88], visible=False, arg3=2500, arg4=100)
        set_mesh(triggerIds=[28], visible=False, arg3=3000, arg4=0)
        set_mesh(triggerIds=[27,26,25,24,23], visible=False, arg3=3100, arg4=100)
        set_mesh(triggerIds=[38,48,58,68,78], visible=False, arg3=3100, arg4=100)
        set_mesh(triggerIds=[73], visible=False, arg3=3500, arg4=0)
        set_mesh(triggerIds=[63,53,43,33], visible=False, arg3=3600, arg4=100)
        set_mesh(triggerIds=[74,75,76,77], visible=False, arg3=3600, arg4=100)
        set_mesh(triggerIds=[37], visible=False, arg3=3900, arg4=0)
        set_mesh(triggerIds=[36,35,34], visible=False, arg3=4000, arg4=100)
        set_mesh(triggerIds=[47,57,67], visible=False, arg3=4000, arg4=100)
        set_mesh(triggerIds=[64], visible=False, arg3=4200, arg4=0)
        set_mesh(triggerIds=[54,44], visible=False, arg3=4300, arg4=100)
        set_mesh(triggerIds=[65,66], visible=False, arg3=4300, arg4=100)


#  12시 방향에서 쭉 내려오는 패턴, 12시 방향 및 6시 방향에서 번갈아서 한줄 씩 띄우고 ㅅ자 형태로 사라짐	 
class 퍼즐패턴32(state.State):
    def on_enter(self):
        set_timer(timerId='1', seconds=14)
        set_mesh(triggerIds=[10], visible=False, arg3=0, arg4=0)
        set_mesh(triggerIds=[9,8,7,6,5,4,3,2,1], visible=False, arg3=100, arg4=100)
        set_mesh(triggerIds=[20,30,40,50,60,70,80,90,100], visible=False, arg3=100, arg4=100)
        set_mesh(triggerIds=[91], visible=False, arg3=900, arg4=0)
        set_mesh(triggerIds=[81,71,61,51,41,31,21,11], visible=False, arg3=1000, arg4=100)
        set_mesh(triggerIds=[92,93,94,95,96,97,98,99], visible=False, arg3=1000, arg4=100)
        set_mesh(triggerIds=[28], visible=False, arg3=1700, arg4=0)
        set_mesh(triggerIds=[27,26,25,24,23,22], visible=False, arg3=1800, arg4=100)
        set_mesh(triggerIds=[38,48,58,68,78,88], visible=False, arg3=1800, arg4=100)
        set_mesh(triggerIds=[73], visible=False, arg3=2400, arg4=0)
        set_mesh(triggerIds=[63,53,43,33,13], visible=False, arg3=2500, arg4=100)
        set_mesh(triggerIds=[74,75,76,77,79], visible=False, arg3=2500, arg4=100)
        set_mesh(triggerIds=[46], visible=False, arg3=3000, arg4=0)
        set_mesh(triggerIds=[45,44,42], visible=False, arg3=3100, arg4=100)
        set_mesh(triggerIds=[56,66,86], visible=False, arg3=3100, arg4=100)
        set_mesh(triggerIds=[55], visible=False, arg3=3500, arg4=0)
        set_mesh(triggerIds=[35,15], visible=False, arg3=3600, arg4=100)
        set_mesh(triggerIds=[57,59], visible=False, arg3=3600, arg4=100)


#  12시에서 3시 방향으로 큐브가 사라짐, 1시 방향에서 7시 방향으로 각 열마다 큐브 하나씩만 대각선으로 남기면서 없어지는 패턴 
class 퍼즐패턴33(state.State):
    def on_enter(self):
        set_timer(timerId='1', seconds=14)
        set_mesh(triggerIds=[20,30,40,50,60,70,80,90,100], visible=False, arg3=0, arg4=0)
        set_mesh(triggerIds=[9,29,39,49,59,69,79,89,99], visible=False, arg3=500, arg4=0)
        set_mesh(triggerIds=[8,18,38,48,58,68,78,88,98], visible=False, arg3=1000, arg4=0)
        set_mesh(triggerIds=[7,17,27,47,57,67,77,87,97], visible=False, arg3=1500, arg4=0)
        set_mesh(triggerIds=[6,16,26,36,56,66,76,86,96], visible=False, arg3=2000, arg4=0)
        set_mesh(triggerIds=[5,15,25,35,45,65,75,85,95], visible=False, arg3=2500, arg4=0)
        set_mesh(triggerIds=[4,14,24,34,44,54,74,84,94], visible=False, arg3=3000, arg4=0)
        set_mesh(triggerIds=[3,13,23,33,43,53,63,83,93], visible=False, arg3=3500, arg4=0)
        set_mesh(triggerIds=[2,12,22,32,42,52,62,72,92], visible=False, arg3=4000, arg4=0)
        set_mesh(triggerIds=[1,11,21,31,41,51,61,71,81], visible=False, arg3=4500, arg4=0)


#  안쪽 사각형 부터 사라지는 패턴 
#  안쪽 사각형 부터 사라지는 패턴, 안쪽부터 소용돌이 모양을 그리며 바깥쪽으로 빠지는 패턴 
class 퍼즐패턴34(state.State):
    def on_enter(self):
        set_timer(timerId='1', seconds=14)
        set_mesh(triggerIds=[46,56,55,45,35,36,37,47,57,67,66,65,64,54,44,34,24,25,26,27,28,38,48,58,68,78,77,76,75,74,73,63,53,43,33,23,13,14,15,16,17,18,19,29,39,49,59,69,79,89,88,87,86,85,84,83,82,72,62,52,42,32,22,12], visible=False, arg3=0, arg4=100)


#  안쪽 사각형 부터 사라지는 패턴, 안쪽부터 소용돌이 모양을 그리며 한 줄씩 띄우고 바깥쪽으로 빠지는 패턴 
class 퍼즐패턴35(state.State):
    def on_enter(self):
        set_timer(timerId='1', seconds=14)
        set_mesh(triggerIds=[46,56,55,45,25,26,27,28,38,48,58,68,78,77,76,75,74,73,63,53,43,33,23,24,30,40,50,60,70,80,90,100,99,98,97,96,95,94,93,92,91,81,71,61,51,41,31,21,11,1,2,3,4,5,6,7,8,9,10,20], visible=False, arg3=0, arg4=100)


#  안쪽 사각형 부터 사라지는 패턴, 안쪽부터 4개가 먼저 사라진 후 바깥쪽으로 이동하여 바깥쪽부터 원을 그리며 사라지는 패턴 
class 퍼즐패턴36(state.State):
    def on_enter(self):
        set_timer(timerId='1', seconds=14)
        set_mesh(triggerIds=[46,56,55,45,35,25,15,5,6,7,8,9,10,20,30,40,50,60,70,80,90,100,99,98,97,96,95,94,93,92,91,81,71,61,51,41,31,21,11,12,13,14,15,16,17,18,19,29,39,49,59,69,79,89,88,87,86,85,84,83,82,72,62,52,42,32,22,23,24,25,26,27,28,38,48,58,68,78,77,76,75,74,73,63,53,43,33,34,35,36,37,47,57,67,66,65,64,54,44], visible=False, arg3=0, arg4=100)


#  안쪽 사각형 부터 사라지는 패턴, 안쪽부터 4개가 먼저 사라진 후 서로 마주보며 U자 형태로 사라짐 
class 퍼즐패턴37(state.State):
    def on_enter(self):
        set_timer(timerId='1', seconds=14)
        set_mesh(triggerIds=[46,56,55,45,64,54,44,34,35,36,37,47,57,67,28,38,48,58,68,78,77,76,75,74,73,63,53,43,33,23,82,72,62,52,42,32,22,12,13,14,15,16,17,18,19,29,39,49,59,69,79,89,10,20,30,40,50,60,70,80,90,100,99,98,97,96,95,94,93,92,91,81,71,61,51,41,31,21,11,1], visible=False, arg3=0, arg4=100)


#  가운데서 사방으로 퍼져나가는 패턴 
#  가운데서 사방으로 퍼져나가는 패턴, 가운데서 사방으로 퍼져가면서 v자 모양으로 사라짐 
class 퍼즐패턴38(state.State):
    def on_enter(self):
        set_timer(timerId='1', seconds=14)
        set_mesh(triggerIds=[45,34,23,12,1], visible=False, arg3=0, arg4=200)
        set_mesh(triggerIds=[46,37,28,19,10], visible=False, arg3=0, arg4=200)
        set_mesh(triggerIds=[56,67,78,89,100], visible=False, arg3=0, arg4=200)
        set_mesh(triggerIds=[55,64,73,82,91], visible=False, arg3=0, arg4=200)
        set_mesh(triggerIds=[44,33,22,11], visible=False, arg3=1300, arg4=200)
        set_mesh(triggerIds=[35,24,13,2], visible=False, arg3=1300, arg4=200)
        set_mesh(triggerIds=[36,27,18,9], visible=False, arg3=1300, arg4=200)
        set_mesh(triggerIds=[47,38,29,20], visible=False, arg3=1300, arg4=200)
        set_mesh(triggerIds=[57,68,79,90], visible=False, arg3=1300, arg4=200)
        set_mesh(triggerIds=[66,77,88,99], visible=False, arg3=1300, arg4=200)
        set_mesh(triggerIds=[65,74,83,92], visible=False, arg3=1300, arg4=200)
        set_mesh(triggerIds=[54,63,72,81], visible=False, arg3=1300, arg4=200)
        set_mesh(triggerIds=[43,32,21], visible=False, arg3=2400, arg4=200)
        set_mesh(triggerIds=[25,14,3], visible=False, arg3=2400, arg4=200)
        set_mesh(triggerIds=[26,17,8], visible=False, arg3=2400, arg4=200)
        set_mesh(triggerIds=[48,39,30], visible=False, arg3=2400, arg4=200)
        set_mesh(triggerIds=[58,69,80], visible=False, arg3=2400, arg4=200)
        set_mesh(triggerIds=[76,87,98], visible=False, arg3=2400, arg4=200)
        set_mesh(triggerIds=[75,84,93], visible=False, arg3=2400, arg4=200)
        set_mesh(triggerIds=[53,62,71], visible=False, arg3=2400, arg4=200)
        set_mesh(triggerIds=[42,31], visible=False, arg3=3500, arg4=200)
        set_mesh(triggerIds=[15,4], visible=False, arg3=3500, arg4=200)
        set_mesh(triggerIds=[16,7], visible=False, arg3=3500, arg4=200)
        set_mesh(triggerIds=[49,40], visible=False, arg3=3500, arg4=200)
        set_mesh(triggerIds=[59,70], visible=False, arg3=3500, arg4=200)
        set_mesh(triggerIds=[86,97], visible=False, arg3=3500, arg4=200)
        set_mesh(triggerIds=[85,94], visible=False, arg3=3500, arg4=200)
        set_mesh(triggerIds=[52,61], visible=False, arg3=3500, arg4=200)


#  가운데서 사방으로 퍼져나가는 패턴, 가운데서 사방으로 퍼져가면서 v자 모양으로 사라짐 
class 퍼즐패턴39(state.State):
    def on_enter(self):
        set_timer(timerId='1', seconds=14)
        set_mesh(triggerIds=[45], visible=False, arg3=0, arg4=0)
        set_mesh(triggerIds=[35,25,15,5], visible=False, arg3=100, arg4=100)
        set_mesh(triggerIds=[44,43,42,41], visible=False, arg3=100, arg4=100)
        set_mesh(triggerIds=[46], visible=False, arg3=0, arg4=0)
        set_mesh(triggerIds=[36,26,16,6], visible=False, arg3=100, arg4=100)
        set_mesh(triggerIds=[47,48,49,50], visible=False, arg3=100, arg4=100)
        set_mesh(triggerIds=[56], visible=False, arg3=0, arg4=0)
        set_mesh(triggerIds=[57,58,59,60], visible=False, arg3=100, arg4=100)
        set_mesh(triggerIds=[66,76,86,96], visible=False, arg3=100, arg4=100)
        set_mesh(triggerIds=[55], visible=False, arg3=0, arg4=0)
        set_mesh(triggerIds=[65,75,85,95], visible=False, arg3=100, arg4=100)
        set_mesh(triggerIds=[54,53,52,51], visible=False, arg3=100, arg4=100)
        set_mesh(triggerIds=[64], visible=False, arg3=900, arg4=0)
        set_mesh(triggerIds=[74,84,94], visible=False, arg3=1000, arg4=100)
        set_mesh(triggerIds=[63,62,61], visible=False, arg3=1000, arg4=100)
        set_mesh(triggerIds=[34], visible=False, arg3=900, arg4=0)
        set_mesh(triggerIds=[33,32,31], visible=False, arg3=1000, arg4=100)
        set_mesh(triggerIds=[24,14,4], visible=False, arg3=1000, arg4=100)
        set_mesh(triggerIds=[37], visible=False, arg3=900, arg4=0)
        set_mesh(triggerIds=[38,39,40], visible=False, arg3=1000, arg4=100)
        set_mesh(triggerIds=[27,17,7], visible=False, arg3=1000, arg4=100)
        set_mesh(triggerIds=[67], visible=False, arg3=900, arg4=0)
        set_mesh(triggerIds=[77,87,97], visible=False, arg3=1000, arg4=100)
        set_mesh(triggerIds=[68,69,70], visible=False, arg3=1000, arg4=100)
        set_mesh(triggerIds=[73], visible=False, arg3=1700, arg4=0)
        set_mesh(triggerIds=[83,93], visible=False, arg3=1800, arg4=100)
        set_mesh(triggerIds=[72,71], visible=False, arg3=1800, arg4=100)
        set_mesh(triggerIds=[23], visible=False, arg3=1700, arg4=0)
        set_mesh(triggerIds=[22,21], visible=False, arg3=1800, arg4=100)
        set_mesh(triggerIds=[13,3], visible=False, arg3=1800, arg4=100)
        set_mesh(triggerIds=[28], visible=False, arg3=1700, arg4=0)
        set_mesh(triggerIds=[18,8], visible=False, arg3=1800, arg4=100)
        set_mesh(triggerIds=[29,30], visible=False, arg3=1800, arg4=100)
        set_mesh(triggerIds=[78], visible=False, arg3=1700, arg4=0)
        set_mesh(triggerIds=[79,80], visible=False, arg3=1800, arg4=100)
        set_mesh(triggerIds=[88,98], visible=False, arg3=1800, arg4=100)
        set_mesh(triggerIds=[82], visible=False, arg3=2400, arg4=0)
        set_mesh(triggerIds=[81], visible=False, arg3=2500, arg4=100)
        set_mesh(triggerIds=[92], visible=False, arg3=2500, arg4=100)
        set_mesh(triggerIds=[12], visible=False, arg3=2400, arg4=0)
        set_mesh(triggerIds=[11], visible=False, arg3=2500, arg4=100)
        set_mesh(triggerIds=[2], visible=False, arg3=2500, arg4=100)
        set_mesh(triggerIds=[19], visible=False, arg3=2400, arg4=0)
        set_mesh(triggerIds=[20], visible=False, arg3=2500, arg4=100)
        set_mesh(triggerIds=[9], visible=False, arg3=2500, arg4=100)
        set_mesh(triggerIds=[89], visible=False, arg3=2400, arg4=0)
        set_mesh(triggerIds=[99], visible=False, arg3=2500, arg4=100)
        set_mesh(triggerIds=[90], visible=False, arg3=2500, arg4=100)


#  12시->6시방향으로 사라짐
#  12시->6시방향으로 사라짐, 한 줄로 땅이 갈라진 후 바깥쪽으로 확대되는 패턴 
class 퍼즐패턴40(state.State):
    def on_enter(self):
        set_timer(timerId='1', seconds=14)
        set_mesh(triggerIds=[10,19,28,37,46,55,64,73,82,91], visible=False, arg3=0, arg4=100)
        set_mesh(triggerIds=[9,18,27,36,45,54,63,72,81,20,29,38,47,56,65,74,83,92], visible=False, arg3=1000, arg4=0)
        set_mesh(triggerIds=[8,17,26,35,44,53,62,71,30,39,48,57,66,75,84,93], visible=False, arg3=1500, arg4=0)
        set_mesh(triggerIds=[7,16,25,34,43,52,61,40,49,58,67,76,85,94], visible=False, arg3=2000, arg4=0)
        set_mesh(triggerIds=[6,15,24,33,42,51,50,59,68,77,86,95], visible=False, arg3=2500, arg4=0)
        set_mesh(triggerIds=[5,14,23,32,41,60,69,78,87,96], visible=False, arg3=2500, arg4=0)
        set_mesh(triggerIds=[4,13,22,31,70,79,88,97], visible=False, arg3=3000, arg4=0)
        set_mesh(triggerIds=[3,12,21,80,89,98], visible=False, arg3=3500, arg4=0)
        set_mesh(triggerIds=[2,11,90,99], visible=False, arg3=4000, arg4=0)


#  12시->6시방향으로 사라짐, 한 줄로 땅이 갈라진 후 바깥쪽으로 확대되는 패턴 
class 퍼즐패턴41(state.State):
    def on_enter(self):
        set_timer(timerId='1', seconds=14)
        set_mesh(triggerIds=[10,19,28,37,46,55,64,73,82,91], visible=False, arg3=0, arg4=100)
        set_mesh(triggerIds=[81,71,61,51,41,31,21,11,1,2,3,4,5,6,7,8,9,18,27,36,45,54,63,72,62,52,42,32,22,12,13,14,15,16,17,26,35,44,53,43,33,23], visible=False, arg3=1000, arg4=100)
        set_mesh(triggerIds=[92,93,94,95,96,97,98,99,100,90,80,70,60,50,40,30,20,29,38,47,56,65,74,83,84,85,86,87,88,89,79,69,59,49,39,48,57,66,75,76,77,78], visible=False, arg3=1000, arg4=100)


#  12시->6시방향으로 사라짐, 한 줄로 땅이 갈라진 후 안쪽으로 원을 만들면서 사라지는 패턴 
class 퍼즐패턴42(state.State):
    def on_enter(self):
        set_timer(timerId='1', seconds=14)
        set_mesh(triggerIds=[10,19,28,37,46,55,64,73,82,91], visible=False, arg3=0, arg4=100)
        set_mesh(triggerIds=[81,71,61,51,41,31,21,11,1,2,3,4,5,6,7,8,9,20,30,40,50,60,70,80,90,100,99,98,97,96,95,94,93,92,72,62,52,42,32,22,12,13,14,15,16,17,18,29,39,49,59,69,79,89,88,87,86,85,84,83,63,53,43,33,23,24,25,26,27,38,48,58,68,78,77,76,75,74,54,44,34,35,36,47,57,67,66,65], visible=False, arg3=1000, arg4=100)


class 퍼즐패턴43(state.State):
    def on_enter(self):
        set_timer(timerId='1', seconds=14)
        set_mesh(triggerIds=[10], visible=False, arg3=0, arg4=0)
        set_mesh(triggerIds=[91], visible=False, arg3=100, arg4=0)
        set_mesh(triggerIds=[9,20], visible=False, arg3=200, arg4=100)
        set_mesh(triggerIds=[81,92], visible=False, arg3=400, arg4=100)
        set_mesh(triggerIds=[8,19,30], visible=False, arg3=600, arg4=100)
        set_mesh(triggerIds=[71,82,93], visible=False, arg3=900, arg4=100)
        set_mesh(triggerIds=[7,18,29,40], visible=False, arg3=1200, arg4=100)
        set_mesh(triggerIds=[61,72,83,94], visible=False, arg3=1600, arg4=100)
        set_mesh(triggerIds=[6,17,28,39,50], visible=False, arg3=2000, arg4=100)
        set_mesh(triggerIds=[51,62,73,84,95], visible=False, arg3=2500, arg4=100)
        set_mesh(triggerIds=[5,16,27,38,49,60], visible=False, arg3=3000, arg4=100)
        set_mesh(triggerIds=[41,52,63,74,85,96], visible=False, arg3=3600, arg4=100)
        set_mesh(triggerIds=[4,15,26,37,48,59,70], visible=False, arg3=4200, arg4=100)
        set_mesh(triggerIds=[31,42,53,64,75,86,97], visible=False, arg3=4900, arg4=100)
        set_mesh(triggerIds=[3,14,25,36,47,58,69,80], visible=False, arg3=5600, arg4=100)
        set_mesh(triggerIds=[21,32,43,54,65,76,87,98], visible=False, arg3=6400, arg4=100)
        set_mesh(triggerIds=[2,13,24,35,46,57,68,79,90], visible=False, arg3=7200, arg4=100)
        set_mesh(triggerIds=[11,22,33,44,55,66,77,88,99], visible=False, arg3=8100, arg4=100)


class 퍼즐패턴44(state.State):
    def on_enter(self):
        set_timer(timerId='1', seconds=14)
        set_mesh(triggerIds=[10], visible=False, arg3=0, arg4=0)
        set_mesh(triggerIds=[9,8,7,6,5,4,3,2,1], visible=False, arg3=100, arg4=100)
        set_mesh(triggerIds=[20,30,40,50,60,70,80,90,100], visible=False, arg3=1000, arg4=100)
        set_mesh(triggerIds=[91], visible=False, arg3=1900, arg4=0)
        set_mesh(triggerIds=[81,71,61,51,41,31,21,11], visible=False, arg3=2000, arg4=100)
        set_mesh(triggerIds=[92,93,94,95,96,97,98,99], visible=False, arg3=2800, arg4=100)
        set_mesh(triggerIds=[19], visible=False, arg3=3600, arg4=0)
        set_mesh(triggerIds=[18,17,16,15,14,13,12], visible=False, arg3=3700, arg4=100)
        set_mesh(triggerIds=[29,39,49,59,69,79,89], visible=False, arg3=4400, arg4=100)
        set_mesh(triggerIds=[82], visible=False, arg3=5100, arg4=0)
        set_mesh(triggerIds=[72,62,52,42,32,22], visible=False, arg3=5200, arg4=100)
        set_mesh(triggerIds=[83,84,85,86,87,88], visible=False, arg3=5800, arg4=100)
        set_mesh(triggerIds=[28], visible=False, arg3=6400, arg4=0)
        set_mesh(triggerIds=[27,26,25,24,23], visible=False, arg3=6500, arg4=100)
        set_mesh(triggerIds=[38,48,58,68,78], visible=False, arg3=7000, arg4=100)
        set_mesh(triggerIds=[73], visible=False, arg3=7500, arg4=0)
        set_mesh(triggerIds=[63,53,43,33], visible=False, arg3=7600, arg4=100)
        set_mesh(triggerIds=[74,75,76,77], visible=False, arg3=8000, arg4=100)
        set_mesh(triggerIds=[37], visible=False, arg3=8400, arg4=0)
        set_mesh(triggerIds=[36,35,34], visible=False, arg3=8500, arg4=100)
        set_mesh(triggerIds=[47,57,67], visible=False, arg3=8800, arg4=100)
        set_mesh(triggerIds=[64], visible=False, arg3=9100, arg4=0)
        set_mesh(triggerIds=[54,44], visible=False, arg3=9200, arg4=100)
        set_mesh(triggerIds=[65,66], visible=False, arg3=9400, arg4=100)


# 신규 추가 패턴
class 퍼즐패턴45(state.State):
    def on_enter(self):
        set_timer(timerId='1', seconds=14)
        set_mesh(triggerIds=[34,33,23,24], visible=False, arg3=0, arg4=100)
        set_mesh(triggerIds=[77,78,68,67], visible=False, arg3=400, arg4=100)
        set_mesh(triggerIds=[37,38,28,27], visible=False, arg3=800, arg4=100)
        set_mesh(triggerIds=[64,63,73,74], visible=False, arg3=1200, arg4=100)
        set_mesh(triggerIds=[55,45,46,56], visible=False, arg3=1600, arg4=100)
        set_mesh(triggerIds=[1,2,3,4,5,6,7,8,9,10], visible=False, arg3=2000, arg4=100)
        set_mesh(triggerIds=[20,30,40,50,60,70,80,90,100,99,98,97,96,95,94,93,92,91,81,71,61,51,41,31,21,11], visible=False, arg3=3000, arg4=100)
        set_mesh(triggerIds=[12,13,14,15,16,17,18,19], visible=False, arg3=5600, arg4=100)
        set_mesh(triggerIds=[29,39,49,59,69,79,89,88,87,86,85,84,83,82,72,62,52,42,32,22], visible=False, arg3=6400, arg4=100)


class 퍼즐패턴46(state.State):
    def on_enter(self):
        set_timer(timerId='1', seconds=14)
        set_mesh(triggerIds=[33,23,24,34], visible=False, arg3=0, arg4=100)
        set_mesh(triggerIds=[44,43,42,32,22,12,13,14,15,25,35,45], visible=False, arg3=400, arg4=100)
        set_mesh(triggerIds=[67,77,78,68,58,57,56,66,76,86,87,88,89,79,69,59], visible=False, arg3=1600, arg4=100)
        set_mesh(triggerIds=[37,38,28,27,26,36,46,47,48,49,39,29,19,18,17,16], visible=False, arg3=3200, arg4=100)
        set_mesh(triggerIds=[64,63,73,74,75,65,55,54,53,52,62,72,82,83,84,85], visible=False, arg3=4800, arg4=100)


class 퍼즐패턴47(state.State):
    def on_enter(self):
        set_timer(timerId='1', seconds=14)
        set_mesh(triggerIds=[33,23,24,34], visible=False, arg3=0, arg4=100)
        set_mesh(triggerIds=[44,43,42,32,22,12,13,14,15,25,35,45], visible=False, arg3=400, arg4=100)
        set_mesh(triggerIds=[55,54,53,52,51,41,31,21,11,1,2,3,4,5,6,16,26,36,46,56], visible=False, arg3=1600, arg4=100)
        set_mesh(triggerIds=[61,71,81,91,92,93,94,95,96,97,98,99,100], visible=False, arg3=3600, arg4=100)
        set_mesh(triggerIds=[90,80,70,60,50,40,30,20,10,9,8,7], visible=False, arg3=4900, arg4=100)
        set_mesh(triggerIds=[17,27,37,47,57,67,77,87,88,89,79,69,59,49,39,29,19,18,28,38,48,58,68,78,88], visible=False, arg3=6100, arg4=100)


class 퍼즐패턴48(state.State):
    def on_enter(self):
        set_timer(timerId='1', seconds=14)
        set_mesh(triggerIds=[33,23,24,34], visible=False, arg3=0, arg4=100)
        set_mesh(triggerIds=[44,43,42,32,22,12,13,14,15,25,35,45], visible=False, arg3=400, arg4=100)
        set_mesh(triggerIds=[55,54,53,52,51,41,31,21,11,1,2,3,4,5,6,16,26,36,46,56], visible=False, arg3=1600, arg4=100)
        set_mesh(triggerIds=[61,71,81,91,92,93,94,95,96,97,98,99,100], visible=False, arg3=3600, arg4=100)
        set_mesh(triggerIds=[90,80,70,60,50,40,30,20,10], visible=False, arg3=4900, arg4=100)
        set_mesh(triggerIds=[9,19,29,39,49,59,69,79,89,88,87,86,85,84,83,82,72,73,74,75,76,77,78,68,67,66,65,64,63,62], visible=False, arg3=5800, arg4=100)


class 퍼즐패턴49(state.State):
    def on_enter(self):
        set_timer(timerId='1', seconds=14)
        set_mesh(triggerIds=[34,33,23,24], visible=False, arg3=0, arg4=100)
        set_mesh(triggerIds=[77,78,68,67], visible=False, arg3=400, arg4=100)
        set_mesh(triggerIds=[45,44,43,42,32,22,12,13,14,15,25,35,56,57,58,59,69,79,89,88,87,86,76,66], visible=False, arg3=800, arg4=100)
        set_mesh(triggerIds=[55,54,53,52,51,41,31,21,11,1,2,3,4,5,6,16,26,36,46,47,48,49,50,60,70,80,90,100,99,98,97,96,95,85,75,65], visible=False, arg3=3200, arg4=100)
        set_mesh(triggerIds=[64], visible=False, arg3=7000, arg4=100)
        set_mesh(triggerIds=[37], visible=False, arg3=7000, arg4=100)
        set_mesh(triggerIds=[63,62,61], visible=False, arg3=7500, arg4=100)
        set_mesh(triggerIds=[74,84,94], visible=False, arg3=7500, arg4=100)
        set_mesh(triggerIds=[27,17,7], visible=False, arg3=7500, arg4=100)
        set_mesh(triggerIds=[38,39,40], visible=False, arg3=7500, arg4=100)
        set_mesh(triggerIds=[28], visible=False, arg3=7700, arg4=100)
        set_mesh(triggerIds=[73], visible=False, arg3=7700, arg4=100)
        set_mesh(triggerIds=[18,8], visible=False, arg3=8200, arg4=100)
        set_mesh(triggerIds=[29,30], visible=False, arg3=8200, arg4=100)
        set_mesh(triggerIds=[72,71], visible=False, arg3=8200, arg4=100)
        set_mesh(triggerIds=[83,93], visible=False, arg3=8200, arg4=100)


class 퍼즐패턴50(state.State):
    def on_enter(self):
        set_timer(timerId='1', seconds=14)
        set_mesh(triggerIds=[34,33,23,24], visible=False, arg3=0, arg4=100)
        set_mesh(triggerIds=[77,78,68,67], visible=False, arg3=400, arg4=100)
        set_mesh(triggerIds=[37,38,28,27,64,63,73,74], visible=False, arg3=1000, arg4=100)
        set_mesh(triggerIds=[82,81,91,92,19,20,10,9], visible=False, arg3=2100, arg4=100)
        set_mesh(triggerIds=[12,11,1,2,89,90,99,100], visible=False, arg3=3200, arg4=100)
        set_mesh(triggerIds=[15,5,6,16,86,96,85,95], visible=False, arg3=4300, arg4=100)
        set_mesh(triggerIds=[42,41,51,52,59,60,50,49], visible=False, arg3=5400, arg4=100)
        set_mesh(triggerIds=[55,45,46,56], visible=False, arg3=6500, arg4=100)


class 퍼즐패턴51(state.State):
    def on_enter(self):
        set_timer(timerId='1', seconds=14)
        set_mesh(triggerIds=[34,33,23,24], visible=False, arg3=0, arg4=100)
        set_mesh(triggerIds=[77,78,68,67], visible=False, arg3=400, arg4=100)
        set_mesh(triggerIds=[37,38,28,27,64,63,73,74], visible=False, arg3=1000, arg4=100)
        set_mesh(triggerIds=[82,83,93,92,91,81,71,72,19,18,8,9,10,20,30,29], visible=False, arg3=2100, arg4=100)
        set_mesh(triggerIds=[12,22,21,11,1,2,3,13,89,79,80,90,100,99,98,88], visible=False, arg3=3700, arg4=100)
        set_mesh(triggerIds=[15,5,6,16,86,96,85,95], visible=False, arg3=5300, arg4=100)
        set_mesh(triggerIds=[42,41,51,52,59,60,50,49], visible=False, arg3=6400, arg4=100)
        set_mesh(triggerIds=[55,45,46,56], visible=False, arg3=7500, arg4=100)
        set_mesh(triggerIds=[66,65,54,44,35,36,47,57], visible=False, arg3=8100, arg4=100)


class 퍼즐패턴52(state.State):
    def on_enter(self):
        set_timer(timerId='1', seconds=14)
        set_mesh(triggerIds=[1], visible=False, arg3=0, arg4=100)
        set_mesh(triggerIds=[13,12,2,3], visible=False, arg3=100, arg4=100)
        set_mesh(triggerIds=[15,16,26,25,24,14,4,5,6], visible=False, arg3=500, arg4=100)
        set_mesh(triggerIds=[18,19,29,28,27,17,7,8,9,10,20,30,40,39,38,37], visible=False, arg3=1400, arg4=100)
        set_mesh(triggerIds=[68,58,59,69,79,78,77,67,57,47,48,49,50,60,70,80,90,89,88,87,86,76,66,56,46], visible=False, arg3=3000, arg4=100)
        set_mesh(triggerIds=[73,74,84,83,82,72,62,63,64,65,75,85,95,94,93,92], visible=False, arg3=5500, arg4=100)
        set_mesh(triggerIds=[42,43,53,52,51,41,31,32,33], visible=False, arg3=7100, arg4=100)
        set_mesh(triggerIds=[44,34,35,45], visible=False, arg3=8000, arg4=100)
        set_mesh(triggerIds=[55], visible=False, arg3=8400, arg4=100)


class 퍼즐패턴53(state.State):
    def on_enter(self):
        set_timer(timerId='1', seconds=14)
        set_mesh(triggerIds=[1], visible=False, arg3=0, arg4=100)
        set_mesh(triggerIds=[13,12,2,3], visible=False, arg3=100, arg4=100)
        set_mesh(triggerIds=[15,16,26,25,24,14,4,5,6], visible=False, arg3=500, arg4=100)
        set_mesh(triggerIds=[18,19,29,28,27,17,7,8,9,10,20,30,40,39,38,37], visible=False, arg3=1400, arg4=100)
        set_mesh(triggerIds=[68,58,59,69,79,78,77,67,57,47,48,49,50,60,70,80,90,89,88,87,86,76,66,56,46], visible=False, arg3=3000, arg4=100)
        set_mesh(triggerIds=[96], visible=False, arg3=5500, arg4=100)
        set_mesh(triggerIds=[95,94,84,85], visible=False, arg3=5600, arg4=100)
        set_mesh(triggerIds=[82,83,93,92,91,81,71,72,73], visible=False, arg3=6000, arg4=100)
        set_mesh(triggerIds=[52,42,43,53,63,62,61,51,41,31,32,33,34,44,54,64], visible=False, arg3=6900, arg4=100)


class 퍼즐패턴54(state.State):
    def on_enter(self):
        set_timer(timerId='1', seconds=14)
        set_mesh(triggerIds=[1,100], visible=False, arg3=0, arg4=100)
        set_mesh(triggerIds=[13,12,2,3,88,89,99,98], visible=False, arg3=200, arg4=100)
        set_mesh(triggerIds=[15,16,26,25,24,14,4,5,6,86,85,75,76,77,87,97,96,95], visible=False, arg3=1000, arg4=100)
        set_mesh(triggerIds=[18,19,29,28,27,17,7,8,9,10,20,30,40,39,38,37,83,82,72,73,74,84,94,93,92,91,81,71,61,62,63,64], visible=False, arg3=2800, arg4=100)
        set_mesh(triggerIds=[50,51], visible=False, arg3=6000, arg4=100)
        set_mesh(triggerIds=[60,70,69,59,41,31,32,42], visible=False, arg3=6200, arg4=100)
        set_mesh(triggerIds=[57,58,68,67,66,56,46,47,48,44,43,33,34,35,45,55,54,53], visible=False, arg3=7000, arg4=100)


class 퍼즐패턴55(state.State):
    def on_enter(self):
        set_timer(timerId='1', seconds=14)
        set_mesh(triggerIds=[1,100], visible=False, arg3=0, arg4=100)
        set_mesh(triggerIds=[13,12,2,3,88,89,99,98], visible=False, arg3=200, arg4=100)
        set_mesh(triggerIds=[15,16,26,25,24,14,4,5,6,86,85,75,76,77,87,97,96,95], visible=False, arg3=1000, arg4=100)
        set_mesh(triggerIds=[18,19,29,28,27,17,7,8,9,10,20,30,40,39,38,37,83,82,72,73,74,84,94,93,92,91,81,71,61,62,63,64], visible=False, arg3=2800, arg4=100)
        set_mesh(triggerIds=[59,60,70,69,68,58,48,49,50,42,41,31,32,33,43,53,52,51], visible=False, arg3=6000, arg4=100)
        set_mesh(triggerIds=[56,57,67,66,45,44,34,35], visible=False, arg3=7800, arg4=100)
        set_mesh(triggerIds=[46,55], visible=False, arg3=8600, arg4=100)


class 퍼즐패턴56(state.State):
    def on_enter(self):
        set_timer(timerId='1', seconds=14)
        set_mesh(triggerIds=[1,2,3,4,5,6,7,8,9,10,20,30,40,50,60,70,80,90,100,99,98,97,96,95,94,93,92,91,81,71,61,51,41,31,21,11,12,13,14,15,16,17,18,19,29,69,79,89,88,87,84,83,82,72,62,22,25,26,38,48,58,78,76,75,73,53,43,33,34,37,47,57,67,66,65,64,54,44,45,46,56,55], visible=False, arg3=0, arg4=100)


class 퍼즐패턴57(state.State):
    def on_enter(self):
        set_timer(timerId='1', seconds=14)
        set_mesh(triggerIds=[1,2,3,4,5,6,8,9,10,20,30,40,50,90,100,99,92,91,81,41,31,21,11,12,13,14,17,18,19,29,39,59,69,79,88,87,86,85,84,83,72,62,52,32,22,23,26,27,28,48,58,68,78,77,74,73,63,53,43,34,35,47,67,66,65,64,44,45,46,56,55], visible=False, arg3=0, arg4=100)


class 퍼즐패턴58(state.State):
    def on_enter(self):
        set_timer(timerId='1', seconds=14)
        set_mesh(triggerIds=[1,2,3,4,5,6,7,8,9,10,20,30,40,50,60,70,80,90,100,99,98,97,96,95,94,93,92,91,81,71,61,51,41,31,21,11,12,13,14,15,16,17,18,29,39,49,59,69,79,89,88,87,86,85,84,83,72,62,52,42,32,22,23,25,26,48,58,78,77,76,75,53,43,33,34,37,67,66,64,44,46,55], visible=False, arg3=0, arg4=100)


class 퍼즐패턴59(state.State):
    def on_enter(self):
        set_timer(timerId='1', seconds=14)
        set_mesh(triggerIds=[1,2,6,7,8,9,10,20,30,40,50,90,100,99,98,97,96,95,94,93,92,91,81,71,61,51,41,31,21,11,13,14,15,17,18,19,29,39,59,69,79,78,77,76,75,74,73,23,24,25,27,28,38,58,68,67,66,65,64,63,53,43,33,34,35,37,57,67,66,65,64,54,44,45,56,55], visible=False, arg3=0, arg4=100)


class 퍼즐패턴60(state.State):
    def on_enter(self):
        set_timer(timerId='1', seconds=14)
        set_mesh(triggerIds=[10], visible=False, arg3=0, arg4=0)
        set_mesh(triggerIds=[9,20], visible=False, arg3=500, arg4=0)
        set_mesh(triggerIds=[8,19,30], visible=False, arg3=1000, arg4=0)
        set_mesh(triggerIds=[7,18,29,40], visible=False, arg3=1500, arg4=0)
        set_mesh(triggerIds=[28,39,50], visible=False, arg3=2000, arg4=0)
        set_mesh(triggerIds=[5,16,49,60], visible=False, arg3=2500, arg4=0)
        set_mesh(triggerIds=[4,15,26,37,59,70], visible=False, arg3=3000, arg4=0)
        set_mesh(triggerIds=[3,14,25,47,69,80], visible=False, arg3=3500, arg4=0)
        set_mesh(triggerIds=[2,13,24,46,57,90], visible=False, arg3=4000, arg4=0)
        set_mesh(triggerIds=[1,12,23,34,45,56,78,100], visible=False, arg3=4500, arg4=0)
        set_mesh(triggerIds=[11,22,55,66,77,88,99], visible=False, arg3=4000, arg4=0)
        set_mesh(triggerIds=[21,43,65,87], visible=False, arg3=3500, arg4=0)
        set_mesh(triggerIds=[31,42,53,64,75], visible=False, arg3=3000, arg4=0)
        set_mesh(triggerIds=[52,74,85,96], visible=False, arg3=2500, arg4=0)
        set_mesh(triggerIds=[73,84,95], visible=False, arg3=2000, arg4=0)
        set_mesh(triggerIds=[61,72,83,94], visible=False, arg3=1500, arg4=0)
        set_mesh(triggerIds=[71,82,93], visible=False, arg3=1000, arg4=0)
        set_mesh(triggerIds=[81,92], visible=False, arg3=500, arg4=0)
        set_mesh(triggerIds=[91], visible=False, arg3=0, arg4=0)


# 퍼즐 패턴 끝
class 실패계단보이기(state.State):
    def on_enter(self):
        end_mini_game_round(winnerBoxId=301)
        end_mini_game(winnerBoxId=301, gameName='trapmaster')
        unset_mini_game_area_for_hack() # 해킹 보안 종료
        set_timer(timerId='1', seconds=1)
        set_event_ui(type=0, arg2='0,0')
        play_system_sound_in_box(boxIds=[301], sound='ME_001_Massive00_14')
        set_event_ui(type=5, arg2='$61000001_ME_001__MASSIVE00__14$', arg3='5000')
        set_mesh(triggerIds=[1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36,37,38,39,40,41,42,43,44,45,46,47,48,49,50,51,52,53,54,55,56,57,58,59,60,61,62,63,64,65,66,67,68,69,70,71,72,73,74,75,76,77,78,79,80,81,82,83,84,85,86,87,88,89,90,91,92,93,94,95,96,97,98,99,100], visible=True)
        set_portal(portalId=777, visible=False, enabled=True, minimapVisible=True)
        set_mesh(triggerIds=[201,202,203,204,205], visible=True)
        set_actor(triggerId=251, visible=True, initialSequence='Eff_MassiveEvent_Stair_Opened')
        set_actor(triggerId=252, visible=True, initialSequence='Eff_MassiveEvent_Stair_Opened')
        set_actor(triggerId=253, visible=True, initialSequence='Eff_MassiveEvent_Stair_Opened')
        set_actor(triggerId=254, visible=True, initialSequence='Eff_MassiveEvent_Stair_Opened')
        set_actor(triggerId=255, visible=True, initialSequence='Eff_MassiveEvent_Stair_Opened')

    def on_tick(self) -> state.State:
        if time_expired(timerId='1'):
            return 실패계단보이기2()

    def on_exit(self):
        reset_timer(timerId='1')


class 실패계단보이기2(state.State):
    def on_enter(self):
        set_timer(timerId='1', seconds=1)
        set_mesh(triggerIds=[206,207,208,209,210], visible=True)
        set_actor(triggerId=256, visible=True, initialSequence='Eff_MassiveEvent_Stair_Opened')
        set_actor(triggerId=257, visible=True, initialSequence='Eff_MassiveEvent_Stair_Opened')
        set_actor(triggerId=258, visible=True, initialSequence='Eff_MassiveEvent_Stair_Opened')
        set_actor(triggerId=259, visible=True, initialSequence='Eff_MassiveEvent_Stair_Opened')
        set_actor(triggerId=260, visible=True, initialSequence='Eff_MassiveEvent_Stair_Opened')

    def on_tick(self) -> state.State:
        if time_expired(timerId='1'):
            return 실패()

    def on_exit(self):
        reset_timer(timerId='1')


class 실패(state.State):
    def on_enter(self):
        set_mesh(triggerIds=[211], visible=True)
        set_actor(triggerId=261, visible=True, initialSequence='Eff_MassiveEvent_Door_Opened')

    def on_tick(self) -> state.State:
        if true(arg1=True):
            return 실패2()


class 실패2(state.State):
    def on_tick(self) -> state.State:
        if wait_tick(waitTick=3000):
            return 유저이동()


class 유저이동(state.State):
    def on_enter(self):
        set_event_ui(type=1, arg2='$61000007_ME__MAINPROCESS_SPRINGBEACH__23$', arg3='5000', arg4='0')

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=120000):
            move_user(mapId=0, portalId=0)
            return 종료()


class 종료(state.State):
    pass


