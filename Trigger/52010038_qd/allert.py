""" trigger/52010038_qd/allert.xml """
from common import *
import state


class 대기(state.State):
    def on_enter(self):
        set_ambient_light(primary=[131,160,209])
        set_directional_light(diffuseColor=[134,160,143], specularColor=[130,130,130])
        set_effect(triggerIds=[6000,6299], visible=False)
        set_effect(triggerIds=[6101,6102,6103,6104,6105,6106,6107,6108,6109], visible=False)
        set_effect(triggerIds=[6201,6202,6203,6204], visible=False)
        set_actor(triggerId=201, visible=True, initialSequence='sf_quest_light_A01_Off')
        set_actor(triggerId=202, visible=True, initialSequence='sf_quest_light_A01_Off')
        set_actor(triggerId=203, visible=True, initialSequence='sf_quest_light_A01_Off')
        set_actor(triggerId=204, visible=True, initialSequence='sf_quest_light_A01_Off')
        set_actor(triggerId=205, visible=True, initialSequence='sf_quest_light_A01_Off')
        set_actor(triggerId=206, visible=True, initialSequence='sf_quest_light_A01_Off')
        set_actor(triggerId=207, visible=True, initialSequence='sf_quest_light_A01_Off')
        set_actor(triggerId=208, visible=True, initialSequence='sf_quest_light_A01_Off')
        set_actor(triggerId=209, visible=True, initialSequence='sf_quest_light_A01_Off')
        set_actor(triggerId=210, visible=True, initialSequence='sf_quest_light_A01_Off')
        set_actor(triggerId=211, visible=True, initialSequence='sf_quest_light_A01_Off')
        set_actor(triggerId=212, visible=True, initialSequence='sf_quest_light_A01_Off')
        set_actor(triggerId=213, visible=True, initialSequence='sf_quest_light_A01_Off')
        set_actor(triggerId=214, visible=True, initialSequence='sf_quest_light_A01_Off')

    def on_tick(self) -> state.State:
        if user_value(key='AllertStart', value=1):
            return 이펙트시퀀스01()


class 이펙트시퀀스01(state.State):
    def on_enter(self):
        set_skill(triggerIds=[701], isEnable=True)
        set_skill(triggerIds=[704], isEnable=True)
        set_effect(triggerIds=[6101,6104], visible=True)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=1500):
            return 이펙트시퀀스02()


class 이펙트시퀀스02(state.State):
    def on_enter(self):
        set_skill(triggerIds=[707], isEnable=True)
        set_skill(triggerIds=[708], isEnable=True)
        set_effect(triggerIds=[6107,6108], visible=True)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=1500):
            return 이펙트시퀀스03()


class 이펙트시퀀스03(state.State):
    def on_enter(self):
        set_ambient_light(primary=[232,92,53])
        set_directional_light(diffuseColor=[41,21,18], specularColor=[130,130,130])
        set_skill(triggerIds=[702], isEnable=True)
        set_skill(triggerIds=[706], isEnable=True)
        set_effect(triggerIds=[6102,6106], visible=True)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=1500):
            return 경보()


class 경보(state.State):
    def on_enter(self):
        set_skill(triggerIds=[709], isEnable=True)
        set_effect(triggerIds=[6109], visible=True)
        side_npc_talk(npcId=11003536, illust='Neirin_normal', duration=8000, script='$52010038_QD__allert__0$', voice='ko/Npc/00002104')
        set_effect(triggerIds=[6000], visible=True)
        set_actor(triggerId=201, visible=True, initialSequence='sf_quest_light_A01_On')
        set_actor(triggerId=202, visible=True, initialSequence='sf_quest_light_A01_On')
        set_actor(triggerId=203, visible=True, initialSequence='sf_quest_light_A01_On')
        set_actor(triggerId=204, visible=True, initialSequence='sf_quest_light_A01_On')
        set_actor(triggerId=205, visible=True, initialSequence='sf_quest_light_A01_On')
        set_actor(triggerId=206, visible=True, initialSequence='sf_quest_light_A01_On')
        set_actor(triggerId=207, visible=True, initialSequence='sf_quest_light_A01_On')
        set_actor(triggerId=208, visible=True, initialSequence='sf_quest_light_A01_On')
        set_actor(triggerId=209, visible=True, initialSequence='sf_quest_light_A01_On')
        set_actor(triggerId=210, visible=True, initialSequence='sf_quest_light_A01_On')
        set_actor(triggerId=211, visible=True, initialSequence='sf_quest_light_A01_On')
        set_actor(triggerId=212, visible=True, initialSequence='sf_quest_light_A01_On')
        set_actor(triggerId=213, visible=True, initialSequence='sf_quest_light_A01_On')
        set_actor(triggerId=214, visible=True, initialSequence='sf_quest_light_A01_On')

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=4202):
            return 이펙트시퀀스04()


class 이펙트시퀀스04(state.State):
    def on_enter(self):
        set_skill(triggerIds=[703], isEnable=True)
        set_skill(triggerIds=[705], isEnable=True)
        set_effect(triggerIds=[6103,6105], visible=True)

    def on_tick(self) -> state.State:
        if user_value(key='AllertEnd', value=1):
            set_user_value(triggerId=999004, key='AllertStart', value=0)
            return 대기()


