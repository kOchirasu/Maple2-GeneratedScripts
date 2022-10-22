""" trigger/02020003_bf/11000_minipuzzle_melody.xml """
from common import *
import state


class Wait(state.State):
    def on_enter(self):
        reset_timer(timerId='1')
        reset_timer(timerId='2')
        enable_local_camera(isEnable=False) # 로컬카메라 전체 OFF
        set_interact_object(triggerIds=[12000202], state=2) # RareBox 맵 별로 유니크하도록 변경해야 하는 값
        set_interact_object(triggerIds=[12000074], state=2) # AntiqueMap / 기믹 시작 오브젝트 / Additional Effect 71001011 부여
        set_interact_object(triggerIds=[12000058], state=2) # Lever C
        set_interact_object(triggerIds=[12000059], state=2) # Lever D
        set_interact_object(triggerIds=[12000060], state=2) # Lever E
        set_interact_object(triggerIds=[12000061], state=2) # Lever F
        set_interact_object(triggerIds=[12000062], state=2) # Lever G
        set_interact_object(triggerIds=[12000063], state=2) # Lever A
        set_interact_object(triggerIds=[12000064], state=2) # Lever B
        set_interact_object(triggerIds=[12000065], state=2) # Lever HighC
        set_user_value(key='AnswerIsRight', value=0)
        set_user_value(key='AnswerIsWrong', value=0)
        set_actor(triggerId=11001, visible=True, initialSequence='ks_quest_musical_B01_off') # Bell C
        set_actor(triggerId=11002, visible=True, initialSequence='ks_quest_musical_B01_off') # Bell D
        set_actor(triggerId=11003, visible=True, initialSequence='ks_quest_musical_B01_off') # Bell E
        set_actor(triggerId=11004, visible=True, initialSequence='ks_quest_musical_B01_off') # Bell F
        set_actor(triggerId=11005, visible=True, initialSequence='ks_quest_musical_B01_off') # Bell G
        set_actor(triggerId=11006, visible=True, initialSequence='ks_quest_musical_B01_off') # Bell A
        set_actor(triggerId=11007, visible=True, initialSequence='ks_quest_musical_B01_off') # Bell B
        set_actor(triggerId=11008, visible=True, initialSequence='ks_quest_musical_B01_off') # Bell HighC
        set_actor(triggerId=11101, visible=True, initialSequence='ks_quest_musical_A01_off') # Dummy Lever C
        set_actor(triggerId=11102, visible=True, initialSequence='ks_quest_musical_A01_off') # Dummy Lever D
        set_actor(triggerId=11103, visible=True, initialSequence='ks_quest_musical_A01_off') # Dummy Lever E
        set_actor(triggerId=11104, visible=True, initialSequence='ks_quest_musical_A01_off') # Dummy Lever F
        set_actor(triggerId=11105, visible=True, initialSequence='ks_quest_musical_A01_off') # Dummy Lever G
        set_actor(triggerId=11106, visible=True, initialSequence='ks_quest_musical_A01_off') # Dummy Lever A
        set_actor(triggerId=11107, visible=True, initialSequence='ks_quest_musical_A01_off') # Dummy Lever B
        set_actor(triggerId=11108, visible=True, initialSequence='ks_quest_musical_A01_off') # Dummy Lever HighC
        set_effect(triggerIds=[11201], visible=False) # Bell C
        set_effect(triggerIds=[11202], visible=False) # Bell D
        set_effect(triggerIds=[11203], visible=False) # Bell E
        set_effect(triggerIds=[11204], visible=False) # Bell F
        set_effect(triggerIds=[11205], visible=False) # Bell G
        set_effect(triggerIds=[11206], visible=False) # Bell A
        set_effect(triggerIds=[11207], visible=False) # Bell B
        set_effect(triggerIds=[11208], visible=False) # Bell HighC
        set_effect(triggerIds=[11300], visible=False) # Success Sound Effect
        set_effect(triggerIds=[11301], visible=False) # Right Sound Effect
        set_effect(triggerIds=[11302], visible=False) # Wrong Sound Effect

    def on_tick(self) -> state.State:
        if user_value(key='TimeEventOn', value=1):
            return Setting()


class Setting(state.State):
    def on_enter(self):
        enable_local_camera(isEnable=True) # 로컬카메라 전체 ON
        set_interact_object(triggerIds=[12000074], state=1) # AntiqueMap

    def on_tick(self) -> state.State:
        if object_interacted(interactIds=[12000074], arg2=0):
            set_timer(timerId='1', seconds=120, clearAtZero=True, display=False, arg5=0)
            return StartMelodyQuiz_Delay01()
        if user_value(key='TimeEventOn', value=0):
            return Wait()


class StartMelodyQuiz_Delay01(state.State):
    def on_enter(self):
        set_effect(triggerIds=[11301], visible=True) # Right Sound Effect
        set_actor(triggerId=11001, visible=True, initialSequence='ks_quest_musical_B01_red') # Bell C
        set_actor(triggerId=11002, visible=True, initialSequence='ks_quest_musical_B01_orange') # Bell D
        set_actor(triggerId=11003, visible=True, initialSequence='ks_quest_musical_B01_yellow') # Bell E
        set_actor(triggerId=11004, visible=True, initialSequence='ks_quest_musical_B01_green') # Bell F
        set_actor(triggerId=11005, visible=True, initialSequence='ks_quest_musical_B01_blue') # Bell G
        set_actor(triggerId=11006, visible=True, initialSequence='ks_quest_musical_B01_navy') # Bell A
        set_actor(triggerId=11007, visible=True, initialSequence='ks_quest_musical_B01_purple') # Bell B
        set_actor(triggerId=11008, visible=True, initialSequence='ks_quest_musical_B01_pink') # Bell HighC

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=1000):
            return StartMelodyQuiz_Delay02()


class StartMelodyQuiz_Delay02(state.State):
    def on_enter(self):
        set_actor(triggerId=11001, visible=True, initialSequence='ks_quest_musical_B01_off') # Bell C
        set_actor(triggerId=11002, visible=True, initialSequence='ks_quest_musical_B01_off') # Bell D
        set_actor(triggerId=11003, visible=True, initialSequence='ks_quest_musical_B01_off') # Bell E
        set_actor(triggerId=11004, visible=True, initialSequence='ks_quest_musical_B01_off') # Bell F
        set_actor(triggerId=11005, visible=True, initialSequence='ks_quest_musical_B01_off') # Bell G
        set_actor(triggerId=11006, visible=True, initialSequence='ks_quest_musical_B01_off') # Bell A
        set_actor(triggerId=11007, visible=True, initialSequence='ks_quest_musical_B01_off') # Bell B
        set_actor(triggerId=11008, visible=True, initialSequence='ks_quest_musical_B01_off') # Bell HighC

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=1000):
            return StartMelodyQuiz_Random()


#  패턴 랜덤픽 
class StartMelodyQuiz_Random(state.State):
    def on_tick(self) -> state.State:
        if random_condition(rate=50):
            return MelodyQuizPattern01()
        if random_condition(rate=50):
            return MelodyQuizPattern02()
        if random_condition(rate=50):
            return MelodyQuizPattern03()
        if random_condition(rate=50):
            return MelodyQuizPattern04()
        if random_condition(rate=50):
            return MelodyQuizPattern05()
        if random_condition(rate=50):
            return MelodyQuizPattern06()
        if random_condition(rate=50):
            return MelodyQuizPattern07()
        if random_condition(rate=50):
            return MelodyQuizPattern08()
        if random_condition(rate=50):
            return MelodyQuizPattern09()
        if random_condition(rate=50):
            return MelodyQuizPattern10()
        if random_condition(rate=50):
            return MelodyQuizPattern11()
        if random_condition(rate=50):
            return MelodyQuizPattern12()
        if random_condition(rate=50):
            return MelodyQuizPattern13()
        if random_condition(rate=50):
            return MelodyQuizPattern14()
        if random_condition(rate=50):
            return MelodyQuizPattern15()
        if random_condition(rate=50):
            return MelodyQuizPattern16()
        if random_condition(rate=50):
            return MelodyQuizPattern17()
        if random_condition(rate=50):
            return MelodyQuizPattern18()
        if random_condition(rate=50):
            return MelodyQuizPattern19()
        if random_condition(rate=50):
            return MelodyQuizPattern20()


#  패턴 모음 
class MelodyQuizPattern01(state.State):
    def on_enter(self):
        set_user_value(key='PatternPick', value=101) # 틀린 경우, 동일한 퀴즈를 다시 들려주기 위해 현재 트리거에서도 선택된 퍼즐 패턴을 기억
        set_user_value(triggerId=101, key='PatternPick', value=1)

    def on_tick(self) -> state.State:
        if user_value(key='AnswerIsRight', value=1):
            return EndMelodyQuiz_Success()
        if user_value(key='AnswerIsWrong', value=1):
            return EndMelodyQuiz_Fail()
        if time_expired(timerId='1'):
            return MelodyQuiz_Fail_Quit()

    def on_exit(self):
        set_user_value(triggerId=101, key='Reset', value=1)


#  패턴 추가 
class MelodyQuizPattern02(state.State):
    def on_enter(self):
        set_user_value(key='PatternPick', value=102) # 틀린 경우, 동일한 퀴즈를 다시 들려주기 위해 현재 트리거에서도 선택된 퍼즐 패턴을 기억
        set_user_value(triggerId=102, key='PatternPick', value=1)

    def on_tick(self) -> state.State:
        if user_value(key='AnswerIsRight', value=1):
            return EndMelodyQuiz_Success()
        if user_value(key='AnswerIsWrong', value=1):
            return EndMelodyQuiz_Fail()
        if time_expired(timerId='1'):
            return MelodyQuiz_Fail_Quit()

    def on_exit(self):
        set_user_value(triggerId=102, key='Reset', value=1)


class MelodyQuizPattern03(state.State):
    def on_enter(self):
        set_user_value(key='PatternPick', value=103) # 틀린 경우, 동일한 퀴즈를 다시 들려주기 위해 현재 트리거에서도 선택된 퍼즐 패턴을 기억
        set_user_value(triggerId=103, key='PatternPick', value=1)

    def on_tick(self) -> state.State:
        if user_value(key='AnswerIsRight', value=1):
            return EndMelodyQuiz_Success()
        if user_value(key='AnswerIsWrong', value=1):
            return EndMelodyQuiz_Fail()
        if time_expired(timerId='1'):
            return MelodyQuiz_Fail_Quit()

    def on_exit(self):
        set_user_value(triggerId=103, key='Reset', value=1)


class MelodyQuizPattern04(state.State):
    def on_enter(self):
        set_user_value(key='PatternPick', value=104) # 틀린 경우, 동일한 퀴즈를 다시 들려주기 위해 현재 트리거에서도 선택된 퍼즐 패턴을 기억
        set_user_value(triggerId=104, key='PatternPick', value=1)

    def on_tick(self) -> state.State:
        if user_value(key='AnswerIsRight', value=1):
            return EndMelodyQuiz_Success()
        if user_value(key='AnswerIsWrong', value=1):
            return EndMelodyQuiz_Fail()
        if time_expired(timerId='1'):
            return MelodyQuiz_Fail_Quit()

    def on_exit(self):
        set_user_value(triggerId=104, key='Reset', value=1)


class MelodyQuizPattern05(state.State):
    def on_enter(self):
        set_user_value(key='PatternPick', value=105) # 틀린 경우, 동일한 퀴즈를 다시 들려주기 위해 현재 트리거에서도 선택된 퍼즐 패턴을 기억
        set_user_value(triggerId=105, key='PatternPick', value=1)

    def on_tick(self) -> state.State:
        if user_value(key='AnswerIsRight', value=1):
            return EndMelodyQuiz_Success()
        if user_value(key='AnswerIsWrong', value=1):
            return EndMelodyQuiz_Fail()
        if time_expired(timerId='1'):
            return MelodyQuiz_Fail_Quit()

    def on_exit(self):
        set_user_value(triggerId=105, key='Reset', value=1)


class MelodyQuizPattern06(state.State):
    def on_enter(self):
        set_user_value(key='PatternPick', value=106) # 틀린 경우, 동일한 퀴즈를 다시 들려주기 위해 현재 트리거에서도 선택된 퍼즐 패턴을 기억
        set_user_value(triggerId=106, key='PatternPick', value=1)

    def on_tick(self) -> state.State:
        if user_value(key='AnswerIsRight', value=1):
            return EndMelodyQuiz_Success()
        if user_value(key='AnswerIsWrong', value=1):
            return EndMelodyQuiz_Fail()
        if time_expired(timerId='1'):
            return MelodyQuiz_Fail_Quit()

    def on_exit(self):
        set_user_value(triggerId=106, key='Reset', value=1)


class MelodyQuizPattern07(state.State):
    def on_enter(self):
        set_user_value(key='PatternPick', value=107) # 틀린 경우, 동일한 퀴즈를 다시 들려주기 위해 현재 트리거에서도 선택된 퍼즐 패턴을 기억
        set_user_value(triggerId=107, key='PatternPick', value=1)

    def on_tick(self) -> state.State:
        if user_value(key='AnswerIsRight', value=1):
            return EndMelodyQuiz_Success()
        if user_value(key='AnswerIsWrong', value=1):
            return EndMelodyQuiz_Fail()
        if time_expired(timerId='1'):
            return MelodyQuiz_Fail_Quit()

    def on_exit(self):
        set_user_value(triggerId=107, key='Reset', value=1)


class MelodyQuizPattern08(state.State):
    def on_enter(self):
        set_user_value(key='PatternPick', value=108) # 틀린 경우, 동일한 퀴즈를 다시 들려주기 위해 현재 트리거에서도 선택된 퍼즐 패턴을 기억
        set_user_value(triggerId=108, key='PatternPick', value=1)

    def on_tick(self) -> state.State:
        if user_value(key='AnswerIsRight', value=1):
            return EndMelodyQuiz_Success()
        if user_value(key='AnswerIsWrong', value=1):
            return EndMelodyQuiz_Fail()
        if time_expired(timerId='1'):
            return MelodyQuiz_Fail_Quit()

    def on_exit(self):
        set_user_value(triggerId=108, key='Reset', value=1)


class MelodyQuizPattern09(state.State):
    def on_enter(self):
        set_user_value(key='PatternPick', value=109) # 틀린 경우, 동일한 퀴즈를 다시 들려주기 위해 현재 트리거에서도 선택된 퍼즐 패턴을 기억
        set_user_value(triggerId=109, key='PatternPick', value=1)

    def on_tick(self) -> state.State:
        if user_value(key='AnswerIsRight', value=1):
            return EndMelodyQuiz_Success()
        if user_value(key='AnswerIsWrong', value=1):
            return EndMelodyQuiz_Fail()
        if time_expired(timerId='1'):
            return MelodyQuiz_Fail_Quit()

    def on_exit(self):
        set_user_value(triggerId=109, key='Reset', value=1)


class MelodyQuizPattern10(state.State):
    def on_enter(self):
        set_user_value(key='PatternPick', value=110) # 틀린 경우, 동일한 퀴즈를 다시 들려주기 위해 현재 트리거에서도 선택된 퍼즐 패턴을 기억
        set_user_value(triggerId=110, key='PatternPick', value=1)

    def on_tick(self) -> state.State:
        if user_value(key='AnswerIsRight', value=1):
            return EndMelodyQuiz_Success()
        if user_value(key='AnswerIsWrong', value=1):
            return EndMelodyQuiz_Fail()
        if time_expired(timerId='1'):
            return MelodyQuiz_Fail_Quit()

    def on_exit(self):
        set_user_value(triggerId=110, key='Reset', value=1)


class MelodyQuizPattern11(state.State):
    def on_enter(self):
        set_user_value(key='PatternPick', value=111) # 틀린 경우, 동일한 퀴즈를 다시 들려주기 위해 현재 트리거에서도 선택된 퍼즐 패턴을 기억
        set_user_value(triggerId=111, key='PatternPick', value=1)

    def on_tick(self) -> state.State:
        if user_value(key='AnswerIsRight', value=1):
            return EndMelodyQuiz_Success()
        if user_value(key='AnswerIsWrong', value=1):
            return EndMelodyQuiz_Fail()
        if time_expired(timerId='1'):
            return MelodyQuiz_Fail_Quit()

    def on_exit(self):
        set_user_value(triggerId=111, key='Reset', value=1)


class MelodyQuizPattern12(state.State):
    def on_enter(self):
        set_user_value(key='PatternPick', value=112) # 틀린 경우, 동일한 퀴즈를 다시 들려주기 위해 현재 트리거에서도 선택된 퍼즐 패턴을 기억
        set_user_value(triggerId=112, key='PatternPick', value=1)

    def on_tick(self) -> state.State:
        if user_value(key='AnswerIsRight', value=1):
            return EndMelodyQuiz_Success()
        if user_value(key='AnswerIsWrong', value=1):
            return EndMelodyQuiz_Fail()
        if time_expired(timerId='1'):
            return MelodyQuiz_Fail_Quit()

    def on_exit(self):
        set_user_value(triggerId=112, key='Reset', value=1)


class MelodyQuizPattern13(state.State):
    def on_enter(self):
        set_user_value(key='PatternPick', value=113) # 틀린 경우, 동일한 퀴즈를 다시 들려주기 위해 현재 트리거에서도 선택된 퍼즐 패턴을 기억
        set_user_value(triggerId=113, key='PatternPick', value=1)

    def on_tick(self) -> state.State:
        if user_value(key='AnswerIsRight', value=1):
            return EndMelodyQuiz_Success()
        if user_value(key='AnswerIsWrong', value=1):
            return EndMelodyQuiz_Fail()
        if time_expired(timerId='1'):
            return MelodyQuiz_Fail_Quit()

    def on_exit(self):
        set_user_value(triggerId=113, key='Reset', value=1)


class MelodyQuizPattern14(state.State):
    def on_enter(self):
        set_user_value(key='PatternPick', value=114) # 틀린 경우, 동일한 퀴즈를 다시 들려주기 위해 현재 트리거에서도 선택된 퍼즐 패턴을 기억
        set_user_value(triggerId=114, key='PatternPick', value=1)

    def on_tick(self) -> state.State:
        if user_value(key='AnswerIsRight', value=1):
            return EndMelodyQuiz_Success()
        if user_value(key='AnswerIsWrong', value=1):
            return EndMelodyQuiz_Fail()
        if time_expired(timerId='1'):
            return MelodyQuiz_Fail_Quit()

    def on_exit(self):
        set_user_value(triggerId=114, key='Reset', value=1)


class MelodyQuizPattern15(state.State):
    def on_enter(self):
        set_user_value(key='PatternPick', value=115) # 틀린 경우, 동일한 퀴즈를 다시 들려주기 위해 현재 트리거에서도 선택된 퍼즐 패턴을 기억
        set_user_value(triggerId=115, key='PatternPick', value=1)

    def on_tick(self) -> state.State:
        if user_value(key='AnswerIsRight', value=1):
            return EndMelodyQuiz_Success()
        if user_value(key='AnswerIsWrong', value=1):
            return EndMelodyQuiz_Fail()
        if time_expired(timerId='1'):
            return MelodyQuiz_Fail_Quit()

    def on_exit(self):
        set_user_value(triggerId=115, key='Reset', value=1)


class MelodyQuizPattern16(state.State):
    def on_enter(self):
        set_user_value(key='PatternPick', value=116) # 틀린 경우, 동일한 퀴즈를 다시 들려주기 위해 현재 트리거에서도 선택된 퍼즐 패턴을 기억
        set_user_value(triggerId=116, key='PatternPick', value=1)

    def on_tick(self) -> state.State:
        if user_value(key='AnswerIsRight', value=1):
            return EndMelodyQuiz_Success()
        if user_value(key='AnswerIsWrong', value=1):
            return EndMelodyQuiz_Fail()
        if time_expired(timerId='1'):
            return MelodyQuiz_Fail_Quit()

    def on_exit(self):
        set_user_value(triggerId=116, key='Reset', value=1)


class MelodyQuizPattern17(state.State):
    def on_enter(self):
        set_user_value(key='PatternPick', value=117) # 틀린 경우, 동일한 퀴즈를 다시 들려주기 위해 현재 트리거에서도 선택된 퍼즐 패턴을 기억
        set_user_value(triggerId=117, key='PatternPick', value=1)

    def on_tick(self) -> state.State:
        if user_value(key='AnswerIsRight', value=1):
            return EndMelodyQuiz_Success()
        if user_value(key='AnswerIsWrong', value=1):
            return EndMelodyQuiz_Fail()
        if time_expired(timerId='1'):
            return MelodyQuiz_Fail_Quit()

    def on_exit(self):
        set_user_value(triggerId=117, key='Reset', value=1)


class MelodyQuizPattern18(state.State):
    def on_enter(self):
        set_user_value(key='PatternPick', value=118) # 틀린 경우, 동일한 퀴즈를 다시 들려주기 위해 현재 트리거에서도 선택된 퍼즐 패턴을 기억
        set_user_value(triggerId=118, key='PatternPick', value=1)

    def on_tick(self) -> state.State:
        if user_value(key='AnswerIsRight', value=1):
            return EndMelodyQuiz_Success()
        if user_value(key='AnswerIsWrong', value=1):
            return EndMelodyQuiz_Fail()
        if time_expired(timerId='1'):
            return MelodyQuiz_Fail_Quit()

    def on_exit(self):
        set_user_value(triggerId=118, key='Reset', value=1)


class MelodyQuizPattern19(state.State):
    def on_enter(self):
        set_user_value(key='PatternPick', value=119) # 틀린 경우, 동일한 퀴즈를 다시 들려주기 위해 현재 트리거에서도 선택된 퍼즐 패턴을 기억
        set_user_value(triggerId=119, key='PatternPick', value=1)

    def on_tick(self) -> state.State:
        if user_value(key='AnswerIsRight', value=1):
            return EndMelodyQuiz_Success()
        if user_value(key='AnswerIsWrong', value=1):
            return EndMelodyQuiz_Fail()
        if time_expired(timerId='1'):
            return MelodyQuiz_Fail_Quit()

    def on_exit(self):
        set_user_value(triggerId=119, key='Reset', value=1)


class MelodyQuizPattern20(state.State):
    def on_enter(self):
        set_user_value(key='PatternPick', value=120) # 틀린 경우, 동일한 퀴즈를 다시 들려주기 위해 현재 트리거에서도 선택된 퍼즐 패턴을 기억
        set_user_value(triggerId=120, key='PatternPick', value=1)

    def on_tick(self) -> state.State:
        if user_value(key='AnswerIsRight', value=1):
            return EndMelodyQuiz_Success()
        if user_value(key='AnswerIsWrong', value=1):
            return EndMelodyQuiz_Fail()
        if time_expired(timerId='1'):
            return MelodyQuiz_Fail_Quit()

    def on_exit(self):
        set_user_value(triggerId=120, key='Reset', value=1)


#  퍼즐 성공 후 종료 
class EndMelodyQuiz_Success(state.State):
    def on_enter(self):
        add_buff(boxIds=[11901], skillId=71001012, level=1, arg4=False, arg5=False)
        set_effect(triggerIds=[11300], visible=True) # Success Sound Effect
        set_interact_object(triggerIds=[12000202], state=1) # RareBox 맵 별로 유니크하도록 변경해야 하는 값
        set_timer(timerId='2', seconds=60, clearAtZero=True, display=False, arg5=0)

    def on_tick(self) -> state.State:
        if object_interacted(interactIds=[12000202], arg2=0):
            return MelodyQuiz_Success_Quit()
        if time_expired(timerId='2'):
            return MelodyQuiz_Success_Quit()
        """
        <condition name="UserValue" key="TimeEventOn" value="0">
        """


#  퍼즐 실패 후 재도전 
class EndMelodyQuiz_Fail(state.State):
    def on_enter(self):
        set_effect(triggerIds=[11302], visible=True) # Wrong Sound Effect

    def on_tick(self) -> state.State:
        if user_value(key='TimeEventOn', value=0):
            return EndMelodyQuiz_Fail_2()
        if time_expired(timerId='1'):
            return MelodyQuiz_Fail_Quit()
        if wait_tick(waitTick=2000):
            return MelodyQuiz_Retry()


class EndMelodyQuiz_Fail_2(state.State):
    def on_tick(self) -> state.State:
        if time_expired(timerId='1'):
            return Wait()
        if wait_tick(waitTick=2000):
            return MelodyQuiz_Retry()


class MelodyQuiz_Retry(state.State):
    def on_enter(self):
        set_user_value(key='AnswerIsWrong', value=0)

    def on_tick(self) -> state.State:
        if user_value(key='PatternPick', value=101):
            return MelodyQuizPattern01()
        if user_value(key='PatternPick', value=102):
            return MelodyQuizPattern02()
        if user_value(key='PatternPick', value=103):
            return MelodyQuizPattern03()
        if user_value(key='PatternPick', value=104):
            return MelodyQuizPattern04()
        if user_value(key='PatternPick', value=105):
            return MelodyQuizPattern05()
        if user_value(key='PatternPick', value=106):
            return MelodyQuizPattern06()
        if user_value(key='PatternPick', value=107):
            return MelodyQuizPattern07()
        if user_value(key='PatternPick', value=108):
            return MelodyQuizPattern08()
        if user_value(key='PatternPick', value=109):
            return MelodyQuizPattern09()
        if user_value(key='PatternPick', value=110):
            return MelodyQuizPattern10()
        if user_value(key='PatternPick', value=111):
            return MelodyQuizPattern11()
        if user_value(key='PatternPick', value=112):
            return MelodyQuizPattern12()
        if user_value(key='PatternPick', value=113):
            return MelodyQuizPattern13()
        if user_value(key='PatternPick', value=114):
            return MelodyQuizPattern14()
        if user_value(key='PatternPick', value=115):
            return MelodyQuizPattern15()
        if user_value(key='PatternPick', value=116):
            return MelodyQuizPattern16()
        if user_value(key='PatternPick', value=117):
            return MelodyQuizPattern17()
        if user_value(key='PatternPick', value=118):
            return MelodyQuizPattern18()
        if user_value(key='PatternPick', value=119):
            return MelodyQuizPattern19()
        if user_value(key='PatternPick', value=120): # 패턴 추가
            return MelodyQuizPattern20()


class MelodyQuiz_Fail_Quit(state.State):
    def on_enter(self):
        reset_timer(timerId='1') # UI 표시 안함 / 황금 상자 소유권 Additional Effect 71001011 지속시간 동일
        reset_timer(timerId='2')

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=1000):
            return Wait()


class MelodyQuiz_Success_Quit(state.State):
    def on_enter(self):
        set_user_value(key='TimeEventOn', value=0)
        # <action name="버프를삭제한다" arg1="9001" arg2="71001011" arg3="true"/>
        reset_timer(timerId='1') # UI 표시 안함 / 황금 상자 소유권 Additional Effect 71001011 지속시간 동일
        reset_timer(timerId='2')

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=1000):
            return Wait()


