""" trigger/03000058_bf/chest.xml """
from common import *
import state


class 대기(state.State):
    def on_enter(self):
        set_interact_object(triggerIds=[11000023], state=1)
        set_interact_object(triggerIds=[11000008], state=2)
        set_interact_object(triggerIds=[11000009], state=2)
        set_effect(triggerIds=[601], visible=False)
        set_effect(triggerIds=[602], visible=False)
        set_effect(triggerIds=[603], visible=False)
        set_effect(triggerIds=[604], visible=False)

    def on_tick(self) -> state.State:
        if user_detected(boxIds=[101]):
            set_interact_object(triggerIds=[11000023], state=2)
            return 차웨이브대기1()


class 차웨이브대기1(state.State):
    def on_enter(self):
        show_guide_summary(entityId=23000003, textId=23000003, duration=5000)
        set_effect(triggerIds=[602], visible=True)
        set_effect(triggerIds=[603], visible=True)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=3000):
            return 차웨이브시작1()


class 차웨이브시작1(state.State):
    def on_enter(self):
        create_monster(spawnIds=[1001,1002], arg2=False)

    def on_tick(self) -> state.State:
        if monster_dead(boxIds=[1001,1002]):
            return 차웨이브대기2()


class 차웨이브대기2(state.State):
    def on_enter(self):
        set_effect(triggerIds=[601], visible=True)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=3000):
            return 차웨이브시작2()


class 차웨이브시작2(state.State):
    def on_enter(self):
        create_monster(spawnIds=[2001], arg2=False)

    def on_tick(self) -> state.State:
        if monster_dead(boxIds=[2001]):
            return 차웨이브대기3()


class 차웨이브대기3(state.State):
    def on_enter(self):
        set_effect(triggerIds=[604], visible=True)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=3000):
            return 차웨이브시작3()


class 차웨이브시작3(state.State):
    def on_enter(self):
        create_monster(spawnIds=[3001], arg2=False)

    def on_tick(self) -> state.State:
        if monster_dead(boxIds=[3001]):
            set_event_ui(type=7, arg3='2000', arg4='0')
            return 상자확률()


class 상자확률(state.State):
    def on_tick(self) -> state.State:
        if random_condition(rate=90):
            set_interact_object(triggerIds=[11000008], state=1)
            return 종료()
        if random_condition(rate=10):
            set_interact_object(triggerIds=[11000009], state=1)
            return 종료()


class 종료(state.State):
    pass


