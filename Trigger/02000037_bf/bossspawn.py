""" trigger/02000037_bf/bossspawn.xml """
from common import *
import state


class 시작대기중(state.State):
    def on_enter(self):
        set_interact_object(triggerIds=[10000931], state=2)
        set_mesh(triggerIds=[4000,4001,4002,4003,4004,4005,4006,4007,4008,4009], visible=False, arg3=0, arg4=0, arg5=0) # Stairs 10
        set_mesh(triggerIds=[4020,4021,4022,4023,4024,4025,4026,4027,4028,4029,4030,4031,4032,4033,4034], visible=False, arg3=0, arg4=0, arg5=0) # Bridge 15
        set_mesh(triggerIds=[4040,4041,4042,4043,4044,4045,4046], visible=False, arg3=0, arg4=0, arg5=0) # Slab 7
        set_mesh(triggerIds=[4050], visible=True, arg3=0, arg4=0, arg5=0) # invisible barrier
        set_portal(portalId=2, visible=False, enabled=False, minimapVisible=False)
        set_effect(triggerIds=[5000], visible=False) # StairsAppear
        set_effect(triggerIds=[5001], visible=False) # Vibrate

    def on_tick(self) -> state.State:
        if user_detected(boxIds=[101]):
            return 난이도체크()


class 난이도체크(state.State):
    def on_tick(self) -> state.State:
        if dungeon_level(level=2):
            return 레이드()
        if dungeon_level(level=3):
            return 카오스레이드()


class 레이드(state.State):
    def on_enter(self):
        create_monster(spawnIds=[2000], arg2=False)

    def on_tick(self) -> state.State:
        if monster_dead(boxIds=[2000]):
            return 연출딜레이()


class 카오스레이드(state.State):
    def on_enter(self):
        create_monster(spawnIds=[2001], arg2=False)

    def on_tick(self) -> state.State:
        if monster_dead(boxIds=[2001]):
            return 연출딜레이()


class 연출딜레이(state.State):
    def on_tick(self) -> state.State:
        if wait_tick(waitTick=2000):
            return 연출종료()


class 연출종료(state.State):
    def on_enter(self):
        set_interact_object(triggerIds=[10000931], state=1)
        set_portal(portalId=2, visible=True, enabled=True, minimapVisible=True)
        dungeon_clear()

    def on_tick(self) -> state.State:
        if object_interacted(interactIds=[10000931]):
            return 사념등장01()


class 사념등장01(state.State):
    def on_enter(self):
        set_mesh(triggerIds=[4050], visible=False, arg3=0, arg4=0, arg5=0) # invisible barrier
        set_effect(triggerIds=[5000], visible=True) # StairsAppear
        set_effect(triggerIds=[5001], visible=True) # Vibrate
        set_random_mesh(triggerIds=[4000,4001,4002,4003,4004,4005,4006,4007,4008,4009], visible=True, meshCount=10, arg4=0, delay=50)
        set_random_mesh(triggerIds=[4040,4041,4042,4043,4044,4045,4046], visible=True, meshCount=7, arg4=400, delay=50)
        set_random_mesh(triggerIds=[4020,4021,4022,4023,4024,4025,4026,4027,4028,4029,4030,4031,4032,4033,4034], visible=True, meshCount=15, arg4=800, delay=50)


