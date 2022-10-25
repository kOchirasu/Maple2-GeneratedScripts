""" trigger/52000051_qd/06_puzzle_secondpiece.xml """
import common


class Wait(common.Trigger):
    def on_enter(self):
        self.set_user_value(key='PickSecondPieceExceptA01', value=0)
        self.set_user_value(key='PickSecondPieceExceptA02', value=0)
        self.set_user_value(key='PickSecondPieceExceptA03', value=0)
        self.set_user_value(key='PickSecondPieceExceptB01', value=0)
        self.set_user_value(key='PickSecondPieceExceptB02', value=0)
        self.set_user_value(key='PickSecondPieceExceptC01', value=0)
        self.set_user_value(key='PickSecondPieceExceptD01', value=0)
        self.set_user_value(key='PickSecondPieceExceptD02', value=0)
        self.set_user_value(key='PickSecondPieceExceptE01', value=0)
        self.set_user_value(key='PickSecondPieceExceptE02', value=0)
        self.set_user_value(key='CheckSecondPiece', value=0)
        self.set_user_value(key='CorrectSecondPiece', value=0)
        self.set_user_value(key='ResetSecondPiece', value=0)
        self.set_user_value(key='LockSecondPiece', value=0)
        self.set_mesh(triggerIds=[3200,3201,3202,3203,3204,3205,3206,3207,3208,3209], visible=False, arg3=0, delay=0, scale=0) # Pattern_Ground
        self.set_mesh(triggerIds=[3210,3211,3212,3213,3214,3215,3216,3217,3218,3219], visible=False, arg3=0, delay=0, scale=0) # Pattern_LightOn

    def on_tick(self) -> common.Trigger:
        if self.user_value(key='PickSecondPieceExceptA01', value=1):
            return RandomPick_ExceptA01(self.ctx)
        if self.user_value(key='PickSecondPieceExceptA02', value=1):
            return RandomPick_ExceptA02(self.ctx)
        if self.user_value(key='PickSecondPieceExceptA03', value=1):
            return RandomPick_ExceptA03(self.ctx)
        if self.user_value(key='PickSecondPieceExceptB01', value=1):
            return RandomPick_ExceptB01(self.ctx)
        if self.user_value(key='PickSecondPieceExceptB02', value=1):
            return RandomPick_ExceptB02(self.ctx)
        if self.user_value(key='PickSecondPieceExceptC01', value=1):
            return RandomPick_ExceptC01(self.ctx)
        if self.user_value(key='PickSecondPieceExceptD01', value=1):
            return RandomPick_ExceptD01(self.ctx)
        if self.user_value(key='PickSecondPieceExceptD02', value=1):
            return RandomPick_ExceptD02(self.ctx)
        if self.user_value(key='PickSecondPieceExceptE01', value=1):
            return RandomPick_ExceptE01(self.ctx)
        if self.user_value(key='PickSecondPieceExceptE02', value=1):
            return RandomPick_ExceptE02(self.ctx)


class RandomPick_ExceptA01(common.Trigger):
    def on_tick(self) -> common.Trigger:
        if self.random_condition(rate=10):
            return Pattern02_Pick(self.ctx)
        if self.random_condition(rate=10):
            return Pattern03_Pick(self.ctx)
        if self.random_condition(rate=10):
            return Pattern04_Pick(self.ctx)
        if self.random_condition(rate=10):
            return Pattern05_Pick(self.ctx)
        if self.random_condition(rate=10):
            return Pattern06_Pick(self.ctx)
        if self.random_condition(rate=10):
            return Pattern07_Pick(self.ctx)
        if self.random_condition(rate=10):
            return Pattern08_Pick(self.ctx)
        if self.random_condition(rate=10):
            return Pattern09_Pick(self.ctx)
        if self.random_condition(rate=10):
            return Pattern10_Pick(self.ctx)


class RandomPick_ExceptA02(common.Trigger):
    def on_tick(self) -> common.Trigger:
        if self.random_condition(rate=10):
            return Pattern01_Pick(self.ctx)
        if self.random_condition(rate=10):
            return Pattern03_Pick(self.ctx)
        if self.random_condition(rate=10):
            return Pattern04_Pick(self.ctx)
        if self.random_condition(rate=10):
            return Pattern05_Pick(self.ctx)
        if self.random_condition(rate=10):
            return Pattern06_Pick(self.ctx)
        if self.random_condition(rate=10):
            return Pattern07_Pick(self.ctx)
        if self.random_condition(rate=10):
            return Pattern08_Pick(self.ctx)
        if self.random_condition(rate=10):
            return Pattern09_Pick(self.ctx)
        if self.random_condition(rate=10):
            return Pattern10_Pick(self.ctx)


class RandomPick_ExceptA03(common.Trigger):
    def on_tick(self) -> common.Trigger:
        if self.random_condition(rate=10):
            return Pattern01_Pick(self.ctx)
        if self.random_condition(rate=10):
            return Pattern02_Pick(self.ctx)
        if self.random_condition(rate=10):
            return Pattern04_Pick(self.ctx)
        if self.random_condition(rate=10):
            return Pattern05_Pick(self.ctx)
        if self.random_condition(rate=10):
            return Pattern06_Pick(self.ctx)
        if self.random_condition(rate=10):
            return Pattern07_Pick(self.ctx)
        if self.random_condition(rate=10):
            return Pattern08_Pick(self.ctx)
        if self.random_condition(rate=10):
            return Pattern09_Pick(self.ctx)
        if self.random_condition(rate=10):
            return Pattern10_Pick(self.ctx)


class RandomPick_ExceptB01(common.Trigger):
    def on_tick(self) -> common.Trigger:
        if self.random_condition(rate=10):
            return Pattern01_Pick(self.ctx)
        if self.random_condition(rate=10):
            return Pattern02_Pick(self.ctx)
        if self.random_condition(rate=10):
            return Pattern03_Pick(self.ctx)
        if self.random_condition(rate=10):
            return Pattern05_Pick(self.ctx)
        if self.random_condition(rate=10):
            return Pattern06_Pick(self.ctx)
        if self.random_condition(rate=10):
            return Pattern07_Pick(self.ctx)
        if self.random_condition(rate=10):
            return Pattern08_Pick(self.ctx)
        if self.random_condition(rate=10):
            return Pattern09_Pick(self.ctx)
        if self.random_condition(rate=10):
            return Pattern10_Pick(self.ctx)


class RandomPick_ExceptB02(common.Trigger):
    def on_tick(self) -> common.Trigger:
        if self.random_condition(rate=10):
            return Pattern01_Pick(self.ctx)
        if self.random_condition(rate=10):
            return Pattern02_Pick(self.ctx)
        if self.random_condition(rate=10):
            return Pattern03_Pick(self.ctx)
        if self.random_condition(rate=10):
            return Pattern04_Pick(self.ctx)
        if self.random_condition(rate=10):
            return Pattern06_Pick(self.ctx)
        if self.random_condition(rate=10):
            return Pattern07_Pick(self.ctx)
        if self.random_condition(rate=10):
            return Pattern08_Pick(self.ctx)
        if self.random_condition(rate=10):
            return Pattern09_Pick(self.ctx)
        if self.random_condition(rate=10):
            return Pattern10_Pick(self.ctx)


class RandomPick_ExceptC01(common.Trigger):
    def on_tick(self) -> common.Trigger:
        if self.random_condition(rate=10):
            return Pattern01_Pick(self.ctx)
        if self.random_condition(rate=10):
            return Pattern02_Pick(self.ctx)
        if self.random_condition(rate=10):
            return Pattern03_Pick(self.ctx)
        if self.random_condition(rate=10):
            return Pattern04_Pick(self.ctx)
        if self.random_condition(rate=10):
            return Pattern05_Pick(self.ctx)
        if self.random_condition(rate=10):
            return Pattern07_Pick(self.ctx)
        if self.random_condition(rate=10):
            return Pattern08_Pick(self.ctx)
        if self.random_condition(rate=10):
            return Pattern09_Pick(self.ctx)
        if self.random_condition(rate=10):
            return Pattern10_Pick(self.ctx)


class RandomPick_ExceptD01(common.Trigger):
    def on_tick(self) -> common.Trigger:
        if self.random_condition(rate=10):
            return Pattern01_Pick(self.ctx)
        if self.random_condition(rate=10):
            return Pattern02_Pick(self.ctx)
        if self.random_condition(rate=10):
            return Pattern03_Pick(self.ctx)
        if self.random_condition(rate=10):
            return Pattern04_Pick(self.ctx)
        if self.random_condition(rate=10):
            return Pattern05_Pick(self.ctx)
        if self.random_condition(rate=10):
            return Pattern06_Pick(self.ctx)
        if self.random_condition(rate=10):
            return Pattern08_Pick(self.ctx)
        if self.random_condition(rate=10):
            return Pattern09_Pick(self.ctx)
        if self.random_condition(rate=10):
            return Pattern10_Pick(self.ctx)


class RandomPick_ExceptD02(common.Trigger):
    def on_tick(self) -> common.Trigger:
        if self.random_condition(rate=10):
            return Pattern01_Pick(self.ctx)
        if self.random_condition(rate=10):
            return Pattern02_Pick(self.ctx)
        if self.random_condition(rate=10):
            return Pattern03_Pick(self.ctx)
        if self.random_condition(rate=10):
            return Pattern04_Pick(self.ctx)
        if self.random_condition(rate=10):
            return Pattern05_Pick(self.ctx)
        if self.random_condition(rate=10):
            return Pattern06_Pick(self.ctx)
        if self.random_condition(rate=10):
            return Pattern07_Pick(self.ctx)
        if self.random_condition(rate=10):
            return Pattern09_Pick(self.ctx)
        if self.random_condition(rate=10):
            return Pattern10_Pick(self.ctx)


class RandomPick_ExceptE01(common.Trigger):
    def on_tick(self) -> common.Trigger:
        if self.random_condition(rate=10):
            return Pattern01_Pick(self.ctx)
        if self.random_condition(rate=10):
            return Pattern02_Pick(self.ctx)
        if self.random_condition(rate=10):
            return Pattern03_Pick(self.ctx)
        if self.random_condition(rate=10):
            return Pattern04_Pick(self.ctx)
        if self.random_condition(rate=10):
            return Pattern05_Pick(self.ctx)
        if self.random_condition(rate=10):
            return Pattern06_Pick(self.ctx)
        if self.random_condition(rate=10):
            return Pattern07_Pick(self.ctx)
        if self.random_condition(rate=10):
            return Pattern08_Pick(self.ctx)
        if self.random_condition(rate=10):
            return Pattern10_Pick(self.ctx)


class RandomPick_ExceptE02(common.Trigger):
    def on_tick(self) -> common.Trigger:
        if self.random_condition(rate=10):
            return Pattern01_Pick(self.ctx)
        if self.random_condition(rate=10):
            return Pattern02_Pick(self.ctx)
        if self.random_condition(rate=10):
            return Pattern03_Pick(self.ctx)
        if self.random_condition(rate=10):
            return Pattern04_Pick(self.ctx)
        if self.random_condition(rate=10):
            return Pattern05_Pick(self.ctx)
        if self.random_condition(rate=10):
            return Pattern06_Pick(self.ctx)
        if self.random_condition(rate=10):
            return Pattern07_Pick(self.ctx)
        if self.random_condition(rate=10):
            return Pattern08_Pick(self.ctx)
        if self.random_condition(rate=10):
            return Pattern09_Pick(self.ctx)


# 첫 번째 패턴 뽑힘
class Pattern01_Pick(common.Trigger):
    def on_enter(self):
        self.set_mesh(triggerIds=[3200], visible=True, arg3=0, delay=0, scale=0) # Pattern_Ground_A01

    def on_tick(self) -> common.Trigger:
        if self.user_value(key='CheckSecondPiece', value=1):
            return Pattern01_Check(self.ctx)


# 첫 번째 패턴 정답 체크
class Pattern01_Check(common.Trigger):
    def on_tick(self) -> common.Trigger:
        if self.detect_liftable_object(boxIds=[2002], itemId=30000565):
            return Pattern01_CorrectAnswer(self.ctx)
        if not self.detect_liftable_object(boxIds=[2002], itemId=30000565):
            return Pattern01_WrongAnswer(self.ctx)


# 첫 번째 패턴 정답
class Pattern01_CorrectAnswer(common.Trigger):
    def on_enter(self):
        self.set_user_value(triggerId=4, key='CorrectSecondPiece', value=1) # 정답
        self.set_mesh(triggerIds=[3210], visible=True, arg3=100, delay=0, scale=5) # Pattern_LightOn_A01

    def on_tick(self) -> common.Trigger:
        if self.user_value(key='ResetSecondPiece', value=1):
            return Pattern01_Reset01(self.ctx)
        if self.user_value(key='LockSecondPiece', value=1):
            return Quit(self.ctx)


# 첫 번째 패턴 오답
class Pattern01_WrongAnswer(common.Trigger):
    def on_enter(self):
        self.set_user_value(triggerId=4, key='CorrectSecondPiece', value=2) # 오답

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=2000):
            return Pattern01_Reset01(self.ctx)


class Pattern01_Reset01(common.Trigger):
    def on_enter(self):
        self.set_user_value(key='CheckSecondPiece', value=0)
        self.set_user_value(key='CorrectSecondPiece', value=0)
        self.set_user_value(key='ResetSecondPiece', value=0)
        self.set_user_value(key='LockSecondPiece', value=0)

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=1000):
            return Pattern01_Reset02(self.ctx)


# 첫 번째 패턴 다시체크
class Pattern01_Reset02(common.Trigger):
    def on_enter(self):
        self.set_mesh(triggerIds=[3210], visible=False, arg3=100, delay=0, scale=5) # Pattern_LightOn_A01

    def on_tick(self) -> common.Trigger:
        if self.user_value(key='CheckSecondPiece', value=1):
            return Pattern01_Check(self.ctx)


# 두 번째 패턴 뽑힘
class Pattern02_Pick(common.Trigger):
    def on_enter(self):
        self.set_mesh(triggerIds=[3201], visible=True, arg3=0, delay=0, scale=0) # Pattern_Ground_A02

    def on_tick(self) -> common.Trigger:
        if self.user_value(key='CheckSecondPiece', value=1):
            return Pattern02_Check(self.ctx)


# 두 번째 패턴 정답 체크
class Pattern02_Check(common.Trigger):
    def on_tick(self) -> common.Trigger:
        if self.detect_liftable_object(boxIds=[2002], itemId=30000566):
            return Pattern02_CorrectAnswer(self.ctx)
        if not self.detect_liftable_object(boxIds=[2002], itemId=30000566):
            return Pattern02_WrongAnswer(self.ctx)


# 두 번째 패턴 정답
class Pattern02_CorrectAnswer(common.Trigger):
    def on_enter(self):
        self.set_user_value(triggerId=4, key='CorrectSecondPiece', value=1) # 정답
        self.set_mesh(triggerIds=[3211], visible=True, arg3=100, delay=0, scale=5) # Pattern_LightOn_A02

    def on_tick(self) -> common.Trigger:
        if self.user_value(key='ResetSecondPiece', value=1):
            return Pattern02_Reset01(self.ctx)
        if self.user_value(key='LockSecondPiece', value=1):
            return Quit(self.ctx)


# 두 번째 패턴 오답
class Pattern02_WrongAnswer(common.Trigger):
    def on_enter(self):
        self.set_user_value(triggerId=4, key='CorrectSecondPiece', value=2) # 오답

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=2000):
            return Pattern02_Reset01(self.ctx)


class Pattern02_Reset01(common.Trigger):
    def on_enter(self):
        self.set_user_value(key='CheckSecondPiece', value=0)
        self.set_user_value(key='CorrectSecondPiece', value=0)
        self.set_user_value(key='ResetSecondPiece', value=0)
        self.set_user_value(key='LockSecondPiece', value=0)

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=1000):
            return Pattern02_Reset02(self.ctx)


# 두 번째 패턴 다시체크
class Pattern02_Reset02(common.Trigger):
    def on_enter(self):
        self.set_mesh(triggerIds=[3211], visible=False, arg3=100, delay=0, scale=5) # Pattern_LightOn_A02

    def on_tick(self) -> common.Trigger:
        if self.user_value(key='CheckSecondPiece', value=1):
            return Pattern02_Check(self.ctx)


# 세 번째 패턴 뽑힘
class Pattern03_Pick(common.Trigger):
    def on_enter(self):
        self.set_mesh(triggerIds=[3202], visible=True, arg3=0, delay=0, scale=0) # Pattern_Ground_A03

    def on_tick(self) -> common.Trigger:
        if self.user_value(key='CheckSecondPiece', value=1):
            return Pattern03_Check(self.ctx)


# 세 번째 패턴 정답 체크
class Pattern03_Check(common.Trigger):
    def on_tick(self) -> common.Trigger:
        if self.detect_liftable_object(boxIds=[2002], itemId=30000567):
            return Pattern03_CorrectAnswer(self.ctx)
        if not self.detect_liftable_object(boxIds=[2002], itemId=30000567):
            return Pattern03_WrongAnswer(self.ctx)


# 세 번째 패턴 정답
class Pattern03_CorrectAnswer(common.Trigger):
    def on_enter(self):
        self.set_user_value(triggerId=4, key='CorrectSecondPiece', value=1) # 정답
        self.set_mesh(triggerIds=[3212], visible=True, arg3=100, delay=0, scale=5) # Pattern_LightOn_A03

    def on_tick(self) -> common.Trigger:
        if self.user_value(key='ResetSecondPiece', value=1):
            return Pattern03_Reset01(self.ctx)
        if self.user_value(key='LockSecondPiece', value=1):
            return Quit(self.ctx)


# 세 번째 패턴 오답
class Pattern03_WrongAnswer(common.Trigger):
    def on_enter(self):
        self.set_user_value(triggerId=4, key='CorrectSecondPiece', value=2) # 오답

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=2000):
            return Pattern03_Reset01(self.ctx)


class Pattern03_Reset01(common.Trigger):
    def on_enter(self):
        self.set_user_value(key='CheckSecondPiece', value=0)
        self.set_user_value(key='CorrectSecondPiece', value=0)
        self.set_user_value(key='ResetSecondPiece', value=0)
        self.set_user_value(key='LockSecondPiece', value=0)

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=1000):
            return Pattern03_Reset02(self.ctx)


# 세 번째 패턴 다시체크
class Pattern03_Reset02(common.Trigger):
    def on_enter(self):
        self.set_mesh(triggerIds=[3212], visible=False, arg3=100, delay=0, scale=5) # Pattern_LightOn_A03

    def on_tick(self) -> common.Trigger:
        if self.user_value(key='CheckSecondPiece', value=1):
            return Pattern03_Check(self.ctx)


# 네 번째 패턴 뽑힘
class Pattern04_Pick(common.Trigger):
    def on_enter(self):
        self.set_mesh(triggerIds=[3203], visible=True, arg3=0, delay=0, scale=0) # Pattern_Ground_B01

    def on_tick(self) -> common.Trigger:
        if self.user_value(key='CheckSecondPiece', value=1):
            return Pattern04_Check(self.ctx)


# 네 번째 패턴 정답 체크
class Pattern04_Check(common.Trigger):
    def on_tick(self) -> common.Trigger:
        if self.detect_liftable_object(boxIds=[2002], itemId=30000568):
            return Pattern04_CorrectAnswer(self.ctx)
        if not self.detect_liftable_object(boxIds=[2002], itemId=30000568):
            return Pattern04_WrongAnswer(self.ctx)


# 네 번째 패턴 정답
class Pattern04_CorrectAnswer(common.Trigger):
    def on_enter(self):
        self.set_user_value(triggerId=4, key='CorrectSecondPiece', value=1) # 정답
        self.set_mesh(triggerIds=[3213], visible=True, arg3=100, delay=0, scale=5) # Pattern_LightOn_B01

    def on_tick(self) -> common.Trigger:
        if self.user_value(key='ResetSecondPiece', value=1):
            return Pattern04_Reset01(self.ctx)
        if self.user_value(key='LockSecondPiece', value=1):
            return Quit(self.ctx)


# 네 번째 패턴 오답
class Pattern04_WrongAnswer(common.Trigger):
    def on_enter(self):
        self.set_user_value(triggerId=4, key='CorrectSecondPiece', value=2) # 오답

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=2000):
            return Pattern04_Reset01(self.ctx)


class Pattern04_Reset01(common.Trigger):
    def on_enter(self):
        self.set_user_value(key='CheckSecondPiece', value=0)
        self.set_user_value(key='CorrectSecondPiece', value=0)
        self.set_user_value(key='ResetSecondPiece', value=0)
        self.set_user_value(key='LockSecondPiece', value=0)

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=1000):
            return Pattern04_Reset02(self.ctx)


# 네 번째 패턴 다시체크
class Pattern04_Reset02(common.Trigger):
    def on_enter(self):
        self.set_mesh(triggerIds=[3213], visible=False, arg3=100, delay=0, scale=5) # Pattern_LightOn_B01

    def on_tick(self) -> common.Trigger:
        if self.user_value(key='CheckSecondPiece', value=1):
            return Pattern04_Check(self.ctx)


# 다섯 번째 패턴 뽑힘
class Pattern05_Pick(common.Trigger):
    def on_enter(self):
        self.set_mesh(triggerIds=[3204], visible=True, arg3=0, delay=0, scale=0) # Pattern_Ground_B02

    def on_tick(self) -> common.Trigger:
        if self.user_value(key='CheckSecondPiece', value=1):
            return Pattern05_Check(self.ctx)


# 다섯 번째 패턴 정답 체크
class Pattern05_Check(common.Trigger):
    def on_tick(self) -> common.Trigger:
        if self.detect_liftable_object(boxIds=[2002], itemId=30000569):
            return Pattern05_CorrectAnswer(self.ctx)
        if not self.detect_liftable_object(boxIds=[2002], itemId=30000569):
            return Pattern05_WrongAnswer(self.ctx)


# 다섯 번째 패턴 정답
class Pattern05_CorrectAnswer(common.Trigger):
    def on_enter(self):
        self.set_user_value(triggerId=4, key='CorrectSecondPiece', value=1) # 정답
        self.set_mesh(triggerIds=[3214], visible=True, arg3=100, delay=0, scale=5) # Pattern_LightOn_B02

    def on_tick(self) -> common.Trigger:
        if self.user_value(key='ResetSecondPiece', value=1):
            return Pattern05_Reset01(self.ctx)
        if self.user_value(key='LockSecondPiece', value=1):
            return Quit(self.ctx)


# 다섯 번째 패턴 오답
class Pattern05_WrongAnswer(common.Trigger):
    def on_enter(self):
        self.set_user_value(triggerId=4, key='CorrectSecondPiece', value=2) # 오답

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=2000):
            return Pattern05_Reset01(self.ctx)


class Pattern05_Reset01(common.Trigger):
    def on_enter(self):
        self.set_user_value(key='CheckSecondPiece', value=0)
        self.set_user_value(key='CorrectSecondPiece', value=0)
        self.set_user_value(key='ResetSecondPiece', value=0)
        self.set_user_value(key='LockSecondPiece', value=0)

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=1000):
            return Pattern05_Reset02(self.ctx)


# 다섯 번째 패턴 다시체크
class Pattern05_Reset02(common.Trigger):
    def on_enter(self):
        self.set_mesh(triggerIds=[3214], visible=False, arg3=100, delay=0, scale=5) # Pattern_LightOn_B02

    def on_tick(self) -> common.Trigger:
        if self.user_value(key='CheckSecondPiece', value=1):
            return Pattern05_Check(self.ctx)


# 여섯 번째 패턴 뽑힘
class Pattern06_Pick(common.Trigger):
    def on_enter(self):
        self.set_mesh(triggerIds=[3205], visible=True, arg3=0, delay=0, scale=0) # Pattern_Ground_C01

    def on_tick(self) -> common.Trigger:
        if self.user_value(key='CheckSecondPiece', value=1):
            return Pattern06_Check(self.ctx)


# 여섯 번째 패턴 정답 체크
class Pattern06_Check(common.Trigger):
    def on_tick(self) -> common.Trigger:
        if self.detect_liftable_object(boxIds=[2002], itemId=30000570):
            return Pattern06_CorrectAnswer(self.ctx)
        if not self.detect_liftable_object(boxIds=[2002], itemId=30000570):
            return Pattern06_WrongAnswer(self.ctx)


# 여섯 번째 패턴 정답
class Pattern06_CorrectAnswer(common.Trigger):
    def on_enter(self):
        self.set_user_value(triggerId=4, key='CorrectSecondPiece', value=1) # 정답
        self.set_mesh(triggerIds=[3215], visible=True, arg3=100, delay=0, scale=5) # Pattern_LightOn_C01

    def on_tick(self) -> common.Trigger:
        if self.user_value(key='ResetSecondPiece', value=1):
            return Pattern06_Reset01(self.ctx)
        if self.user_value(key='LockSecondPiece', value=1):
            return Quit(self.ctx)


# 여섯 번째 패턴 오답
class Pattern06_WrongAnswer(common.Trigger):
    def on_enter(self):
        self.set_user_value(triggerId=4, key='CorrectSecondPiece', value=2) # 오답

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=2000):
            return Pattern06_Reset01(self.ctx)


class Pattern06_Reset01(common.Trigger):
    def on_enter(self):
        self.set_user_value(key='CheckSecondPiece', value=0)
        self.set_user_value(key='CorrectSecondPiece', value=0)
        self.set_user_value(key='ResetSecondPiece', value=0)
        self.set_user_value(key='LockSecondPiece', value=0)

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=1000):
            return Pattern06_Reset02(self.ctx)


# 여섯 번째 패턴 다시체크
class Pattern06_Reset02(common.Trigger):
    def on_enter(self):
        self.set_mesh(triggerIds=[3215], visible=False, arg3=100, delay=0, scale=5) # Pattern_LightOn_C01

    def on_tick(self) -> common.Trigger:
        if self.user_value(key='CheckSecondPiece', value=1):
            return Pattern06_Check(self.ctx)


# 일곱 번째 패턴 뽑힘
class Pattern07_Pick(common.Trigger):
    def on_enter(self):
        self.set_mesh(triggerIds=[3206], visible=True, arg3=0, delay=0, scale=0) # Pattern_Ground_D01

    def on_tick(self) -> common.Trigger:
        if self.user_value(key='CheckSecondPiece', value=1):
            return Pattern07_Check(self.ctx)


# 일곱 번째 패턴 정답 체크
class Pattern07_Check(common.Trigger):
    def on_tick(self) -> common.Trigger:
        if self.detect_liftable_object(boxIds=[2002], itemId=30000571):
            return Pattern07_CorrectAnswer(self.ctx)
        if not self.detect_liftable_object(boxIds=[2002], itemId=30000571):
            return Pattern07_WrongAnswer(self.ctx)


# 일곱 번째 패턴 정답
class Pattern07_CorrectAnswer(common.Trigger):
    def on_enter(self):
        self.set_user_value(triggerId=4, key='CorrectSecondPiece', value=1) # 정답
        self.set_mesh(triggerIds=[3216], visible=True, arg3=100, delay=0, scale=5) # Pattern_LightOn_D01

    def on_tick(self) -> common.Trigger:
        if self.user_value(key='ResetSecondPiece', value=1):
            return Pattern07_Reset01(self.ctx)
        if self.user_value(key='LockSecondPiece', value=1):
            return Quit(self.ctx)


# 일곱 번째 패턴 오답
class Pattern07_WrongAnswer(common.Trigger):
    def on_enter(self):
        self.set_user_value(triggerId=4, key='CorrectSecondPiece', value=2) # 오답

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=2000):
            return Pattern07_Reset01(self.ctx)


class Pattern07_Reset01(common.Trigger):
    def on_enter(self):
        self.set_user_value(key='CheckSecondPiece', value=0)
        self.set_user_value(key='CorrectSecondPiece', value=0)
        self.set_user_value(key='ResetSecondPiece', value=0)
        self.set_user_value(key='LockSecondPiece', value=0)

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=1000):
            return Pattern07_Reset02(self.ctx)


# 일곱 번째 패턴 다시체크
class Pattern07_Reset02(common.Trigger):
    def on_enter(self):
        self.set_mesh(triggerIds=[3216], visible=False, arg3=100, delay=0, scale=5) # Pattern_LightOn_D01

    def on_tick(self) -> common.Trigger:
        if self.user_value(key='CheckSecondPiece', value=1):
            return Pattern07_Check(self.ctx)


# 여덟 번째 패턴 뽑힘
class Pattern08_Pick(common.Trigger):
    def on_enter(self):
        self.set_mesh(triggerIds=[3207], visible=True, arg3=0, delay=0, scale=0) # Pattern_Ground_D02

    def on_tick(self) -> common.Trigger:
        if self.user_value(key='CheckSecondPiece', value=1):
            return Pattern08_Check(self.ctx)


# 여덟 번째 패턴 정답 체크
class Pattern08_Check(common.Trigger):
    def on_tick(self) -> common.Trigger:
        if self.detect_liftable_object(boxIds=[2002], itemId=30000572):
            return Pattern08_CorrectAnswer(self.ctx)
        if not self.detect_liftable_object(boxIds=[2002], itemId=30000572):
            return Pattern08_WrongAnswer(self.ctx)


# 여덟 번째 패턴 정답
class Pattern08_CorrectAnswer(common.Trigger):
    def on_enter(self):
        self.set_user_value(triggerId=4, key='CorrectSecondPiece', value=1) # 정답
        self.set_mesh(triggerIds=[3217], visible=True, arg3=100, delay=0, scale=5) # Pattern_LightOn_D02

    def on_tick(self) -> common.Trigger:
        if self.user_value(key='ResetSecondPiece', value=1):
            return Pattern08_Reset01(self.ctx)
        if self.user_value(key='LockSecondPiece', value=1):
            return Quit(self.ctx)


# 여덟 번째 패턴 오답
class Pattern08_WrongAnswer(common.Trigger):
    def on_enter(self):
        self.set_user_value(triggerId=4, key='CorrectSecondPiece', value=2) # 오답

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=2000):
            return Pattern08_Reset01(self.ctx)


class Pattern08_Reset01(common.Trigger):
    def on_enter(self):
        self.set_user_value(key='CheckSecondPiece', value=0)
        self.set_user_value(key='CorrectSecondPiece', value=0)
        self.set_user_value(key='ResetSecondPiece', value=0)
        self.set_user_value(key='LockSecondPiece', value=0)

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=1000):
            return Pattern08_Reset02(self.ctx)


# 여덟 번째 패턴 다시체크
class Pattern08_Reset02(common.Trigger):
    def on_enter(self):
        self.set_mesh(triggerIds=[3217], visible=False, arg3=100, delay=0, scale=5) # Pattern_LightOn_D02

    def on_tick(self) -> common.Trigger:
        if self.user_value(key='CheckSecondPiece', value=1):
            return Pattern08_Check(self.ctx)


# 아홉 번째 패턴 뽑힘
class Pattern09_Pick(common.Trigger):
    def on_enter(self):
        self.set_mesh(triggerIds=[3208], visible=True, arg3=0, delay=0, scale=0) # Pattern_Ground_E01

    def on_tick(self) -> common.Trigger:
        if self.user_value(key='CheckSecondPiece', value=1):
            return Pattern09_Check(self.ctx)


# 아홉 번째 패턴 정답 체크
class Pattern09_Check(common.Trigger):
    def on_tick(self) -> common.Trigger:
        if self.detect_liftable_object(boxIds=[2002], itemId=30000573):
            return Pattern09_CorrectAnswer(self.ctx)
        if not self.detect_liftable_object(boxIds=[2002], itemId=30000573):
            return Pattern09_WrongAnswer(self.ctx)


# 아홉 번째 패턴 정답
class Pattern09_CorrectAnswer(common.Trigger):
    def on_enter(self):
        self.set_user_value(triggerId=4, key='CorrectSecondPiece', value=1) # 정답
        self.set_mesh(triggerIds=[3218], visible=True, arg3=100, delay=0, scale=5) # Pattern_LightOn_E01

    def on_tick(self) -> common.Trigger:
        if self.user_value(key='ResetSecondPiece', value=1):
            return Pattern09_Reset01(self.ctx)
        if self.user_value(key='LockSecondPiece', value=1):
            return Quit(self.ctx)


# 아홉 번째 패턴 오답
class Pattern09_WrongAnswer(common.Trigger):
    def on_enter(self):
        self.set_user_value(triggerId=4, key='CorrectSecondPiece', value=2) # 오답

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=2000):
            return Pattern09_Reset01(self.ctx)


class Pattern09_Reset01(common.Trigger):
    def on_enter(self):
        self.set_user_value(key='CheckSecondPiece', value=0)
        self.set_user_value(key='CorrectSecondPiece', value=0)
        self.set_user_value(key='ResetSecondPiece', value=0)
        self.set_user_value(key='LockSecondPiece', value=0)

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=1000):
            return Pattern09_Reset02(self.ctx)


# 아홉 번째 패턴 다시체크
class Pattern09_Reset02(common.Trigger):
    def on_enter(self):
        self.set_mesh(triggerIds=[3218], visible=False, arg3=100, delay=0, scale=5) # Pattern_LightOn_E01

    def on_tick(self) -> common.Trigger:
        if self.user_value(key='CheckSecondPiece', value=1):
            return Pattern09_Check(self.ctx)


# 열 번째 패턴 뽑힘
class Pattern10_Pick(common.Trigger):
    def on_enter(self):
        self.set_mesh(triggerIds=[3209], visible=True, arg3=0, delay=0, scale=0) # Pattern_Ground_E02

    def on_tick(self) -> common.Trigger:
        if self.user_value(key='CheckSecondPiece', value=1):
            return Pattern10_Check(self.ctx)


# 열 번째 패턴 정답 체크
class Pattern10_Check(common.Trigger):
    def on_tick(self) -> common.Trigger:
        if self.detect_liftable_object(boxIds=[2002], itemId=30000574):
            return Pattern10_CorrectAnswer(self.ctx)
        if not self.detect_liftable_object(boxIds=[2002], itemId=30000574):
            return Pattern10_WrongAnswer(self.ctx)


# 열 번째 패턴 정답
class Pattern10_CorrectAnswer(common.Trigger):
    def on_enter(self):
        self.set_user_value(triggerId=4, key='CorrectSecondPiece', value=1) # 정답
        self.set_mesh(triggerIds=[3219], visible=True, arg3=100, delay=0, scale=5) # Pattern_LightOn_E02

    def on_tick(self) -> common.Trigger:
        if self.user_value(key='ResetSecondPiece', value=1):
            return Pattern10_Reset01(self.ctx)
        if self.user_value(key='LockSecondPiece', value=1):
            return Quit(self.ctx)


# 열 번째 패턴 오답
class Pattern10_WrongAnswer(common.Trigger):
    def on_enter(self):
        self.set_user_value(triggerId=4, key='CorrectSecondPiece', value=2) # 오답

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=2000):
            return Pattern10_Reset01(self.ctx)


class Pattern10_Reset01(common.Trigger):
    def on_enter(self):
        self.set_user_value(key='CheckSecondPiece', value=0)
        self.set_user_value(key='CorrectSecondPiece', value=0)
        self.set_user_value(key='ResetSecondPiece', value=0)
        self.set_user_value(key='LockSecondPiece', value=0)

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=1000):
            return Pattern10_Reset02(self.ctx)


# 열 번째 패턴 다시체크
class Pattern10_Reset02(common.Trigger):
    def on_enter(self):
        self.set_mesh(triggerIds=[3219], visible=False, arg3=100, delay=0, scale=5) # Pattern_LightOn_E02

    def on_tick(self) -> common.Trigger:
        if self.user_value(key='CheckSecondPiece', value=1):
            return Pattern10_Check(self.ctx)


class Quit(common.Trigger):
    pass


initial_state = Wait
