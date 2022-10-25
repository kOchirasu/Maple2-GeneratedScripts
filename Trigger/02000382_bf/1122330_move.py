""" trigger/02000382_bf/1122330_move.xml """
import common


class Wait(common.Trigger):
    def on_enter(self):
        self.set_portal(portalId=20, visible=False, enable=False, minimapVisible=False) # Emergency
        self.set_mesh(triggerIds=[3000], visible=True, arg3=0, delay=0, scale=0) # ElevatorHallRoof
        self.set_mesh(triggerIds=[3001], visible=True, arg3=0, delay=0, scale=0) # ElevatorHallGround
        self.set_mesh(triggerIds=[3100,3101,3102,3103,3104,3105,3106,3107,3108,3109,3110,3111,3112,3113,3114,3115,3116,3117,3118,3119,3120,3121], visible=True, arg3=0, delay=0, scale=0) # VisibleRoof
        self.set_mesh(triggerIds=[3200,3201,3202,3203,3204,3205,3206,3207,3208,3209,3210,3211,3212,3213,3214,3215,3216,3217,3218,3219,3220,3221], visible=True, arg3=0, delay=0, scale=0) # VisibleGround
        self.set_agent(triggerIds=[8000], visible=True)
        self.set_agent(triggerIds=[8001], visible=True)
        self.set_agent(triggerIds=[8002], visible=True)
        self.set_agent(triggerIds=[8003], visible=True)
        self.set_agent(triggerIds=[8004], visible=True)
        self.set_agent(triggerIds=[8005], visible=True)
        self.set_agent(triggerIds=[8006], visible=True)
        self.set_agent(triggerIds=[8007], visible=True)
        self.set_agent(triggerIds=[8008], visible=True)
        self.set_agent(triggerIds=[8009], visible=True)
        self.set_agent(triggerIds=[8010], visible=True)
        self.set_agent(triggerIds=[8011], visible=True)
        self.set_agent(triggerIds=[8012], visible=True)
        self.set_agent(triggerIds=[8013], visible=True)
        self.set_agent(triggerIds=[8014], visible=True)
        self.set_agent(triggerIds=[8015], visible=True)
        self.set_agent(triggerIds=[8016], visible=True)
        self.set_agent(triggerIds=[8017], visible=True)
        self.set_agent(triggerIds=[8018], visible=True)
        self.set_agent(triggerIds=[8019], visible=True)
        self.set_breakable(triggerIds=[4000], enable=False) # Move_GoUp
        self.set_breakable(triggerIds=[4001], enable=False) # Move_GoUp
        self.set_breakable(triggerIds=[4002], enable=False) # Move_GoUp
        self.set_breakable(triggerIds=[4003], enable=False) # Move_GoUp
        self.set_breakable(triggerIds=[4004], enable=False) # Move_GoUp
        self.set_breakable(triggerIds=[4005], enable=False) # Move_GoUp
        self.set_breakable(triggerIds=[4006], enable=False) # Move_GoUp
        self.set_breakable(triggerIds=[4007], enable=False) # Move_GoUp
        self.set_breakable(triggerIds=[4008], enable=False) # Move_GoUp
        self.set_breakable(triggerIds=[4009], enable=False) # Move_GoUp
        self.set_breakable(triggerIds=[4010], enable=False) # Move_GoUp
        self.set_breakable(triggerIds=[4011], enable=False) # Move_GoUp
        self.set_breakable(triggerIds=[4012], enable=False) # Move_GoUp
        self.set_breakable(triggerIds=[4013], enable=False) # Move_GoUp
        self.set_breakable(triggerIds=[4014], enable=False) # Move_GoUp
        self.set_breakable(triggerIds=[4015], enable=False) # Move_GoUp
        self.set_breakable(triggerIds=[4016], enable=False) # Move_GoUp
        self.set_breakable(triggerIds=[4017], enable=False) # Move_GoUp
        self.set_breakable(triggerIds=[4018], enable=False) # Move_GoUp
        self.set_breakable(triggerIds=[4019], enable=False) # Move_GoUp
        self.set_breakable(triggerIds=[4020], enable=False) # Move_GoUp
        self.set_breakable(triggerIds=[4021], enable=False) # Move_GoUp
        self.set_visible_breakable_object(triggerIds=[4000], visible=False) # Move_GoUp
        self.set_visible_breakable_object(triggerIds=[4001], visible=False) # Move_GoUp
        self.set_visible_breakable_object(triggerIds=[4002], visible=False) # Move_GoUp
        self.set_visible_breakable_object(triggerIds=[4003], visible=False) # Move_GoUp
        self.set_visible_breakable_object(triggerIds=[4004], visible=False) # Move_GoUp
        self.set_visible_breakable_object(triggerIds=[4005], visible=False) # Move_GoUp
        self.set_visible_breakable_object(triggerIds=[4006], visible=False) # Move_GoUp
        self.set_visible_breakable_object(triggerIds=[4007], visible=False) # Move_GoUp
        self.set_visible_breakable_object(triggerIds=[4008], visible=False) # Move_GoUp
        self.set_visible_breakable_object(triggerIds=[4009], visible=False) # Move_GoUp
        self.set_visible_breakable_object(triggerIds=[4010], visible=False) # Move_GoUp
        self.set_visible_breakable_object(triggerIds=[4011], visible=False) # Move_GoUp
        self.set_visible_breakable_object(triggerIds=[4012], visible=False) # Move_GoUp
        self.set_visible_breakable_object(triggerIds=[4013], visible=False) # Move_GoUp
        self.set_visible_breakable_object(triggerIds=[4014], visible=False) # Move_GoUp
        self.set_visible_breakable_object(triggerIds=[4015], visible=False) # Move_GoUp
        self.set_visible_breakable_object(triggerIds=[4016], visible=False) # Move_GoUp
        self.set_visible_breakable_object(triggerIds=[4017], visible=False) # Move_GoUp
        self.set_visible_breakable_object(triggerIds=[4018], visible=False) # Move_GoUp
        self.set_visible_breakable_object(triggerIds=[4019], visible=False) # Move_GoUp
        self.set_visible_breakable_object(triggerIds=[4020], visible=False) # Move_GoUp
        self.set_visible_breakable_object(triggerIds=[4021], visible=False) # Move_GoUp
        self.set_interact_object(triggerIds=[10001107], state=2) # IceSwitch
        self.set_user_value(key='ElevatorOn', value=0)
        self.set_user_value(key='DungeonClear', value=0)
        self.set_user_value(key='AgentOff', value=0)

    def on_tick(self) -> common.Trigger:
        if self.user_value(key='ElevatorOn', value=1):
            return BoardApp01(self.ctx)
        if self.user_value(key='AgentOff', value=1):
            return AgentOff01(self.ctx)


class BoardApp01(common.Trigger):
    def on_enter(self):
        self.show_guide_summary(entityId=20038102, textId=20038102) # 스위치를 작동시켜보세요
        self.set_interact_object(triggerIds=[10001107], state=1) # IceSwitch

    def on_tick(self) -> common.Trigger:
        if self.object_interacted(interactIds=[10001107], stateValue=0):
            return BoardGoUp01(self.ctx)


class BoardGoUp01(common.Trigger):
    def on_enter(self):
        self.hide_guide_summary(entityId=20038102)
        self.set_interact_object(triggerIds=[10001107], state=2) # Lever
        self.set_breakable(triggerIds=[4000], enable=True) # Move_GoUp
        self.set_breakable(triggerIds=[4001], enable=True) # Move_GoUp
        self.set_breakable(triggerIds=[4002], enable=True) # Move_GoUp
        self.set_breakable(triggerIds=[4003], enable=True) # Move_GoUp
        self.set_breakable(triggerIds=[4004], enable=True) # Move_GoUp
        self.set_breakable(triggerIds=[4005], enable=True) # Move_GoUp
        self.set_breakable(triggerIds=[4006], enable=True) # Move_GoUp
        self.set_breakable(triggerIds=[4007], enable=True) # Move_GoUp
        self.set_breakable(triggerIds=[4008], enable=True) # Move_GoUp
        self.set_breakable(triggerIds=[4009], enable=True) # Move_GoUp
        self.set_breakable(triggerIds=[4010], enable=True) # Move_GoUp
        self.set_breakable(triggerIds=[4011], enable=True) # Move_GoUp
        self.set_breakable(triggerIds=[4012], enable=True) # Move_GoUp
        self.set_breakable(triggerIds=[4013], enable=True) # Move_GoUp
        self.set_breakable(triggerIds=[4014], enable=True) # Move_GoUp
        self.set_breakable(triggerIds=[4015], enable=True) # Move_GoUp
        self.set_breakable(triggerIds=[4016], enable=True) # Move_GoUp
        self.set_breakable(triggerIds=[4017], enable=True) # Move_GoUp
        self.set_breakable(triggerIds=[4018], enable=True) # Move_GoUp
        self.set_breakable(triggerIds=[4019], enable=True) # Move_GoUp
        self.set_breakable(triggerIds=[4020], enable=True) # Move_GoUp
        self.set_breakable(triggerIds=[4021], enable=True) # Move_GoUp
        self.set_visible_breakable_object(triggerIds=[4000], visible=True) # Move_GoUp
        self.set_visible_breakable_object(triggerIds=[4001], visible=True) # Move_GoUp
        self.set_visible_breakable_object(triggerIds=[4002], visible=True) # Move_GoUp
        self.set_visible_breakable_object(triggerIds=[4003], visible=True) # Move_GoUp
        self.set_visible_breakable_object(triggerIds=[4004], visible=True) # Move_GoUp
        self.set_visible_breakable_object(triggerIds=[4005], visible=True) # Move_GoUp
        self.set_visible_breakable_object(triggerIds=[4006], visible=True) # Move_GoUp
        self.set_visible_breakable_object(triggerIds=[4007], visible=True) # Move_GoUp
        self.set_visible_breakable_object(triggerIds=[4008], visible=True) # Move_GoUp
        self.set_visible_breakable_object(triggerIds=[4009], visible=True) # Move_GoUp
        self.set_visible_breakable_object(triggerIds=[4010], visible=True) # Move_GoUp
        self.set_visible_breakable_object(triggerIds=[4011], visible=True) # Move_GoUp
        self.set_visible_breakable_object(triggerIds=[4012], visible=True) # Move_GoUp
        self.set_visible_breakable_object(triggerIds=[4013], visible=True) # Move_GoUp
        self.set_visible_breakable_object(triggerIds=[4014], visible=True) # Move_GoUp
        self.set_visible_breakable_object(triggerIds=[4015], visible=True) # Move_GoUp
        self.set_visible_breakable_object(triggerIds=[4016], visible=True) # Move_GoUp
        self.set_visible_breakable_object(triggerIds=[4017], visible=True) # Move_GoUp
        self.set_visible_breakable_object(triggerIds=[4018], visible=True) # Move_GoUp
        self.set_visible_breakable_object(triggerIds=[4019], visible=True) # Move_GoUp
        self.set_visible_breakable_object(triggerIds=[4020], visible=True) # Move_GoUp
        self.set_visible_breakable_object(triggerIds=[4021], visible=True) # Move_GoUp
        self.set_mesh(triggerIds=[3000], visible=False, arg3=500, delay=0, scale=0) # ElevatorHallRoof
        self.set_mesh(triggerIds=[3001], visible=False, arg3=500, delay=0, scale=0) # ElevatorHallGround
        self.set_mesh(triggerIds=[3100,3101,3102,3103,3104,3105,3106,3107,3108,3109,3110,3111,3112,3113,3114,3115,3116,3117,3118,3119,3120,3121], visible=False, arg3=200, delay=0, scale=2) # VisibleRoof
        self.set_mesh(triggerIds=[3200,3201,3202,3203,3204,3205,3206,3207,3208,3209,3210,3211,3212,3213,3214,3215,3216,3217,3218,3219,3220,3221], visible=False, arg3=200, delay=0, scale=2) # VisibleGround

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=6000):
            return BoardGoUp02(self.ctx)


class BoardGoUp02(common.Trigger):
    def on_enter(self):
        self.set_mesh(triggerIds=[3000], visible=True, arg3=100, delay=0, scale=0) # ElevatorHallRoof
        self.set_mesh(triggerIds=[3100,3101,3102,3103,3104,3105,3106,3107,3108,3109,3110,3111,3112,3113,3114,3115,3116,3117,3118,3119,3120,3121], visible=True, arg3=100, delay=0, scale=2) # VisibleRoof

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=500):
            return BoardGoUp03(self.ctx)


class BoardGoUp03(common.Trigger):
    def on_enter(self):
        self.set_breakable(triggerIds=[4000], enable=False) # Move_GoUp
        self.set_breakable(triggerIds=[4001], enable=False) # Move_GoUp
        self.set_breakable(triggerIds=[4002], enable=False) # Move_GoUp
        self.set_breakable(triggerIds=[4003], enable=False) # Move_GoUp
        self.set_breakable(triggerIds=[4004], enable=False) # Move_GoUp
        self.set_breakable(triggerIds=[4005], enable=False) # Move_GoUp
        self.set_breakable(triggerIds=[4006], enable=False) # Move_GoUp
        self.set_breakable(triggerIds=[4007], enable=False) # Move_GoUp
        self.set_breakable(triggerIds=[4008], enable=False) # Move_GoUp
        self.set_breakable(triggerIds=[4009], enable=False) # Move_GoUp
        self.set_breakable(triggerIds=[4010], enable=False) # Move_GoUp
        self.set_breakable(triggerIds=[4011], enable=False) # Move_GoUp
        self.set_breakable(triggerIds=[4012], enable=False) # Move_GoUp
        self.set_breakable(triggerIds=[4013], enable=False) # Move_GoUp
        self.set_breakable(triggerIds=[4014], enable=False) # Move_GoUp
        self.set_breakable(triggerIds=[4015], enable=False) # Move_GoUp
        self.set_breakable(triggerIds=[4016], enable=False) # Move_GoUp
        self.set_breakable(triggerIds=[4017], enable=False) # Move_GoUp
        self.set_breakable(triggerIds=[4018], enable=False) # Move_GoUp
        self.set_breakable(triggerIds=[4019], enable=False) # Move_GoUp
        self.set_breakable(triggerIds=[4020], enable=False) # Move_GoUp
        self.set_breakable(triggerIds=[4021], enable=False) # Move_GoUp
        self.set_visible_breakable_object(triggerIds=[4000], visible=False) # Move_GoUp
        self.set_visible_breakable_object(triggerIds=[4001], visible=False) # Move_GoUp
        self.set_visible_breakable_object(triggerIds=[4002], visible=False) # Move_GoUp
        self.set_visible_breakable_object(triggerIds=[4003], visible=False) # Move_GoUp
        self.set_visible_breakable_object(triggerIds=[4004], visible=False) # Move_GoUp
        self.set_visible_breakable_object(triggerIds=[4005], visible=False) # Move_GoUp
        self.set_visible_breakable_object(triggerIds=[4006], visible=False) # Move_GoUp
        self.set_visible_breakable_object(triggerIds=[4007], visible=False) # Move_GoUp
        self.set_visible_breakable_object(triggerIds=[4008], visible=False) # Move_GoUp
        self.set_visible_breakable_object(triggerIds=[4009], visible=False) # Move_GoUp
        self.set_visible_breakable_object(triggerIds=[4010], visible=False) # Move_GoUp
        self.set_visible_breakable_object(triggerIds=[4011], visible=False) # Move_GoUp
        self.set_visible_breakable_object(triggerIds=[4012], visible=False) # Move_GoUp
        self.set_visible_breakable_object(triggerIds=[4013], visible=False) # Move_GoUp
        self.set_visible_breakable_object(triggerIds=[4014], visible=False) # Move_GoUp
        self.set_visible_breakable_object(triggerIds=[4015], visible=False) # Move_GoUp
        self.set_visible_breakable_object(triggerIds=[4016], visible=False) # Move_GoUp
        self.set_visible_breakable_object(triggerIds=[4017], visible=False) # Move_GoUp
        self.set_visible_breakable_object(triggerIds=[4018], visible=False) # Move_GoUp
        self.set_visible_breakable_object(triggerIds=[4019], visible=False) # Move_GoUp
        self.set_visible_breakable_object(triggerIds=[4020], visible=False) # Move_GoUp
        self.set_visible_breakable_object(triggerIds=[4021], visible=False) # Move_GoUp
        self.set_agent(triggerIds=[8000], visible=False)
        self.set_agent(triggerIds=[8001], visible=False)
        self.set_agent(triggerIds=[8002], visible=False)
        self.set_agent(triggerIds=[8003], visible=False)
        self.set_agent(triggerIds=[8004], visible=False)
        self.set_agent(triggerIds=[8005], visible=False)
        self.set_agent(triggerIds=[8006], visible=False)
        self.set_agent(triggerIds=[8007], visible=False)
        self.set_agent(triggerIds=[8008], visible=False)
        self.set_agent(triggerIds=[8009], visible=False)
        self.set_agent(triggerIds=[8010], visible=False)
        self.set_agent(triggerIds=[8011], visible=False)
        self.set_agent(triggerIds=[8012], visible=False)
        self.set_agent(triggerIds=[8013], visible=False)
        self.set_agent(triggerIds=[8014], visible=False)
        self.set_agent(triggerIds=[8015], visible=False)
        self.set_agent(triggerIds=[8016], visible=False)
        self.set_agent(triggerIds=[8017], visible=False)
        self.set_agent(triggerIds=[8018], visible=False)
        self.set_agent(triggerIds=[8019], visible=False)

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=3000):
            return EmergencyPortalOn(self.ctx)


class EmergencyPortalOn(common.Trigger):
    def on_enter(self):
        self.set_portal(portalId=20, visible=True, enable=True, minimapVisible=False) # Emergency


# 좌우 상단 입장 시
class AgentOff01(common.Trigger):
    def on_enter(self):
        self.set_agent(triggerIds=[8000], visible=False)
        self.set_agent(triggerIds=[8001], visible=False)
        self.set_agent(triggerIds=[8002], visible=False)
        self.set_agent(triggerIds=[8003], visible=False)
        self.set_agent(triggerIds=[8004], visible=False)
        self.set_agent(triggerIds=[8005], visible=False)
        self.set_agent(triggerIds=[8006], visible=False)
        self.set_agent(triggerIds=[8007], visible=False)
        self.set_agent(triggerIds=[8008], visible=False)
        self.set_agent(triggerIds=[8009], visible=False)
        self.set_agent(triggerIds=[8010], visible=False)
        self.set_agent(triggerIds=[8011], visible=False)
        self.set_agent(triggerIds=[8012], visible=False)
        self.set_agent(triggerIds=[8013], visible=False)
        self.set_agent(triggerIds=[8014], visible=False)
        self.set_agent(triggerIds=[8015], visible=False)
        self.set_agent(triggerIds=[8016], visible=False)
        self.set_agent(triggerIds=[8017], visible=False)
        self.set_agent(triggerIds=[8018], visible=False)
        self.set_agent(triggerIds=[8019], visible=False)


initial_state = Wait
