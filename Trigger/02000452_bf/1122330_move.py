""" trigger/02000452_bf/1122330_move.xml """
import trigger_api


class Wait(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_portal(portal_id=20, visible=False, enable=False, minimap_visible=False) # Emergency
        self.set_mesh(trigger_ids=[3000], visible=True, start_delay=0, interval=0, fade=0) # ElevatorHallRoof
        self.set_mesh(trigger_ids=[3001], visible=True, start_delay=0, interval=0, fade=0) # ElevatorHallGround
        self.set_mesh(trigger_ids=[3100,3101,3102,3103,3104,3105,3106,3107,3108,3109,3110,3111,3112,3113,3114,3115,3116,3117,3118,3119,3120,3121], visible=True, start_delay=0, interval=0, fade=0) # VisibleRoof
        self.set_mesh(trigger_ids=[3200,3201,3202,3203,3204,3205,3206,3207,3208,3209,3210,3211,3212,3213,3214,3215,3216,3217,3218,3219,3220,3221], visible=True, start_delay=0, interval=0, fade=0) # VisibleGround
        self.set_agent(trigger_ids=[8000], visible=True)
        self.set_agent(trigger_ids=[8001], visible=True)
        self.set_agent(trigger_ids=[8002], visible=True)
        self.set_agent(trigger_ids=[8003], visible=True)
        self.set_agent(trigger_ids=[8004], visible=True)
        self.set_agent(trigger_ids=[8005], visible=True)
        self.set_agent(trigger_ids=[8006], visible=True)
        self.set_agent(trigger_ids=[8007], visible=True)
        self.set_agent(trigger_ids=[8008], visible=True)
        self.set_agent(trigger_ids=[8009], visible=True)
        self.set_agent(trigger_ids=[8010], visible=True)
        self.set_agent(trigger_ids=[8011], visible=True)
        self.set_agent(trigger_ids=[8012], visible=True)
        self.set_agent(trigger_ids=[8013], visible=True)
        self.set_agent(trigger_ids=[8014], visible=True)
        self.set_agent(trigger_ids=[8015], visible=True)
        self.set_agent(trigger_ids=[8016], visible=True)
        self.set_agent(trigger_ids=[8017], visible=True)
        self.set_agent(trigger_ids=[8018], visible=True)
        self.set_agent(trigger_ids=[8019], visible=True)
        self.set_breakable(trigger_ids=[4000], enable=False) # Move_GoUp
        self.set_breakable(trigger_ids=[4001], enable=False) # Move_GoUp
        self.set_breakable(trigger_ids=[4002], enable=False) # Move_GoUp
        self.set_breakable(trigger_ids=[4003], enable=False) # Move_GoUp
        self.set_breakable(trigger_ids=[4004], enable=False) # Move_GoUp
        self.set_breakable(trigger_ids=[4005], enable=False) # Move_GoUp
        self.set_breakable(trigger_ids=[4006], enable=False) # Move_GoUp
        self.set_breakable(trigger_ids=[4007], enable=False) # Move_GoUp
        self.set_breakable(trigger_ids=[4008], enable=False) # Move_GoUp
        self.set_breakable(trigger_ids=[4009], enable=False) # Move_GoUp
        self.set_breakable(trigger_ids=[4010], enable=False) # Move_GoUp
        self.set_breakable(trigger_ids=[4011], enable=False) # Move_GoUp
        self.set_breakable(trigger_ids=[4012], enable=False) # Move_GoUp
        self.set_breakable(trigger_ids=[4013], enable=False) # Move_GoUp
        self.set_breakable(trigger_ids=[4014], enable=False) # Move_GoUp
        self.set_breakable(trigger_ids=[4015], enable=False) # Move_GoUp
        self.set_breakable(trigger_ids=[4016], enable=False) # Move_GoUp
        self.set_breakable(trigger_ids=[4017], enable=False) # Move_GoUp
        self.set_breakable(trigger_ids=[4018], enable=False) # Move_GoUp
        self.set_breakable(trigger_ids=[4019], enable=False) # Move_GoUp
        self.set_breakable(trigger_ids=[4020], enable=False) # Move_GoUp
        self.set_breakable(trigger_ids=[4021], enable=False) # Move_GoUp
        self.set_visible_breakable_object(trigger_ids=[4000], visible=False) # Move_GoUp
        self.set_visible_breakable_object(trigger_ids=[4001], visible=False) # Move_GoUp
        self.set_visible_breakable_object(trigger_ids=[4002], visible=False) # Move_GoUp
        self.set_visible_breakable_object(trigger_ids=[4003], visible=False) # Move_GoUp
        self.set_visible_breakable_object(trigger_ids=[4004], visible=False) # Move_GoUp
        self.set_visible_breakable_object(trigger_ids=[4005], visible=False) # Move_GoUp
        self.set_visible_breakable_object(trigger_ids=[4006], visible=False) # Move_GoUp
        self.set_visible_breakable_object(trigger_ids=[4007], visible=False) # Move_GoUp
        self.set_visible_breakable_object(trigger_ids=[4008], visible=False) # Move_GoUp
        self.set_visible_breakable_object(trigger_ids=[4009], visible=False) # Move_GoUp
        self.set_visible_breakable_object(trigger_ids=[4010], visible=False) # Move_GoUp
        self.set_visible_breakable_object(trigger_ids=[4011], visible=False) # Move_GoUp
        self.set_visible_breakable_object(trigger_ids=[4012], visible=False) # Move_GoUp
        self.set_visible_breakable_object(trigger_ids=[4013], visible=False) # Move_GoUp
        self.set_visible_breakable_object(trigger_ids=[4014], visible=False) # Move_GoUp
        self.set_visible_breakable_object(trigger_ids=[4015], visible=False) # Move_GoUp
        self.set_visible_breakable_object(trigger_ids=[4016], visible=False) # Move_GoUp
        self.set_visible_breakable_object(trigger_ids=[4017], visible=False) # Move_GoUp
        self.set_visible_breakable_object(trigger_ids=[4018], visible=False) # Move_GoUp
        self.set_visible_breakable_object(trigger_ids=[4019], visible=False) # Move_GoUp
        self.set_visible_breakable_object(trigger_ids=[4020], visible=False) # Move_GoUp
        self.set_visible_breakable_object(trigger_ids=[4021], visible=False) # Move_GoUp
        self.set_interact_object(trigger_ids=[10002013], state=2) # IceSwitch
        self.set_user_value(key='ElevatorOn', value=0)
        self.set_user_value(key='DungeonClear', value=0)
        self.set_user_value(key='AgentOff', value=0)

    def on_tick(self) -> trigger_api.Trigger:
        if self.user_value(key='ElevatorOn') >= 1:
            return BoardApp01(self.ctx)
        if self.user_value(key='AgentOff') >= 1:
            return AgentOff01(self.ctx)


class BoardApp01(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.show_guide_summary(entity_id=20038102, text_id=20038102) # 스위치를 작동시켜보세요
        self.set_interact_object(trigger_ids=[10002013], state=1) # IceSwitch

    def on_tick(self) -> trigger_api.Trigger:
        if self.object_interacted(interact_ids=[10002013], state=0):
            return BoardGoUp01(self.ctx)


class BoardGoUp01(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.hide_guide_summary(entity_id=20038102)
        self.set_interact_object(trigger_ids=[10002013], state=2) # Lever
        self.set_breakable(trigger_ids=[4000], enable=True) # Move_GoUp
        self.set_breakable(trigger_ids=[4001], enable=True) # Move_GoUp
        self.set_breakable(trigger_ids=[4002], enable=True) # Move_GoUp
        self.set_breakable(trigger_ids=[4003], enable=True) # Move_GoUp
        self.set_breakable(trigger_ids=[4004], enable=True) # Move_GoUp
        self.set_breakable(trigger_ids=[4005], enable=True) # Move_GoUp
        self.set_breakable(trigger_ids=[4006], enable=True) # Move_GoUp
        self.set_breakable(trigger_ids=[4007], enable=True) # Move_GoUp
        self.set_breakable(trigger_ids=[4008], enable=True) # Move_GoUp
        self.set_breakable(trigger_ids=[4009], enable=True) # Move_GoUp
        self.set_breakable(trigger_ids=[4010], enable=True) # Move_GoUp
        self.set_breakable(trigger_ids=[4011], enable=True) # Move_GoUp
        self.set_breakable(trigger_ids=[4012], enable=True) # Move_GoUp
        self.set_breakable(trigger_ids=[4013], enable=True) # Move_GoUp
        self.set_breakable(trigger_ids=[4014], enable=True) # Move_GoUp
        self.set_breakable(trigger_ids=[4015], enable=True) # Move_GoUp
        self.set_breakable(trigger_ids=[4016], enable=True) # Move_GoUp
        self.set_breakable(trigger_ids=[4017], enable=True) # Move_GoUp
        self.set_breakable(trigger_ids=[4018], enable=True) # Move_GoUp
        self.set_breakable(trigger_ids=[4019], enable=True) # Move_GoUp
        self.set_breakable(trigger_ids=[4020], enable=True) # Move_GoUp
        self.set_breakable(trigger_ids=[4021], enable=True) # Move_GoUp
        self.set_visible_breakable_object(trigger_ids=[4000], visible=True) # Move_GoUp
        self.set_visible_breakable_object(trigger_ids=[4001], visible=True) # Move_GoUp
        self.set_visible_breakable_object(trigger_ids=[4002], visible=True) # Move_GoUp
        self.set_visible_breakable_object(trigger_ids=[4003], visible=True) # Move_GoUp
        self.set_visible_breakable_object(trigger_ids=[4004], visible=True) # Move_GoUp
        self.set_visible_breakable_object(trigger_ids=[4005], visible=True) # Move_GoUp
        self.set_visible_breakable_object(trigger_ids=[4006], visible=True) # Move_GoUp
        self.set_visible_breakable_object(trigger_ids=[4007], visible=True) # Move_GoUp
        self.set_visible_breakable_object(trigger_ids=[4008], visible=True) # Move_GoUp
        self.set_visible_breakable_object(trigger_ids=[4009], visible=True) # Move_GoUp
        self.set_visible_breakable_object(trigger_ids=[4010], visible=True) # Move_GoUp
        self.set_visible_breakable_object(trigger_ids=[4011], visible=True) # Move_GoUp
        self.set_visible_breakable_object(trigger_ids=[4012], visible=True) # Move_GoUp
        self.set_visible_breakable_object(trigger_ids=[4013], visible=True) # Move_GoUp
        self.set_visible_breakable_object(trigger_ids=[4014], visible=True) # Move_GoUp
        self.set_visible_breakable_object(trigger_ids=[4015], visible=True) # Move_GoUp
        self.set_visible_breakable_object(trigger_ids=[4016], visible=True) # Move_GoUp
        self.set_visible_breakable_object(trigger_ids=[4017], visible=True) # Move_GoUp
        self.set_visible_breakable_object(trigger_ids=[4018], visible=True) # Move_GoUp
        self.set_visible_breakable_object(trigger_ids=[4019], visible=True) # Move_GoUp
        self.set_visible_breakable_object(trigger_ids=[4020], visible=True) # Move_GoUp
        self.set_visible_breakable_object(trigger_ids=[4021], visible=True) # Move_GoUp
        self.set_mesh(trigger_ids=[3000], visible=False, start_delay=500, interval=0, fade=0) # ElevatorHallRoof
        self.set_mesh(trigger_ids=[3001], visible=False, start_delay=500, interval=0, fade=0) # ElevatorHallGround
        self.set_mesh(trigger_ids=[3100,3101,3102,3103,3104,3105,3106,3107,3108,3109,3110,3111,3112,3113,3114,3115,3116,3117,3118,3119,3120,3121], visible=False, start_delay=200, interval=0, fade=2) # VisibleRoof
        self.set_mesh(trigger_ids=[3200,3201,3202,3203,3204,3205,3206,3207,3208,3209,3210,3211,3212,3213,3214,3215,3216,3217,3218,3219,3220,3221], visible=False, start_delay=200, interval=0, fade=2) # VisibleGround

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=6000):
            return BoardGoUp02(self.ctx)


class BoardGoUp02(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_mesh(trigger_ids=[3000], visible=True, start_delay=100, interval=0, fade=0) # ElevatorHallRoof
        self.set_mesh(trigger_ids=[3100,3101,3102,3103,3104,3105,3106,3107,3108,3109,3110,3111,3112,3113,3114,3115,3116,3117,3118,3119,3120,3121], visible=True, start_delay=100, interval=0, fade=2) # VisibleRoof

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=500):
            return BoardGoUp03(self.ctx)


class BoardGoUp03(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_breakable(trigger_ids=[4000], enable=False) # Move_GoUp
        self.set_breakable(trigger_ids=[4001], enable=False) # Move_GoUp
        self.set_breakable(trigger_ids=[4002], enable=False) # Move_GoUp
        self.set_breakable(trigger_ids=[4003], enable=False) # Move_GoUp
        self.set_breakable(trigger_ids=[4004], enable=False) # Move_GoUp
        self.set_breakable(trigger_ids=[4005], enable=False) # Move_GoUp
        self.set_breakable(trigger_ids=[4006], enable=False) # Move_GoUp
        self.set_breakable(trigger_ids=[4007], enable=False) # Move_GoUp
        self.set_breakable(trigger_ids=[4008], enable=False) # Move_GoUp
        self.set_breakable(trigger_ids=[4009], enable=False) # Move_GoUp
        self.set_breakable(trigger_ids=[4010], enable=False) # Move_GoUp
        self.set_breakable(trigger_ids=[4011], enable=False) # Move_GoUp
        self.set_breakable(trigger_ids=[4012], enable=False) # Move_GoUp
        self.set_breakable(trigger_ids=[4013], enable=False) # Move_GoUp
        self.set_breakable(trigger_ids=[4014], enable=False) # Move_GoUp
        self.set_breakable(trigger_ids=[4015], enable=False) # Move_GoUp
        self.set_breakable(trigger_ids=[4016], enable=False) # Move_GoUp
        self.set_breakable(trigger_ids=[4017], enable=False) # Move_GoUp
        self.set_breakable(trigger_ids=[4018], enable=False) # Move_GoUp
        self.set_breakable(trigger_ids=[4019], enable=False) # Move_GoUp
        self.set_breakable(trigger_ids=[4020], enable=False) # Move_GoUp
        self.set_breakable(trigger_ids=[4021], enable=False) # Move_GoUp
        self.set_visible_breakable_object(trigger_ids=[4000], visible=False) # Move_GoUp
        self.set_visible_breakable_object(trigger_ids=[4001], visible=False) # Move_GoUp
        self.set_visible_breakable_object(trigger_ids=[4002], visible=False) # Move_GoUp
        self.set_visible_breakable_object(trigger_ids=[4003], visible=False) # Move_GoUp
        self.set_visible_breakable_object(trigger_ids=[4004], visible=False) # Move_GoUp
        self.set_visible_breakable_object(trigger_ids=[4005], visible=False) # Move_GoUp
        self.set_visible_breakable_object(trigger_ids=[4006], visible=False) # Move_GoUp
        self.set_visible_breakable_object(trigger_ids=[4007], visible=False) # Move_GoUp
        self.set_visible_breakable_object(trigger_ids=[4008], visible=False) # Move_GoUp
        self.set_visible_breakable_object(trigger_ids=[4009], visible=False) # Move_GoUp
        self.set_visible_breakable_object(trigger_ids=[4010], visible=False) # Move_GoUp
        self.set_visible_breakable_object(trigger_ids=[4011], visible=False) # Move_GoUp
        self.set_visible_breakable_object(trigger_ids=[4012], visible=False) # Move_GoUp
        self.set_visible_breakable_object(trigger_ids=[4013], visible=False) # Move_GoUp
        self.set_visible_breakable_object(trigger_ids=[4014], visible=False) # Move_GoUp
        self.set_visible_breakable_object(trigger_ids=[4015], visible=False) # Move_GoUp
        self.set_visible_breakable_object(trigger_ids=[4016], visible=False) # Move_GoUp
        self.set_visible_breakable_object(trigger_ids=[4017], visible=False) # Move_GoUp
        self.set_visible_breakable_object(trigger_ids=[4018], visible=False) # Move_GoUp
        self.set_visible_breakable_object(trigger_ids=[4019], visible=False) # Move_GoUp
        self.set_visible_breakable_object(trigger_ids=[4020], visible=False) # Move_GoUp
        self.set_visible_breakable_object(trigger_ids=[4021], visible=False) # Move_GoUp
        self.set_agent(trigger_ids=[8000], visible=False)
        self.set_agent(trigger_ids=[8001], visible=False)
        self.set_agent(trigger_ids=[8002], visible=False)
        self.set_agent(trigger_ids=[8003], visible=False)
        self.set_agent(trigger_ids=[8004], visible=False)
        self.set_agent(trigger_ids=[8005], visible=False)
        self.set_agent(trigger_ids=[8006], visible=False)
        self.set_agent(trigger_ids=[8007], visible=False)
        self.set_agent(trigger_ids=[8008], visible=False)
        self.set_agent(trigger_ids=[8009], visible=False)
        self.set_agent(trigger_ids=[8010], visible=False)
        self.set_agent(trigger_ids=[8011], visible=False)
        self.set_agent(trigger_ids=[8012], visible=False)
        self.set_agent(trigger_ids=[8013], visible=False)
        self.set_agent(trigger_ids=[8014], visible=False)
        self.set_agent(trigger_ids=[8015], visible=False)
        self.set_agent(trigger_ids=[8016], visible=False)
        self.set_agent(trigger_ids=[8017], visible=False)
        self.set_agent(trigger_ids=[8018], visible=False)
        self.set_agent(trigger_ids=[8019], visible=False)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=3000):
            return EmergencyPortalOn(self.ctx)


class EmergencyPortalOn(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_portal(portal_id=20, visible=True, enable=True, minimap_visible=False) # Emergency


# 좌우 상단 입장 시
class AgentOff01(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_agent(trigger_ids=[8000], visible=False)
        self.set_agent(trigger_ids=[8001], visible=False)
        self.set_agent(trigger_ids=[8002], visible=False)
        self.set_agent(trigger_ids=[8003], visible=False)
        self.set_agent(trigger_ids=[8004], visible=False)
        self.set_agent(trigger_ids=[8005], visible=False)
        self.set_agent(trigger_ids=[8006], visible=False)
        self.set_agent(trigger_ids=[8007], visible=False)
        self.set_agent(trigger_ids=[8008], visible=False)
        self.set_agent(trigger_ids=[8009], visible=False)
        self.set_agent(trigger_ids=[8010], visible=False)
        self.set_agent(trigger_ids=[8011], visible=False)
        self.set_agent(trigger_ids=[8012], visible=False)
        self.set_agent(trigger_ids=[8013], visible=False)
        self.set_agent(trigger_ids=[8014], visible=False)
        self.set_agent(trigger_ids=[8015], visible=False)
        self.set_agent(trigger_ids=[8016], visible=False)
        self.set_agent(trigger_ids=[8017], visible=False)
        self.set_agent(trigger_ids=[8018], visible=False)
        self.set_agent(trigger_ids=[8019], visible=False)


initial_state = Wait
