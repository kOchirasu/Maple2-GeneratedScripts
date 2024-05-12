""" trigger/99999870/11000_minipuzzle_melody.xml """
import trigger_api


class Wait(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        # UI 표시 안함 / 황금 상자 소유권 Additional Effect 71001011 지속시간 동일
        self.reset_timer(timerId='1')
        self.reset_timer(timerId='2')
        self.enable_local_camera(isEnable=False) # 로컬카메라 전체 OFF
        # RareBox 맵 별로 유니크하도록 변경해야 하는 값
        self.set_interact_object(triggerIds=[12000066], state=2)
        # AntiqueMap / 기믹 시작 오브젝트 / Additional Effect 71001011 부여
        self.set_interact_object(triggerIds=[12000074], state=2)
        self.set_interact_object(triggerIds=[12000058], state=2) # Lever C
        self.set_interact_object(triggerIds=[12000059], state=2) # Lever D
        self.set_interact_object(triggerIds=[12000060], state=2) # Lever E
        self.set_interact_object(triggerIds=[12000061], state=2) # Lever F
        self.set_interact_object(triggerIds=[12000062], state=2) # Lever G
        self.set_interact_object(triggerIds=[12000063], state=2) # Lever A
        self.set_interact_object(triggerIds=[12000064], state=2) # Lever B
        self.set_interact_object(triggerIds=[12000065], state=2) # Lever HighC
        # self.set_user_value(key='TimeEventOn', value=0)
        self.set_user_value(key='AnswerIsRight', value=0)
        self.set_user_value(key='AnswerIsWrong', value=0)
        self.set_actor(triggerId=11001, visible=True, initialSequence='ks_quest_musical_B01_off') # Bell C
        self.set_actor(triggerId=11002, visible=True, initialSequence='ks_quest_musical_B01_off') # Bell D
        self.set_actor(triggerId=11003, visible=True, initialSequence='ks_quest_musical_B01_off') # Bell E
        self.set_actor(triggerId=11004, visible=True, initialSequence='ks_quest_musical_B01_off') # Bell F
        self.set_actor(triggerId=11005, visible=True, initialSequence='ks_quest_musical_B01_off') # Bell G
        self.set_actor(triggerId=11006, visible=True, initialSequence='ks_quest_musical_B01_off') # Bell A
        self.set_actor(triggerId=11007, visible=True, initialSequence='ks_quest_musical_B01_off') # Bell B
        self.set_actor(triggerId=11008, visible=True, initialSequence='ks_quest_musical_B01_off') # Bell HighC
        self.set_actor(triggerId=11101, visible=True, initialSequence='ks_quest_musical_A01_off') # Dummy Lever C
        self.set_actor(triggerId=11102, visible=True, initialSequence='ks_quest_musical_A01_off') # Dummy Lever D
        self.set_actor(triggerId=11103, visible=True, initialSequence='ks_quest_musical_A01_off') # Dummy Lever E
        self.set_actor(triggerId=11104, visible=True, initialSequence='ks_quest_musical_A01_off') # Dummy Lever F
        self.set_actor(triggerId=11105, visible=True, initialSequence='ks_quest_musical_A01_off') # Dummy Lever G
        self.set_actor(triggerId=11106, visible=True, initialSequence='ks_quest_musical_A01_off') # Dummy Lever A
        self.set_actor(triggerId=11107, visible=True, initialSequence='ks_quest_musical_A01_off') # Dummy Lever B
        self.set_actor(triggerId=11108, visible=True, initialSequence='ks_quest_musical_A01_off') # Dummy Lever HighC
        self.set_effect(triggerIds=[11201], visible=False) # Bell C
        self.set_effect(triggerIds=[11202], visible=False) # Bell D
        self.set_effect(triggerIds=[11203], visible=False) # Bell E
        self.set_effect(triggerIds=[11204], visible=False) # Bell F
        self.set_effect(triggerIds=[11205], visible=False) # Bell G
        self.set_effect(triggerIds=[11206], visible=False) # Bell A
        self.set_effect(triggerIds=[11207], visible=False) # Bell B
        self.set_effect(triggerIds=[11208], visible=False) # Bell HighC
        self.set_effect(triggerIds=[11300], visible=False) # Success Sound Effect
        self.set_effect(triggerIds=[11301], visible=False) # Right Sound Effect
        self.set_effect(triggerIds=[11302], visible=False) # Wrong Sound Effect

    def on_tick(self) -> trigger_api.Trigger:
        if self.user_value(key='TimeEventOn', value=1):
            return Setting(self.ctx)


class Setting(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.enable_local_camera(isEnable=True) # 로컬카메라 전체 ON
        self.set_interact_object(triggerIds=[12000074], state=1) # AntiqueMap

    def on_tick(self) -> trigger_api.Trigger:
        if self.object_interacted(interactIds=[12000074], stateValue=0):
            # UI 표시 안함 / 황금 상자 소유권 Additional Effect 71001011 지속시간 동일
            self.set_timer(timerId='1', seconds=120, startDelay=1, interval=0, vOffset=0)
            return StartMelodyQuiz_Delay01(self.ctx)
        if self.user_value(key='TimeEventOn', value=0):
            return Wait(self.ctx)


class StartMelodyQuiz_Delay01(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_effect(triggerIds=[11301], visible=True) # Right Sound Effect
        self.set_actor(triggerId=11001, visible=True, initialSequence='ks_quest_musical_B01_red') # Bell C
        self.set_actor(triggerId=11002, visible=True, initialSequence='ks_quest_musical_B01_orange') # Bell D
        self.set_actor(triggerId=11003, visible=True, initialSequence='ks_quest_musical_B01_yellow') # Bell E
        self.set_actor(triggerId=11004, visible=True, initialSequence='ks_quest_musical_B01_green') # Bell F
        self.set_actor(triggerId=11005, visible=True, initialSequence='ks_quest_musical_B01_blue') # Bell G
        self.set_actor(triggerId=11006, visible=True, initialSequence='ks_quest_musical_B01_navy') # Bell A
        self.set_actor(triggerId=11007, visible=True, initialSequence='ks_quest_musical_B01_purple') # Bell B
        self.set_actor(triggerId=11008, visible=True, initialSequence='ks_quest_musical_B01_pink') # Bell HighC

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=1000):
            return StartMelodyQuiz_Delay02(self.ctx)


class StartMelodyQuiz_Delay02(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_actor(triggerId=11001, visible=True, initialSequence='ks_quest_musical_B01_off') # Bell C
        self.set_actor(triggerId=11002, visible=True, initialSequence='ks_quest_musical_B01_off') # Bell D
        self.set_actor(triggerId=11003, visible=True, initialSequence='ks_quest_musical_B01_off') # Bell E
        self.set_actor(triggerId=11004, visible=True, initialSequence='ks_quest_musical_B01_off') # Bell F
        self.set_actor(triggerId=11005, visible=True, initialSequence='ks_quest_musical_B01_off') # Bell G
        self.set_actor(triggerId=11006, visible=True, initialSequence='ks_quest_musical_B01_off') # Bell A
        self.set_actor(triggerId=11007, visible=True, initialSequence='ks_quest_musical_B01_off') # Bell B
        self.set_actor(triggerId=11008, visible=True, initialSequence='ks_quest_musical_B01_off') # Bell HighC

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=1000):
            return StartMelodyQuiz_Random(self.ctx)


# 패턴 랜덤픽
class StartMelodyQuiz_Random(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.random_condition(rate=50):
            return MelodyQuizPattern20(self.ctx)


# 패턴 모음
class MelodyQuizPattern01(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        # 틀린 경우, 동일한 퀴즈를 다시 들려주기 위해 현재 트리거에서도 선택된 퍼즐 패턴을 기억
        self.set_user_value(key='PatternPick', value=101)
        self.set_user_value(triggerId=101, key='PatternPick', value=1)

    def on_tick(self) -> trigger_api.Trigger:
        if self.user_value(key='AnswerIsRight', value=1):
            return EndMelodyQuiz_Success(self.ctx)
        if self.user_value(key='AnswerIsWrong', value=1):
            return EndMelodyQuiz_Fail(self.ctx)
        if self.time_expired(timerId='1'):
            # UI 표시 안함 / 황금 상자 소유권 Additional Effect 71001011 지속시간 동일
            return MelodyQuiz_Fail_Quit(self.ctx)

    def on_exit(self) -> None:
        self.set_user_value(triggerId=101, key='Reset', value=1)


# 패턴 추가
class MelodyQuizPattern02(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        # 틀린 경우, 동일한 퀴즈를 다시 들려주기 위해 현재 트리거에서도 선택된 퍼즐 패턴을 기억
        self.set_user_value(key='PatternPick', value=102)
        self.set_user_value(triggerId=102, key='PatternPick', value=1)

    def on_tick(self) -> trigger_api.Trigger:
        if self.user_value(key='AnswerIsRight', value=1):
            return EndMelodyQuiz_Success(self.ctx)
        if self.user_value(key='AnswerIsWrong', value=1):
            return EndMelodyQuiz_Fail(self.ctx)
        if self.time_expired(timerId='1'):
            # UI 표시 안함 / 황금 상자 소유권 Additional Effect 71001011 지속시간 동일
            return MelodyQuiz_Fail_Quit(self.ctx)

    def on_exit(self) -> None:
        self.set_user_value(triggerId=102, key='Reset', value=1)


class MelodyQuizPattern03(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        # 틀린 경우, 동일한 퀴즈를 다시 들려주기 위해 현재 트리거에서도 선택된 퍼즐 패턴을 기억
        self.set_user_value(key='PatternPick', value=103)
        self.set_user_value(triggerId=103, key='PatternPick', value=1)

    def on_tick(self) -> trigger_api.Trigger:
        if self.user_value(key='AnswerIsRight', value=1):
            return EndMelodyQuiz_Success(self.ctx)
        if self.user_value(key='AnswerIsWrong', value=1):
            return EndMelodyQuiz_Fail(self.ctx)
        if self.time_expired(timerId='1'):
            # UI 표시 안함 / 황금 상자 소유권 Additional Effect 71001011 지속시간 동일
            return MelodyQuiz_Fail_Quit(self.ctx)

    def on_exit(self) -> None:
        self.set_user_value(triggerId=103, key='Reset', value=1)


class MelodyQuizPattern04(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        # 틀린 경우, 동일한 퀴즈를 다시 들려주기 위해 현재 트리거에서도 선택된 퍼즐 패턴을 기억
        self.set_user_value(key='PatternPick', value=104)
        self.set_user_value(triggerId=104, key='PatternPick', value=1)

    def on_tick(self) -> trigger_api.Trigger:
        if self.user_value(key='AnswerIsRight', value=1):
            return EndMelodyQuiz_Success(self.ctx)
        if self.user_value(key='AnswerIsWrong', value=1):
            return EndMelodyQuiz_Fail(self.ctx)
        if self.time_expired(timerId='1'):
            # UI 표시 안함 / 황금 상자 소유권 Additional Effect 71001011 지속시간 동일
            return MelodyQuiz_Fail_Quit(self.ctx)

    def on_exit(self) -> None:
        self.set_user_value(triggerId=104, key='Reset', value=1)


class MelodyQuizPattern05(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        # 틀린 경우, 동일한 퀴즈를 다시 들려주기 위해 현재 트리거에서도 선택된 퍼즐 패턴을 기억
        self.set_user_value(key='PatternPick', value=105)
        self.set_user_value(triggerId=105, key='PatternPick', value=1)

    def on_tick(self) -> trigger_api.Trigger:
        if self.user_value(key='AnswerIsRight', value=1):
            return EndMelodyQuiz_Success(self.ctx)
        if self.user_value(key='AnswerIsWrong', value=1):
            return EndMelodyQuiz_Fail(self.ctx)
        if self.time_expired(timerId='1'):
            # UI 표시 안함 / 황금 상자 소유권 Additional Effect 71001011 지속시간 동일
            return MelodyQuiz_Fail_Quit(self.ctx)

    def on_exit(self) -> None:
        self.set_user_value(triggerId=105, key='Reset', value=1)


class MelodyQuizPattern06(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        # 틀린 경우, 동일한 퀴즈를 다시 들려주기 위해 현재 트리거에서도 선택된 퍼즐 패턴을 기억
        self.set_user_value(key='PatternPick', value=106)
        self.set_user_value(triggerId=106, key='PatternPick', value=1)

    def on_tick(self) -> trigger_api.Trigger:
        if self.user_value(key='AnswerIsRight', value=1):
            return EndMelodyQuiz_Success(self.ctx)
        if self.user_value(key='AnswerIsWrong', value=1):
            return EndMelodyQuiz_Fail(self.ctx)
        if self.time_expired(timerId='1'):
            # UI 표시 안함 / 황금 상자 소유권 Additional Effect 71001011 지속시간 동일
            return MelodyQuiz_Fail_Quit(self.ctx)

    def on_exit(self) -> None:
        self.set_user_value(triggerId=106, key='Reset', value=1)


class MelodyQuizPattern07(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        # 틀린 경우, 동일한 퀴즈를 다시 들려주기 위해 현재 트리거에서도 선택된 퍼즐 패턴을 기억
        self.set_user_value(key='PatternPick', value=107)
        self.set_user_value(triggerId=107, key='PatternPick', value=1)

    def on_tick(self) -> trigger_api.Trigger:
        if self.user_value(key='AnswerIsRight', value=1):
            return EndMelodyQuiz_Success(self.ctx)
        if self.user_value(key='AnswerIsWrong', value=1):
            return EndMelodyQuiz_Fail(self.ctx)
        if self.time_expired(timerId='1'):
            # UI 표시 안함 / 황금 상자 소유권 Additional Effect 71001011 지속시간 동일
            return MelodyQuiz_Fail_Quit(self.ctx)

    def on_exit(self) -> None:
        self.set_user_value(triggerId=107, key='Reset', value=1)


class MelodyQuizPattern08(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        # 틀린 경우, 동일한 퀴즈를 다시 들려주기 위해 현재 트리거에서도 선택된 퍼즐 패턴을 기억
        self.set_user_value(key='PatternPick', value=108)
        self.set_user_value(triggerId=108, key='PatternPick', value=1)

    def on_tick(self) -> trigger_api.Trigger:
        if self.user_value(key='AnswerIsRight', value=1):
            return EndMelodyQuiz_Success(self.ctx)
        if self.user_value(key='AnswerIsWrong', value=1):
            return EndMelodyQuiz_Fail(self.ctx)
        if self.time_expired(timerId='1'):
            # UI 표시 안함 / 황금 상자 소유권 Additional Effect 71001011 지속시간 동일
            return MelodyQuiz_Fail_Quit(self.ctx)

    def on_exit(self) -> None:
        self.set_user_value(triggerId=108, key='Reset', value=1)


class MelodyQuizPattern09(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        # 틀린 경우, 동일한 퀴즈를 다시 들려주기 위해 현재 트리거에서도 선택된 퍼즐 패턴을 기억
        self.set_user_value(key='PatternPick', value=109)
        self.set_user_value(triggerId=109, key='PatternPick', value=1)

    def on_tick(self) -> trigger_api.Trigger:
        if self.user_value(key='AnswerIsRight', value=1):
            return EndMelodyQuiz_Success(self.ctx)
        if self.user_value(key='AnswerIsWrong', value=1):
            return EndMelodyQuiz_Fail(self.ctx)
        if self.time_expired(timerId='1'):
            # UI 표시 안함 / 황금 상자 소유권 Additional Effect 71001011 지속시간 동일
            return MelodyQuiz_Fail_Quit(self.ctx)

    def on_exit(self) -> None:
        self.set_user_value(triggerId=109, key='Reset', value=1)


class MelodyQuizPattern10(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        # 틀린 경우, 동일한 퀴즈를 다시 들려주기 위해 현재 트리거에서도 선택된 퍼즐 패턴을 기억
        self.set_user_value(key='PatternPick', value=110)
        self.set_user_value(triggerId=110, key='PatternPick', value=1)

    def on_tick(self) -> trigger_api.Trigger:
        if self.user_value(key='AnswerIsRight', value=1):
            return EndMelodyQuiz_Success(self.ctx)
        if self.user_value(key='AnswerIsWrong', value=1):
            return EndMelodyQuiz_Fail(self.ctx)
        if self.time_expired(timerId='1'):
            # UI 표시 안함 / 황금 상자 소유권 Additional Effect 71001011 지속시간 동일
            return MelodyQuiz_Fail_Quit(self.ctx)

    def on_exit(self) -> None:
        self.set_user_value(triggerId=110, key='Reset', value=1)


class MelodyQuizPattern11(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        # 틀린 경우, 동일한 퀴즈를 다시 들려주기 위해 현재 트리거에서도 선택된 퍼즐 패턴을 기억
        self.set_user_value(key='PatternPick', value=111)
        self.set_user_value(triggerId=111, key='PatternPick', value=1)

    def on_tick(self) -> trigger_api.Trigger:
        if self.user_value(key='AnswerIsRight', value=1):
            return EndMelodyQuiz_Success(self.ctx)
        if self.user_value(key='AnswerIsWrong', value=1):
            return EndMelodyQuiz_Fail(self.ctx)
        if self.time_expired(timerId='1'):
            # UI 표시 안함 / 황금 상자 소유권 Additional Effect 71001011 지속시간 동일
            return MelodyQuiz_Fail_Quit(self.ctx)

    def on_exit(self) -> None:
        self.set_user_value(triggerId=111, key='Reset', value=1)


class MelodyQuizPattern12(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        # 틀린 경우, 동일한 퀴즈를 다시 들려주기 위해 현재 트리거에서도 선택된 퍼즐 패턴을 기억
        self.set_user_value(key='PatternPick', value=112)
        self.set_user_value(triggerId=112, key='PatternPick', value=1)

    def on_tick(self) -> trigger_api.Trigger:
        if self.user_value(key='AnswerIsRight', value=1):
            return EndMelodyQuiz_Success(self.ctx)
        if self.user_value(key='AnswerIsWrong', value=1):
            return EndMelodyQuiz_Fail(self.ctx)
        if self.time_expired(timerId='1'):
            # UI 표시 안함 / 황금 상자 소유권 Additional Effect 71001011 지속시간 동일
            return MelodyQuiz_Fail_Quit(self.ctx)

    def on_exit(self) -> None:
        self.set_user_value(triggerId=112, key='Reset', value=1)


class MelodyQuizPattern13(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        # 틀린 경우, 동일한 퀴즈를 다시 들려주기 위해 현재 트리거에서도 선택된 퍼즐 패턴을 기억
        self.set_user_value(key='PatternPick', value=113)
        self.set_user_value(triggerId=113, key='PatternPick', value=1)

    def on_tick(self) -> trigger_api.Trigger:
        if self.user_value(key='AnswerIsRight', value=1):
            return EndMelodyQuiz_Success(self.ctx)
        if self.user_value(key='AnswerIsWrong', value=1):
            return EndMelodyQuiz_Fail(self.ctx)
        if self.time_expired(timerId='1'):
            # UI 표시 안함 / 황금 상자 소유권 Additional Effect 71001011 지속시간 동일
            return MelodyQuiz_Fail_Quit(self.ctx)

    def on_exit(self) -> None:
        self.set_user_value(triggerId=113, key='Reset', value=1)


class MelodyQuizPattern14(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        # 틀린 경우, 동일한 퀴즈를 다시 들려주기 위해 현재 트리거에서도 선택된 퍼즐 패턴을 기억
        self.set_user_value(key='PatternPick', value=114)
        self.set_user_value(triggerId=114, key='PatternPick', value=1)

    def on_tick(self) -> trigger_api.Trigger:
        if self.user_value(key='AnswerIsRight', value=1):
            return EndMelodyQuiz_Success(self.ctx)
        if self.user_value(key='AnswerIsWrong', value=1):
            return EndMelodyQuiz_Fail(self.ctx)
        if self.time_expired(timerId='1'):
            # UI 표시 안함 / 황금 상자 소유권 Additional Effect 71001011 지속시간 동일
            return MelodyQuiz_Fail_Quit(self.ctx)

    def on_exit(self) -> None:
        self.set_user_value(triggerId=114, key='Reset', value=1)


class MelodyQuizPattern15(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        # 틀린 경우, 동일한 퀴즈를 다시 들려주기 위해 현재 트리거에서도 선택된 퍼즐 패턴을 기억
        self.set_user_value(key='PatternPick', value=115)
        self.set_user_value(triggerId=115, key='PatternPick', value=1)

    def on_tick(self) -> trigger_api.Trigger:
        if self.user_value(key='AnswerIsRight', value=1):
            return EndMelodyQuiz_Success(self.ctx)
        if self.user_value(key='AnswerIsWrong', value=1):
            return EndMelodyQuiz_Fail(self.ctx)
        if self.time_expired(timerId='1'):
            # UI 표시 안함 / 황금 상자 소유권 Additional Effect 71001011 지속시간 동일
            return MelodyQuiz_Fail_Quit(self.ctx)

    def on_exit(self) -> None:
        self.set_user_value(triggerId=115, key='Reset', value=1)


class MelodyQuizPattern16(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        # 틀린 경우, 동일한 퀴즈를 다시 들려주기 위해 현재 트리거에서도 선택된 퍼즐 패턴을 기억
        self.set_user_value(key='PatternPick', value=116)
        self.set_user_value(triggerId=116, key='PatternPick', value=1)

    def on_tick(self) -> trigger_api.Trigger:
        if self.user_value(key='AnswerIsRight', value=1):
            return EndMelodyQuiz_Success(self.ctx)
        if self.user_value(key='AnswerIsWrong', value=1):
            return EndMelodyQuiz_Fail(self.ctx)
        if self.time_expired(timerId='1'):
            # UI 표시 안함 / 황금 상자 소유권 Additional Effect 71001011 지속시간 동일
            return MelodyQuiz_Fail_Quit(self.ctx)

    def on_exit(self) -> None:
        self.set_user_value(triggerId=116, key='Reset', value=1)


class MelodyQuizPattern17(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        # 틀린 경우, 동일한 퀴즈를 다시 들려주기 위해 현재 트리거에서도 선택된 퍼즐 패턴을 기억
        self.set_user_value(key='PatternPick', value=117)
        self.set_user_value(triggerId=117, key='PatternPick', value=1)

    def on_tick(self) -> trigger_api.Trigger:
        if self.user_value(key='AnswerIsRight', value=1):
            return EndMelodyQuiz_Success(self.ctx)
        if self.user_value(key='AnswerIsWrong', value=1):
            return EndMelodyQuiz_Fail(self.ctx)
        if self.time_expired(timerId='1'):
            # UI 표시 안함 / 황금 상자 소유권 Additional Effect 71001011 지속시간 동일
            return MelodyQuiz_Fail_Quit(self.ctx)

    def on_exit(self) -> None:
        self.set_user_value(triggerId=117, key='Reset', value=1)


class MelodyQuizPattern18(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        # 틀린 경우, 동일한 퀴즈를 다시 들려주기 위해 현재 트리거에서도 선택된 퍼즐 패턴을 기억
        self.set_user_value(key='PatternPick', value=118)
        self.set_user_value(triggerId=118, key='PatternPick', value=1)

    def on_tick(self) -> trigger_api.Trigger:
        if self.user_value(key='AnswerIsRight', value=1):
            return EndMelodyQuiz_Success(self.ctx)
        if self.user_value(key='AnswerIsWrong', value=1):
            return EndMelodyQuiz_Fail(self.ctx)
        if self.time_expired(timerId='1'):
            # UI 표시 안함 / 황금 상자 소유권 Additional Effect 71001011 지속시간 동일
            return MelodyQuiz_Fail_Quit(self.ctx)

    def on_exit(self) -> None:
        self.set_user_value(triggerId=118, key='Reset', value=1)


class MelodyQuizPattern19(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        # 틀린 경우, 동일한 퀴즈를 다시 들려주기 위해 현재 트리거에서도 선택된 퍼즐 패턴을 기억
        self.set_user_value(key='PatternPick', value=119)
        self.set_user_value(triggerId=119, key='PatternPick', value=1)

    def on_tick(self) -> trigger_api.Trigger:
        if self.user_value(key='AnswerIsRight', value=1):
            return EndMelodyQuiz_Success(self.ctx)
        if self.user_value(key='AnswerIsWrong', value=1):
            return EndMelodyQuiz_Fail(self.ctx)
        if self.time_expired(timerId='1'):
            # UI 표시 안함 / 황금 상자 소유권 Additional Effect 71001011 지속시간 동일
            return MelodyQuiz_Fail_Quit(self.ctx)

    def on_exit(self) -> None:
        self.set_user_value(triggerId=119, key='Reset', value=1)


class MelodyQuizPattern20(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        # 틀린 경우, 동일한 퀴즈를 다시 들려주기 위해 현재 트리거에서도 선택된 퍼즐 패턴을 기억
        self.set_user_value(key='PatternPick', value=120)
        self.set_user_value(triggerId=120, key='PatternPick', value=1)

    def on_tick(self) -> trigger_api.Trigger:
        if self.user_value(key='AnswerIsRight', value=1):
            return EndMelodyQuiz_Success(self.ctx)
        if self.user_value(key='AnswerIsWrong', value=1):
            return EndMelodyQuiz_Fail(self.ctx)
        if self.time_expired(timerId='1'):
            # UI 표시 안함 / 황금 상자 소유권 Additional Effect 71001011 지속시간 동일
            return MelodyQuiz_Fail_Quit(self.ctx)

    def on_exit(self) -> None:
        self.set_user_value(triggerId=120, key='Reset', value=1)


# 퍼즐 성공 후 종료
class EndMelodyQuiz_Success(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.add_buff(boxIds=[11901], skillId=71001012, level=1, isPlayer=False, isSkillSet=False)
        self.set_effect(triggerIds=[11300], visible=True) # Success Sound Effect
        # RareBox 맵 별로 유니크하도록 변경해야 하는 값
        self.set_interact_object(triggerIds=[12000066], state=1)
        self.set_timer(timerId='2', seconds=60, startDelay=1, interval=0, vOffset=0)

    def on_tick(self) -> trigger_api.Trigger:
        if self.object_interacted(interactIds=[12000066], stateValue=0):
            # RareBox 맵 별로 유니크하도록 변경해야 하는 값
            return MelodyQuiz_Success_Quit(self.ctx)
        # <condition name="UserValue" key="TimeEventOn" value="0">
        if self.time_expired(timerId='2'):
            return MelodyQuiz_Success_Quit(self.ctx)


# 퍼즐 실패 후 재도전
class EndMelodyQuiz_Fail(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_effect(triggerIds=[11302], visible=True) # Wrong Sound Effect

    def on_tick(self) -> trigger_api.Trigger:
        if self.user_value(key='TimeEventOn', value=0):
            return EndMelodyQuiz_Fail_2(self.ctx)
        if self.time_expired(timerId='1'):
            # UI 표시 안함 / 황금 상자 소유권 Additional Effect 71001011 지속시간 동일
            return MelodyQuiz_Fail_Quit(self.ctx)
        if self.wait_tick(waitTick=2000):
            return MelodyQuiz_Retry(self.ctx)


class EndMelodyQuiz_Fail_2(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timerId='1'):
            # UI 표시 안함 / 황금 상자 소유권 Additional Effect 71001011 지속시간 동일
            return Wait(self.ctx)
        if self.wait_tick(waitTick=2000):
            return MelodyQuiz_Retry(self.ctx)


class MelodyQuiz_Retry(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_user_value(key='AnswerIsWrong', value=0)

    def on_tick(self) -> trigger_api.Trigger:
        if self.user_value(key='PatternPick', value=101):
            return MelodyQuizPattern01(self.ctx)
        if self.user_value(key='PatternPick', value=102):
            return MelodyQuizPattern02(self.ctx)
        if self.user_value(key='PatternPick', value=103):
            return MelodyQuizPattern03(self.ctx)
        if self.user_value(key='PatternPick', value=104):
            return MelodyQuizPattern04(self.ctx)
        if self.user_value(key='PatternPick', value=105):
            return MelodyQuizPattern05(self.ctx)
        if self.user_value(key='PatternPick', value=106):
            return MelodyQuizPattern06(self.ctx)
        if self.user_value(key='PatternPick', value=107):
            return MelodyQuizPattern07(self.ctx)
        if self.user_value(key='PatternPick', value=108):
            return MelodyQuizPattern08(self.ctx)
        if self.user_value(key='PatternPick', value=109):
            return MelodyQuizPattern09(self.ctx)
        if self.user_value(key='PatternPick', value=110):
            return MelodyQuizPattern10(self.ctx)
        if self.user_value(key='PatternPick', value=111):
            return MelodyQuizPattern11(self.ctx)
        if self.user_value(key='PatternPick', value=112):
            return MelodyQuizPattern12(self.ctx)
        if self.user_value(key='PatternPick', value=113):
            return MelodyQuizPattern13(self.ctx)
        if self.user_value(key='PatternPick', value=114):
            return MelodyQuizPattern14(self.ctx)
        if self.user_value(key='PatternPick', value=115):
            return MelodyQuizPattern15(self.ctx)
        if self.user_value(key='PatternPick', value=116):
            return MelodyQuizPattern16(self.ctx)
        if self.user_value(key='PatternPick', value=117):
            return MelodyQuizPattern17(self.ctx)
        if self.user_value(key='PatternPick', value=118):
            return MelodyQuizPattern18(self.ctx)
        if self.user_value(key='PatternPick', value=119):
            return MelodyQuizPattern19(self.ctx)
        if self.user_value(key='PatternPick', value=120): # 패턴 추가
            return MelodyQuizPattern20(self.ctx)


class MelodyQuiz_Fail_Quit(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        # self.set_user_value(key='TimeEventOn', value=0)
        # self.remove_buff(boxId=9001, skillId=71001011, isPlayer=True)
        # UI 표시 안함 / 황금 상자 소유권 Additional Effect 71001011 지속시간 동일
        self.reset_timer(timerId='1')
        self.reset_timer(timerId='2')

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=1000):
            return Wait(self.ctx)


class MelodyQuiz_Success_Quit(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_user_value(key='TimeEventOn', value=0)
        # self.remove_buff(boxId=9001, skillId=71001011, isPlayer=True)
        # UI 표시 안함 / 황금 상자 소유권 Additional Effect 71001011 지속시간 동일
        self.reset_timer(timerId='1')
        self.reset_timer(timerId='2')

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=1000):
            return Wait(self.ctx)


initial_state = Wait
