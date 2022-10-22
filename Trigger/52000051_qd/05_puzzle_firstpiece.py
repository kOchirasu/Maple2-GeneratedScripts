""" trigger/52000051_qd/05_puzzle_firstpiece.xml """
from common import *
import state


class Wait(state.State):
    def on_enter(self):
        set_user_value(key='PickFirstPiece', value=0)
        set_user_value(key='CheckFirstPiece', value=0)
        set_user_value(key='CorrectFirstPiece', value=0)
        set_user_value(key='ResetFirstPiece', value=0)
        set_user_value(key='LockFirstPiece', value=0)
        set_mesh(triggerIds=[3100,3101,3102,3103,3104,3105,3106,3107,3108,3109], visible=False, arg3=0, arg4=0, arg5=0) # Pattern_Ground
        set_mesh(triggerIds=[3110,3111,3112,3113,3114,3115,3116,3117,3118,3119], visible=False, arg3=0, arg4=0, arg5=0) # Pattern_LightOn

    def on_tick(self) -> state.State:
        if user_value(key='PickFirstPiece', value=1):
            return RandomPick()


class RandomPick(state.State):
    def on_tick(self) -> state.State:
        if random_condition(rate=10):
            return Pattern01_Pick()
        if random_condition(rate=10):
            return Pattern02_Pick()
        if random_condition(rate=10):
            return Pattern03_Pick()
        if random_condition(rate=10):
            return Pattern04_Pick()
        if random_condition(rate=10):
            return Pattern05_Pick()
        if random_condition(rate=10):
            return Pattern06_Pick()
        if random_condition(rate=10):
            return Pattern07_Pick()
        if random_condition(rate=10):
            return Pattern08_Pick()
        if random_condition(rate=10):
            return Pattern09_Pick()
        if random_condition(rate=10):
            return Pattern10_Pick()


#  첫 번째 패턴 뽑힘 
class Pattern01_Pick(state.State):
    def on_enter(self):
        set_mesh(triggerIds=[3100], visible=True, arg3=0, arg4=0, arg5=0) # Pattern_Ground_A01
        set_user_value(triggerId=6, key='PickSecondPieceExceptA01', value=1)

    def on_tick(self) -> state.State:
        if user_value(key='CheckFirstPiece', value=1):
            return Pattern01_Check()


#  첫 번째 패턴 정답 체크 
class Pattern01_Check(state.State):
    def on_tick(self) -> state.State:
        if detect_liftable_object(boxIds=[2001], itemId=30000565):
            return Pattern01_CorrectAnswer()
        if not detect_liftable_object(boxIds=[2001], itemId=30000565):
            return Pattern01_WrongAnswer()


#  첫 번째 패턴 정답 
class Pattern01_CorrectAnswer(state.State):
    def on_enter(self):
        set_user_value(triggerId=4, key='CorrectFirstPiece', value=1) # 정답
        set_mesh(triggerIds=[3110], visible=True, arg3=100, arg4=0, arg5=5) # Pattern_LightOn_A01

    def on_tick(self) -> state.State:
        if user_value(key='ResetFirstPiece', value=1):
            return Pattern01_Reset01()
        if user_value(key='LockFirstPiece', value=1):
            return Quit()


#  첫 번째 패턴 오답 
class Pattern01_WrongAnswer(state.State):
    def on_enter(self):
        set_user_value(triggerId=4, key='CorrectFirstPiece', value=2) # 오답

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=2000):
            return Pattern01_Reset01()


class Pattern01_Reset01(state.State):
    def on_enter(self):
        set_user_value(key='CheckFirstPiece', value=0)
        set_user_value(key='CorrectFirstPiece', value=0)
        set_user_value(key='ResetFirstPiece', value=0)
        set_user_value(key='LockFirstPiece', value=0)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=1000):
            return Pattern01_Reset02()


#  첫 번째 패턴 다시체크 
class Pattern01_Reset02(state.State):
    def on_enter(self):
        set_mesh(triggerIds=[3110], visible=False, arg3=100, arg4=0, arg5=5) # Pattern_LightOn_A01

    def on_tick(self) -> state.State:
        if user_value(key='CheckFirstPiece', value=1):
            return Pattern01_Check()


#  두 번째 패턴 뽑힘 
class Pattern02_Pick(state.State):
    def on_enter(self):
        set_mesh(triggerIds=[3101], visible=True, arg3=0, arg4=0, arg5=0) # Pattern_Ground_A02
        set_user_value(triggerId=6, key='PickSecondPieceExceptA02', value=1)

    def on_tick(self) -> state.State:
        if user_value(key='CheckFirstPiece', value=1):
            return Pattern02_Check()


#  두 번째 패턴 정답 체크 
class Pattern02_Check(state.State):
    def on_tick(self) -> state.State:
        if detect_liftable_object(boxIds=[2001], itemId=30000566):
            return Pattern02_CorrectAnswer()
        if not detect_liftable_object(boxIds=[2001], itemId=30000566):
            return Pattern02_WrongAnswer()


#  두 번째 패턴 정답 
class Pattern02_CorrectAnswer(state.State):
    def on_enter(self):
        set_user_value(triggerId=4, key='CorrectFirstPiece', value=1) # 정답
        set_mesh(triggerIds=[3111], visible=True, arg3=100, arg4=0, arg5=5) # Pattern_LightOn_A02

    def on_tick(self) -> state.State:
        if user_value(key='ResetFirstPiece', value=1):
            return Pattern02_Reset01()
        if user_value(key='LockFirstPiece', value=1):
            return Quit()


#  두 번째 패턴 오답 
class Pattern02_WrongAnswer(state.State):
    def on_enter(self):
        set_user_value(triggerId=4, key='CorrectFirstPiece', value=2) # 오답

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=2000):
            return Pattern02_Reset01()


class Pattern02_Reset01(state.State):
    def on_enter(self):
        set_user_value(key='CheckFirstPiece', value=0)
        set_user_value(key='CorrectFirstPiece', value=0)
        set_user_value(key='ResetFirstPiece', value=0)
        set_user_value(key='LockFirstPiece', value=0)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=1000):
            return Pattern02_Reset02()


#  두 번째 패턴 다시체크 
class Pattern02_Reset02(state.State):
    def on_enter(self):
        set_mesh(triggerIds=[3111], visible=False, arg3=100, arg4=0, arg5=5) # Pattern_LightOn_A02

    def on_tick(self) -> state.State:
        if user_value(key='CheckFirstPiece', value=1):
            return Pattern02_Check()


#  세 번째 패턴 뽑힘 
class Pattern03_Pick(state.State):
    def on_enter(self):
        set_mesh(triggerIds=[3102], visible=True, arg3=0, arg4=0, arg5=0) # Pattern_Ground_A03
        set_user_value(triggerId=6, key='PickSecondPieceExceptA03', value=1)

    def on_tick(self) -> state.State:
        if user_value(key='CheckFirstPiece', value=1):
            return Pattern03_Check()


#  세 번째 패턴 정답 체크 
class Pattern03_Check(state.State):
    def on_tick(self) -> state.State:
        if detect_liftable_object(boxIds=[2001], itemId=30000567):
            return Pattern03_CorrectAnswer()
        if not detect_liftable_object(boxIds=[2001], itemId=30000567):
            return Pattern03_WrongAnswer()


#  세 번째 패턴 정답 
class Pattern03_CorrectAnswer(state.State):
    def on_enter(self):
        set_user_value(triggerId=4, key='CorrectFirstPiece', value=1) # 정답
        set_mesh(triggerIds=[3112], visible=True, arg3=100, arg4=0, arg5=5) # Pattern_LightOn_A03

    def on_tick(self) -> state.State:
        if user_value(key='ResetFirstPiece', value=1):
            return Pattern03_Reset01()
        if user_value(key='LockFirstPiece', value=1):
            return Quit()


#  세 번째 패턴 오답 
class Pattern03_WrongAnswer(state.State):
    def on_enter(self):
        set_user_value(triggerId=4, key='CorrectFirstPiece', value=2) # 오답

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=2000):
            return Pattern03_Reset01()


class Pattern03_Reset01(state.State):
    def on_enter(self):
        set_user_value(key='CheckFirstPiece', value=0)
        set_user_value(key='CorrectFirstPiece', value=0)
        set_user_value(key='ResetFirstPiece', value=0)
        set_user_value(key='LockFirstPiece', value=0)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=1000):
            return Pattern03_Reset02()


#  세 번째 패턴 다시체크 
class Pattern03_Reset02(state.State):
    def on_enter(self):
        set_mesh(triggerIds=[3112], visible=False, arg3=100, arg4=0, arg5=5) # Pattern_LightOn_A03

    def on_tick(self) -> state.State:
        if user_value(key='CheckFirstPiece', value=1):
            return Pattern03_Check()


#  네 번째 패턴 뽑힘 
class Pattern04_Pick(state.State):
    def on_enter(self):
        set_mesh(triggerIds=[3103], visible=True, arg3=0, arg4=0, arg5=0) # Pattern_Ground_B01
        set_user_value(triggerId=6, key='PickSecondPieceExceptB01', value=1)

    def on_tick(self) -> state.State:
        if user_value(key='CheckFirstPiece', value=1):
            return Pattern04_Check()


#  네 번째 패턴 정답 체크 
class Pattern04_Check(state.State):
    def on_tick(self) -> state.State:
        if detect_liftable_object(boxIds=[2001], itemId=30000568):
            return Pattern04_CorrectAnswer()
        if not detect_liftable_object(boxIds=[2001], itemId=30000568):
            return Pattern04_WrongAnswer()


#  네 번째 패턴 정답 
class Pattern04_CorrectAnswer(state.State):
    def on_enter(self):
        set_user_value(triggerId=4, key='CorrectFirstPiece', value=1) # 정답
        set_mesh(triggerIds=[3113], visible=True, arg3=100, arg4=0, arg5=5) # Pattern_LightOn_B01

    def on_tick(self) -> state.State:
        if user_value(key='ResetFirstPiece', value=1):
            return Pattern04_Reset01()
        if user_value(key='LockFirstPiece', value=1):
            return Quit()


#  네 번째 패턴 오답 
class Pattern04_WrongAnswer(state.State):
    def on_enter(self):
        set_user_value(triggerId=4, key='CorrectFirstPiece', value=2) # 오답

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=2000):
            return Pattern04_Reset01()


class Pattern04_Reset01(state.State):
    def on_enter(self):
        set_user_value(key='CheckFirstPiece', value=0)
        set_user_value(key='CorrectFirstPiece', value=0)
        set_user_value(key='ResetFirstPiece', value=0)
        set_user_value(key='LockFirstPiece', value=0)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=1000):
            return Pattern04_Reset02()


#  네 번째 패턴 다시체크 
class Pattern04_Reset02(state.State):
    def on_enter(self):
        set_mesh(triggerIds=[3113], visible=False, arg3=100, arg4=0, arg5=5) # Pattern_LightOn_B01

    def on_tick(self) -> state.State:
        if user_value(key='CheckFirstPiece', value=1):
            return Pattern04_Check()


#  다섯 번째 패턴 뽑힘 
class Pattern05_Pick(state.State):
    def on_enter(self):
        set_mesh(triggerIds=[3104], visible=True, arg3=0, arg4=0, arg5=0) # Pattern_Ground_B02
        set_user_value(triggerId=6, key='PickSecondPieceExceptB02', value=1)

    def on_tick(self) -> state.State:
        if user_value(key='CheckFirstPiece', value=1):
            return Pattern05_Check()


#  다섯 번째 패턴 정답 체크 
class Pattern05_Check(state.State):
    def on_tick(self) -> state.State:
        if detect_liftable_object(boxIds=[2001], itemId=30000569):
            return Pattern05_CorrectAnswer()
        if not detect_liftable_object(boxIds=[2001], itemId=30000569):
            return Pattern05_WrongAnswer()


#  다섯 번째 패턴 정답 
class Pattern05_CorrectAnswer(state.State):
    def on_enter(self):
        set_user_value(triggerId=4, key='CorrectFirstPiece', value=1) # 정답
        set_mesh(triggerIds=[3114], visible=True, arg3=100, arg4=0, arg5=5) # Pattern_LightOn_B02

    def on_tick(self) -> state.State:
        if user_value(key='ResetFirstPiece', value=1):
            return Pattern05_Reset01()
        if user_value(key='LockFirstPiece', value=1):
            return Quit()


#  다섯 번째 패턴 오답 
class Pattern05_WrongAnswer(state.State):
    def on_enter(self):
        set_user_value(triggerId=4, key='CorrectFirstPiece', value=2) # 오답

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=2000):
            return Pattern05_Reset01()


class Pattern05_Reset01(state.State):
    def on_enter(self):
        set_user_value(key='CheckFirstPiece', value=0)
        set_user_value(key='CorrectFirstPiece', value=0)
        set_user_value(key='ResetFirstPiece', value=0)
        set_user_value(key='LockFirstPiece', value=0)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=1000):
            return Pattern05_Reset02()


#  다섯 번째 패턴 다시체크 
class Pattern05_Reset02(state.State):
    def on_enter(self):
        set_mesh(triggerIds=[3114], visible=False, arg3=100, arg4=0, arg5=5) # Pattern_LightOn_B02

    def on_tick(self) -> state.State:
        if user_value(key='CheckFirstPiece', value=1):
            return Pattern05_Check()


#  여섯 번째 패턴 뽑힘 
class Pattern06_Pick(state.State):
    def on_enter(self):
        set_mesh(triggerIds=[3105], visible=True, arg3=0, arg4=0, arg5=0) # Pattern_Ground_C01
        set_user_value(triggerId=6, key='PickSecondPieceExceptC01', value=1)

    def on_tick(self) -> state.State:
        if user_value(key='CheckFirstPiece', value=1):
            return Pattern06_Check()


#  여섯 번째 패턴 정답 체크 
class Pattern06_Check(state.State):
    def on_tick(self) -> state.State:
        if detect_liftable_object(boxIds=[2001], itemId=30000570):
            return Pattern06_CorrectAnswer()
        if not detect_liftable_object(boxIds=[2001], itemId=30000570):
            return Pattern06_WrongAnswer()


#  여섯 번째 패턴 정답 
class Pattern06_CorrectAnswer(state.State):
    def on_enter(self):
        set_user_value(triggerId=4, key='CorrectFirstPiece', value=1) # 정답
        set_mesh(triggerIds=[3115], visible=True, arg3=100, arg4=0, arg5=5) # Pattern_LightOn_C01

    def on_tick(self) -> state.State:
        if user_value(key='ResetFirstPiece', value=1):
            return Pattern06_Reset01()
        if user_value(key='LockFirstPiece', value=1):
            return Quit()


#  여섯 번째 패턴 오답 
class Pattern06_WrongAnswer(state.State):
    def on_enter(self):
        set_user_value(triggerId=4, key='CorrectFirstPiece', value=2) # 오답

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=2000):
            return Pattern06_Reset01()


class Pattern06_Reset01(state.State):
    def on_enter(self):
        set_user_value(key='CheckFirstPiece', value=0)
        set_user_value(key='CorrectFirstPiece', value=0)
        set_user_value(key='ResetFirstPiece', value=0)
        set_user_value(key='LockFirstPiece', value=0)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=1000):
            return Pattern06_Reset02()


#  여섯 번째 패턴 다시체크 
class Pattern06_Reset02(state.State):
    def on_enter(self):
        set_mesh(triggerIds=[3115], visible=False, arg3=100, arg4=0, arg5=5) # Pattern_LightOn_C01

    def on_tick(self) -> state.State:
        if user_value(key='CheckFirstPiece', value=1):
            return Pattern06_Check()


#  일곱 번째 패턴 뽑힘 
class Pattern07_Pick(state.State):
    def on_enter(self):
        set_mesh(triggerIds=[3106], visible=True, arg3=0, arg4=0, arg5=0) # Pattern_Ground_D01
        set_user_value(triggerId=6, key='PickSecondPieceExceptD01', value=1)

    def on_tick(self) -> state.State:
        if user_value(key='CheckFirstPiece', value=1):
            return Pattern07_Check()


#  일곱 번째 패턴 정답 체크 
class Pattern07_Check(state.State):
    def on_tick(self) -> state.State:
        if detect_liftable_object(boxIds=[2001], itemId=30000571):
            return Pattern07_CorrectAnswer()
        if not detect_liftable_object(boxIds=[2001], itemId=30000571):
            return Pattern07_WrongAnswer()


#  일곱 번째 패턴 정답 
class Pattern07_CorrectAnswer(state.State):
    def on_enter(self):
        set_user_value(triggerId=4, key='CorrectFirstPiece', value=1) # 정답
        set_mesh(triggerIds=[3116], visible=True, arg3=100, arg4=0, arg5=5) # Pattern_LightOn_D01

    def on_tick(self) -> state.State:
        if user_value(key='ResetFirstPiece', value=1):
            return Pattern07_Reset01()
        if user_value(key='LockFirstPiece', value=1):
            return Quit()


#  일곱 번째 패턴 오답 
class Pattern07_WrongAnswer(state.State):
    def on_enter(self):
        set_user_value(triggerId=4, key='CorrectFirstPiece', value=2) # 오답

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=2000):
            return Pattern07_Reset01()


class Pattern07_Reset01(state.State):
    def on_enter(self):
        set_user_value(key='CheckFirstPiece', value=0)
        set_user_value(key='CorrectFirstPiece', value=0)
        set_user_value(key='ResetFirstPiece', value=0)
        set_user_value(key='LockFirstPiece', value=0)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=1000):
            return Pattern07_Reset02()


#  일곱 번째 패턴 다시체크 
class Pattern07_Reset02(state.State):
    def on_enter(self):
        set_mesh(triggerIds=[3116], visible=False, arg3=100, arg4=0, arg5=5) # Pattern_LightOn_D01

    def on_tick(self) -> state.State:
        if user_value(key='CheckFirstPiece', value=1):
            return Pattern07_Check()


#  여덟 번째 패턴 뽑힘 
class Pattern08_Pick(state.State):
    def on_enter(self):
        set_mesh(triggerIds=[3107], visible=True, arg3=0, arg4=0, arg5=0) # Pattern_Ground_D02
        set_user_value(triggerId=6, key='PickSecondPieceExceptD02', value=1)

    def on_tick(self) -> state.State:
        if user_value(key='CheckFirstPiece', value=1):
            return Pattern08_Check()


#  여덟 번째 패턴 정답 체크 
class Pattern08_Check(state.State):
    def on_tick(self) -> state.State:
        if detect_liftable_object(boxIds=[2001], itemId=30000572):
            return Pattern08_CorrectAnswer()
        if not detect_liftable_object(boxIds=[2001], itemId=30000572):
            return Pattern08_WrongAnswer()


#  여덟 번째 패턴 정답 
class Pattern08_CorrectAnswer(state.State):
    def on_enter(self):
        set_user_value(triggerId=4, key='CorrectFirstPiece', value=1) # 정답
        set_mesh(triggerIds=[3117], visible=True, arg3=100, arg4=0, arg5=5) # Pattern_LightOn_D02

    def on_tick(self) -> state.State:
        if user_value(key='ResetFirstPiece', value=1):
            return Pattern08_Reset01()
        if user_value(key='LockFirstPiece', value=1):
            return Quit()


#  여덟 번째 패턴 오답 
class Pattern08_WrongAnswer(state.State):
    def on_enter(self):
        set_user_value(triggerId=4, key='CorrectFirstPiece', value=2) # 오답

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=2000):
            return Pattern08_Reset01()


class Pattern08_Reset01(state.State):
    def on_enter(self):
        set_user_value(key='CheckFirstPiece', value=0)
        set_user_value(key='CorrectFirstPiece', value=0)
        set_user_value(key='ResetFirstPiece', value=0)
        set_user_value(key='LockFirstPiece', value=0)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=1000):
            return Pattern08_Reset02()


#  여덟 번째 패턴 다시체크 
class Pattern08_Reset02(state.State):
    def on_enter(self):
        set_mesh(triggerIds=[3117], visible=False, arg3=100, arg4=0, arg5=5) # Pattern_LightOn_D02

    def on_tick(self) -> state.State:
        if user_value(key='CheckFirstPiece', value=1):
            return Pattern08_Check()


#  아홉 번째 패턴 뽑힘 
class Pattern09_Pick(state.State):
    def on_enter(self):
        set_mesh(triggerIds=[3108], visible=True, arg3=0, arg4=0, arg5=0) # Pattern_Ground_E01
        set_user_value(triggerId=6, key='PickSecondPieceExceptE01', value=1)

    def on_tick(self) -> state.State:
        if user_value(key='CheckFirstPiece', value=1):
            return Pattern09_Check()


#  아홉 번째 패턴 정답 체크 
class Pattern09_Check(state.State):
    def on_tick(self) -> state.State:
        if detect_liftable_object(boxIds=[2001], itemId=30000573):
            return Pattern09_CorrectAnswer()
        if not detect_liftable_object(boxIds=[2001], itemId=30000573):
            return Pattern09_WrongAnswer()


#  아홉 번째 패턴 정답 
class Pattern09_CorrectAnswer(state.State):
    def on_enter(self):
        set_user_value(triggerId=4, key='CorrectFirstPiece', value=1) # 정답
        set_mesh(triggerIds=[3118], visible=True, arg3=100, arg4=0, arg5=5) # Pattern_LightOn_E01

    def on_tick(self) -> state.State:
        if user_value(key='ResetFirstPiece', value=1):
            return Pattern09_Reset01()
        if user_value(key='LockFirstPiece', value=1):
            return Quit()


#  아홉 번째 패턴 오답 
class Pattern09_WrongAnswer(state.State):
    def on_enter(self):
        set_user_value(triggerId=4, key='CorrectFirstPiece', value=2) # 오답

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=2000):
            return Pattern09_Reset01()


class Pattern09_Reset01(state.State):
    def on_enter(self):
        set_user_value(key='CheckFirstPiece', value=0)
        set_user_value(key='CorrectFirstPiece', value=0)
        set_user_value(key='ResetFirstPiece', value=0)
        set_user_value(key='LockFirstPiece', value=0)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=1000):
            return Pattern09_Reset02()


#  아홉 번째 패턴 다시체크 
class Pattern09_Reset02(state.State):
    def on_enter(self):
        set_mesh(triggerIds=[3118], visible=False, arg3=100, arg4=0, arg5=5) # Pattern_LightOn_E01

    def on_tick(self) -> state.State:
        if user_value(key='CheckFirstPiece', value=1):
            return Pattern09_Check()


#  열 번째 패턴 뽑힘 
class Pattern10_Pick(state.State):
    def on_enter(self):
        set_mesh(triggerIds=[3109], visible=True, arg3=0, arg4=0, arg5=0) # Pattern_Ground_E02
        set_user_value(triggerId=6, key='PickSecondPieceExceptE02', value=1)

    def on_tick(self) -> state.State:
        if user_value(key='CheckFirstPiece', value=1):
            return Pattern10_Check()


#  열 번째 패턴 정답 체크 
class Pattern10_Check(state.State):
    def on_tick(self) -> state.State:
        if detect_liftable_object(boxIds=[2001], itemId=30000574):
            return Pattern10_CorrectAnswer()
        if not detect_liftable_object(boxIds=[2001], itemId=30000574):
            return Pattern10_WrongAnswer()


#  열 번째 패턴 정답 
class Pattern10_CorrectAnswer(state.State):
    def on_enter(self):
        set_user_value(triggerId=4, key='CorrectFirstPiece', value=1) # 정답
        set_mesh(triggerIds=[3119], visible=True, arg3=100, arg4=0, arg5=5) # Pattern_LightOn_E02

    def on_tick(self) -> state.State:
        if user_value(key='ResetFirstPiece', value=1):
            return Pattern10_Reset01()
        if user_value(key='LockFirstPiece', value=1):
            return Quit()


#  열 번째 패턴 오답 
class Pattern10_WrongAnswer(state.State):
    def on_enter(self):
        set_user_value(triggerId=4, key='CorrectFirstPiece', value=2) # 오답

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=2000):
            return Pattern10_Reset01()


class Pattern10_Reset01(state.State):
    def on_enter(self):
        set_user_value(key='CheckFirstPiece', value=0)
        set_user_value(key='CorrectFirstPiece', value=0)
        set_user_value(key='ResetFirstPiece', value=0)
        set_user_value(key='LockFirstPiece', value=0)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=1000):
            return Pattern10_Reset02()


#  열 번째 패턴 다시체크 
class Pattern10_Reset02(state.State):
    def on_enter(self):
        set_mesh(triggerIds=[3119], visible=False, arg3=100, arg4=0, arg5=5) # Pattern_LightOn_E02

    def on_tick(self) -> state.State:
        if user_value(key='CheckFirstPiece', value=1):
            return Pattern10_Check()


class Quit(state.State):
    pass


