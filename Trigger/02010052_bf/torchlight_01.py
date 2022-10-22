""" trigger/02010052_bf/torchlight_01.xml """
from common import *
import state


class idle(state.State):
    def on_enter(self):
        set_effect(triggerIds=[81001], visible=False) # 얼음이 녹는 이펙트
        set_effect(triggerIds=[81002], visible=False) # 얼음이 녹는 이펙트
        set_effect(triggerIds=[81003], visible=False) # 얼음이 녹는 이펙트
        set_effect(triggerIds=[81004], visible=False) # 얼음이 녹는 이펙트
        set_effect(triggerIds=[81005], visible=False) # 얼음이 녹는 이펙트

    def on_tick(self) -> state.State:
        if monster_dead(boxIds=[101]):
            return burn_state()


class burn_state(state.State):
    def on_enter(self):
        set_mesh(triggerIds=[6001,6002,6003,6004,6005,6006,6007,6008,6009,6010,6011,6012], visible=False, arg3=800, arg4=100, arg5=0) # 벽 해제
        set_event_ui(type=1, arg2='$02010052_BF__TORCHLIGHT_01__0$', arg3='3000')
        set_effect(triggerIds=[7001], visible=True) # 횃불에 불이 붙는 이펙트
        set_timer(timerId='1', seconds=1, display=False)

    def on_tick(self) -> state.State:
        if time_expired(timerId='1'):
            return spawn_state()


class spawn_state(state.State):
    def on_enter(self):
        hide_guide_summary(entityId=200)
        set_effect(triggerIds=[7501], visible=True) # 얼음 녹는 소리
        set_effect(triggerIds=[81001], visible=True) # 얼음이 녹는 이펙트
        set_effect(triggerIds=[81002], visible=True) # 얼음이 녹는 이펙트
        set_effect(triggerIds=[81003], visible=True) # 얼음이 녹는 이펙트
        set_effect(triggerIds=[81004], visible=True) # 얼음이 녹는 이펙트
        set_effect(triggerIds=[81005], visible=True) # 얼음이 녹는 이펙트
        set_actor(triggerId=8101, visible=False, initialSequence='Dmg_A')
        set_actor(triggerId=8102, visible=False, initialSequence='Dmg_A')
        set_actor(triggerId=8103, visible=False, initialSequence='Dmg_A')
        set_actor(triggerId=8104, visible=False, initialSequence='Dmg_A')
        set_actor(triggerId=8105, visible=False, initialSequence='Dmg_A')
        create_monster(spawnIds=[311,312,313,314,315], arg2=True) # 얼음이 녹으며 등장하는 몬스터들


