""" trigger/02000492_bf/main.xml """
from common import *
import state


class 대기(state.State):
    def on_enter(self):
        set_mesh(triggerIds=[3100], visible=True, arg3=0, arg4=0, arg5=0)
        set_mesh(triggerIds=[3101,3102,3103,3104,3105,3106,3107,3108,3109,3110,3111,3112,3113,3114,3115,3116,3117,3118,3119,3120,3121,3122,3123,3124,3125,3126,3127,3128,3129,3130,3131,3132,3133,3134,3135,3136,3137,3138,3139,3140,3141,3142,3143,3144,3145,3146,3147], visible=False, arg3=0, arg4=0, arg5=0)
        set_interact_object(triggerIds=[10000999], state=0)
        set_portal(portalId=10, visible=False, enabled=False, minimapVisible=False)
        set_portal(portalId=20, visible=False, enabled=False, minimapVisible=False)
        set_portal(portalId=30, visible=False, enabled=False, minimapVisible=False)
        set_portal(portalId=40, visible=False, enabled=False, minimapVisible=False)
        set_portal(portalId=50, visible=False, enabled=False, minimapVisible=False)
        set_portal(portalId=60, visible=False, enabled=False, minimapVisible=False)
        set_portal(portalId=70, visible=False, enabled=False, minimapVisible=False)
        set_portal(portalId=80, visible=False, enabled=False, minimapVisible=False)
        set_portal(portalId=100, visible=False, enabled=False, minimapVisible=False)

    def on_tick(self) -> state.State:
        if user_detected(boxIds=[1001]):
            return 전투감지()
        if user_detected(boxIds=[1002]):
            return 전투감지()


class 전투감지(state.State):
    def on_tick(self) -> state.State:
        if monster_dead(boxIds=[101,111,201,211,301,311,401,411]):
            return 전투감지2()


class 전투감지2(state.State):
    def on_tick(self) -> state.State:
        if monster_dead(boxIds=[102,202,302,402]):
            return 포털개방()


class 포털개방(state.State):
    def on_enter(self):
        set_interact_object(triggerIds=[10000999], state=1)
        set_portal(portalId=10, visible=True, enabled=True, minimapVisible=False)
        set_portal(portalId=20, visible=True, enabled=True, minimapVisible=False)
        set_portal(portalId=30, visible=True, enabled=True, minimapVisible=False)
        set_portal(portalId=70, visible=True, enabled=True, minimapVisible=False)
        set_portal(portalId=80, visible=True, enabled=True, minimapVisible=False)

    def on_tick(self) -> state.State:
        if object_interacted(interactIds=[10000999], arg2=0):
            return 다리생성()


class 다리생성(state.State):
    def on_enter(self):
        set_mesh(triggerIds=[3002,3003,3004,3005], visible=False, arg3=0, arg4=0, arg5=0)
        set_mesh(triggerIds=[3100], visible=False, arg3=0, arg4=0, arg5=0)
        set_mesh(triggerIds=[3101,3102,3103,3104,3105,3106,3107,3108,3109,3110,3111,3112,3113,3114,3115,3116,3117,3118,3119,3120,3121,3122,3123,3124,3125,3126,3127,3128,3129,3130,3131,3132,3133,3134,3135,3136,3137,3138,3139,3140,3141,3142,3143,3144,3145,3146,3147], visible=True, arg3=0, arg4=10, arg5=0)
        set_portal(portalId=100, visible=True, enabled=True, minimapVisible=False)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=1000):
            return 종료()


class 종료(state.State):
    pass


