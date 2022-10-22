""" trigger/02000066_bf/oscal.xml """
from common import *
import state


class 시작(state.State):
    def on_tick(self) -> state.State:
        if user_value(key='randomTalk', value=1):
            create_monster(spawnIds=[5003], arg2=False)
            return 전투대기()


class 전투대기(state.State):
    def on_tick(self) -> state.State:
        if monster_in_combat(boxIds=[5003]):
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
        set_conversation(type=1, spawnId=5003, script='$02000066_BF__OSCAL__0$', arg4=3)

    def on_tick(self) -> state.State:
        if true():
            return 대기시간()


class NPC대사02(state.State):
    def on_enter(self):
        set_conversation(type=1, spawnId=5003, script='$02000066_BF__OSCAL__1$', arg4=3)

    def on_tick(self) -> state.State:
        if true():
            return 대기시간()


class NPC대사03(state.State):
    def on_enter(self):
        set_conversation(type=1, spawnId=5003, script='$02000066_BF__OSCAL__2$', arg4=2)

    def on_tick(self) -> state.State:
        if true():
            return 대기시간()


class NPC대사04(state.State):
    def on_enter(self):
        set_conversation(type=1, spawnId=5003, script='$02000066_BF__OSCAL__3$', arg4=3)

    def on_tick(self) -> state.State:
        if true():
            return 대기시간()


class 대기시간(state.State):
    def on_tick(self) -> state.State:
        if wait_tick(waitTick=10000):
            return 전투대기()


