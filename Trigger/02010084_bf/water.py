""" trigger/02010084_bf/water.xml """
from common import *
import state


class 대기(state.State):
    def on_enter(self):
        set_mesh(triggerIds=[3001,3002,3003,3004,3005,3006,3007,3008,3009,3010,3011,3012,3013,3014,3015,3016,3017,3018,3019,3020,3021,3022,3023,3024,3025,3026,3027,3028,3029,3030,3031,3032,3033,3034,3035,3036,3037,3038,3039,3040,3041,3042,3043,3044,3045,3046,3047,3048,3049,3050,3051,3052,3053,3054,3055,3056,3057,3058,3059,3060,3061,3062,3063], visible=True, arg3=0, arg4=30, arg5=2)
        set_interact_object(triggerIds=[10000830], state=1)

    def on_tick(self) -> state.State:
        if object_interacted(interactIds=[10000830], arg2=0):
            return 부서짐()


class 부서짐(state.State):
    def on_enter(self):
        set_mesh(triggerIds=[3001,3002,3003,3004,3005,3006,3007,3008,3009,3010,3011,3012,3013,3014,3015,3016,3017,3018,3019,3020,3021,3022,3023,3024,3025,3026,3027,3028,3029,3030,3031,3032,3033,3034,3035,3036,3037,3038,3039,3040,3041,3042,3043,3044,3045,3046,3047,3048,3049,3050,3051,3052,3053,3054,3055,3056,3057,3058,3059,3060,3061,3062,3063], visible=False, arg3=0, arg4=30, arg5=2)
        set_timer(timerId='25', seconds=25)

    def on_tick(self) -> state.State:
        if time_expired(timerId='25'):
            return 대기()


