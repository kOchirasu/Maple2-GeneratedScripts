""" trigger/02000543_bf/main.xml """
from common import *
import state


#  플레이어 감지 
class idle(state.State):
    def on_enter(self):
        set_ambient_light(primary=[17,196,181], secondary=[0,0,0])
        set_mesh(triggerIds=[5000,5001], visible=True)
        set_portal(portalId=2, visible=False, enabled=False, minimapVisible=False)
        enable_spawn_point_pc(spawnId=0, isEnable=True)
        enable_spawn_point_pc(spawnId=1, isEnable=False)
        set_effect(triggerIds=[3000], visible=False)
        set_effect(triggerIds=[3002], visible=False)
        set_effect(triggerIds=[3001], visible=False)
        set_effect(triggerIds=[3003], visible=False)
        set_effect(triggerIds=[3004], visible=False)
        set_effect(triggerIds=[3005], visible=False)
        set_skill(triggerIds=[4000], isEnable=False)
        set_skill(triggerIds=[4001], isEnable=False)
        set_onetime_effect(id=1, enable=False, path='BG/Common/ScreenMask/Eff_fadein_1sec.xml')
        set_onetime_effect(id=101, enable=False, path='BG/Common/Eff_Com_Vibrate_Short.xml')
        set_onetime_effect(id=102, enable=False, path='BG/Common/Eff_Com_Vibrate_Short.xml')
        set_onetime_effect(id=103, enable=False, path='BG/Common/Eff_Com_Vibrate_Short.xml')
        set_onetime_effect(id=104, enable=False, path='BG/Common/Eff_Com_Vibrate_Short.xml')
        set_onetime_effect(id=105, enable=False, path='BG/Common/Eff_Com_Vibrate_Short.xml')
        set_onetime_effect(id=106, enable=False, path='BG/Common/Eff_Com_Vibrate_Short.xml')

    def on_tick(self) -> state.State:
        if user_detected(boxIds=[703], jobCode=0):
            return 뒤큐브날리기전()


class 뒤큐브날리기전(state.State):
    def on_enter(self):
        set_skill(triggerIds=[4000], isEnable=True)
        create_monster(spawnIds=[104,105,110], arg2=False)
        set_onetime_effect(id=101, enable=True, path='BG/Common/Eff_Com_Vibrate_Short.xml')

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=500):
            return 뒤큐브날리기()


class 뒤큐브날리기(state.State):
    def on_enter(self):
        set_effect(triggerIds=[3001], visible=True)
        side_npc_talk(npcId=11004644, illust='SlaveMan3_normal', duration=3000, script='$02000543_BF__MAIN__0$')

    def on_tick(self) -> state.State:
        if user_detected(boxIds=[701], jobCode=0):
            return 게임안내()


class 게임안내(state.State):
    def on_enter(self):
        select_camera_path(pathIds=[7000], returnView=False)
        side_npc_talk(npcId=11004644, illust='SlaveMan3_normal', duration=3000, script='$02000543_BF__MAIN__1$')
        lock_my_pc(isLock=True)
        set_mesh(triggerIds=[5000,5001], visible=True)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=3000):
            return 게임안내2()


class 게임안내2(state.State):
    def on_enter(self):
        select_camera_path(pathIds=[7000], returnView=True)
        lock_my_pc(isLock=False)
        add_balloon_talk(spawnId=104, msg='$02000543_BF__MAIN__2$', duration=3500, delayTick=0)
        add_balloon_talk(spawnId=105, msg='$02000543_BF__MAIN__3$', duration=3500, delayTick=500)
        create_monster(spawnIds=[107], arg2=True)
        create_monster(spawnIds=[111], arg2=False)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=5000):
            return 카메라리셋()


class 카메라리셋(state.State):
    def on_enter(self):
        reset_camera(interpolationTime=1)
        create_monster(spawnIds=[106], arg2=True)
        create_monster(spawnIds=[112], arg2=False)
        side_npc_talk(npcId=11004644, illust='SlaveMan3_normal', duration=4000, script='$02000543_BF__MAIN__4$')

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=5000):
            return 게임설정()


class 게임설정(state.State):
    def on_enter(self):
        side_npc_talk(npcId=21450036, illust='DesertDragonMagicGreen_normal', duration=4000, script='$02000543_BF__MAIN__5$')
        set_onetime_effect(id=101, enable=False, path='BG/Common/Eff_Com_Vibrate_Short.xml')
        set_effect(triggerIds=[3002], visible=True)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=3000):
            return 조건체크몬스터스폰1()


class 조건체크몬스터스폰1(state.State):
    def on_enter(self):
        destroy_monster(spawnIds=[110])
        set_event_ui(type=1, arg2='$02000543_BF__MAIN__6$', arg3='3000')
        set_onetime_effect(id=104, enable=True, path='BG/Common/Eff_Com_Vibrate_Short.xml')

    def on_tick(self) -> state.State:
        if user_value(key='main', value=4):
            return 조건체크몬스터스폰2()


class 조건체크몬스터스폰2(state.State):
    def on_tick(self) -> state.State:
        if wait_tick(waitTick=10000):
            return 조건체크몬스터스폰3()


class 조건체크몬스터스폰3(state.State):
    def on_enter(self):
        create_monster(spawnIds=[108], arg2=True)

    def on_tick(self) -> state.State:
        if monster_dead(boxIds=[108]):
            return 단계가기전1_2()


class 단계가기전1_2(state.State):
    def on_tick(self) -> state.State:
        if wait_tick(waitTick=2000):
            return 단계가기전2_2()


class 단계가기전2_2(state.State):
    def on_enter(self):
        set_event_ui(type=1, arg2='$02000543_BF__MAIN__7$', arg3='3000')

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=1000):
            set_ai_extra_data(key='phaseSecond', value=1)
            return 단계2()


class 단계2(state.State):
    def on_enter(self):
        set_effect(triggerIds=[3000], visible=True)

    def on_tick(self) -> state.State:
        if user_value(key='main', value=5):
            return 단계시작2()


class 단계시작2(state.State):
    def on_enter(self):
        set_onetime_effect(id=103, enable=True, path='BG/Common/Eff_Com_Vibrate_Short.xml')

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=10000):
            return 단계조건체크몬스터2()


class 단계조건체크몬스터2(state.State):
    def on_enter(self):
        create_monster(spawnIds=[109], arg2=True)
        add_balloon_talk(spawnId=107, msg='$02000543_BF__MAIN__8$', duration=3500, delayTick=500)

    def on_tick(self) -> state.State:
        if monster_dead(boxIds=[109]):
            return 단계시작전1_3()


class 단계시작전1_3(state.State):
    def on_tick(self) -> state.State:
        if wait_tick(waitTick=2000):
            return 단계시작전2_3()


class 단계시작전2_3(state.State):
    def on_tick(self) -> state.State:
        if wait_tick(waitTick=1000):
            set_ai_extra_data(key='phaseSecond', value=5)
            set_ai_extra_data(key='phase', value=5)
            return 단계3()


class 단계3(state.State):
    def on_enter(self):
        set_event_ui(type=1, arg2='$02000543_BF__MAIN__9$', arg3='3000')

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=3000):
            return 조건체크몬스터스폰()


class 조건체크몬스터스폰(state.State):
    def on_enter(self):
        side_npc_talk(npcId=21450036, illust='DesertDragonMagicGreen_normal', duration=4000, script='$02000543_BF__MAIN__10$')

    def on_tick(self) -> state.State:
        if user_value(key='main', value=8):
            return 응접실문열기전몬스터스폰()


class 응접실문열기전몬스터스폰(state.State):
    def on_enter(self):
        create_monster(spawnIds=[101,102], arg2=True)

    def on_tick(self) -> state.State:
        if monster_dead(boxIds=[101,102]):
            return 응접실문대기()


class 응접실문대기(state.State):
    def on_enter(self):
        set_ambient_light(primary=[201,38,70], secondary=[0,0,0])
        set_onetime_effect(id=106, enable=True, path='BG/Common/Eff_Com_Vibrate_Short.xml')
        set_event_ui(type=1, arg2='$02000543_BF__MAIN__11$', arg3='3000')
        destroy_monster(spawnIds=[106,107])

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=3000):
            return 응접실문열기1()


class 응접실문열기1(state.State):
    def on_enter(self):
        set_effect(triggerIds=[3003], visible=True)
        lock_my_pc(isLock=True)
        side_npc_talk(npcId=21450036, illust='DesertDragonMagicGreen_normal', duration=3000, script='$02000543_BF__MAIN__12$')

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=3000):
            return 응접실문열기11()


class 응접실문열기11(state.State):
    def on_enter(self):
        set_effect(triggerIds=[3000], visible=False)
        set_effect(triggerIds=[3002], visible=False)
        set_effect(triggerIds=[3004], visible=True)
        set_effect(triggerIds=[3005], visible=True)
        side_npc_talk(npcId=21450036, illust='DesertDragonMagicGreen_normal', duration=4000, script='$02000543_BF__MAIN__13$')

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=3000):
            return 응접실문열기31()


class 응접실문열기31(state.State):
    def on_enter(self):
        set_event_ui(type=1, arg2='$02000543_BF__MAIN__14$', arg3='3000')
        destroy_monster(spawnIds=[111,112])
        set_effect(triggerIds=[3004], visible=False)
        set_effect(triggerIds=[3005], visible=False)
        lock_my_pc(isLock=False)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=3000):
            return 응접실문열기4()


class 응접실문열기4(state.State):
    def on_enter(self):
        set_onetime_effect(id=102, enable=True, path='BG/Common/Eff_Com_Vibrate_Short.xml')
        set_skill(triggerIds=[4001], isEnable=True)
        set_effect(triggerIds=[3003], visible=False)
        add_balloon_talk(spawnId=104, msg='$02000543_BF__MAIN__15$', duration=3500)
        add_balloon_talk(spawnId=105, msg='$02000543_BF__MAIN__16$', duration=3500)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=4000):
            return 응접실문열고나서처리()


class 응접실문열고나서처리(state.State):
    def on_enter(self):
        side_npc_talk(npcId=11004644, illust='SlaveMan3_normal', duration=4000, script='$02000543_BF__MAIN__17$')
        destroy_monster(spawnIds=[104,105])
        enable_spawn_point_pc(spawnId=0, isEnable=False)
        enable_spawn_point_pc(spawnId=1, isEnable=True)

    def on_tick(self) -> state.State:
        if user_detected(boxIds=[702], jobCode=0):
            return 보스스폰()


class 보스스폰(state.State):
    def on_enter(self):
        set_onetime_effect(id=102, enable=False, path='BG/Common/Eff_Com_Vibrate_Short.xml')
        set_onetime_effect(id=103, enable=True, path='BG/Common/Eff_Com_Vibrate_Short.xml')

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=1000):
            return 보스스폰2()


class 보스스폰2(state.State):
    def on_enter(self):
        set_onetime_effect(id=103, enable=False, path='BG/Common/Eff_Com_Vibrate_Short.xml')
        create_monster(spawnIds=[103], arg2=True)

    def on_tick(self) -> state.State:
        if monster_dead(boxIds=[103]):
            return 포탈열기()


class 포탈열기(state.State):
    def on_enter(self):
        set_portal(portalId=2, visible=True, enabled=True, minimapVisible=True)


