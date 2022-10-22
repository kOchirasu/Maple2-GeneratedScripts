""" trigger/52010038_qd/event.xml """
from common import *
import state


class 대기(state.State):
    def on_enter(self):
        set_agent(triggerIds=[8001], visible=True)
        set_agent(triggerIds=[8002], visible=True)
        set_agent(triggerIds=[8003], visible=True)
        set_agent(triggerIds=[8004], visible=True)
        set_agent(triggerIds=[8005], visible=True)
        set_agent(triggerIds=[8006], visible=True)
        set_agent(triggerIds=[8007], visible=True)
        set_agent(triggerIds=[8008], visible=True)
        set_agent(triggerIds=[8009], visible=True)
        set_agent(triggerIds=[8010], visible=True)
        set_agent(triggerIds=[8011], visible=True)
        set_agent(triggerIds=[8012], visible=True)
        set_agent(triggerIds=[8013], visible=True)
        set_skill(triggerIds=[710], isEnable=False)
        set_skill(triggerIds=[711], isEnable=False)
        set_effect(triggerIds=[6110], visible=False)
        set_effect(triggerIds=[6111], visible=False)
        set_effect(triggerIds=[6298], visible=False)
        set_actor(triggerId=220, visible=False)
        set_actor(triggerId=221, visible=False)
        set_actor(triggerId=222, visible=False)

    def on_tick(self) -> state.State:
        if user_value(key='EventStart', value=1):
            return 이벤트조건()


class 이벤트조건(state.State):
    def on_enter(self):
        set_effect(triggerIds=[6298], visible=True)

    def on_tick(self) -> state.State:
        if user_detected(boxIds=[103]):
            return 이벤트시작()


class 이벤트시작(state.State):
    def on_enter(self):
        create_monster(spawnIds=[1200], arg2=False)
        destroy_monster(spawnIds=[1201])
        set_conversation(type=1, spawnId=1200, script='$52010038_QD__EVENT__0$', arg4=2, arg5=0)
        move_npc(spawnId=1200, patrolName='MS2PatrolData_1200')

    def on_tick(self) -> state.State:
        if npc_detected(boxId=104, spawnIds=[1200]):
            return 생성()


class 생성(state.State):
    def on_enter(self):
        set_skill(triggerIds=[710], isEnable=True)
        set_effect(triggerIds=[6110], visible=True)
        create_monster(spawnIds=[2012,2013,2014,2015], arg2=True)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=1500):
            return 감지대기()


class 감지대기(state.State):
    def on_enter(self):
        set_agent(triggerIds=[8005], visible=False)
        set_agent(triggerIds=[8006], visible=False)
        set_agent(triggerIds=[8007], visible=False)
        set_agent(triggerIds=[8008], visible=False)
        set_agent(triggerIds=[8009], visible=False)
        set_agent(triggerIds=[8010], visible=False)
        set_agent(triggerIds=[8011], visible=False)
        set_agent(triggerIds=[8012], visible=False)
        set_agent(triggerIds=[8013], visible=False)
        set_conversation(type=1, spawnId=1200, script='$52010038_QD__EVENT__2$', arg4=3, arg5=2)

    def on_tick(self) -> state.State:
        if user_detected(boxIds=[105]):
            return 폭발시퀀스시작()


class 폭발시퀀스시작(state.State):
    def on_enter(self):
        set_actor(triggerId=220, visible=True, initialSequence='Regen_A')
        set_actor(triggerId=221, visible=True, initialSequence='Regen_A')
        set_actor(triggerId=222, visible=True, initialSequence='Regen_A')

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=500):
            return 폭발딜레이()


class 폭발딜레이(state.State):
    def on_enter(self):
        set_actor(triggerId=220, visible=True, initialSequence='Attack_01_A')
        set_actor(triggerId=221, visible=True, initialSequence='Attack_01_A')
        set_actor(triggerId=222, visible=True, initialSequence='Attack_01_A')

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=800):
            return 폭발()


class 폭발(state.State):
    def on_enter(self):
        set_actor(triggerId=220, visible=True, initialSequence='Attack_02_A')
        set_actor(triggerId=221, visible=True, initialSequence='Attack_02_A')
        set_actor(triggerId=222, visible=True, initialSequence='Attack_02_A')
        set_skill(triggerIds=[711], isEnable=True)
        set_effect(triggerIds=[6298], visible=False)
        set_effect(triggerIds=[6111], visible=True)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=200):
            return 폭탄숨김()


class 폭탄숨김(state.State):
    def on_enter(self):
        set_actor(triggerId=220, visible=False)
        set_actor(triggerId=221, visible=False)
        set_actor(triggerId=222, visible=False)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=1300):
            return 점수()


class 점수(state.State):
    def on_enter(self):
        create_monster(spawnIds=[4010], arg2=False)
        create_monster(spawnIds=[4030], arg2=False)
        side_npc_talk(npcId=11003536, illust='Neirin_normal', duration=5000, script='$52010038_QD__event__4$', voice='ko/Npc/00002105')

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=1000):
            return 종료()


class 종료(state.State):
    pass


