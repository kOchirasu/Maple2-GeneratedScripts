""" trigger/02000369_bf/main.xml """
from common import *
import state


class 대기(state.State):
    def on_enter(self):
        set_effect(triggerIds=[6001], visible=False)
        set_effect(triggerIds=[6002], visible=True)
        set_effect(triggerIds=[6003], visible=True)
        set_effect(triggerIds=[6004], visible=True)
        set_effect(triggerIds=[6005], visible=True)
        set_effect(triggerIds=[6006], visible=True)
        set_effect(triggerIds=[6007], visible=True)
        set_effect(triggerIds=[6008], visible=True)
        set_effect(triggerIds=[6009], visible=True)
        set_effect(triggerIds=[6010], visible=True)
        set_skill(triggerIds=[7001], isEnable=False)
        set_skill(triggerIds=[7002], isEnable=False)
        set_skill(triggerIds=[7003], isEnable=False)
        set_mesh(triggerIds=[3001,3002,3003,3004,3005,3006,3007,3008,3009,3010,3011,3012,3013,3014,3015,3016,3017,3018,3019,3020,3021,3022,3023,3024,3025,3026,3027,3028,3029,3030,3031,3032,3033,3034,3035,3036,3037,3038,3039,3040,3041,3042,3043,3044,3045,3046,3047,3048,3049,3050,3051,3052,3053,3054,3055,3056], visible=False, arg3=0, arg4=0, arg5=0)
        set_mesh(triggerIds=[3060,3061,3062,3063,3064,3065,3066,3067], visible=True, arg3=0, arg4=0, arg5=0)
        set_mesh(triggerIds=[3070,3071], visible=True, arg3=0, arg4=0, arg5=0)
        set_ladder(triggerIds=[3101], visible=True, animationEffect=True, animationDelay=0)
        set_ladder(triggerIds=[3102], visible=True, animationEffect=True, animationDelay=0)
        set_ladder(triggerIds=[3103], visible=True, animationEffect=True, animationDelay=0)
        set_ladder(triggerIds=[3104], visible=True, animationEffect=True, animationDelay=0)
        set_ladder(triggerIds=[3105], visible=True, animationEffect=True, animationDelay=0)
        set_ladder(triggerIds=[3106], visible=True, animationEffect=True, animationDelay=0)
        set_ladder(triggerIds=[3107], visible=True, animationEffect=True, animationDelay=0)
        set_ladder(triggerIds=[3108], visible=True, animationEffect=True, animationDelay=0)
        set_ladder(triggerIds=[3109], visible=True, animationEffect=True, animationDelay=0)
        set_ladder(triggerIds=[3110], visible=True, animationEffect=True, animationDelay=0)
        set_ladder(triggerIds=[3111], visible=True, animationEffect=True, animationDelay=0)
        set_ladder(triggerIds=[3112], visible=True, animationEffect=True, animationDelay=0)
        set_interact_object(triggerIds=[10000978], state=2)
        set_interact_object(triggerIds=[10000979], state=2)
        set_interact_object(triggerIds=[10000980], state=2)
        set_interact_object(triggerIds=[10000981], state=2)
        set_interact_object(triggerIds=[10000982], state=2)
        set_portal(portalId=32, visible=False, enabled=False, minimapVisible=False)

    def on_tick(self) -> state.State:
        if user_detected(boxIds=[1001]):
            return 연출시작()


class 연출시작(state.State):
    def on_enter(self):
        create_monster(spawnIds=[101,102,103,111,112,113,114,115,116,117,118,119,121,122,123,124,125,126,127,128,129], arg2=False)
        create_widget(type='SceneMovie')
        widget_action(type='SceneMovie', func='Clear')
        play_scene_movie(fileName='Nutaman_intro.swf', movieId=1)
        set_cinematic_ui(type=1)
        set_cinematic_ui(type=3)

    def on_tick(self) -> state.State:
        if widget_condition(type='SceneMovie', name='IsStop', condition='1'):
            return 전투01()

    def on_exit(self):
        set_cinematic_ui(type=0)
        set_cinematic_ui(type=2)


class 전투01(state.State):
    def on_tick(self) -> state.State:
        if monster_dead(boxIds=[101,102,103,111,112,113,114,115,116,117,118,119,121,122,123,124,125,126,127,128,129]):
            return 전투02()


class 전투02(state.State):
    def on_enter(self):
        set_interact_object(triggerIds=[10000978], state=1)
        set_interact_object(triggerIds=[10000979], state=1)
        set_interact_object(triggerIds=[10000980], state=1)
        create_monster(spawnIds=[201,202,203,204,205,211,212,213,214,215,216,217,218,221,222,223,224,225,226,227,228], arg2=False)

    def on_tick(self) -> state.State:
        if monster_dead(boxIds=[201,202,203,204,205,211,212,213,214,215,216,217,218,221,222,223,224,225,226,227,228]):
            return 전투03()


class 전투03(state.State):
    def on_enter(self):
        set_interact_object(triggerIds=[10000981], state=1)
        set_interact_object(triggerIds=[10000982], state=1)
        create_monster(spawnIds=[301,302,303], arg2=False)

    def on_tick(self) -> state.State:
        if monster_dead(boxIds=[301,302,303]):
            set_mesh(triggerIds=[3060,3061,3062,3063,3064,3065,3066,3067], visible=False, arg3=0, arg4=0, arg5=0)
            set_mesh(triggerIds=[3001,3002,3003,3004,3005,3006,3007,3008,3009,3010,3011,3012,3013,3014,3015,3016,3017,3018,3019,3020,3021,3022,3023,3024,3025,3026,3027,3028,3029,3030,3031,3032,3033,3034,3035,3036,3037,3038,3039,3040,3041,3042,3043,3044,3045,3046,3047,3048,3049,3050,3051,3052,3053,3054,3055,3056], visible=True, arg3=0, arg4=50, arg5=1)
            return 전투04()


class 전투04(state.State):
    def on_enter(self):
        create_monster(spawnIds=[411,412,413,414,421,422,423,424], arg2=False)

    def on_tick(self) -> state.State:
        if monster_dead(boxIds=[411,412,413,414,421,422,423,424]):
            return 포털개방()


class 포털개방(state.State):
    def on_enter(self):
        set_effect(triggerIds=[6002], visible=False)
        set_effect(triggerIds=[6003], visible=False)
        set_effect(triggerIds=[6004], visible=False)
        set_effect(triggerIds=[6005], visible=False)
        set_effect(triggerIds=[6006], visible=False)
        set_effect(triggerIds=[6007], visible=False)
        set_effect(triggerIds=[6008], visible=False)
        set_effect(triggerIds=[6009], visible=False)
        set_effect(triggerIds=[6010], visible=False)
        set_mesh(triggerIds=[3070,3071], visible=False, arg3=0, arg4=0, arg5=0)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=1000):
            return 종료()


class 종료(state.State):
    pass


