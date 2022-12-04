""" trigger/52000051_qd/07_puzzle_thirdpiece.xml """
import trigger_api


class Wait(trigger_api.Trigger):
    def on_enter(self):
        self.set_user_value(key='PickThirdPiece', value=0)
        self.set_user_value(key='CheckThirdPiece', value=0)
        self.set_user_value(key='CorrectThirdPiece', value=0)
        self.set_user_value(key='ResetThirdPiece', value=0)
        self.set_user_value(key='LockThirdPiece', value=0)
        self.set_mesh(triggerIds=[3300,3301,3302,3303,3304,3305,3306,3307,3308,3309], visible=False, arg3=0, delay=0, scale=0) # Pattern_Ground
        self.set_mesh(triggerIds=[3310,3311,3312,3313,3314,3315,3316,3317,3318,3319], visible=False, arg3=0, delay=0, scale=0) # Pattern_LightOn

    def on_tick(self) -> trigger_api.Trigger:
        if self.user_value(key='PickThirdPiece', value=1):
            return RandomPick(self.ctx)


class RandomPick(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
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
class Pattern01_Pick(trigger_api.Trigger):
    def on_enter(self):
        self.set_mesh(triggerIds=[3300], visible=True, arg3=0, delay=0, scale=0) # Pattern_Ground_A01
        self.set_user_value(triggerId=8, key='PickFourthPieceExceptA01', value=1)

    def on_tick(self) -> trigger_api.Trigger:
        if self.user_value(key='CheckThirdPiece', value=1):
            return Pattern01_Check(self.ctx)


# 첫 번째 패턴 정답 체크
class Pattern01_Check(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.detect_liftable_object(boxIds=[2003], itemId=30000565):
            return Pattern01_CorrectAnswer(self.ctx)
        if not self.detect_liftable_object(boxIds=[2003], itemId=30000565):
            return Pattern01_WrongAnswer(self.ctx)


# 첫 번째 패턴 정답
class Pattern01_CorrectAnswer(trigger_api.Trigger):
    def on_enter(self):
        self.set_user_value(triggerId=4, key='CorrectThirdPiece', value=1) # 정답
        self.set_mesh(triggerIds=[3310], visible=True, arg3=100, delay=0, scale=5) # Pattern_LightOn_A01

    def on_tick(self) -> trigger_api.Trigger:
        if self.user_value(key='ResetThirdPiece', value=1):
            return Pattern01_Reset01(self.ctx)
        if self.user_value(key='LockThirdPiece', value=1):
            return Quit(self.ctx)


# 첫 번째 패턴 오답
class Pattern01_WrongAnswer(trigger_api.Trigger):
    def on_enter(self):
        self.set_user_value(triggerId=4, key='CorrectThirdPiece', value=2) # 오답

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=2000):
            return Pattern01_Reset01(self.ctx)


class Pattern01_Reset01(trigger_api.Trigger):
    def on_enter(self):
        self.set_user_value(key='CheckThirdPiece', value=0)
        self.set_user_value(key='CorrectThirdPiece', value=0)
        self.set_user_value(key='ResetThirdPiece', value=0)
        self.set_user_value(key='LockThirdPiece', value=0)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=1000):
            return Pattern01_Reset02(self.ctx)


# 첫 번째 패턴 다시체크
class Pattern01_Reset02(trigger_api.Trigger):
    def on_enter(self):
        self.set_mesh(triggerIds=[3310], visible=False, arg3=100, delay=0, scale=5) # Pattern_LightOn_A01

    def on_tick(self) -> trigger_api.Trigger:
        if self.user_value(key='CheckThirdPiece', value=1):
            return Pattern01_Check(self.ctx)


# 두 번째 패턴 뽑힘
class Pattern02_Pick(trigger_api.Trigger):
    def on_enter(self):
        self.set_mesh(triggerIds=[3301], visible=True, arg3=0, delay=0, scale=0) # Pattern_Ground_A02
        self.set_user_value(triggerId=8, key='PickFourthPieceExceptA02', value=1)

    def on_tick(self) -> trigger_api.Trigger:
        if self.user_value(key='CheckThirdPiece', value=1):
            return Pattern02_Check(self.ctx)


# 두 번째 패턴 정답 체크
class Pattern02_Check(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.detect_liftable_object(boxIds=[2003], itemId=30000566):
            return Pattern02_CorrectAnswer(self.ctx)
        if not self.detect_liftable_object(boxIds=[2003], itemId=30000566):
            return Pattern02_WrongAnswer(self.ctx)


# 두 번째 패턴 정답
class Pattern02_CorrectAnswer(trigger_api.Trigger):
    def on_enter(self):
        self.set_user_value(triggerId=4, key='CorrectThirdPiece', value=1) # 정답
        self.set_mesh(triggerIds=[3311], visible=True, arg3=100, delay=0, scale=5) # Pattern_LightOn_A02

    def on_tick(self) -> trigger_api.Trigger:
        if self.user_value(key='ResetThirdPiece', value=1):
            return Pattern02_Reset01(self.ctx)
        if self.user_value(key='LockThirdPiece', value=1):
            return Quit(self.ctx)


# 두 번째 패턴 오답
class Pattern02_WrongAnswer(trigger_api.Trigger):
    def on_enter(self):
        self.set_user_value(triggerId=4, key='CorrectThirdPiece', value=2) # 오답

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=2000):
            return Pattern02_Reset01(self.ctx)


class Pattern02_Reset01(trigger_api.Trigger):
    def on_enter(self):
        self.set_user_value(key='CheckThirdPiece', value=0)
        self.set_user_value(key='CorrectThirdPiece', value=0)
        self.set_user_value(key='ResetThirdPiece', value=0)
        self.set_user_value(key='LockThirdPiece', value=0)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=1000):
            return Pattern02_Reset02(self.ctx)


# 두 번째 패턴 다시체크
class Pattern02_Reset02(trigger_api.Trigger):
    def on_enter(self):
        self.set_mesh(triggerIds=[3311], visible=False, arg3=100, delay=0, scale=5) # Pattern_LightOn_A02

    def on_tick(self) -> trigger_api.Trigger:
        if self.user_value(key='CheckThirdPiece', value=1):
            return Pattern02_Check(self.ctx)


# 세 번째 패턴 뽑힘
class Pattern03_Pick(trigger_api.Trigger):
    def on_enter(self):
        self.set_mesh(triggerIds=[3302], visible=True, arg3=0, delay=0, scale=0) # Pattern_Ground_A03
        self.set_user_value(triggerId=8, key='PickFourthPieceExceptA03', value=1)

    def on_tick(self) -> trigger_api.Trigger:
        if self.user_value(key='CheckThirdPiece', value=1):
            return Pattern03_Check(self.ctx)


# 세 번째 패턴 정답 체크
class Pattern03_Check(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.detect_liftable_object(boxIds=[2003], itemId=30000567):
            return Pattern03_CorrectAnswer(self.ctx)
        if not self.detect_liftable_object(boxIds=[2003], itemId=30000567):
            return Pattern03_WrongAnswer(self.ctx)


# 세 번째 패턴 정답
class Pattern03_CorrectAnswer(trigger_api.Trigger):
    def on_enter(self):
        self.set_user_value(triggerId=4, key='CorrectThirdPiece', value=1) # 정답
        self.set_mesh(triggerIds=[3312], visible=True, arg3=100, delay=0, scale=5) # Pattern_LightOn_A03

    def on_tick(self) -> trigger_api.Trigger:
        if self.user_value(key='ResetThirdPiece', value=1):
            return Pattern03_Reset01(self.ctx)
        if self.user_value(key='LockThirdPiece', value=1):
            return Quit(self.ctx)


# 세 번째 패턴 오답
class Pattern03_WrongAnswer(trigger_api.Trigger):
    def on_enter(self):
        self.set_user_value(triggerId=4, key='CorrectThirdPiece', value=2) # 오답

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=2000):
            return Pattern03_Reset01(self.ctx)


class Pattern03_Reset01(trigger_api.Trigger):
    def on_enter(self):
        self.set_user_value(key='CheckThirdPiece', value=0)
        self.set_user_value(key='CorrectThirdPiece', value=0)
        self.set_user_value(key='ResetThirdPiece', value=0)
        self.set_user_value(key='LockThirdPiece', value=0)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=1000):
            return Pattern03_Reset02(self.ctx)


# 세 번째 패턴 다시체크
class Pattern03_Reset02(trigger_api.Trigger):
    def on_enter(self):
        self.set_mesh(triggerIds=[3312], visible=False, arg3=100, delay=0, scale=5) # Pattern_LightOn_A03

    def on_tick(self) -> trigger_api.Trigger:
        if self.user_value(key='CheckThirdPiece', value=1):
            return Pattern03_Check(self.ctx)


# 네 번째 패턴 뽑힘
class Pattern04_Pick(trigger_api.Trigger):
    def on_enter(self):
        self.set_mesh(triggerIds=[3303], visible=True, arg3=0, delay=0, scale=0) # Pattern_Ground_B01
        self.set_user_value(triggerId=8, key='PickFourthPieceExceptB01', value=1)

    def on_tick(self) -> trigger_api.Trigger:
        if self.user_value(key='CheckThirdPiece', value=1):
            return Pattern04_Check(self.ctx)


# 네 번째 패턴 정답 체크
class Pattern04_Check(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.detect_liftable_object(boxIds=[2003], itemId=30000568):
            return Pattern04_CorrectAnswer(self.ctx)
        if not self.detect_liftable_object(boxIds=[2003], itemId=30000568):
            return Pattern04_WrongAnswer(self.ctx)


# 네 번째 패턴 정답
class Pattern04_CorrectAnswer(trigger_api.Trigger):
    def on_enter(self):
        self.set_user_value(triggerId=4, key='CorrectThirdPiece', value=1) # 정답
        self.set_mesh(triggerIds=[3313], visible=True, arg3=100, delay=0, scale=5) # Pattern_LightOn_B01

    def on_tick(self) -> trigger_api.Trigger:
        if self.user_value(key='ResetThirdPiece', value=1):
            return Pattern04_Reset01(self.ctx)
        if self.user_value(key='LockThirdPiece', value=1):
            return Quit(self.ctx)


# 네 번째 패턴 오답
class Pattern04_WrongAnswer(trigger_api.Trigger):
    def on_enter(self):
        self.set_user_value(triggerId=4, key='CorrectThirdPiece', value=2) # 오답

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=2000):
            return Pattern04_Reset01(self.ctx)


class Pattern04_Reset01(trigger_api.Trigger):
    def on_enter(self):
        self.set_user_value(key='CheckThirdPiece', value=0)
        self.set_user_value(key='CorrectThirdPiece', value=0)
        self.set_user_value(key='ResetThirdPiece', value=0)
        self.set_user_value(key='LockThirdPiece', value=0)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=1000):
            return Pattern04_Reset02(self.ctx)


# 네 번째 패턴 다시체크
class Pattern04_Reset02(trigger_api.Trigger):
    def on_enter(self):
        self.set_mesh(triggerIds=[3313], visible=False, arg3=100, delay=0, scale=5) # Pattern_LightOn_B01

    def on_tick(self) -> trigger_api.Trigger:
        if self.user_value(key='CheckThirdPiece', value=1):
            return Pattern04_Check(self.ctx)


# 다섯 번째 패턴 뽑힘
class Pattern05_Pick(trigger_api.Trigger):
    def on_enter(self):
        self.set_mesh(triggerIds=[3304], visible=True, arg3=0, delay=0, scale=0) # Pattern_Ground_B02
        self.set_user_value(triggerId=8, key='PickFourthPieceExceptB02', value=1)

    def on_tick(self) -> trigger_api.Trigger:
        if self.user_value(key='CheckThirdPiece', value=1):
            return Pattern05_Check(self.ctx)


# 다섯 번째 패턴 정답 체크
class Pattern05_Check(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.detect_liftable_object(boxIds=[2003], itemId=30000569):
            return Pattern05_CorrectAnswer(self.ctx)
        if not self.detect_liftable_object(boxIds=[2003], itemId=30000569):
            return Pattern05_WrongAnswer(self.ctx)


# 다섯 번째 패턴 정답
class Pattern05_CorrectAnswer(trigger_api.Trigger):
    def on_enter(self):
        self.set_user_value(triggerId=4, key='CorrectThirdPiece', value=1) # 정답
        self.set_mesh(triggerIds=[3314], visible=True, arg3=100, delay=0, scale=5) # Pattern_LightOn_B02

    def on_tick(self) -> trigger_api.Trigger:
        if self.user_value(key='ResetThirdPiece', value=1):
            return Pattern05_Reset01(self.ctx)
        if self.user_value(key='LockThirdPiece', value=1):
            return Quit(self.ctx)


# 다섯 번째 패턴 오답
class Pattern05_WrongAnswer(trigger_api.Trigger):
    def on_enter(self):
        self.set_user_value(triggerId=4, key='CorrectThirdPiece', value=2) # 오답

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=2000):
            return Pattern05_Reset01(self.ctx)


class Pattern05_Reset01(trigger_api.Trigger):
    def on_enter(self):
        self.set_user_value(key='CheckThirdPiece', value=0)
        self.set_user_value(key='CorrectThirdPiece', value=0)
        self.set_user_value(key='ResetThirdPiece', value=0)
        self.set_user_value(key='LockThirdPiece', value=0)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=1000):
            return Pattern05_Reset02(self.ctx)


# 다섯 번째 패턴 다시체크
class Pattern05_Reset02(trigger_api.Trigger):
    def on_enter(self):
        self.set_mesh(triggerIds=[3314], visible=False, arg3=100, delay=0, scale=5) # Pattern_LightOn_B02

    def on_tick(self) -> trigger_api.Trigger:
        if self.user_value(key='CheckThirdPiece', value=1):
            return Pattern05_Check(self.ctx)


# 여섯 번째 패턴 뽑힘
class Pattern06_Pick(trigger_api.Trigger):
    def on_enter(self):
        self.set_mesh(triggerIds=[3305], visible=True, arg3=0, delay=0, scale=0) # Pattern_Ground_C01
        self.set_user_value(triggerId=8, key='PickFourthPieceExceptC01', value=1)

    def on_tick(self) -> trigger_api.Trigger:
        if self.user_value(key='CheckThirdPiece', value=1):
            return Pattern06_Check(self.ctx)


# 여섯 번째 패턴 정답 체크
class Pattern06_Check(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.detect_liftable_object(boxIds=[2003], itemId=30000570):
            return Pattern06_CorrectAnswer(self.ctx)
        if not self.detect_liftable_object(boxIds=[2003], itemId=30000570):
            return Pattern06_WrongAnswer(self.ctx)


# 여섯 번째 패턴 정답
class Pattern06_CorrectAnswer(trigger_api.Trigger):
    def on_enter(self):
        self.set_user_value(triggerId=4, key='CorrectThirdPiece', value=1) # 정답
        self.set_mesh(triggerIds=[3315], visible=True, arg3=100, delay=0, scale=5) # Pattern_LightOn_C01

    def on_tick(self) -> trigger_api.Trigger:
        if self.user_value(key='ResetThirdPiece', value=1):
            return Pattern06_Reset01(self.ctx)
        if self.user_value(key='LockThirdPiece', value=1):
            return Quit(self.ctx)


# 여섯 번째 패턴 오답
class Pattern06_WrongAnswer(trigger_api.Trigger):
    def on_enter(self):
        self.set_user_value(triggerId=4, key='CorrectThirdPiece', value=2) # 오답

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=2000):
            return Pattern06_Reset01(self.ctx)


class Pattern06_Reset01(trigger_api.Trigger):
    def on_enter(self):
        self.set_user_value(key='CheckThirdPiece', value=0)
        self.set_user_value(key='CorrectThirdPiece', value=0)
        self.set_user_value(key='ResetThirdPiece', value=0)
        self.set_user_value(key='LockThirdPiece', value=0)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=1000):
            return Pattern06_Reset02(self.ctx)


# 여섯 번째 패턴 다시체크
class Pattern06_Reset02(trigger_api.Trigger):
    def on_enter(self):
        self.set_mesh(triggerIds=[3315], visible=False, arg3=100, delay=0, scale=5) # Pattern_LightOn_C01

    def on_tick(self) -> trigger_api.Trigger:
        if self.user_value(key='CheckThirdPiece', value=1):
            return Pattern06_Check(self.ctx)


# 일곱 번째 패턴 뽑힘
class Pattern07_Pick(trigger_api.Trigger):
    def on_enter(self):
        self.set_mesh(triggerIds=[3306], visible=True, arg3=0, delay=0, scale=0) # Pattern_Ground_D01
        self.set_user_value(triggerId=8, key='PickFourthPieceExceptD01', value=1)

    def on_tick(self) -> trigger_api.Trigger:
        if self.user_value(key='CheckThirdPiece', value=1):
            return Pattern07_Check(self.ctx)


# 일곱 번째 패턴 정답 체크
class Pattern07_Check(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.detect_liftable_object(boxIds=[2003], itemId=30000571):
            return Pattern07_CorrectAnswer(self.ctx)
        if not self.detect_liftable_object(boxIds=[2003], itemId=30000571):
            return Pattern07_WrongAnswer(self.ctx)


# 일곱 번째 패턴 정답
class Pattern07_CorrectAnswer(trigger_api.Trigger):
    def on_enter(self):
        self.set_user_value(triggerId=4, key='CorrectThirdPiece', value=1) # 정답
        self.set_mesh(triggerIds=[3316], visible=True, arg3=100, delay=0, scale=5) # Pattern_LightOn_D01

    def on_tick(self) -> trigger_api.Trigger:
        if self.user_value(key='ResetThirdPiece', value=1):
            return Pattern07_Reset01(self.ctx)
        if self.user_value(key='LockThirdPiece', value=1):
            return Quit(self.ctx)


# 일곱 번째 패턴 오답
class Pattern07_WrongAnswer(trigger_api.Trigger):
    def on_enter(self):
        self.set_user_value(triggerId=4, key='CorrectThirdPiece', value=2) # 오답

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=2000):
            return Pattern07_Reset01(self.ctx)


class Pattern07_Reset01(trigger_api.Trigger):
    def on_enter(self):
        self.set_user_value(key='CheckThirdPiece', value=0)
        self.set_user_value(key='CorrectThirdPiece', value=0)
        self.set_user_value(key='ResetThirdPiece', value=0)
        self.set_user_value(key='LockThirdPiece', value=0)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=1000):
            return Pattern07_Reset02(self.ctx)


# 일곱 번째 패턴 다시체크
class Pattern07_Reset02(trigger_api.Trigger):
    def on_enter(self):
        self.set_mesh(triggerIds=[3316], visible=False, arg3=100, delay=0, scale=5) # Pattern_LightOn_D01

    def on_tick(self) -> trigger_api.Trigger:
        if self.user_value(key='CheckThirdPiece', value=1):
            return Pattern07_Check(self.ctx)


# 여덟 번째 패턴 뽑힘
class Pattern08_Pick(trigger_api.Trigger):
    def on_enter(self):
        self.set_mesh(triggerIds=[3307], visible=True, arg3=0, delay=0, scale=0) # Pattern_Ground_D02
        self.set_user_value(triggerId=8, key='PickFourthPieceExceptD02', value=1)

    def on_tick(self) -> trigger_api.Trigger:
        if self.user_value(key='CheckThirdPiece', value=1):
            return Pattern08_Check(self.ctx)


# 여덟 번째 패턴 정답 체크
class Pattern08_Check(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.detect_liftable_object(boxIds=[2003], itemId=30000572):
            return Pattern08_CorrectAnswer(self.ctx)
        if not self.detect_liftable_object(boxIds=[2003], itemId=30000572):
            return Pattern08_WrongAnswer(self.ctx)


# 여덟 번째 패턴 정답
class Pattern08_CorrectAnswer(trigger_api.Trigger):
    def on_enter(self):
        self.set_user_value(triggerId=4, key='CorrectThirdPiece', value=1) # 정답
        self.set_mesh(triggerIds=[3317], visible=True, arg3=100, delay=0, scale=5) # Pattern_LightOn_D02

    def on_tick(self) -> trigger_api.Trigger:
        if self.user_value(key='ResetThirdPiece', value=1):
            return Pattern08_Reset01(self.ctx)
        if self.user_value(key='LockThirdPiece', value=1):
            return Quit(self.ctx)


# 여덟 번째 패턴 오답
class Pattern08_WrongAnswer(trigger_api.Trigger):
    def on_enter(self):
        self.set_user_value(triggerId=4, key='CorrectThirdPiece', value=2) # 오답

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=2000):
            return Pattern08_Reset01(self.ctx)


class Pattern08_Reset01(trigger_api.Trigger):
    def on_enter(self):
        self.set_user_value(key='CheckThirdPiece', value=0)
        self.set_user_value(key='CorrectThirdPiece', value=0)
        self.set_user_value(key='ResetThirdPiece', value=0)
        self.set_user_value(key='LockThirdPiece', value=0)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=1000):
            return Pattern08_Reset02(self.ctx)


# 여덟 번째 패턴 다시체크
class Pattern08_Reset02(trigger_api.Trigger):
    def on_enter(self):
        self.set_mesh(triggerIds=[3317], visible=False, arg3=100, delay=0, scale=5) # Pattern_LightOn_D02

    def on_tick(self) -> trigger_api.Trigger:
        if self.user_value(key='CheckThirdPiece', value=1):
            return Pattern08_Check(self.ctx)


# 아홉 번째 패턴 뽑힘
class Pattern09_Pick(trigger_api.Trigger):
    def on_enter(self):
        self.set_mesh(triggerIds=[3308], visible=True, arg3=0, delay=0, scale=0) # Pattern_Ground_E01
        self.set_user_value(triggerId=8, key='PickFourthPieceExceptE01', value=1)

    def on_tick(self) -> trigger_api.Trigger:
        if self.user_value(key='CheckThirdPiece', value=1):
            return Pattern09_Check(self.ctx)


# 아홉 번째 패턴 정답 체크
class Pattern09_Check(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.detect_liftable_object(boxIds=[2003], itemId=30000573):
            return Pattern09_CorrectAnswer(self.ctx)
        if not self.detect_liftable_object(boxIds=[2003], itemId=30000573):
            return Pattern09_WrongAnswer(self.ctx)


# 아홉 번째 패턴 정답
class Pattern09_CorrectAnswer(trigger_api.Trigger):
    def on_enter(self):
        self.set_user_value(triggerId=4, key='CorrectThirdPiece', value=1) # 정답
        self.set_mesh(triggerIds=[3318], visible=True, arg3=100, delay=0, scale=5) # Pattern_LightOn_E01

    def on_tick(self) -> trigger_api.Trigger:
        if self.user_value(key='ResetThirdPiece', value=1):
            return Pattern09_Reset01(self.ctx)
        if self.user_value(key='LockThirdPiece', value=1):
            return Quit(self.ctx)


# 아홉 번째 패턴 오답
class Pattern09_WrongAnswer(trigger_api.Trigger):
    def on_enter(self):
        self.set_user_value(triggerId=4, key='CorrectThirdPiece', value=2) # 오답

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=2000):
            return Pattern09_Reset01(self.ctx)


class Pattern09_Reset01(trigger_api.Trigger):
    def on_enter(self):
        self.set_user_value(key='CheckThirdPiece', value=0)
        self.set_user_value(key='CorrectThirdPiece', value=0)
        self.set_user_value(key='ResetThirdPiece', value=0)
        self.set_user_value(key='LockThirdPiece', value=0)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=1000):
            return Pattern09_Reset02(self.ctx)


# 아홉 번째 패턴 다시체크
class Pattern09_Reset02(trigger_api.Trigger):
    def on_enter(self):
        self.set_mesh(triggerIds=[3318], visible=False, arg3=100, delay=0, scale=5) # Pattern_LightOn_E01

    def on_tick(self) -> trigger_api.Trigger:
        if self.user_value(key='CheckThirdPiece', value=1):
            return Pattern09_Check(self.ctx)


# 열 번째 패턴 뽑힘
class Pattern10_Pick(trigger_api.Trigger):
    def on_enter(self):
        self.set_mesh(triggerIds=[3309], visible=True, arg3=0, delay=0, scale=0) # Pattern_Ground_E02
        self.set_user_value(triggerId=8, key='PickFourthPieceExceptE02', value=1)

    def on_tick(self) -> trigger_api.Trigger:
        if self.user_value(key='CheckThirdPiece', value=1):
            return Pattern10_Check(self.ctx)


# 열 번째 패턴 정답 체크
class Pattern10_Check(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.detect_liftable_object(boxIds=[2003], itemId=30000574):
            return Pattern10_CorrectAnswer(self.ctx)
        if not self.detect_liftable_object(boxIds=[2003], itemId=30000574):
            return Pattern10_WrongAnswer(self.ctx)


# 열 번째 패턴 정답
class Pattern10_CorrectAnswer(trigger_api.Trigger):
    def on_enter(self):
        self.set_user_value(triggerId=4, key='CorrectThirdPiece', value=1) # 정답
        self.set_mesh(triggerIds=[3319], visible=True, arg3=100, delay=0, scale=5) # Pattern_LightOn_E02

    def on_tick(self) -> trigger_api.Trigger:
        if self.user_value(key='ResetThirdPiece', value=1):
            return Pattern10_Reset01(self.ctx)
        if self.user_value(key='LockThirdPiece', value=1):
            return Quit(self.ctx)


# 열 번째 패턴 오답
class Pattern10_WrongAnswer(trigger_api.Trigger):
    def on_enter(self):
        self.set_user_value(triggerId=4, key='CorrectThirdPiece', value=2) # 오답

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=2000):
            return Pattern10_Reset01(self.ctx)


class Pattern10_Reset01(trigger_api.Trigger):
    def on_enter(self):
        self.set_user_value(key='CheckThirdPiece', value=0)
        self.set_user_value(key='CorrectThirdPiece', value=0)
        self.set_user_value(key='ResetThirdPiece', value=0)
        self.set_user_value(key='LockThirdPiece', value=0)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=1000):
            return Pattern10_Reset02(self.ctx)


# 열 번째 패턴 다시체크
class Pattern10_Reset02(trigger_api.Trigger):
    def on_enter(self):
        self.set_mesh(triggerIds=[3319], visible=False, arg3=100, delay=0, scale=5) # Pattern_LightOn_E02

    def on_tick(self) -> trigger_api.Trigger:
        if self.user_value(key='CheckThirdPiece', value=1):
            return Pattern10_Check(self.ctx)


class Quit(trigger_api.Trigger):
    pass


initial_state = Wait
