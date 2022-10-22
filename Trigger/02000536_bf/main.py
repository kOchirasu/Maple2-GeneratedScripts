""" trigger/02000536_bf/main.xml """
from common import *
import state


#  플레이어 감지 
class idle(state.State):
    def on_enter(self):
        set_portal(portalId=2, visible=False, enabled=False, minimapVisible=False)
        create_monster(spawnIds=[501,502,504,505,506,507,508,509,510,511], arg2=False)
        set_interact_object(triggerIds=[10003147], state=0)
        set_mesh(triggerIds=[9999], visible=True)

    def on_tick(self) -> state.State:
        if user_detected(boxIds=[701], jobCode=0):
            return ready()


class ready(state.State):
    def on_enter(self):
        set_portal(portalId=2, visible=False, enabled=False, minimapVisible=False)
        set_onetime_effect(id=1, enable=True, path='BG/Common/ScreenMask/Eff_fadein_1sec.xml')
        set_cinematic_ui(type=1)
        set_cinematic_ui(type=3)
        set_scene_skip()
        create_monster(spawnIds=[102], arg2=False)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=1000):
            return start()


class start(state.State):
    def on_enter(self):
        set_scene_skip(state=전투시작, arg2='nextState')
        select_camera_path(pathIds=[7000,7003], returnView=False)
        set_onetime_effect(id=1, enable=False, path='BG/Common/ScreenMask/Eff_fadein_1sec.xml')
        show_caption(type='VerticalCaption', title='$02000536_BF__MAIN__0$', desc='$02000536_BF__MAIN__1$', align='centerRight', offsetRateX=0, offsetRateY=0, duration=3000, scale=2)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=4000):
            return 하렌인사()


class 하렌인사(state.State):
    def on_enter(self):
        select_camera_path(pathIds=[7003,7001], returnView=False)
        set_npc_emotion_loop(spawnId=102, sequenceName='Bore_A', duration=5000)
        add_cinematic_talk(npcId=23300001, msg='$02000536_BF__MAIN__2$', align='center', duration=4000)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=4500):
            return 하렌인사2()


class 하렌인사2(state.State):
    def on_enter(self):
        set_npc_emotion_sequence(spawnId=102, sequenceName='Attack_01_E,Attack_01_B')
        add_cinematic_talk(npcId=23300001, msg='$02000536_BF__MAIN__3$', align='center', duration=4000)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=4000):
            return 전투시작()


class 전투시작(state.State):
    def on_enter(self):
        set_cinematic_ui(type=0)
        set_cinematic_ui(type=2)
        reset_camera(interpolationTime=1)
        set_event_ui(type=1, arg2='$02000536_BF__MAIN__4$', arg3='3000')
        create_monster(spawnIds=[101], arg2=False)
        destroy_monster(spawnIds=[102])

    def on_tick(self) -> state.State:
        if check_npc_hp(compare='lowerEqual', value=70, spawnId=101, isRelative=True):
            return 메이드군단을스폰()


class 메이드군단을스폰(state.State):
    def on_enter(self):
        create_monster(spawnIds=[301,302,303,304], arg2=False)
        side_npc_talk(npcId=23300001, illust='Haren_serious', duration=4000, script='$02000536_BF__MAIN__5$')

    def on_tick(self) -> state.State:
        if check_npc_hp(compare='lowerEqual', value=50, spawnId=101, isRelative=True):
            return 메이드군단을스폰2()


class 메이드군단을스폰2(state.State):
    def on_enter(self):
        create_monster(spawnIds=[401,402,403,404], arg2=False)

    def on_tick(self) -> state.State:
        if check_npc_hp(compare='lowerEqual', value=30, spawnId=101, isRelative=True):
            return 몬스터사망체크()


class 몬스터사망체크(state.State):
    def on_enter(self):
        side_npc_talk(npcId=23300001, illust='Haren_serious', duration=4000, script='$02000536_BF__MAIN__6$')
        create_monster(spawnIds=[201,202,203,204], arg2=False)

    def on_tick(self) -> state.State:
        if monster_dead(boxIds=[101]):
            return 던전클리어()


class 던전클리어(state.State):
    def on_enter(self):
        side_npc_talk(npcId=23300001, illust='Haren_serious', duration=3000, script='$02000536_BF__MAIN__8$')
        set_mesh(triggerIds=[9999], visible=False)
        destroy_monster(spawnIds=[-1])
        dungeon_clear() # 보스 잡히고 던전 클리어 선언 먼저

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=1000):
            return 트리거완료()


class 트리거완료(state.State):
    def on_enter(self):
        destroy_monster(spawnIds=[-1]) # 보스가 순삭 될 경우 트리거 타이밍이 어긋나서 소환몹 제거 안될 수 있기 때문에 혹시 몰라 최종 마지막에 몬스터 제거 명령 설정함
        set_portal(portalId=2, visible=True, enabled=True, minimapVisible=True) # 보스가 순삭될 경우 던전 클리어 선언되기 전에 포털로 나갈 우려가 있으므로 포털 오픈은 던전 클리어 이후 시점으로


