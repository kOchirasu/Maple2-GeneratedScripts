""" trigger/02000066_bf/anos.xml """
from common import *
import state


class 시작(state.State):
    def on_tick(self) -> state.State:
        if user_detected(boxIds=[103]):
            return NPC생성()


class NPC생성(state.State):
    def on_enter(self):
        create_monster(spawnIds=[98], arg2=False)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=5000):
            return 대기시간()


class 대기시간(state.State):
    def on_tick(self) -> state.State:
        if wait_tick(waitTick=10000):
            return 말풍선랜덤()


class 말풍선랜덤(state.State):
    def on_tick(self) -> state.State:
        if random_condition(rate=25):
            return NPC대사01()
        if random_condition(rate=25):
            return NPC대사02()
        if random_condition(rate=25):
            return NPC대사03()
        if random_condition(rate=25):
            return NPC대사04()


class NPC대사01(state.State):
    def on_enter(self):
        set_conversation(type=1, spawnId=98, script='$02000066_BF__ANOS__0$', arg4=3)

    def on_tick(self) -> state.State:
        if true():
            return 대기시간()


class NPC대사02(state.State):
    def on_enter(self):
        set_conversation(type=1, spawnId=98, script='$02000066_BF__ANOS__1$', arg4=3)

    def on_tick(self) -> state.State:
        if true():
            return 대기시간()


class NPC대사03(state.State):
    def on_enter(self):
        set_conversation(type=1, spawnId=98, script='$02000066_BF__ANOS__2$', arg4=3)

    def on_tick(self) -> state.State:
        if true():
            return 대기시간()


class NPC대사04(state.State):
    def on_enter(self):
        set_conversation(type=1, spawnId=98, script='$02000066_BF__ANOS__3$', arg4=3)

    def on_tick(self) -> state.State:
        if true():
            return 대기시간()


