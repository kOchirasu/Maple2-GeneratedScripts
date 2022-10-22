""" trigger/52000014_qd/collapse_2800.xml """
from common import *
import state


class 대기(state.State):
    def on_enter(self):
        set_mesh(triggerIds=[2800,2801,2802,2803], visible=True, arg3=0, arg4=0, arg5=0) # 첫 번째, 위, 4
        set_mesh(triggerIds=[2810,2811,2812,2813,2814,2815], visible=True, arg3=0, arg4=0, arg5=0) # 두 번째, 위, 6
        set_mesh(triggerIds=[2820,2821,2822,2823,2824], visible=True, arg3=0, arg4=0, arg5=0) # 세 번째, 위, 5
        set_mesh(triggerIds=[2830,2831,2832,2833], visible=True, arg3=0, arg4=0, arg5=0) # 네 번째, 위, 4
        set_mesh(triggerIds=[2840,2841,2842,2843], visible=True, arg3=0, arg4=0, arg5=0) # 다섯 번째, 위, 4
        set_mesh(triggerIds=[2850,2851,2852,2853,2854,2855], visible=True, arg3=0, arg4=0, arg5=0) # 첫 번째, 아래, 6
        set_mesh(triggerIds=[2860,2861,2862,2863], visible=True, arg3=0, arg4=0, arg5=0) # 두 번째, 아래, 4
        set_mesh(triggerIds=[2870,2871,2872,2873,2874], visible=True, arg3=0, arg4=0, arg5=0) # 세 번째, 아래, 5
        set_mesh(triggerIds=[2880,2881,2882,2883], visible=True, arg3=0, arg4=0, arg5=0) # 네 번째, 아래, 4
        set_mesh(triggerIds=[2890,2891,2892,2893], visible=True, arg3=0, arg4=0, arg5=0) # 다섯 번째, 아래, 4
        set_effect(triggerIds=[12800], visible=False) # Vibrate Short
        set_effect(triggerIds=[22800], visible=False) # Vibrate Sound
        set_effect(triggerIds=[12810], visible=False) # Vibrate Short
        set_effect(triggerIds=[22810], visible=False) # Vibrate Sound
        set_effect(triggerIds=[12820], visible=False) # Vibrate Short
        set_effect(triggerIds=[22820], visible=False) # Vibrate Sound
        set_effect(triggerIds=[12830], visible=False) # Vibrate Short
        set_effect(triggerIds=[22830], visible=False) # Vibrate Sound
        set_effect(triggerIds=[12840], visible=False) # Vibrate Short
        set_effect(triggerIds=[22840], visible=False) # Vibrate Sound
        set_effect(triggerIds=[12850], visible=False) # Vibrate Short
        set_effect(triggerIds=[22850], visible=False) # Vibrate Sound

    def on_tick(self) -> state.State:
        if user_detected(boxIds=[92800]):
            return 무너짐경고01()


class 무너짐경고01(state.State):
    def on_enter(self):
        set_event_ui(type=1, arg2='$52000014_QD__COLLAPSE_2800__0$', arg3='4000', arg4='0')
        set_effect(triggerIds=[12800], visible=True) # Vibrate Short
        set_effect(triggerIds=[22800], visible=True) # Vibrate Sound
        set_random_mesh(triggerIds=[2850,2851,2852,2853,2854,2855], visible=False, meshCount=6, arg4=0, delay=300) # 첫 번째, 아래, 6

    def on_tick(self) -> state.State:
        if user_detected(boxIds=[92801]):
            return 무너짐경고02()


class 무너짐경고02(state.State):
    def on_enter(self):
        set_effect(triggerIds=[12810], visible=True) # Vibrate Short
        set_effect(triggerIds=[22810], visible=True) # Vibrate Sound
        set_random_mesh(triggerIds=[2860,2861,2862,2863], visible=False, meshCount=4, arg4=0, delay=200) # 두 번째, 아래, 4
        set_random_mesh(triggerIds=[2800,2801,2802,2803], visible=False, meshCount=4, arg4=300, delay=400) # 첫 번째, 위, 4

    def on_tick(self) -> state.State:
        if user_detected(boxIds=[92802]):
            return 무너짐경고03()


class 무너짐경고03(state.State):
    def on_enter(self):
        set_effect(triggerIds=[12820], visible=True) # Vibrate Short
        set_effect(triggerIds=[22820], visible=True) # Vibrate Sound
        set_random_mesh(triggerIds=[2870,2871,2872,2873,2874], visible=False, meshCount=5, arg4=0, delay=250) # 세 번째, 아래, 5
        set_random_mesh(triggerIds=[2810,2811,2812,2813,2814,2815], visible=False, meshCount=6, arg4=300, delay=200) # 두 번째, 위, 6

    def on_tick(self) -> state.State:
        if user_detected(boxIds=[92803]):
            return 무너짐경고04()


class 무너짐경고04(state.State):
    def on_enter(self):
        set_effect(triggerIds=[12830], visible=True) # Vibrate Short
        set_effect(triggerIds=[22830], visible=True) # Vibrate Sound
        set_random_mesh(triggerIds=[2880,2881,2882,2883], visible=False, meshCount=4, arg4=0, delay=300) # 네 번째, 아래, 4
        set_random_mesh(triggerIds=[2820,2821,2822,2823,2824], visible=False, meshCount=5, arg4=200, delay=300) # 세 번째, 위, 5

    def on_tick(self) -> state.State:
        if user_detected(boxIds=[92804]):
            return 무너짐경고05()


class 무너짐경고05(state.State):
    def on_enter(self):
        set_effect(triggerIds=[12840], visible=True) # Vibrate Short
        set_effect(triggerIds=[22840], visible=True) # Vibrate Sound
        set_random_mesh(triggerIds=[2890,2891,2892,2893], visible=False, meshCount=4, arg4=0, delay=200) # 다섯 번째, 아래, 4
        set_random_mesh(triggerIds=[2830,2831,2832,2833], visible=False, meshCount=4, arg4=300, delay=200) # 네 번째, 위, 4

    def on_tick(self) -> state.State:
        if user_detected(boxIds=[9003]):
            return 무너짐경고06()


class 무너짐경고06(state.State):
    def on_enter(self):
        set_timer(timerId='10', seconds=10)
        set_effect(triggerIds=[12850], visible=True) # Vibrate Short
        set_effect(triggerIds=[22850], visible=True) # Vibrate Sound
        set_random_mesh(triggerIds=[2840,2841,2842,2843], visible=False, meshCount=4, arg4=100, delay=150) # 다섯 번째, 위, 4

    def on_tick(self) -> state.State:
        if time_expired(timerId='10'):
            return 종료()


class 종료(state.State):
    def on_enter(self):
        set_effect(triggerIds=[12800], visible=False) # Vibrate Short
        set_effect(triggerIds=[22800], visible=False) # Vibrate Sound
        set_effect(triggerIds=[12810], visible=False) # Vibrate Short
        set_effect(triggerIds=[22810], visible=False) # Vibrate Sound
        set_effect(triggerIds=[12820], visible=False) # Vibrate Short
        set_effect(triggerIds=[22820], visible=False) # Vibrate Sound
        set_effect(triggerIds=[12830], visible=False) # Vibrate Short
        set_effect(triggerIds=[22830], visible=False) # Vibrate Sound
        set_effect(triggerIds=[12840], visible=False) # Vibrate Short
        set_effect(triggerIds=[22840], visible=False) # Vibrate Sound
        set_effect(triggerIds=[12850], visible=False) # Vibrate Short
        set_effect(triggerIds=[22850], visible=False) # Vibrate Sound


