""" trigger/52000051_qd/04_puzzlemain.xml """
import trigger_api


class Wait(trigger_api.Trigger):
    def on_enter(self):
        self.set_user_value(key='CorrectFirstPiece', value=0)
        self.set_user_value(key='CorrectSecondPiece', value=0)
        self.set_user_value(key='CorrectThirdPiece', value=0)
        self.set_user_value(key='CorrectFouthPiece', value=0)
        self.set_effect(triggerIds=[5002], visible=False) # 가이드 서머리 사운드 이펙트
        self.set_effect(triggerIds=[5003], visible=False) # Pattern_LightOn
        self.set_interact_object(triggerIds=[10001023], state=0) # Lever
        self.set_user_value(key='PuzzleStart', value=0)
        self.set_mesh(triggerIds=[3100,3101,3102,3103,3104,3105,3106,3107,3108,3109], visible=False, arg3=0, delay=0, scale=0) # Quiz
        self.set_mesh(triggerIds=[3001,3002,3003,3004], visible=False, arg3=0, delay=0, scale=0) # BaseRock
        self.set_mesh(triggerIds=[3020], visible=False, arg3=0, delay=0, scale=0) # LionStone

    def on_tick(self) -> trigger_api.Trigger:
        if self.user_value(key='PuzzleStart', value=1):
            return StartPuzzle(self.ctx)


class StartPuzzle(trigger_api.Trigger):
    def on_enter(self):
        self.set_user_value(triggerId=5, key='PickFirstPiece', value=1) # 두 번째 문양은 첫 번째 뽑힌 문양을 제외하고 6번 트리거에서 뽑음 , 중복 2개 제한 장치
        self.set_user_value(triggerId=7, key='PickThirdPiece', value=1) # 네 번째 문양은 세 번째 뽑힌 문양을 제외하고 8번 트리거에서 뽑음 , 중복 2개 제한 장치
        self.set_interact_object(triggerIds=[10001023], state=1) # Lever
        self.set_mesh(triggerIds=[3020], visible=True, arg3=0, delay=0, scale=0) # LionStone
        self.set_effect(triggerIds=[5002], visible=True) # 가이드 서머리 사운드 이펙트

    def on_tick(self) -> trigger_api.Trigger:
        if self.object_interacted(interactIds=[10001023], stateValue=0):
            return CheckAnswer01(self.ctx)


class CheckAnswer01(trigger_api.Trigger):
    def on_enter(self):
        self.set_mesh(triggerIds=[3020], visible=False, arg3=200, delay=0, scale=0) # LionStone
        self.set_user_value(triggerId=5, key='CheckFirstPiece', value=1)
        self.set_user_value(triggerId=6, key='CheckSecondPiece', value=1)
        self.set_user_value(triggerId=7, key='CheckThirdPiece', value=1)
        self.set_user_value(triggerId=8, key='CheckFourthPiece', value=1)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=300):
            return CheckAnswer02(self.ctx)


# 순차적으로 체크
class CheckAnswer02(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.user_value(key='CorrectFirstPiece', value=2):
            return Retry01(self.ctx)
        if self.user_value(key='CorrectSecondPiece', value=2):
            return Retry01(self.ctx)
        if self.user_value(key='CorrectThirdPiece', value=2):
            return Retry01(self.ctx)
        if self.user_value(key='CorrectFouthPiece', value=2):
            return Retry01(self.ctx)
        if self.user_value(key='CorrectFirstPiece', value=1):
            return CheckAnswer03(self.ctx)


class CheckAnswer03(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.user_value(key='CorrectFirstPiece', value=2):
            return Retry01(self.ctx)
        if self.user_value(key='CorrectSecondPiece', value=2):
            return Retry01(self.ctx)
        if self.user_value(key='CorrectThirdPiece', value=2):
            return Retry01(self.ctx)
        if self.user_value(key='CorrectFouthPiece', value=2):
            return Retry01(self.ctx)
        if self.user_value(key='CorrectSecondPiece', value=1):
            return CheckAnswer04(self.ctx)


class CheckAnswer04(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.user_value(key='CorrectFirstPiece', value=2):
            return Retry01(self.ctx)
        if self.user_value(key='CorrectSecondPiece', value=2):
            return Retry01(self.ctx)
        if self.user_value(key='CorrectThirdPiece', value=2):
            return Retry01(self.ctx)
        if self.user_value(key='CorrectFourthPiece', value=2):
            return Retry01(self.ctx)
        if self.user_value(key='CorrectThirdPiece', value=1):
            return CheckAnswer05(self.ctx)


class CheckAnswer05(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.user_value(key='CorrectFirstPiece', value=2):
            return Retry01(self.ctx)
        if self.user_value(key='CorrectSecondPiece', value=2):
            return Retry01(self.ctx)
        if self.user_value(key='CorrectThirdPiece', value=2):
            return Retry01(self.ctx)
        if self.user_value(key='CorrectFourthPiece', value=2):
            return Retry01(self.ctx)
        if self.user_value(key='CorrectFourthPiece', value=1):
            return PuzzleSolved(self.ctx)


# 4개 중 하나라도 맞지 않으면 재시도
class Retry01(trigger_api.Trigger):
    def on_enter(self):
        self.set_effect(triggerIds=[5002], visible=True) # 가이드 서머리 사운드 이펙트
        self.set_event_ui(type=1, arg2='$52000051_QD__04_PUZZLEMAIN__0$', arg3='3000', arg4='0')
        self.set_user_value(key='CorrectFirstPiece', value=0)
        self.set_user_value(key='CorrectSecondPiece', value=0)
        self.set_user_value(key='CorrectThirdPiece', value=0)
        self.set_user_value(key='CorrectFouthPiece', value=0)
        self.set_user_value(triggerId=5, key='ResetFirstPiece', value=1)
        self.set_user_value(triggerId=6, key='ResetSecondPiece', value=1)
        self.set_user_value(triggerId=7, key='ResetThirdPiece', value=1)
        self.set_user_value(triggerId=8, key='ResetFourthPiece', value=1)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=3000):
            return Retry02(self.ctx)


class Retry02(trigger_api.Trigger):
    def on_enter(self):
        self.set_interact_object(triggerIds=[10001023], state=1) # Lever
        self.set_mesh(triggerIds=[3020], visible=True, arg3=0, delay=0, scale=0) # LionStone

    def on_tick(self) -> trigger_api.Trigger:
        if self.object_interacted(interactIds=[10001023], stateValue=0):
            return CheckAnswer01(self.ctx)

    def on_exit(self):
        self.hide_guide_summary(entityId=10036010)


class PuzzleSolved(trigger_api.Trigger):
    def on_enter(self):
        self.set_effect(triggerIds=[5003], visible=True) # Pattern_LightOn
        self.set_mesh(triggerIds=[3001,3002,3003,3004], visible=True, arg3=0, delay=0, scale=0) # BaseRock
        self.set_user_value(triggerId=1, key='PuzzleSolved', value=1)
        self.set_user_value(triggerId=5, key='LockFirstPiece', value=1)
        self.set_user_value(triggerId=6, key='LockSecondPiece', value=1)
        self.set_user_value(triggerId=7, key='LockThirdPiece', value=1)
        self.set_user_value(triggerId=8, key='LockFourthPiece', value=1)
        self.set_achievement(triggerId=9001, type='trigger', achieve='OrientPattern_Puzzle')

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=1000):
            return Quit(self.ctx)


class Quit(trigger_api.Trigger):
    pass


initial_state = Wait
