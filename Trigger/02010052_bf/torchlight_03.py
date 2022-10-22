""" trigger/02010052_bf/torchlight_03.xml """
from common import *
import state


class idle(state.State):
    def on_enter(self):
        set_actor(triggerId=20499, visible=False, initialSequence='Closed')
        set_actor(triggerId=20501, visible=True, initialSequence='Closed') # 얼어붙은 문
        set_mesh(triggerIds=[20500], visible=True, arg3=1, arg4=1, arg5=1) # 철문
        set_effect(triggerIds=[7002], visible=False) # 횃불에 불이 붙는 이펙트
        set_effect(triggerIds=[7003], visible=False) # 횃불에 불이 붙는 이펙트

    def on_tick(self) -> state.State:
        if monster_dead(boxIds=[102]):
            return burn_state_01()
        if monster_dead(boxIds=[103]):
            return burn_state_02()

    def on_exit(self):
        set_effect(triggerIds=[71001], visible=True)
        set_effect(triggerIds=[71002], visible=True)
        set_effect(triggerIds=[71003], visible=True)
        set_effect(triggerIds=[71004], visible=True)
        set_effect(triggerIds=[71005], visible=True)
        set_actor(triggerId=8001, visible=False, initialSequence='Dmg_A')
        set_actor(triggerId=8002, visible=False, initialSequence='Dmg_A')
        set_actor(triggerId=8003, visible=False, initialSequence='Dmg_A')
        set_actor(triggerId=8004, visible=False, initialSequence='Dmg_A')
        set_actor(triggerId=8005, visible=False, initialSequence='Dmg_A')
        create_monster(spawnIds=[301,302,303,304,305], arg2=False) # 기본 배치 될 몬스터 등장
        set_conversation(type=1, spawnId=993, script='$02010052_BF__TORCHLIGHT_03__0$', arg4=3) # 카나 말풍선 대사


class burn_state_01(state.State):
    def on_enter(self):
        set_effect(triggerIds=[7002], visible=True)

    def on_tick(self) -> state.State:
        if monster_dead(boxIds=[103]):
            return burn_state_complete()

    def on_exit(self):
        set_effect(triggerIds=[7003], visible=True)


class burn_state_02(state.State):
    def on_enter(self):
        set_effect(triggerIds=[7003], visible=True)

    def on_tick(self) -> state.State:
        if monster_dead(boxIds=[102]):
            return burn_state_complete()

    def on_exit(self):
        set_effect(triggerIds=[7002], visible=True)


class burn_state_complete(state.State):
    def on_enter(self):
        set_effect(triggerIds=[7503], visible=True) # 얼음 녹는 소리
        set_mesh(triggerIds=[6021,6022,6023,6024,6025,6026,6027,6028,6029,6030,6031,6032], visible=False, arg3=800, arg4=100, arg5=8) # 벽 해제
        set_conversation(type=1, spawnId=9999, script='$02010052_BF__TORCHLIGHT_03__1$', arg4=3) # 카나 말풍선 대사
        hide_guide_summary(entityId=200)
        set_event_ui(type=1, arg2='$02010052_BF__TORCHLIGHT_03__2$', arg3='3000')
        set_timer(timerId='1', seconds=1, display=False)

    def on_tick(self) -> state.State:
        if time_expired(timerId='1'):
            return spawn_state()


class spawn_state(state.State):
    def on_enter(self):
        show_guide_summary(entityId=299, textId=20105203) # 거대 다크 슬링을 처치하세요
        set_mesh(triggerIds=[5100,5101,5102,5103,5104,5105,5106,5107,5108,5109,5110], visible=False, arg3=800, arg4=100, arg5=8) # 카나 위에 있는 벽 해제
        set_effect(triggerIds=[7902], visible=True) # 카나 사라짐
        destroy_monster(spawnIds=[9999]) # 카나 사라짐
        set_actor(triggerId=8100, visible=False, initialSequence='Dmg_A')
        set_actor(triggerId=8006, visible=False, initialSequence='Dmg_A')
        set_actor(triggerId=8007, visible=False, initialSequence='Dmg_A')
        set_actor(triggerId=8008, visible=False, initialSequence='Dmg_A')
        set_actor(triggerId=8009, visible=False, initialSequence='Dmg_A')
        set_actor(triggerId=8010, visible=False, initialSequence='Dmg_A')
        create_monster(spawnIds=[199], arg2=True) # 얼음이 녹으며 등장하는 몬스터들 (중간)
        create_monster(spawnIds=[321,322,323,324,325], arg2=True) # 얼음이 녹으며 등장하는 몬스터들

    def on_tick(self) -> state.State:
        if monster_dead(boxIds=[199]):
            return monsterkill()

    def on_exit(self):
        hide_guide_summary(entityId=299)


class monsterkill(state.State):
    def on_enter(self):
        set_actor(triggerId=20499, visible=True, initialSequence='Opening')
        set_actor(triggerId=20501, visible=False, initialSequence='Closed') # 얼어붙은 문
        set_mesh(triggerIds=[20500], visible=False, arg3=0, arg4=0, arg5=0) # 철문


