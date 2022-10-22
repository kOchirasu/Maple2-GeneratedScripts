""" trigger/02000367_bf/main.xml """
from common import *
import state


class 대기(state.State):
    def on_enter(self):
        set_mesh(triggerIds=[3000], visible=True, arg3=0, arg4=0, arg5=0)
        set_mesh(triggerIds=[3101,3102,3103,3104,3105,3106], visible=True, arg3=0, arg4=0, arg5=0)
        set_mesh(triggerIds=[3113,3114], visible=True, arg3=0, arg4=0, arg5=0)
        set_portal(portalId=11, visible=False, enabled=False, minimapVisible=False)
        set_portal(portalId=22, visible=False, enabled=False, minimapVisible=False)
        set_portal(portalId=33, visible=False, enabled=False, minimapVisible=False)
        set_portal(portalId=44, visible=False, enabled=False, minimapVisible=False)
        set_interact_object(triggerIds=[10000983], state=2)
        set_interact_object(triggerIds=[10000984], state=2)
        set_interact_object(triggerIds=[10000985], state=2)
        set_interact_object(triggerIds=[10000986], state=2)
        set_interact_object(triggerIds=[10000987], state=2)
        set_interact_object(triggerIds=[10000988], state=2)
        set_interact_object(triggerIds=[10000995], state=2)
        set_interact_object(triggerIds=[10000996], state=2)

    def on_tick(self) -> state.State:
        if user_detected(boxIds=[1001]):
            return 전투01()


class 전투01(state.State):
    def on_enter(self):
        create_monster(spawnIds=[11101,11102,11103,11104,11105,11106,11107,11201,11202,11203,11204,11205], arg2=False)

    def on_tick(self) -> state.State:
        if monster_dead(boxIds=[11101,11102,11103,11104,11105,11106,11107,11201,11202,11203,11204,11205]):
            return 전투02()


class 전투02(state.State):
    def on_enter(self):
        set_mesh(triggerIds=[3101,3102], visible=False, arg3=0, arg4=0, arg5=0)
        set_interact_object(triggerIds=[10000983], state=1)
        set_interact_object(triggerIds=[10000984], state=1)
        create_monster(spawnIds=[12101,12102,12201,12202,12203,12204,12205,12206,12207], arg2=False)

    def on_tick(self) -> state.State:
        if monster_dead(boxIds=[12101,12102,12201,12202,12203,12204,12205,12206,12207]):
            return 전투03()


class 전투03(state.State):
    def on_enter(self):
        set_mesh(triggerIds=[3103,3104], visible=False, arg3=0, arg4=0, arg5=0)
        set_interact_object(triggerIds=[10000985], state=1)
        set_interact_object(triggerIds=[10000986], state=1)
        create_monster(spawnIds=[13101,13102,13103,13104,13105,13106,13107,13108,13109,13201,13202,13203,13204], arg2=False)

    def on_tick(self) -> state.State:
        if monster_dead(boxIds=[13101,13102,13103,13104,13105,13106,13107,13108,13109,13201,13202,13203,13204]):
            set_mesh(triggerIds=[3105,3106], visible=False, arg3=0, arg4=0, arg5=0)
            set_interact_object(triggerIds=[10000987], state=1)
            set_interact_object(triggerIds=[10000988], state=1)
            return 합류대기()


class 합류대기(state.State):
    def on_tick(self) -> state.State:
        if user_value(key='main', value=1):
            return 전투04()


class 전투04(state.State):
    def on_enter(self):
        create_monster(spawnIds=[30001,30002,30003,30004], arg2=False)

    def on_tick(self) -> state.State:
        if monster_dead(boxIds=[30001,30002,30003,30004]):
            return 포털개방()


class 포털개방(state.State):
    def on_enter(self):
        set_portal(portalId=11, visible=True, enabled=True, minimapVisible=False)
        set_portal(portalId=22, visible=True, enabled=True, minimapVisible=False)
        set_portal(portalId=33, visible=True, enabled=True, minimapVisible=False)
        set_portal(portalId=44, visible=True, enabled=True, minimapVisible=False)
        create_monster(spawnIds=[41101,41102,41103,41104,41105,41106,41201,41202,41203,41204], arg2=False)
        set_user_value(triggerId=9999900, key='main2', value=1)

    def on_tick(self) -> state.State:
        if monster_dead(boxIds=[41101,41102,41103,41104,41105,41106,41201,41202,41203,41204]):
            set_mesh(triggerIds=[3113,3114], visible=False, arg3=0, arg4=0, arg5=0)
            set_interact_object(triggerIds=[10000995], state=1)
            set_interact_object(triggerIds=[10000996], state=1)
            return 종료()


class 종료(state.State):
    pass


