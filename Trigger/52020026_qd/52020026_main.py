""" trigger/52020026_qd/52020026_main.xml """
from common import *
import state


class 감지(state.State):
    def on_enter(self):
        set_portal(portalId=1, visible=False, enabled=False)
        set_portal(portalId=2, visible=False, enabled=False)
        set_mesh(triggerIds=[1001,1002,1003,1004,1005,1006,1007,1008,1009,1010,1011,1012,1013,1014,1015,1016,1017,1018], visible=False)
        set_agent(triggerIds=[9001], visible=True)
        set_agent(triggerIds=[9002], visible=True)
        set_agent(triggerIds=[9003], visible=True)
        set_agent(triggerIds=[9004], visible=True)
        set_agent(triggerIds=[9005], visible=True)
        set_agent(triggerIds=[9006], visible=True)
        set_agent(triggerIds=[9007], visible=True)
        set_agent(triggerIds=[9008], visible=True)
        set_agent(triggerIds=[9009], visible=True)
        set_agent(triggerIds=[9010], visible=True)
        set_agent(triggerIds=[9011], visible=True)
        set_agent(triggerIds=[9012], visible=True)
        set_agent(triggerIds=[9013], visible=True)
        set_agent(triggerIds=[9014], visible=True)
        set_agent(triggerIds=[9015], visible=True)
        set_agent(triggerIds=[9016], visible=True)
        set_agent(triggerIds=[9017], visible=True)
        set_agent(triggerIds=[9018], visible=True)
        set_agent(triggerIds=[9019], visible=True)
        set_agent(triggerIds=[9020], visible=True)
        set_agent(triggerIds=[9021], visible=True)
        set_agent(triggerIds=[9022], visible=True)
        set_agent(triggerIds=[9023], visible=True)
        set_agent(triggerIds=[9024], visible=True)
        set_agent(triggerIds=[9025], visible=True)
        set_agent(triggerIds=[9026], visible=True)
        set_agent(triggerIds=[9027], visible=True)
        set_agent(triggerIds=[9028], visible=True)
        set_agent(triggerIds=[9029], visible=True)
        set_agent(triggerIds=[9030], visible=True)
        set_agent(triggerIds=[9031], visible=True)
        set_agent(triggerIds=[9032], visible=True)
        set_interact_object(triggerIds=[10001320], state=2)
        set_interact_object(triggerIds=[10001321], state=2)
        set_interact_object(triggerIds=[10001322], state=2)
        set_interact_object(triggerIds=[10001323], state=2)
        set_interact_object(triggerIds=[10001324], state=2)
        set_interact_object(triggerIds=[10001325], state=2)

    def on_tick(self) -> state.State:
        if user_detected(boxIds=[901]):
            return 대기()


class 대기(state.State):
    def on_enter(self):
        create_monster(spawnIds=[101], arg2=False)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=2000):
            return 층1()


class 층1(state.State):
    def on_tick(self) -> state.State:
        if monster_dead(boxIds=[101]):
            return 층레버활성1()


class 층레버활성1(state.State):
    def on_enter(self):
        set_event_ui(type=1, arg2='레버를 작동시켜 계단을 완성하세요.', arg3='5000')
        set_interact_object(triggerIds=[10001320], state=1)

    def on_tick(self) -> state.State:
        if object_interacted(interactIds=[10001320], arg2=0):
            return 층2()


class 층2(state.State):
    def on_enter(self):
        create_monster(spawnIds=[102], arg2=False)
        set_mesh(triggerIds=[1001,1002,1003], visible=True, arg3=0, arg4=500, arg5=3)

    def on_tick(self) -> state.State:
        if monster_dead(boxIds=[102]):
            return 층레버활성2()


class 층레버활성2(state.State):
    def on_enter(self):
        set_interact_object(triggerIds=[10001321], state=1)

    def on_tick(self) -> state.State:
        if object_interacted(interactIds=[10001321], arg2=0):
            return 층3()


class 층3(state.State):
    def on_enter(self):
        create_monster(spawnIds=[103], arg2=False)
        create_monster(spawnIds=[104], arg2=False)
        set_mesh(triggerIds=[1004,1005,1006], visible=True, arg3=0, arg4=500, arg5=3)

    def on_tick(self) -> state.State:
        if monster_dead(boxIds=[103,104]):
            return 층레버활성3()


class 층레버활성3(state.State):
    def on_enter(self):
        set_interact_object(triggerIds=[10001322], state=1)

    def on_tick(self) -> state.State:
        if object_interacted(interactIds=[10001322], arg2=0):
            return 층4()


class 층4(state.State):
    def on_enter(self):
        create_monster(spawnIds=[105], arg2=False)
        create_monster(spawnIds=[106], arg2=False)
        set_mesh(triggerIds=[1007,1008,1009], visible=True, arg3=0, arg4=500, arg5=3)

    def on_tick(self) -> state.State:
        if monster_dead(boxIds=[105,106]):
            return 층레버활성4()


class 층레버활성4(state.State):
    def on_enter(self):
        set_interact_object(triggerIds=[10001323], state=1)

    def on_tick(self) -> state.State:
        if object_interacted(interactIds=[10001323], arg2=0):
            return 층5()


class 층5(state.State):
    def on_enter(self):
        create_monster(spawnIds=[107], arg2=False)
        set_mesh(triggerIds=[1010,1011,1012], visible=True, arg3=0, arg4=500, arg5=3)

    def on_tick(self) -> state.State:
        if user_detected(boxIds=[906]):
            return 층_벽부수기5()


class 층_벽부수기5(state.State):
    def on_enter(self):
        set_agent(triggerIds=[9001], visible=False)
        set_agent(triggerIds=[9002], visible=False)
        set_agent(triggerIds=[9003], visible=False)
        set_agent(triggerIds=[9004], visible=False)
        set_agent(triggerIds=[9005], visible=False)
        set_agent(triggerIds=[9006], visible=False)
        set_agent(triggerIds=[9007], visible=False)
        set_agent(triggerIds=[9008], visible=False)
        set_agent(triggerIds=[9009], visible=False)
        set_agent(triggerIds=[9010], visible=False)
        set_agent(triggerIds=[9011], visible=False)
        set_agent(triggerIds=[9012], visible=False)
        set_agent(triggerIds=[9013], visible=False)
        set_agent(triggerIds=[9014], visible=False)
        set_agent(triggerIds=[9015], visible=False)
        set_agent(triggerIds=[9016], visible=False)
        create_monster(spawnIds=[108], arg2=True)
        set_skill(triggerIds=[1], isEnable=True)

    def on_tick(self) -> state.State:
        if monster_dead(boxIds=[107,108]):
            return 층레버활성5()


class 층레버활성5(state.State):
    def on_enter(self):
        set_interact_object(triggerIds=[10001324], state=1)

    def on_tick(self) -> state.State:
        if object_interacted(interactIds=[10001324], arg2=0):
            return 층6()


class 층6(state.State):
    def on_enter(self):
        create_monster(spawnIds=[109], arg2=False)
        create_monster(spawnIds=[110], arg2=False)
        set_mesh(triggerIds=[1013,1014,1015], visible=True, arg3=0, arg4=500, arg5=3)

    def on_tick(self) -> state.State:
        if user_detected(boxIds=[907]):
            return 층_벽부수기6()


class 층_벽부수기6(state.State):
    def on_enter(self):
        set_agent(triggerIds=[9017], visible=False)
        set_agent(triggerIds=[9018], visible=False)
        set_agent(triggerIds=[9019], visible=False)
        set_agent(triggerIds=[9020], visible=False)
        set_agent(triggerIds=[9021], visible=False)
        set_agent(triggerIds=[9022], visible=False)
        set_agent(triggerIds=[9023], visible=False)
        set_agent(triggerIds=[9024], visible=False)
        set_agent(triggerIds=[9025], visible=False)
        set_agent(triggerIds=[9026], visible=False)
        set_agent(triggerIds=[9027], visible=False)
        set_agent(triggerIds=[9028], visible=False)
        set_agent(triggerIds=[9029], visible=False)
        set_agent(triggerIds=[9030], visible=False)
        set_agent(triggerIds=[9031], visible=False)
        set_agent(triggerIds=[9032], visible=False)
        create_monster(spawnIds=[111], arg2=True)
        set_skill(triggerIds=[2], isEnable=True)

    def on_tick(self) -> state.State:
        if monster_dead(boxIds=[109,110,111]):
            return 층레버활성6()


class 층레버활성6(state.State):
    def on_enter(self):
        set_interact_object(triggerIds=[10001325], state=1)

    def on_tick(self) -> state.State:
        if object_interacted(interactIds=[10001325], arg2=0):
            return 포탈활성화()


class 포탈활성화(state.State):
    def on_enter(self):
        set_mesh(triggerIds=[1016,1017,1018], visible=True, arg3=0, arg4=500, arg5=3)
        set_portal(portalId=2, visible=True, enabled=True, minimapVisible=True)

    def on_tick(self) -> state.State:
        if true():
            return 종료()


class 종료(state.State):
    pass


