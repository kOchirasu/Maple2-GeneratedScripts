""" trigger/02000533_bf/main.xml """
from common import *
import state


#  플레이어 감지 
class idle(state.State):
    def on_enter(self):
        set_mesh(triggerIds=[901], visible=True)
        set_mesh(triggerIds=[3000,3001,3002,3003], visible=True)
        set_interact_object(triggerIds=[10003144], state=0)
        set_portal(portalId=2, visible=False)
        set_effect(triggerIds=[7000], visible=False)
        create_monster(spawnIds=[603,604,605,606], arg2=True)
        move_npc(spawnId=603, patrolName='MS2PatrolData_5003')
        move_npc(spawnId=604, patrolName='MS2PatrolData_5004')
        move_npc(spawnId=605, patrolName='MS2PatrolData_5005')
        move_npc(spawnId=606, patrolName='MS2PatrolData_5006')

    def on_tick(self) -> state.State:
        if user_detected(boxIds=[701], jobCode=0):
            return 출입문부시기()


class 출입문부시기(state.State):
    def on_enter(self):
        set_portal(portalId=2, visible=False)
        side_npc_talk(npcId=11004639, illust='Jay_normal', duration=3000, script='$02000533_BF__MAIN__0$')

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=2000):
            return 출입문부시기2()


class 출입문부시기2(state.State):
    def on_enter(self):
        set_event_ui(type=1, arg2='$02000533_BF__MAIN__1$', arg3='3000')
        create_monster(spawnIds=[508], arg2=True)

    def on_tick(self) -> state.State:
        if monster_dead(boxIds=[508]):
            return 시작()


class 시작(state.State):
    def on_enter(self):
        set_effect(triggerIds=[7000], visible=True)
        set_mesh(triggerIds=[3000,3001,3002,3003], visible=False)
        create_monster(spawnIds=[501,502], arg2=True)
        add_balloon_talk(spawnId=501, msg='$02000533_BF__MAIN__2$', duration=3500, delayTick=0)
        side_npc_talk(npcId=21450001, illust='Mafia1_normal', duration=4000, script='$02000533_BF__MAIN__3$')

    def on_tick(self) -> state.State:
        if user_detected(boxIds=[704], jobCode=0):
            return 층으로22_3()


class 층으로22_3(state.State):
    def on_enter(self):
        create_monster(spawnIds=[503,5503], arg2=True)
        side_npc_talk(npcId=11004639, illust='Jay_normal', duration=4000, script='$02000533_BF__MAIN__4$')

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=2000):
            return 층으로3_3()


class 층으로3_3(state.State):
    def on_enter(self):
        create_monster(spawnIds=[504,5504,505,506,509], arg2=True)
        add_balloon_talk(spawnId=5504, msg='$02000533_BF__MAIN__5$', duration=3500, delayTick=2000)
        add_balloon_talk(spawnId=505, msg='$02000533_BF__MAIN__6$', duration=3500, delayTick=1000)

    def on_tick(self) -> state.State:
        if monster_dead(boxIds=[501,502,503,504,5503,5504,505,506,509]):
            return 다죽이면()


class 다죽이면(state.State):
    def on_enter(self):
        set_interact_object(triggerIds=[10003144], state=1)

    def on_tick(self) -> state.State:
        if object_interacted(interactIds=[10003144], arg2=0):
            return 문열기시도()


class 문열기시도(state.State):
    def on_tick(self) -> state.State:
        if wait_tick(waitTick=1000):
            return 문열기게임()


class 문열기게임(state.State):
    def on_enter(self):
        set_cinematic_ui(type=0)
        set_cinematic_ui(type=2)
        side_npc_talk(npcId=11004639, illust='Jay_normal', duration=4000, script='$02000533_BF__MAIN__7$')
        set_user_value(key='GameLogicEnd', value=999)
        widget_action(type='Round', func='InitWidgetRound')
        set_user_value(triggerId=9002, key='GameLogicStart', value=999)
        lock_my_pc(isLock=True)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=4000):
            return 문열기시작2()


class 문열기시작2(state.State):
    def on_enter(self):
        set_event_ui(type=1, arg2='$02000533_BF__MAIN__8$', arg3='4000')
        lock_my_pc(isLock=True)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=4000):
            set_user_value(triggerId=9002, key='GameLogicStart', value=1)
            return 게임로직종료대기()


class 게임로직종료대기(state.State):
    def on_tick(self) -> state.State:
        if user_value(key='GameLogicEnd', value=1):
            return 게임로직종료및성공()
        if user_value(key='GameLogicEnd', value=2):
            return 게임로직종료및실패()


class 게임로직종료및성공(state.State):
    def on_tick(self) -> state.State:
        if true():
            return 게임로직종료()


class 게임로직종료및실패(state.State):
    def on_tick(self) -> state.State:
        if true():
            return 실패게임로직종료()


class 게임로직종료(state.State):
    def on_enter(self):
        set_event_ui(type=1, arg2='$02000533_BF__MAIN__9$', arg3='3000')
        lock_my_pc(isLock=False)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=3000):
            return 이동하자()


class 실패게임로직종료(state.State):
    def on_enter(self):
        set_event_ui(type=1, arg2='$02000533_BF__MAIN__10$', arg3='3000')
        lock_my_pc(isLock=False)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=3000):
            return 문손으로부시기()


class 문손으로부시기(state.State):
    def on_enter(self):
        set_scene_skip()
        set_cinematic_ui(type=1)
        set_cinematic_ui(type=3)
        lock_my_pc(isLock=False)
        add_cinematic_talk(npcId=0, msg='$02000533_BF__MAIN__11$', duration=3000)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=3000):
            return 문부시기안내()


class 문부시기안내(state.State):
    def on_enter(self):
        set_cinematic_ui(type=0)
        set_cinematic_ui(type=2)
        set_event_ui(type=1, arg2='$02000533_BF__MAIN__12$', arg3='5000')

    def on_tick(self) -> state.State:
        if monster_dead(boxIds=[507]):
            return 문을부시고이동()


class 문을부시고이동(state.State):
    def on_enter(self):
        side_npc_talk(npcId=11004639, illust='Jay_normal', duration=4000, script='$02000533_BF__MAIN__13$')
        create_monster(spawnIds=[507], arg2=True)

    def on_tick(self) -> state.State:
        if monster_dead(boxIds=[507]):
            return 문을부시고이동2()


class 문을부시고이동2(state.State):
    def on_enter(self):
        set_mesh(triggerIds=[901], visible=False, arg3=1)
        set_portal(portalId=2, visible=True)
        lock_my_pc(isLock=False)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=3000):
            return 이동하자()


class 이동하자(state.State):
    def on_enter(self):
        side_npc_talk(npcId=11004639, illust='Jay_normal', duration=4000, script='$02000533_BF__MAIN__14$')
        set_mesh(triggerIds=[901], visible=False, arg3=1)
        set_portal(portalId=2, visible=True)
        set_cinematic_ui(type=0)
        set_cinematic_ui(type=2)
        lock_my_pc(isLock=False)


