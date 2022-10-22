""" trigger/02000471_bf/move.xml """
from common import *
import state


class 시작(state.State):
    def on_enter(self):
        create_item(spawnIds=[9001,9002,9003,9004,9005,9006,9007,9008,9009,9010,9011,9012,9013,9014,9015,9016,9017,9018,9019,9020,9021,9022,9023,9024,9025,9026,9027,9028,9029,9030])
        set_mesh(triggerIds=[3001,3002,3003,3004,3005,3006,3007,3008,3009,3010,3011,3012,3013,3014,3015,3016,3017,3018,3019,3020,3021,3022,3023,3024,3025,3026,3027,3028,3029,3030,3031,3032,3033,3034,3035,3036,3037,3038,3039,3040,3041,3042,3043,3044,3045,3046,3047,3048,3049,3050,3051,3052,3053,3054,3055,3056,3057,3058,3059,3060,3061,3062,3063,3064,3065,3066,3067,3068,3069,3070,3071,3072,3073,3074,3075,3076,3077,3078,3079,3080,3081,3082,3083,3084,3085,3086,3087,3088,3089,3090,3091,3092,3093,3094,3095,3096,3097,3098,3099,3100], visible=False, arg3=0, arg4=0, arg5=0)
        set_interact_object(triggerIds=[11000001], state=1)
        set_timer(timerId='60', seconds=60, clearAtZero=False, display=True)

    def on_tick(self) -> state.State:
        if user_detected(boxIds=[102]):
            return 보물상자()


class 보물상자(state.State):
    def on_enter(self):
        set_interact_object(triggerIds=[11000001], state=1)

    def on_tick(self) -> state.State:
        if user_detected(boxIds=[105]):
            return 랜덤블록1()


class 랜덤블록1(state.State):
    def on_enter(self):
        set_random_mesh(triggerIds=[3047,3048,3049,3050,3051,3052,3053,3054], visible=True, meshCount=4, arg4=0, delay=1)

    def on_tick(self) -> state.State:
        if user_detected(boxIds=[106]):
            return 랜덤블록2()


class 랜덤블록2(state.State):
    def on_enter(self):
        set_random_mesh(triggerIds=[3055,3056,3057,3058,3059,3060,3061,3062,3063], visible=True, meshCount=4, arg4=0, delay=1)

    def on_tick(self) -> state.State:
        if user_detected(boxIds=[107]):
            return 랜덤블록3()


class 랜덤블록3(state.State):
    def on_enter(self):
        set_random_mesh(triggerIds=[3064,3065,3066,3067,3068,3069,3070,3071,3072], visible=True, meshCount=4, arg4=0, delay=1)

    def on_tick(self) -> state.State:
        if user_detected(boxIds=[108]):
            return 랜덤블록4()


class 랜덤블록4(state.State):
    def on_enter(self):
        set_random_mesh(triggerIds=[3073,3074,3075,3076,3077,3078,3079,3080], visible=True, meshCount=4, arg4=0, delay=1)

    def on_tick(self) -> state.State:
        if user_detected(boxIds=[109]):
            return 랜덤블록5()


class 랜덤블록5(state.State):
    def on_enter(self):
        set_random_mesh(triggerIds=[3080,3081,3082,3083,3084,3085], visible=True, meshCount=4, arg4=0, delay=1)

    def on_tick(self) -> state.State:
        if user_detected(boxIds=[110]):
            return None # Missing State: 랜덤블록6


