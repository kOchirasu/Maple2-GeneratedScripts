""" trigger/52000051_qd/04_puzzlemain.xml """
from common import *
import state


class Wait(state.State):
    def on_enter(self):
        set_user_value(key='CorrectFirstPiece', value=0)
        set_user_value(key='CorrectSecondPiece', value=0)
        set_user_value(key='CorrectThirdPiece', value=0)
        set_user_value(key='CorrectFouthPiece', value=0)
        set_effect(triggerIds=[5002], visible=False) # 가이드 서머리 사운드 이펙트
        set_effect(triggerIds=[5003], visible=False) # Pattern_LightOn
        set_interact_object(triggerIds=[10001023], state=0) # Lever
        set_user_value(key='PuzzleStart', value=0)
        set_mesh(triggerIds=[3100,3101,3102,3103,3104,3105,3106,3107,3108,3109], visible=False, arg3=0, arg4=0, arg5=0) # Quiz
        set_mesh(triggerIds=[3001,3002,3003,3004], visible=False, arg3=0, arg4=0, arg5=0) # BaseRock
        set_mesh(triggerIds=[3020], visible=False, arg3=0, arg4=0, arg5=0) # LionStone

    def on_tick(self) -> state.State:
        if user_value(key='PuzzleStart', value=1):
            return StartPuzzle()


class StartPuzzle(state.State):
    def on_enter(self):
        set_user_value(triggerId=5, key='PickFirstPiece', value=1) # 두 번째 문양은 첫 번째 뽑힌 문양을 제외하고 6번 트리거에서 뽑음 , 중복 2개 제한 장치
        set_user_value(triggerId=7, key='PickThirdPiece', value=1) # 네 번째 문양은 세 번째 뽑힌 문양을 제외하고 8번 트리거에서 뽑음 , 중복 2개 제한 장치
        set_interact_object(triggerIds=[10001023], state=1) # Lever
        set_mesh(triggerIds=[3020], visible=True, arg3=0, arg4=0, arg5=0) # LionStone
        set_effect(triggerIds=[5002], visible=True) # 가이드 서머리 사운드 이펙트

    def on_tick(self) -> state.State:
        if object_interacted(interactIds=[10001023], arg2=0):
            return CheckAnswer01()


class CheckAnswer01(state.State):
    def on_enter(self):
        set_mesh(triggerIds=[3020], visible=False, arg3=200, arg4=0, arg5=0) # LionStone
        set_user_value(triggerId=5, key='CheckFirstPiece', value=1)
        set_user_value(triggerId=6, key='CheckSecondPiece', value=1)
        set_user_value(triggerId=7, key='CheckThirdPiece', value=1)
        set_user_value(triggerId=8, key='CheckFourthPiece', value=1)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=300):
            return CheckAnswer02()


#  순차적으로 체크 
class CheckAnswer02(state.State):
    def on_tick(self) -> state.State:
        if user_value(key='CorrectFirstPiece', value=2):
            return Retry01()
        if user_value(key='CorrectSecondPiece', value=2):
            return Retry01()
        if user_value(key='CorrectThirdPiece', value=2):
            return Retry01()
        if user_value(key='CorrectFouthPiece', value=2):
            return Retry01()
        if user_value(key='CorrectFirstPiece', value=1):
            return CheckAnswer03()


class CheckAnswer03(state.State):
    def on_tick(self) -> state.State:
        if user_value(key='CorrectFirstPiece', value=2):
            return Retry01()
        if user_value(key='CorrectSecondPiece', value=2):
            return Retry01()
        if user_value(key='CorrectThirdPiece', value=2):
            return Retry01()
        if user_value(key='CorrectFouthPiece', value=2):
            return Retry01()
        if user_value(key='CorrectSecondPiece', value=1):
            return CheckAnswer04()


class CheckAnswer04(state.State):
    def on_tick(self) -> state.State:
        if user_value(key='CorrectFirstPiece', value=2):
            return Retry01()
        if user_value(key='CorrectSecondPiece', value=2):
            return Retry01()
        if user_value(key='CorrectThirdPiece', value=2):
            return Retry01()
        if user_value(key='CorrectFourthPiece', value=2):
            return Retry01()
        if user_value(key='CorrectThirdPiece', value=1):
            return CheckAnswer05()


class CheckAnswer05(state.State):
    def on_tick(self) -> state.State:
        if user_value(key='CorrectFirstPiece', value=2):
            return Retry01()
        if user_value(key='CorrectSecondPiece', value=2):
            return Retry01()
        if user_value(key='CorrectThirdPiece', value=2):
            return Retry01()
        if user_value(key='CorrectFourthPiece', value=2):
            return Retry01()
        if user_value(key='CorrectFourthPiece', value=1):
            return PuzzleSolved()


#  4개 중 하나라도 맞지 않으면 재시도 
class Retry01(state.State):
    def on_enter(self):
        set_effect(triggerIds=[5002], visible=True) # 가이드 서머리 사운드 이펙트
        set_event_ui(type=1, arg2='$52000051_QD__04_PUZZLEMAIN__0$', arg3='3000', arg4='0')
        set_user_value(key='CorrectFirstPiece', value=0)
        set_user_value(key='CorrectSecondPiece', value=0)
        set_user_value(key='CorrectThirdPiece', value=0)
        set_user_value(key='CorrectFouthPiece', value=0)
        set_user_value(triggerId=5, key='ResetFirstPiece', value=1)
        set_user_value(triggerId=6, key='ResetSecondPiece', value=1)
        set_user_value(triggerId=7, key='ResetThirdPiece', value=1)
        set_user_value(triggerId=8, key='ResetFourthPiece', value=1)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=3000):
            return Retry02()


class Retry02(state.State):
    def on_enter(self):
        set_interact_object(triggerIds=[10001023], state=1) # Lever
        set_mesh(triggerIds=[3020], visible=True, arg3=0, arg4=0, arg5=0) # LionStone

    def on_tick(self) -> state.State:
        if object_interacted(interactIds=[10001023], arg2=0):
            return CheckAnswer01()

    def on_exit(self):
        hide_guide_summary(entityId=10036010)


class PuzzleSolved(state.State):
    def on_enter(self):
        set_effect(triggerIds=[5003], visible=True) # Pattern_LightOn
        set_mesh(triggerIds=[3001,3002,3003,3004], visible=True, arg3=0, arg4=0, arg5=0) # BaseRock
        set_user_value(triggerId=1, key='PuzzleSolved', value=1)
        set_user_value(triggerId=5, key='LockFirstPiece', value=1)
        set_user_value(triggerId=6, key='LockSecondPiece', value=1)
        set_user_value(triggerId=7, key='LockThirdPiece', value=1)
        set_user_value(triggerId=8, key='LockFourthPiece', value=1)
        set_achievement(triggerId=9001, type='trigger', achieve='OrientPattern_Puzzle')

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=1000):
            return Quit()


class Quit(state.State):
    pass


