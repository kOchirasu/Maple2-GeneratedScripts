""" trigger/02000382_bf/1122330_move.xml """
from common import *
import state


class Wait(state.State):
    def on_enter(self):
        set_portal(portalId=20, visible=False, enabled=False, minimapVisible=False) # Emergency
        set_mesh(triggerIds=[3000], visible=True, arg3=0, arg4=0, arg5=0) # ElevatorHallRoof
        set_mesh(triggerIds=[3001], visible=True, arg3=0, arg4=0, arg5=0) # ElevatorHallGround
        set_mesh(triggerIds=[3100,3101,3102,3103,3104,3105,3106,3107,3108,3109,3110,3111,3112,3113,3114,3115,3116,3117,3118,3119,3120,3121], visible=True, arg3=0, arg4=0, arg5=0) # VisibleRoof
        set_mesh(triggerIds=[3200,3201,3202,3203,3204,3205,3206,3207,3208,3209,3210,3211,3212,3213,3214,3215,3216,3217,3218,3219,3220,3221], visible=True, arg3=0, arg4=0, arg5=0) # VisibleGround
        set_agent(triggerIds=[8000], visible=True)
        set_agent(triggerIds=[8001], visible=True)
        set_agent(triggerIds=[8002], visible=True)
        set_agent(triggerIds=[8003], visible=True)
        set_agent(triggerIds=[8004], visible=True)
        set_agent(triggerIds=[8005], visible=True)
        set_agent(triggerIds=[8006], visible=True)
        set_agent(triggerIds=[8007], visible=True)
        set_agent(triggerIds=[8008], visible=True)
        set_agent(triggerIds=[8009], visible=True)
        set_agent(triggerIds=[8010], visible=True)
        set_agent(triggerIds=[8011], visible=True)
        set_agent(triggerIds=[8012], visible=True)
        set_agent(triggerIds=[8013], visible=True)
        set_agent(triggerIds=[8014], visible=True)
        set_agent(triggerIds=[8015], visible=True)
        set_agent(triggerIds=[8016], visible=True)
        set_agent(triggerIds=[8017], visible=True)
        set_agent(triggerIds=[8018], visible=True)
        set_agent(triggerIds=[8019], visible=True)
        set_breakable(triggerIds=[4000], enabled=False) # Move_GoUp
        set_breakable(triggerIds=[4001], enabled=False) # Move_GoUp
        set_breakable(triggerIds=[4002], enabled=False) # Move_GoUp
        set_breakable(triggerIds=[4003], enabled=False) # Move_GoUp
        set_breakable(triggerIds=[4004], enabled=False) # Move_GoUp
        set_breakable(triggerIds=[4005], enabled=False) # Move_GoUp
        set_breakable(triggerIds=[4006], enabled=False) # Move_GoUp
        set_breakable(triggerIds=[4007], enabled=False) # Move_GoUp
        set_breakable(triggerIds=[4008], enabled=False) # Move_GoUp
        set_breakable(triggerIds=[4009], enabled=False) # Move_GoUp
        set_breakable(triggerIds=[4010], enabled=False) # Move_GoUp
        set_breakable(triggerIds=[4011], enabled=False) # Move_GoUp
        set_breakable(triggerIds=[4012], enabled=False) # Move_GoUp
        set_breakable(triggerIds=[4013], enabled=False) # Move_GoUp
        set_breakable(triggerIds=[4014], enabled=False) # Move_GoUp
        set_breakable(triggerIds=[4015], enabled=False) # Move_GoUp
        set_breakable(triggerIds=[4016], enabled=False) # Move_GoUp
        set_breakable(triggerIds=[4017], enabled=False) # Move_GoUp
        set_breakable(triggerIds=[4018], enabled=False) # Move_GoUp
        set_breakable(triggerIds=[4019], enabled=False) # Move_GoUp
        set_breakable(triggerIds=[4020], enabled=False) # Move_GoUp
        set_breakable(triggerIds=[4021], enabled=False) # Move_GoUp
        set_visible_breakable_object(triggerIds=[4000], arg2=False) # Move_GoUp
        set_visible_breakable_object(triggerIds=[4001], arg2=False) # Move_GoUp
        set_visible_breakable_object(triggerIds=[4002], arg2=False) # Move_GoUp
        set_visible_breakable_object(triggerIds=[4003], arg2=False) # Move_GoUp
        set_visible_breakable_object(triggerIds=[4004], arg2=False) # Move_GoUp
        set_visible_breakable_object(triggerIds=[4005], arg2=False) # Move_GoUp
        set_visible_breakable_object(triggerIds=[4006], arg2=False) # Move_GoUp
        set_visible_breakable_object(triggerIds=[4007], arg2=False) # Move_GoUp
        set_visible_breakable_object(triggerIds=[4008], arg2=False) # Move_GoUp
        set_visible_breakable_object(triggerIds=[4009], arg2=False) # Move_GoUp
        set_visible_breakable_object(triggerIds=[4010], arg2=False) # Move_GoUp
        set_visible_breakable_object(triggerIds=[4011], arg2=False) # Move_GoUp
        set_visible_breakable_object(triggerIds=[4012], arg2=False) # Move_GoUp
        set_visible_breakable_object(triggerIds=[4013], arg2=False) # Move_GoUp
        set_visible_breakable_object(triggerIds=[4014], arg2=False) # Move_GoUp
        set_visible_breakable_object(triggerIds=[4015], arg2=False) # Move_GoUp
        set_visible_breakable_object(triggerIds=[4016], arg2=False) # Move_GoUp
        set_visible_breakable_object(triggerIds=[4017], arg2=False) # Move_GoUp
        set_visible_breakable_object(triggerIds=[4018], arg2=False) # Move_GoUp
        set_visible_breakable_object(triggerIds=[4019], arg2=False) # Move_GoUp
        set_visible_breakable_object(triggerIds=[4020], arg2=False) # Move_GoUp
        set_visible_breakable_object(triggerIds=[4021], arg2=False) # Move_GoUp
        set_interact_object(triggerIds=[10001107], state=2) # IceSwitch
        set_user_value(key='ElevatorOn', value=0)
        set_user_value(key='DungeonClear', value=0)
        set_user_value(key='AgentOff', value=0)

    def on_tick(self) -> state.State:
        if user_value(key='ElevatorOn', value=1):
            return BoardApp01()
        if user_value(key='AgentOff', value=1):
            return AgentOff01()


class BoardApp01(state.State):
    def on_enter(self):
        show_guide_summary(entityId=20038102, textId=20038102) # 스위치를 작동시켜보세요
        set_interact_object(triggerIds=[10001107], state=1) # IceSwitch

    def on_tick(self) -> state.State:
        if object_interacted(interactIds=[10001107], arg2=0):
            return BoardGoUp01()


class BoardGoUp01(state.State):
    def on_enter(self):
        hide_guide_summary(entityId=20038102)
        set_interact_object(triggerIds=[10001107], state=2) # Lever
        set_breakable(triggerIds=[4000], enabled=True) # Move_GoUp
        set_breakable(triggerIds=[4001], enabled=True) # Move_GoUp
        set_breakable(triggerIds=[4002], enabled=True) # Move_GoUp
        set_breakable(triggerIds=[4003], enabled=True) # Move_GoUp
        set_breakable(triggerIds=[4004], enabled=True) # Move_GoUp
        set_breakable(triggerIds=[4005], enabled=True) # Move_GoUp
        set_breakable(triggerIds=[4006], enabled=True) # Move_GoUp
        set_breakable(triggerIds=[4007], enabled=True) # Move_GoUp
        set_breakable(triggerIds=[4008], enabled=True) # Move_GoUp
        set_breakable(triggerIds=[4009], enabled=True) # Move_GoUp
        set_breakable(triggerIds=[4010], enabled=True) # Move_GoUp
        set_breakable(triggerIds=[4011], enabled=True) # Move_GoUp
        set_breakable(triggerIds=[4012], enabled=True) # Move_GoUp
        set_breakable(triggerIds=[4013], enabled=True) # Move_GoUp
        set_breakable(triggerIds=[4014], enabled=True) # Move_GoUp
        set_breakable(triggerIds=[4015], enabled=True) # Move_GoUp
        set_breakable(triggerIds=[4016], enabled=True) # Move_GoUp
        set_breakable(triggerIds=[4017], enabled=True) # Move_GoUp
        set_breakable(triggerIds=[4018], enabled=True) # Move_GoUp
        set_breakable(triggerIds=[4019], enabled=True) # Move_GoUp
        set_breakable(triggerIds=[4020], enabled=True) # Move_GoUp
        set_breakable(triggerIds=[4021], enabled=True) # Move_GoUp
        set_visible_breakable_object(triggerIds=[4000], arg2=True) # Move_GoUp
        set_visible_breakable_object(triggerIds=[4001], arg2=True) # Move_GoUp
        set_visible_breakable_object(triggerIds=[4002], arg2=True) # Move_GoUp
        set_visible_breakable_object(triggerIds=[4003], arg2=True) # Move_GoUp
        set_visible_breakable_object(triggerIds=[4004], arg2=True) # Move_GoUp
        set_visible_breakable_object(triggerIds=[4005], arg2=True) # Move_GoUp
        set_visible_breakable_object(triggerIds=[4006], arg2=True) # Move_GoUp
        set_visible_breakable_object(triggerIds=[4007], arg2=True) # Move_GoUp
        set_visible_breakable_object(triggerIds=[4008], arg2=True) # Move_GoUp
        set_visible_breakable_object(triggerIds=[4009], arg2=True) # Move_GoUp
        set_visible_breakable_object(triggerIds=[4010], arg2=True) # Move_GoUp
        set_visible_breakable_object(triggerIds=[4011], arg2=True) # Move_GoUp
        set_visible_breakable_object(triggerIds=[4012], arg2=True) # Move_GoUp
        set_visible_breakable_object(triggerIds=[4013], arg2=True) # Move_GoUp
        set_visible_breakable_object(triggerIds=[4014], arg2=True) # Move_GoUp
        set_visible_breakable_object(triggerIds=[4015], arg2=True) # Move_GoUp
        set_visible_breakable_object(triggerIds=[4016], arg2=True) # Move_GoUp
        set_visible_breakable_object(triggerIds=[4017], arg2=True) # Move_GoUp
        set_visible_breakable_object(triggerIds=[4018], arg2=True) # Move_GoUp
        set_visible_breakable_object(triggerIds=[4019], arg2=True) # Move_GoUp
        set_visible_breakable_object(triggerIds=[4020], arg2=True) # Move_GoUp
        set_visible_breakable_object(triggerIds=[4021], arg2=True) # Move_GoUp
        set_mesh(triggerIds=[3000], visible=False, arg3=500, arg4=0, arg5=0) # ElevatorHallRoof
        set_mesh(triggerIds=[3001], visible=False, arg3=500, arg4=0, arg5=0) # ElevatorHallGround
        set_mesh(triggerIds=[3100,3101,3102,3103,3104,3105,3106,3107,3108,3109,3110,3111,3112,3113,3114,3115,3116,3117,3118,3119,3120,3121], visible=False, arg3=200, arg4=0, arg5=2) # VisibleRoof
        set_mesh(triggerIds=[3200,3201,3202,3203,3204,3205,3206,3207,3208,3209,3210,3211,3212,3213,3214,3215,3216,3217,3218,3219,3220,3221], visible=False, arg3=200, arg4=0, arg5=2) # VisibleGround

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=6000):
            return BoardGoUp02()


class BoardGoUp02(state.State):
    def on_enter(self):
        set_mesh(triggerIds=[3000], visible=True, arg3=100, arg4=0, arg5=0) # ElevatorHallRoof
        set_mesh(triggerIds=[3100,3101,3102,3103,3104,3105,3106,3107,3108,3109,3110,3111,3112,3113,3114,3115,3116,3117,3118,3119,3120,3121], visible=True, arg3=100, arg4=0, arg5=2) # VisibleRoof

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=500):
            return BoardGoUp03()


class BoardGoUp03(state.State):
    def on_enter(self):
        set_breakable(triggerIds=[4000], enabled=False) # Move_GoUp
        set_breakable(triggerIds=[4001], enabled=False) # Move_GoUp
        set_breakable(triggerIds=[4002], enabled=False) # Move_GoUp
        set_breakable(triggerIds=[4003], enabled=False) # Move_GoUp
        set_breakable(triggerIds=[4004], enabled=False) # Move_GoUp
        set_breakable(triggerIds=[4005], enabled=False) # Move_GoUp
        set_breakable(triggerIds=[4006], enabled=False) # Move_GoUp
        set_breakable(triggerIds=[4007], enabled=False) # Move_GoUp
        set_breakable(triggerIds=[4008], enabled=False) # Move_GoUp
        set_breakable(triggerIds=[4009], enabled=False) # Move_GoUp
        set_breakable(triggerIds=[4010], enabled=False) # Move_GoUp
        set_breakable(triggerIds=[4011], enabled=False) # Move_GoUp
        set_breakable(triggerIds=[4012], enabled=False) # Move_GoUp
        set_breakable(triggerIds=[4013], enabled=False) # Move_GoUp
        set_breakable(triggerIds=[4014], enabled=False) # Move_GoUp
        set_breakable(triggerIds=[4015], enabled=False) # Move_GoUp
        set_breakable(triggerIds=[4016], enabled=False) # Move_GoUp
        set_breakable(triggerIds=[4017], enabled=False) # Move_GoUp
        set_breakable(triggerIds=[4018], enabled=False) # Move_GoUp
        set_breakable(triggerIds=[4019], enabled=False) # Move_GoUp
        set_breakable(triggerIds=[4020], enabled=False) # Move_GoUp
        set_breakable(triggerIds=[4021], enabled=False) # Move_GoUp
        set_visible_breakable_object(triggerIds=[4000], arg2=False) # Move_GoUp
        set_visible_breakable_object(triggerIds=[4001], arg2=False) # Move_GoUp
        set_visible_breakable_object(triggerIds=[4002], arg2=False) # Move_GoUp
        set_visible_breakable_object(triggerIds=[4003], arg2=False) # Move_GoUp
        set_visible_breakable_object(triggerIds=[4004], arg2=False) # Move_GoUp
        set_visible_breakable_object(triggerIds=[4005], arg2=False) # Move_GoUp
        set_visible_breakable_object(triggerIds=[4006], arg2=False) # Move_GoUp
        set_visible_breakable_object(triggerIds=[4007], arg2=False) # Move_GoUp
        set_visible_breakable_object(triggerIds=[4008], arg2=False) # Move_GoUp
        set_visible_breakable_object(triggerIds=[4009], arg2=False) # Move_GoUp
        set_visible_breakable_object(triggerIds=[4010], arg2=False) # Move_GoUp
        set_visible_breakable_object(triggerIds=[4011], arg2=False) # Move_GoUp
        set_visible_breakable_object(triggerIds=[4012], arg2=False) # Move_GoUp
        set_visible_breakable_object(triggerIds=[4013], arg2=False) # Move_GoUp
        set_visible_breakable_object(triggerIds=[4014], arg2=False) # Move_GoUp
        set_visible_breakable_object(triggerIds=[4015], arg2=False) # Move_GoUp
        set_visible_breakable_object(triggerIds=[4016], arg2=False) # Move_GoUp
        set_visible_breakable_object(triggerIds=[4017], arg2=False) # Move_GoUp
        set_visible_breakable_object(triggerIds=[4018], arg2=False) # Move_GoUp
        set_visible_breakable_object(triggerIds=[4019], arg2=False) # Move_GoUp
        set_visible_breakable_object(triggerIds=[4020], arg2=False) # Move_GoUp
        set_visible_breakable_object(triggerIds=[4021], arg2=False) # Move_GoUp
        set_agent(triggerIds=[8000], visible=False)
        set_agent(triggerIds=[8001], visible=False)
        set_agent(triggerIds=[8002], visible=False)
        set_agent(triggerIds=[8003], visible=False)
        set_agent(triggerIds=[8004], visible=False)
        set_agent(triggerIds=[8005], visible=False)
        set_agent(triggerIds=[8006], visible=False)
        set_agent(triggerIds=[8007], visible=False)
        set_agent(triggerIds=[8008], visible=False)
        set_agent(triggerIds=[8009], visible=False)
        set_agent(triggerIds=[8010], visible=False)
        set_agent(triggerIds=[8011], visible=False)
        set_agent(triggerIds=[8012], visible=False)
        set_agent(triggerIds=[8013], visible=False)
        set_agent(triggerIds=[8014], visible=False)
        set_agent(triggerIds=[8015], visible=False)
        set_agent(triggerIds=[8016], visible=False)
        set_agent(triggerIds=[8017], visible=False)
        set_agent(triggerIds=[8018], visible=False)
        set_agent(triggerIds=[8019], visible=False)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=3000):
            return EmergencyPortalOn()


class EmergencyPortalOn(state.State):
    def on_enter(self):
        set_portal(portalId=20, visible=True, enabled=True, minimapVisible=False) # Emergency


#  좌우 상단 입장 시 
class AgentOff01(state.State):
    def on_enter(self):
        set_agent(triggerIds=[8000], visible=False)
        set_agent(triggerIds=[8001], visible=False)
        set_agent(triggerIds=[8002], visible=False)
        set_agent(triggerIds=[8003], visible=False)
        set_agent(triggerIds=[8004], visible=False)
        set_agent(triggerIds=[8005], visible=False)
        set_agent(triggerIds=[8006], visible=False)
        set_agent(triggerIds=[8007], visible=False)
        set_agent(triggerIds=[8008], visible=False)
        set_agent(triggerIds=[8009], visible=False)
        set_agent(triggerIds=[8010], visible=False)
        set_agent(triggerIds=[8011], visible=False)
        set_agent(triggerIds=[8012], visible=False)
        set_agent(triggerIds=[8013], visible=False)
        set_agent(triggerIds=[8014], visible=False)
        set_agent(triggerIds=[8015], visible=False)
        set_agent(triggerIds=[8016], visible=False)
        set_agent(triggerIds=[8017], visible=False)
        set_agent(triggerIds=[8018], visible=False)
        set_agent(triggerIds=[8019], visible=False)


