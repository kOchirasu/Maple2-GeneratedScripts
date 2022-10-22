""" trigger/02000532_bf/main.xml """
from common import *
import state


#  플레이어 감지 
class idle(state.State):
    def on_enter(self):
        set_mesh(triggerIds=[3000,3001], visible=True)
        set_mesh(triggerIds=[3002,3003], visible=True)
        set_mesh(triggerIds=[3004], visible=True)
        set_portal(portalId=1, visible=False, enabled=False, minimapVisible=False)
        set_effect(triggerIds=[7001], visible=False)
        set_effect(triggerIds=[7006], visible=False)
        set_effect(triggerIds=[7007], visible=False)

    def on_tick(self) -> state.State:
        if user_detected(boxIds=[701], jobCode=0):
            return ready()


class ready(state.State):
    def on_enter(self):
        set_onetime_effect(id=1, enable=True, path='BG/Common/ScreenMask/Eff_fadein_1sec.xml')
        set_cinematic_ui(type=1)
        set_cinematic_ui(type=3)
        set_scene_skip()
        create_monster(spawnIds=[216,101,102,103,104,105,106,107,108,109,111,112,113], arg2=True)
        create_monster(spawnIds=[110,111], arg2=True)
        move_npc(spawnId=110, patrolName='MS2PatrolData_8000')
        move_npc(spawnId=111, patrolName='MS2PatrolData_8001')
        set_portal(portalId=1, visible=False, enabled=False, minimapVisible=False)
        set_mesh(triggerIds=[3000,3001], visible=True)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=1000):
            return start()


class start(state.State):
    def on_enter(self):
        set_scene_skip(state=목표, arg2='nextState')
        select_camera_path(pathIds=[604,603], returnView=True)
        set_onetime_effect(id=1, enable=False, path='BG/Common/ScreenMask/Eff_fadein_1sec.xml')
        show_caption(type='VerticalCaption', title='$02000532_BF__MAIN__0$', desc='$02000532_BF__MAIN__1$', align='centerRight', offsetRateX=0, offsetRateY=0, duration=3000, scale=2)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=6000):
            return 목표()


class 목표(state.State):
    def on_enter(self):
        set_cinematic_ui(type=0)
        set_cinematic_ui(type=2)
        lock_my_pc(isLock=False)
        reset_camera(interpolationTime=1)
        set_event_ui(type=1, arg2='$02000532_BF__MAIN__2$', arg3='3000')

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=3500):
            return 문들어가기()


class 문들어가기(state.State):
    def on_enter(self):
        set_cinematic_ui(type=0)
        set_cinematic_ui(type=2)
        set_event_ui(type=1, arg2='$02000532_BF__MAIN__3$', arg3='3000')
        set_effect(triggerIds=[7006], visible=True)
        set_effect(triggerIds=[7007], visible=True)
        create_monster(spawnIds=[408], arg2=True)

    def on_tick(self) -> state.State:
        if monster_dead(boxIds=[408], arg2=False):
            return 문이열림()


class 문이열림(state.State):
    def on_enter(self):
        set_mesh(triggerIds=[3004], visible=False)
        add_balloon_talk(spawnId=112, msg='$02000532_BF__MAIN__4$', duration=3500, delayTick=0)
        add_balloon_talk(spawnId=112, msg='$02000532_BF__MAIN__5$', duration=3500, delayTick=3500)
        add_balloon_talk(spawnId=102, msg='$02000532_BF__MAIN__6$', duration=3500, delayTick=500)
        add_balloon_talk(spawnId=113, msg='$02000532_BF__MAIN__7$', duration=3500, delayTick=900)
        set_npc_emotion_loop(spawnId=102, sequenceName='Talk_A', duration=10000)
        set_npc_emotion_loop(spawnId=113, sequenceName='Sit_Down_A', duration=10000)
        set_npc_emotion_loop(spawnId=112, sequenceName='Talk_A', duration=10000)
        set_effect(triggerIds=[7001], visible=True)
        set_mesh(triggerIds=[3000,3001], visible=False)
        set_scene_skip()

    def on_tick(self) -> state.State:
        if user_detected(boxIds=[702], jobCode=0):
            return 경계하기()


class 경계하기(state.State):
    def on_enter(self):
        set_cinematic_ui(type=1)
        set_cinematic_ui(type=3)
        lock_my_pc(isLock=True)
        set_scene_skip(state=흑성회의반격, arg2='nextState')
        add_balloon_talk(spawnId=104, msg='$02000532_BF__MAIN__8$', duration=3500, delayTick=0)
        add_balloon_talk(spawnId=105, msg='$02000532_BF__MAIN__9$', duration=3500, delayTick=2500)
        add_balloon_talk(spawnId=103, msg='$02000532_BF__MAIN__10$', duration=3500, delayTick=2800)
        set_effect(triggerIds=[7006], visible=False)
        set_effect(triggerIds=[7007], visible=False)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=6500):
            return 통신을받은제이부하()


class 통신을받은제이부하(state.State):
    def on_enter(self):
        select_camera_path(pathIds=[602], returnView=False)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=800):
            return 통신을받은제이부하2()


class 통신을받은제이부하2(state.State):
    def on_enter(self):
        add_balloon_talk(spawnId=205, msg='$02000532_BF__MAIN__11$', duration=3500, delayTick=500)
        add_balloon_talk(spawnId=300, msg='$02000532_BF__MAIN__12$', duration=3500, delayTick=3000)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=5000):
            return 불안한제이()


class 불안한제이(state.State):
    def on_enter(self):
        set_cinematic_ui(type=0)
        set_cinematic_ui(type=2)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=500):
            return 불안한제이2()


class 불안한제이2(state.State):
    def on_enter(self):
        side_npc_talk(npcId=11004639, illust='Jay_normal', duration=4000, script='$02000532_BF__MAIN__13$')
        add_balloon_talk(spawnId=205, msg='$02000532_BF__MAIN__14$', duration=3500, delayTick=4100)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=6000):
            return 흑성회의반격()


class 흑성회의반격(state.State):
    def on_enter(self):
        set_cinematic_ui(type=0)
        set_cinematic_ui(type=2)
        set_mesh(triggerIds=[3002,3003], visible=False)
        lock_my_pc(isLock=False)
        reset_camera(interpolationTime=1)
        set_event_ui(type=1, arg2='$02000532_BF__MAIN__15$', arg3='3000')

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=1000):
            return 흑성회의반격2()


class 흑성회의반격2(state.State):
    def on_enter(self):
        destroy_monster(spawnIds=[101,102,103,104,105,106,107,110,111,112,113])
        create_monster(spawnIds=[401,402,403,404,412,405], arg2=True)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=1000):
            return 흑성회의반격22()


class 흑성회의반격22(state.State):
    def on_enter(self):
        side_npc_talk(npcId=21450001, illust='Mafia1_normal', duration=3000, script='$02000532_BF__MAIN__16$')

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=3000):
            return 골목체크()


class 골목체크(state.State):
    def on_enter(self):
        side_npc_talk(npcId=11004639, illust='Jay_normal', duration=3000, script='$02000532_BF__MAIN__17$')

    def on_tick(self) -> state.State:
        if user_detected(boxIds=[705], jobCode=0):
            return 길목에서나오는몬스터()


class 길목에서나오는몬스터(state.State):
    def on_enter(self):
        destroy_monster(spawnIds=[108,109])
        create_monster(spawnIds=[406,407,409,410,411], arg2=True)
        add_balloon_talk(spawnId=409, msg='$02000532_BF__MAIN__18$', duration=3500, delayTick=1500)
        add_balloon_talk(spawnId=410, msg='$02000532_BF__MAIN__19$', duration=3500, delayTick=1500)
        add_balloon_talk(spawnId=407, msg='$02000532_BF__MAIN__20$', duration=3500, delayTick=500)

    def on_tick(self) -> state.State:
        if monster_dead(boxIds=[401,402,403,404,405,406,407,409,410,411,412]):
            return 차생성2()


class 차생성2(state.State):
    def on_enter(self):
        side_npc_talk(npcId=11004639, illust='Jay_normal', duration=3000, script='$02000532_BF__MAIN__21$')

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=3000):
            return 엘리베이터안내()


class 엘리베이터안내(state.State):
    def on_enter(self):
        set_event_ui(type=1, arg2='$02000532_BF__MAIN__22$', arg3='3000')
        set_portal(portalId=1, visible=True, enabled=True, minimapVisible=True)


