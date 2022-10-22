""" trigger/02010060_bf/bridge.xml """
from common import *
import state


class NPC감지대기(state.State):
    def on_enter(self):
        set_skill(triggerIds=[701], isEnable=False)
        set_effect(triggerIds=[610], visible=False)
        set_mesh(triggerIds=[3001,3002,3003,3004,3005,3006,3007,3008,3009,3010,3011,3012,3013,3014,3015,3016,3017,3018,3019,3020,3021,3022,3023,3024,3025,3026,3027,3028,3029,3030,3031,3032,3033,3034,3035,3036,3037,3038,3039,3040,3041,3042,3043,3044,3045,3046,3047,3048,3049,3050,3051,3052,3053,3054,3055,3056,3057,3058,3059,3060,3061,3062,3063,3064,3065,3066,3067,3068,3069,3070,3071,3072,3073,3074,3075,3076,3077,3078], visible=False, arg3=0, arg4=0, arg5=0)
        set_mesh(triggerIds=[3101,3102,3103,3104,3105,3106,3107,3108,3109,3110,3111,3112,3113,3114,3115,3116,3117,3118,3119,3120,3121,3122,3123,3124,3125,3126,3127,3128,3129,3130], visible=False, arg3=0, arg4=0, arg5=0)
        set_interact_object(triggerIds=[10000918], state=2)

    def on_tick(self) -> state.State:
        if npc_detected(boxId=102, spawnIds=[2099]):
            return 오브젝트반응대기()
        if user_value(key='FirstPhaseEnd', value=1):
            return 오브젝트반응대기()


class 오브젝트반응대기(state.State):
    def on_enter(self):
        set_skill(triggerIds=[701], isEnable=True)
        set_interact_object(triggerIds=[10000918], state=1)

    def on_tick(self) -> state.State:
        if object_interacted(interactIds=[10000918], arg2=0):
            return 다리생성()


class 다리생성(state.State):
    def on_enter(self):
        set_achievement(triggerId=100, type='trigger', achieve='TruthOfKargon')
        set_effect(triggerIds=[610], visible=True)
        set_mesh(triggerIds=[3001,3002,3003,3004,3005,3006,3007,3008,3009,3010,3011,3012,3013,3014,3015,3016,3017,3018,3019,3020,3021,3022,3023,3024,3025,3026,3027,3028,3029,3030,3031,3032,3033,3034,3035,3036,3037,3038,3039,3040,3041,3042,3043,3044,3045,3046,3047,3048,3049,3050,3051,3052,3053,3054,3055,3056,3057,3058,3059,3060,3061,3062,3063,3064,3065,3066,3067,3068,3069,3070,3071,3072,3073,3074,3075,3076,3077,3078], visible=True, arg3=0, arg4=50, arg5=2)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=1500):
            return 이펙트생성()


class 이펙트생성(state.State):
    def on_enter(self):
        set_mesh(triggerIds=[3101,3102,3103,3104,3105,3106,3107,3108,3109,3110,3111,3112,3113,3114,3115,3116,3117,3118,3119,3120,3121,3122,3123,3124,3125,3126,3127,3128,3129,3130], visible=True, arg3=0, arg4=100, arg5=2)


