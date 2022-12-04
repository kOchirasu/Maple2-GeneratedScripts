""" trigger/02000533_bf/main.xml """
import trigger_api


# 플레이어 감지
class idle(trigger_api.Trigger):
    def on_enter(self):
        self.set_mesh(triggerIds=[901], visible=True)
        self.set_mesh(triggerIds=[3000,3001,3002,3003], visible=True)
        self.set_interact_object(triggerIds=[10003144], state=0)
        self.set_portal(portalId=2, visible=False)
        self.set_effect(triggerIds=[7000], visible=False)
        self.create_monster(spawnIds=[603,604,605,606], animationEffect=True)
        self.move_npc(spawnId=603, patrolName='MS2PatrolData_5003')
        self.move_npc(spawnId=604, patrolName='MS2PatrolData_5004')
        self.move_npc(spawnId=605, patrolName='MS2PatrolData_5005')
        self.move_npc(spawnId=606, patrolName='MS2PatrolData_5006')

    def on_tick(self) -> trigger_api.Trigger:
        if self.user_detected(boxIds=[701], jobCode=0):
            return 출입문부시기(self.ctx)


class 출입문부시기(trigger_api.Trigger):
    def on_enter(self):
        self.set_portal(portalId=2, visible=False)
        self.side_npc_talk(npcId=11004639, illust='Jay_normal', duration=3000, script='$02000533_BF__MAIN__0$')

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=2000):
            return 출입문부시기2(self.ctx)


class 출입문부시기2(trigger_api.Trigger):
    def on_enter(self):
        self.set_event_ui(type=1, arg2='$02000533_BF__MAIN__1$', arg3='3000')
        self.create_monster(spawnIds=[508], animationEffect=True)

    def on_tick(self) -> trigger_api.Trigger:
        if self.monster_dead(boxIds=[508]):
            return 시작(self.ctx)


class 시작(trigger_api.Trigger):
    def on_enter(self):
        self.set_effect(triggerIds=[7000], visible=True)
        self.set_mesh(triggerIds=[3000,3001,3002,3003], visible=False)
        self.create_monster(spawnIds=[501,502], animationEffect=True)
        self.add_balloon_talk(spawnId=501, msg='$02000533_BF__MAIN__2$', duration=3500, delayTick=0)
        self.side_npc_talk(npcId=21450001, illust='Mafia1_normal', duration=4000, script='$02000533_BF__MAIN__3$')

    def on_tick(self) -> trigger_api.Trigger:
        if self.user_detected(boxIds=[704], jobCode=0):
            return 층으로22_3(self.ctx)


class 층으로22_3(trigger_api.Trigger):
    def on_enter(self):
        self.create_monster(spawnIds=[503,5503], animationEffect=True)
        self.side_npc_talk(npcId=11004639, illust='Jay_normal', duration=4000, script='$02000533_BF__MAIN__4$')

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=2000):
            return 층으로3_3(self.ctx)


class 층으로3_3(trigger_api.Trigger):
    def on_enter(self):
        self.create_monster(spawnIds=[504,5504,505,506,509], animationEffect=True)
        self.add_balloon_talk(spawnId=5504, msg='$02000533_BF__MAIN__5$', duration=3500, delayTick=2000)
        self.add_balloon_talk(spawnId=505, msg='$02000533_BF__MAIN__6$', duration=3500, delayTick=1000)

    def on_tick(self) -> trigger_api.Trigger:
        if self.monster_dead(boxIds=[501,502,503,504,5503,5504,505,506,509]):
            return 다죽이면(self.ctx)


class 다죽이면(trigger_api.Trigger):
    def on_enter(self):
        self.set_interact_object(triggerIds=[10003144], state=1)

    def on_tick(self) -> trigger_api.Trigger:
        if self.object_interacted(interactIds=[10003144], stateValue=0):
            return 문열기시도(self.ctx)


class 문열기시도(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=1000):
            return 문열기게임(self.ctx)


class 문열기게임(trigger_api.Trigger):
    def on_enter(self):
        self.set_cinematic_ui(type=0)
        self.set_cinematic_ui(type=2)
        self.side_npc_talk(npcId=11004639, illust='Jay_normal', duration=4000, script='$02000533_BF__MAIN__7$')
        self.set_user_value(key='GameLogicEnd', value=999)
        self.widget_action(type='Round', func='InitWidgetRound')
        self.set_user_value(triggerId=9002, key='GameLogicStart', value=999)
        self.lock_my_pc(isLock=True)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=4000):
            return 문열기시작2(self.ctx)


class 문열기시작2(trigger_api.Trigger):
    def on_enter(self):
        self.set_event_ui(type=1, arg2='$02000533_BF__MAIN__8$', arg3='4000')
        self.lock_my_pc(isLock=True)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=4000):
            self.set_user_value(triggerId=9002, key='GameLogicStart', value=1)
            return 게임로직종료대기(self.ctx)


class 게임로직종료대기(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.user_value(key='GameLogicEnd', value=1):
            return 게임로직종료및성공(self.ctx)
        if self.user_value(key='GameLogicEnd', value=2):
            return 게임로직종료및실패(self.ctx)


class 게임로직종료및성공(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.true():
            return 게임로직종료(self.ctx)


class 게임로직종료및실패(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.true():
            return 실패게임로직종료(self.ctx)


class 게임로직종료(trigger_api.Trigger):
    def on_enter(self):
        self.set_event_ui(type=1, arg2='$02000533_BF__MAIN__9$', arg3='3000')
        self.lock_my_pc(isLock=False)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=3000):
            return 이동하자(self.ctx)


class 실패게임로직종료(trigger_api.Trigger):
    def on_enter(self):
        self.set_event_ui(type=1, arg2='$02000533_BF__MAIN__10$', arg3='3000')
        self.lock_my_pc(isLock=False)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=3000):
            return 문손으로부시기(self.ctx)


class 문손으로부시기(trigger_api.Trigger):
    def on_enter(self):
        self.set_scene_skip()
        self.set_cinematic_ui(type=1)
        self.set_cinematic_ui(type=3)
        self.lock_my_pc(isLock=False)
        self.add_cinematic_talk(npcId=0, msg='$02000533_BF__MAIN__11$', duration=3000)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=3000):
            return 문부시기안내(self.ctx)


class 문부시기안내(trigger_api.Trigger):
    def on_enter(self):
        self.set_cinematic_ui(type=0)
        self.set_cinematic_ui(type=2)
        self.set_event_ui(type=1, arg2='$02000533_BF__MAIN__12$', arg3='5000')

    def on_tick(self) -> trigger_api.Trigger:
        if self.monster_dead(boxIds=[507]):
            return 문을부시고이동(self.ctx)


class 문을부시고이동(trigger_api.Trigger):
    def on_enter(self):
        self.side_npc_talk(npcId=11004639, illust='Jay_normal', duration=4000, script='$02000533_BF__MAIN__13$')
        self.create_monster(spawnIds=[507], animationEffect=True)

    def on_tick(self) -> trigger_api.Trigger:
        if self.monster_dead(boxIds=[507]):
            return 문을부시고이동2(self.ctx)


class 문을부시고이동2(trigger_api.Trigger):
    def on_enter(self):
        self.set_mesh(triggerIds=[901], visible=False, arg3=1)
        self.set_portal(portalId=2, visible=True)
        self.lock_my_pc(isLock=False)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=3000):
            return 이동하자(self.ctx)


class 이동하자(trigger_api.Trigger):
    def on_enter(self):
        self.side_npc_talk(npcId=11004639, illust='Jay_normal', duration=4000, script='$02000533_BF__MAIN__14$')
        self.set_mesh(triggerIds=[901], visible=False, arg3=1)
        self.set_portal(portalId=2, visible=True)
        self.set_cinematic_ui(type=0)
        self.set_cinematic_ui(type=2)
        self.lock_my_pc(isLock=False)


initial_state = idle
