""" trigger/52000051_qd/05_puzzle_firstpiece.xml """
import common


class Wait(common.Trigger):
    def on_enter(self):
        self.set_user_value(key='PickFirstPiece', value=0)
        self.set_user_value(key='CheckFirstPiece', value=0)
        self.set_user_value(key='CorrectFirstPiece', value=0)
        self.set_user_value(key='ResetFirstPiece', value=0)
        self.set_user_value(key='LockFirstPiece', value=0)
        self.set_mesh(triggerIds=[3100,3101,3102,3103,3104,3105,3106,3107,3108,3109], visible=False, arg3=0, delay=0, scale=0) # Pattern_Ground
        self.set_mesh(triggerIds=[3110,3111,3112,3113,3114,3115,3116,3117,3118,3119], visible=False, arg3=0, delay=0, scale=0) # Pattern_LightOn

    def on_tick(self) -> common.Trigger:
        if self.user_value(key='PickFirstPiece', value=1):
            return RandomPick(self.ctx)


class RandomPick(common.Trigger):
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
        if self.random_condition(rate=10):
            return Pattern10_Pick(self.ctx)


# 첫 번째 패턴 뽑힘
class Pattern01_Pick(common.Trigger):
    def on_enter(self):
        self.set_mesh(triggerIds=[3100], visible=True, arg3=0, delay=0, scale=0) # Pattern_Ground_A01
        self.set_user_value(triggerId=6, key='PickSecondPieceExceptA01', value=1)

    def on_tick(self) -> common.Trigger:
        if self.user_value(key='CheckFirstPiece', value=1):
            return Pattern01_Check(self.ctx)


# 첫 번째 패턴 정답 체크
class Pattern01_Check(common.Trigger):
    def on_tick(self) -> common.Trigger:
        if self.detect_liftable_object(boxIds=[2001], itemId=30000565):
            return Pattern01_CorrectAnswer(self.ctx)
        if not self.detect_liftable_object(boxIds=[2001], itemId=30000565):
            return Pattern01_WrongAnswer(self.ctx)


# 첫 번째 패턴 정답
class Pattern01_CorrectAnswer(common.Trigger):
    def on_enter(self):
        self.set_user_value(triggerId=4, key='CorrectFirstPiece', value=1) # 정답
        self.set_mesh(triggerIds=[3110], visible=True, arg3=100, delay=0, scale=5) # Pattern_LightOn_A01

    def on_tick(self) -> common.Trigger:
        if self.user_value(key='ResetFirstPiece', value=1):
            return Pattern01_Reset01(self.ctx)
        if self.user_value(key='LockFirstPiece', value=1):
            return Quit(self.ctx)


# 첫 번째 패턴 오답
class Pattern01_WrongAnswer(common.Trigger):
    def on_enter(self):
        self.set_user_value(triggerId=4, key='CorrectFirstPiece', value=2) # 오답

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=2000):
            return Pattern01_Reset01(self.ctx)


class Pattern01_Reset01(common.Trigger):
    def on_enter(self):
        self.set_user_value(key='CheckFirstPiece', value=0)
        self.set_user_value(key='CorrectFirstPiece', value=0)
        self.set_user_value(key='ResetFirstPiece', value=0)
        self.set_user_value(key='LockFirstPiece', value=0)

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=1000):
            return Pattern01_Reset02(self.ctx)


# 첫 번째 패턴 다시체크
class Pattern01_Reset02(common.Trigger):
    def on_enter(self):
        self.set_mesh(triggerIds=[3110], visible=False, arg3=100, delay=0, scale=5) # Pattern_LightOn_A01

    def on_tick(self) -> common.Trigger:
        if self.user_value(key='CheckFirstPiece', value=1):
            return Pattern01_Check(self.ctx)


# 두 번째 패턴 뽑힘
class Pattern02_Pick(common.Trigger):
    def on_enter(self):
        self.set_mesh(triggerIds=[3101], visible=True, arg3=0, delay=0, scale=0) # Pattern_Ground_A02
        self.set_user_value(triggerId=6, key='PickSecondPieceExceptA02', value=1)

    def on_tick(self) -> common.Trigger:
        if self.user_value(key='CheckFirstPiece', value=1):
            return Pattern02_Check(self.ctx)


# 두 번째 패턴 정답 체크
class Pattern02_Check(common.Trigger):
    def on_tick(self) -> common.Trigger:
        if self.detect_liftable_object(boxIds=[2001], itemId=30000566):
            return Pattern02_CorrectAnswer(self.ctx)
        if not self.detect_liftable_object(boxIds=[2001], itemId=30000566):
            return Pattern02_WrongAnswer(self.ctx)


# 두 번째 패턴 정답
class Pattern02_CorrectAnswer(common.Trigger):
    def on_enter(self):
        self.set_user_value(triggerId=4, key='CorrectFirstPiece', value=1) # 정답
        self.set_mesh(triggerIds=[3111], visible=True, arg3=100, delay=0, scale=5) # Pattern_LightOn_A02

    def on_tick(self) -> common.Trigger:
        if self.user_value(key='ResetFirstPiece', value=1):
            return Pattern02_Reset01(self.ctx)
        if self.user_value(key='LockFirstPiece', value=1):
            return Quit(self.ctx)


# 두 번째 패턴 오답
class Pattern02_WrongAnswer(common.Trigger):
    def on_enter(self):
        self.set_user_value(triggerId=4, key='CorrectFirstPiece', value=2) # 오답

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=2000):
            return Pattern02_Reset01(self.ctx)


class Pattern02_Reset01(common.Trigger):
    def on_enter(self):
        self.set_user_value(key='CheckFirstPiece', value=0)
        self.set_user_value(key='CorrectFirstPiece', value=0)
        self.set_user_value(key='ResetFirstPiece', value=0)
        self.set_user_value(key='LockFirstPiece', value=0)

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=1000):
            return Pattern02_Reset02(self.ctx)


# 두 번째 패턴 다시체크
class Pattern02_Reset02(common.Trigger):
    def on_enter(self):
        self.set_mesh(triggerIds=[3111], visible=False, arg3=100, delay=0, scale=5) # Pattern_LightOn_A02

    def on_tick(self) -> common.Trigger:
        if self.user_value(key='CheckFirstPiece', value=1):
            return Pattern02_Check(self.ctx)


# 세 번째 패턴 뽑힘
class Pattern03_Pick(common.Trigger):
    def on_enter(self):
        self.set_mesh(triggerIds=[3102], visible=True, arg3=0, delay=0, scale=0) # Pattern_Ground_A03
        self.set_user_value(triggerId=6, key='PickSecondPieceExceptA03', value=1)

    def on_tick(self) -> common.Trigger:
        if self.user_value(key='CheckFirstPiece', value=1):
            return Pattern03_Check(self.ctx)


# 세 번째 패턴 정답 체크
class Pattern03_Check(common.Trigger):
    def on_tick(self) -> common.Trigger:
        if self.detect_liftable_object(boxIds=[2001], itemId=30000567):
            return Pattern03_CorrectAnswer(self.ctx)
        if not self.detect_liftable_object(boxIds=[2001], itemId=30000567):
            return Pattern03_WrongAnswer(self.ctx)


# 세 번째 패턴 정답
class Pattern03_CorrectAnswer(common.Trigger):
    def on_enter(self):
        self.set_user_value(triggerId=4, key='CorrectFirstPiece', value=1) # 정답
        self.set_mesh(triggerIds=[3112], visible=True, arg3=100, delay=0, scale=5) # Pattern_LightOn_A03

    def on_tick(self) -> common.Trigger:
        if self.user_value(key='ResetFirstPiece', value=1):
            return Pattern03_Reset01(self.ctx)
        if self.user_value(key='LockFirstPiece', value=1):
            return Quit(self.ctx)


# 세 번째 패턴 오답
class Pattern03_WrongAnswer(common.Trigger):
    def on_enter(self):
        self.set_user_value(triggerId=4, key='CorrectFirstPiece', value=2) # 오답

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=2000):
            return Pattern03_Reset01(self.ctx)


class Pattern03_Reset01(common.Trigger):
    def on_enter(self):
        self.set_user_value(key='CheckFirstPiece', value=0)
        self.set_user_value(key='CorrectFirstPiece', value=0)
        self.set_user_value(key='ResetFirstPiece', value=0)
        self.set_user_value(key='LockFirstPiece', value=0)

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=1000):
            return Pattern03_Reset02(self.ctx)


# 세 번째 패턴 다시체크
class Pattern03_Reset02(common.Trigger):
    def on_enter(self):
        self.set_mesh(triggerIds=[3112], visible=False, arg3=100, delay=0, scale=5) # Pattern_LightOn_A03

    def on_tick(self) -> common.Trigger:
        if self.user_value(key='CheckFirstPiece', value=1):
            return Pattern03_Check(self.ctx)


# 네 번째 패턴 뽑힘
class Pattern04_Pick(common.Trigger):
    def on_enter(self):
        self.set_mesh(triggerIds=[3103], visible=True, arg3=0, delay=0, scale=0) # Pattern_Ground_B01
        self.set_user_value(triggerId=6, key='PickSecondPieceExceptB01', value=1)

    def on_tick(self) -> common.Trigger:
        if self.user_value(key='CheckFirstPiece', value=1):
            return Pattern04_Check(self.ctx)


# 네 번째 패턴 정답 체크
class Pattern04_Check(common.Trigger):
    def on_tick(self) -> common.Trigger:
        if self.detect_liftable_object(boxIds=[2001], itemId=30000568):
            return Pattern04_CorrectAnswer(self.ctx)
        if not self.detect_liftable_object(boxIds=[2001], itemId=30000568):
            return Pattern04_WrongAnswer(self.ctx)


# 네 번째 패턴 정답
class Pattern04_CorrectAnswer(common.Trigger):
    def on_enter(self):
        self.set_user_value(triggerId=4, key='CorrectFirstPiece', value=1) # 정답
        self.set_mesh(triggerIds=[3113], visible=True, arg3=100, delay=0, scale=5) # Pattern_LightOn_B01

    def on_tick(self) -> common.Trigger:
        if self.user_value(key='ResetFirstPiece', value=1):
            return Pattern04_Reset01(self.ctx)
        if self.user_value(key='LockFirstPiece', value=1):
            return Quit(self.ctx)


# 네 번째 패턴 오답
class Pattern04_WrongAnswer(common.Trigger):
    def on_enter(self):
        self.set_user_value(triggerId=4, key='CorrectFirstPiece', value=2) # 오답

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=2000):
            return Pattern04_Reset01(self.ctx)


class Pattern04_Reset01(common.Trigger):
    def on_enter(self):
        self.set_user_value(key='CheckFirstPiece', value=0)
        self.set_user_value(key='CorrectFirstPiece', value=0)
        self.set_user_value(key='ResetFirstPiece', value=0)
        self.set_user_value(key='LockFirstPiece', value=0)

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=1000):
            return Pattern04_Reset02(self.ctx)


# 네 번째 패턴 다시체크
class Pattern04_Reset02(common.Trigger):
    def on_enter(self):
        self.set_mesh(triggerIds=[3113], visible=False, arg3=100, delay=0, scale=5) # Pattern_LightOn_B01

    def on_tick(self) -> common.Trigger:
        if self.user_value(key='CheckFirstPiece', value=1):
            return Pattern04_Check(self.ctx)


# 다섯 번째 패턴 뽑힘
class Pattern05_Pick(common.Trigger):
    def on_enter(self):
        self.set_mesh(triggerIds=[3104], visible=True, arg3=0, delay=0, scale=0) # Pattern_Ground_B02
        self.set_user_value(triggerId=6, key='PickSecondPieceExceptB02', value=1)

    def on_tick(self) -> common.Trigger:
        if self.user_value(key='CheckFirstPiece', value=1):
            return Pattern05_Check(self.ctx)


# 다섯 번째 패턴 정답 체크
class Pattern05_Check(common.Trigger):
    def on_tick(self) -> common.Trigger:
        if self.detect_liftable_object(boxIds=[2001], itemId=30000569):
            return Pattern05_CorrectAnswer(self.ctx)
        if not self.detect_liftable_object(boxIds=[2001], itemId=30000569):
            return Pattern05_WrongAnswer(self.ctx)


# 다섯 번째 패턴 정답
class Pattern05_CorrectAnswer(common.Trigger):
    def on_enter(self):
        self.set_user_value(triggerId=4, key='CorrectFirstPiece', value=1) # 정답
        self.set_mesh(triggerIds=[3114], visible=True, arg3=100, delay=0, scale=5) # Pattern_LightOn_B02

    def on_tick(self) -> common.Trigger:
        if self.user_value(key='ResetFirstPiece', value=1):
            return Pattern05_Reset01(self.ctx)
        if self.user_value(key='LockFirstPiece', value=1):
            return Quit(self.ctx)


# 다섯 번째 패턴 오답
class Pattern05_WrongAnswer(common.Trigger):
    def on_enter(self):
        self.set_user_value(triggerId=4, key='CorrectFirstPiece', value=2) # 오답

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=2000):
            return Pattern05_Reset01(self.ctx)


class Pattern05_Reset01(common.Trigger):
    def on_enter(self):
        self.set_user_value(key='CheckFirstPiece', value=0)
        self.set_user_value(key='CorrectFirstPiece', value=0)
        self.set_user_value(key='ResetFirstPiece', value=0)
        self.set_user_value(key='LockFirstPiece', value=0)

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=1000):
            return Pattern05_Reset02(self.ctx)


# 다섯 번째 패턴 다시체크
class Pattern05_Reset02(common.Trigger):
    def on_enter(self):
        self.set_mesh(triggerIds=[3114], visible=False, arg3=100, delay=0, scale=5) # Pattern_LightOn_B02

    def on_tick(self) -> common.Trigger:
        if self.user_value(key='CheckFirstPiece', value=1):
            return Pattern05_Check(self.ctx)


# 여섯 번째 패턴 뽑힘
class Pattern06_Pick(common.Trigger):
    def on_enter(self):
        self.set_mesh(triggerIds=[3105], visible=True, arg3=0, delay=0, scale=0) # Pattern_Ground_C01
        self.set_user_value(triggerId=6, key='PickSecondPieceExceptC01', value=1)

    def on_tick(self) -> common.Trigger:
        if self.user_value(key='CheckFirstPiece', value=1):
            return Pattern06_Check(self.ctx)


# 여섯 번째 패턴 정답 체크
class Pattern06_Check(common.Trigger):
    def on_tick(self) -> common.Trigger:
        if self.detect_liftable_object(boxIds=[2001], itemId=30000570):
            return Pattern06_CorrectAnswer(self.ctx)
        if not self.detect_liftable_object(boxIds=[2001], itemId=30000570):
            return Pattern06_WrongAnswer(self.ctx)


# 여섯 번째 패턴 정답
class Pattern06_CorrectAnswer(common.Trigger):
    def on_enter(self):
        self.set_user_value(triggerId=4, key='CorrectFirstPiece', value=1) # 정답
        self.set_mesh(triggerIds=[3115], visible=True, arg3=100, delay=0, scale=5) # Pattern_LightOn_C01

    def on_tick(self) -> common.Trigger:
        if self.user_value(key='ResetFirstPiece', value=1):
            return Pattern06_Reset01(self.ctx)
        if self.user_value(key='LockFirstPiece', value=1):
            return Quit(self.ctx)


# 여섯 번째 패턴 오답
class Pattern06_WrongAnswer(common.Trigger):
    def on_enter(self):
        self.set_user_value(triggerId=4, key='CorrectFirstPiece', value=2) # 오답

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=2000):
            return Pattern06_Reset01(self.ctx)


class Pattern06_Reset01(common.Trigger):
    def on_enter(self):
        self.set_user_value(key='CheckFirstPiece', value=0)
        self.set_user_value(key='CorrectFirstPiece', value=0)
        self.set_user_value(key='ResetFirstPiece', value=0)
        self.set_user_value(key='LockFirstPiece', value=0)

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=1000):
            return Pattern06_Reset02(self.ctx)


# 여섯 번째 패턴 다시체크
class Pattern06_Reset02(common.Trigger):
    def on_enter(self):
        self.set_mesh(triggerIds=[3115], visible=False, arg3=100, delay=0, scale=5) # Pattern_LightOn_C01

    def on_tick(self) -> common.Trigger:
        if self.user_value(key='CheckFirstPiece', value=1):
            return Pattern06_Check(self.ctx)


# 일곱 번째 패턴 뽑힘
class Pattern07_Pick(common.Trigger):
    def on_enter(self):
        self.set_mesh(triggerIds=[3106], visible=True, arg3=0, delay=0, scale=0) # Pattern_Ground_D01
        self.set_user_value(triggerId=6, key='PickSecondPieceExceptD01', value=1)

    def on_tick(self) -> common.Trigger:
        if self.user_value(key='CheckFirstPiece', value=1):
            return Pattern07_Check(self.ctx)


# 일곱 번째 패턴 정답 체크
class Pattern07_Check(common.Trigger):
    def on_tick(self) -> common.Trigger:
        if self.detect_liftable_object(boxIds=[2001], itemId=30000571):
            return Pattern07_CorrectAnswer(self.ctx)
        if not self.detect_liftable_object(boxIds=[2001], itemId=30000571):
            return Pattern07_WrongAnswer(self.ctx)


# 일곱 번째 패턴 정답
class Pattern07_CorrectAnswer(common.Trigger):
    def on_enter(self):
        self.set_user_value(triggerId=4, key='CorrectFirstPiece', value=1) # 정답
        self.set_mesh(triggerIds=[3116], visible=True, arg3=100, delay=0, scale=5) # Pattern_LightOn_D01

    def on_tick(self) -> common.Trigger:
        if self.user_value(key='ResetFirstPiece', value=1):
            return Pattern07_Reset01(self.ctx)
        if self.user_value(key='LockFirstPiece', value=1):
            return Quit(self.ctx)


# 일곱 번째 패턴 오답
class Pattern07_WrongAnswer(common.Trigger):
    def on_enter(self):
        self.set_user_value(triggerId=4, key='CorrectFirstPiece', value=2) # 오답

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=2000):
            return Pattern07_Reset01(self.ctx)


class Pattern07_Reset01(common.Trigger):
    def on_enter(self):
        self.set_user_value(key='CheckFirstPiece', value=0)
        self.set_user_value(key='CorrectFirstPiece', value=0)
        self.set_user_value(key='ResetFirstPiece', value=0)
        self.set_user_value(key='LockFirstPiece', value=0)

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=1000):
            return Pattern07_Reset02(self.ctx)


# 일곱 번째 패턴 다시체크
class Pattern07_Reset02(common.Trigger):
    def on_enter(self):
        self.set_mesh(triggerIds=[3116], visible=False, arg3=100, delay=0, scale=5) # Pattern_LightOn_D01

    def on_tick(self) -> common.Trigger:
        if self.user_value(key='CheckFirstPiece', value=1):
            return Pattern07_Check(self.ctx)


# 여덟 번째 패턴 뽑힘
class Pattern08_Pick(common.Trigger):
    def on_enter(self):
        self.set_mesh(triggerIds=[3107], visible=True, arg3=0, delay=0, scale=0) # Pattern_Ground_D02
        self.set_user_value(triggerId=6, key='PickSecondPieceExceptD02', value=1)

    def on_tick(self) -> common.Trigger:
        if self.user_value(key='CheckFirstPiece', value=1):
            return Pattern08_Check(self.ctx)


# 여덟 번째 패턴 정답 체크
class Pattern08_Check(common.Trigger):
    def on_tick(self) -> common.Trigger:
        if self.detect_liftable_object(boxIds=[2001], itemId=30000572):
            return Pattern08_CorrectAnswer(self.ctx)
        if not self.detect_liftable_object(boxIds=[2001], itemId=30000572):
            return Pattern08_WrongAnswer(self.ctx)


# 여덟 번째 패턴 정답
class Pattern08_CorrectAnswer(common.Trigger):
    def on_enter(self):
        self.set_user_value(triggerId=4, key='CorrectFirstPiece', value=1) # 정답
        self.set_mesh(triggerIds=[3117], visible=True, arg3=100, delay=0, scale=5) # Pattern_LightOn_D02

    def on_tick(self) -> common.Trigger:
        if self.user_value(key='ResetFirstPiece', value=1):
            return Pattern08_Reset01(self.ctx)
        if self.user_value(key='LockFirstPiece', value=1):
            return Quit(self.ctx)


# 여덟 번째 패턴 오답
class Pattern08_WrongAnswer(common.Trigger):
    def on_enter(self):
        self.set_user_value(triggerId=4, key='CorrectFirstPiece', value=2) # 오답

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=2000):
            return Pattern08_Reset01(self.ctx)


class Pattern08_Reset01(common.Trigger):
    def on_enter(self):
        self.set_user_value(key='CheckFirstPiece', value=0)
        self.set_user_value(key='CorrectFirstPiece', value=0)
        self.set_user_value(key='ResetFirstPiece', value=0)
        self.set_user_value(key='LockFirstPiece', value=0)

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=1000):
            return Pattern08_Reset02(self.ctx)


# 여덟 번째 패턴 다시체크
class Pattern08_Reset02(common.Trigger):
    def on_enter(self):
        self.set_mesh(triggerIds=[3117], visible=False, arg3=100, delay=0, scale=5) # Pattern_LightOn_D02

    def on_tick(self) -> common.Trigger:
        if self.user_value(key='CheckFirstPiece', value=1):
            return Pattern08_Check(self.ctx)


# 아홉 번째 패턴 뽑힘
class Pattern09_Pick(common.Trigger):
    def on_enter(self):
        self.set_mesh(triggerIds=[3108], visible=True, arg3=0, delay=0, scale=0) # Pattern_Ground_E01
        self.set_user_value(triggerId=6, key='PickSecondPieceExceptE01', value=1)

    def on_tick(self) -> common.Trigger:
        if self.user_value(key='CheckFirstPiece', value=1):
            return Pattern09_Check(self.ctx)


# 아홉 번째 패턴 정답 체크
class Pattern09_Check(common.Trigger):
    def on_tick(self) -> common.Trigger:
        if self.detect_liftable_object(boxIds=[2001], itemId=30000573):
            return Pattern09_CorrectAnswer(self.ctx)
        if not self.detect_liftable_object(boxIds=[2001], itemId=30000573):
            return Pattern09_WrongAnswer(self.ctx)


# 아홉 번째 패턴 정답
class Pattern09_CorrectAnswer(common.Trigger):
    def on_enter(self):
        self.set_user_value(triggerId=4, key='CorrectFirstPiece', value=1) # 정답
        self.set_mesh(triggerIds=[3118], visible=True, arg3=100, delay=0, scale=5) # Pattern_LightOn_E01

    def on_tick(self) -> common.Trigger:
        if self.user_value(key='ResetFirstPiece', value=1):
            return Pattern09_Reset01(self.ctx)
        if self.user_value(key='LockFirstPiece', value=1):
            return Quit(self.ctx)


# 아홉 번째 패턴 오답
class Pattern09_WrongAnswer(common.Trigger):
    def on_enter(self):
        self.set_user_value(triggerId=4, key='CorrectFirstPiece', value=2) # 오답

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=2000):
            return Pattern09_Reset01(self.ctx)


class Pattern09_Reset01(common.Trigger):
    def on_enter(self):
        self.set_user_value(key='CheckFirstPiece', value=0)
        self.set_user_value(key='CorrectFirstPiece', value=0)
        self.set_user_value(key='ResetFirstPiece', value=0)
        self.set_user_value(key='LockFirstPiece', value=0)

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=1000):
            return Pattern09_Reset02(self.ctx)


# 아홉 번째 패턴 다시체크
class Pattern09_Reset02(common.Trigger):
    def on_enter(self):
        self.set_mesh(triggerIds=[3118], visible=False, arg3=100, delay=0, scale=5) # Pattern_LightOn_E01

    def on_tick(self) -> common.Trigger:
        if self.user_value(key='CheckFirstPiece', value=1):
            return Pattern09_Check(self.ctx)


# 열 번째 패턴 뽑힘
class Pattern10_Pick(common.Trigger):
    def on_enter(self):
        self.set_mesh(triggerIds=[3109], visible=True, arg3=0, delay=0, scale=0) # Pattern_Ground_E02
        self.set_user_value(triggerId=6, key='PickSecondPieceExceptE02', value=1)

    def on_tick(self) -> common.Trigger:
        if self.user_value(key='CheckFirstPiece', value=1):
            return Pattern10_Check(self.ctx)


# 열 번째 패턴 정답 체크
class Pattern10_Check(common.Trigger):
    def on_tick(self) -> common.Trigger:
        if self.detect_liftable_object(boxIds=[2001], itemId=30000574):
            return Pattern10_CorrectAnswer(self.ctx)
        if not self.detect_liftable_object(boxIds=[2001], itemId=30000574):
            return Pattern10_WrongAnswer(self.ctx)


# 열 번째 패턴 정답
class Pattern10_CorrectAnswer(common.Trigger):
    def on_enter(self):
        self.set_user_value(triggerId=4, key='CorrectFirstPiece', value=1) # 정답
        self.set_mesh(triggerIds=[3119], visible=True, arg3=100, delay=0, scale=5) # Pattern_LightOn_E02

    def on_tick(self) -> common.Trigger:
        if self.user_value(key='ResetFirstPiece', value=1):
            return Pattern10_Reset01(self.ctx)
        if self.user_value(key='LockFirstPiece', value=1):
            return Quit(self.ctx)


# 열 번째 패턴 오답
class Pattern10_WrongAnswer(common.Trigger):
    def on_enter(self):
        self.set_user_value(triggerId=4, key='CorrectFirstPiece', value=2) # 오답

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=2000):
            return Pattern10_Reset01(self.ctx)


class Pattern10_Reset01(common.Trigger):
    def on_enter(self):
        self.set_user_value(key='CheckFirstPiece', value=0)
        self.set_user_value(key='CorrectFirstPiece', value=0)
        self.set_user_value(key='ResetFirstPiece', value=0)
        self.set_user_value(key='LockFirstPiece', value=0)

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=1000):
            return Pattern10_Reset02(self.ctx)


# 열 번째 패턴 다시체크
class Pattern10_Reset02(common.Trigger):
    def on_enter(self):
        self.set_mesh(triggerIds=[3119], visible=False, arg3=100, delay=0, scale=5) # Pattern_LightOn_E02

    def on_tick(self) -> common.Trigger:
        if self.user_value(key='CheckFirstPiece', value=1):
            return Pattern10_Check(self.ctx)


class Quit(common.Trigger):
    pass


initial_state = Wait
