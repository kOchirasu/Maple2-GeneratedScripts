""" trigger/02000543_bf/main.xml """
import trigger_api


# 플레이어 감지
class idle(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_ambient_light(primary=[17,196,181], secondary=[0,0,0])
        self.set_mesh(triggerIds=[5000,5001], visible=True)
        self.set_portal(portalId=2, visible=False, enable=False, minimapVisible=False)
        self.enable_spawn_point_pc(spawnId=0, isEnable=True)
        self.enable_spawn_point_pc(spawnId=1, isEnable=False)
        self.set_effect(triggerIds=[3000], visible=False)
        self.set_effect(triggerIds=[3002], visible=False)
        self.set_effect(triggerIds=[3001], visible=False)
        self.set_effect(triggerIds=[3003], visible=False)
        self.set_effect(triggerIds=[3004], visible=False)
        self.set_effect(triggerIds=[3005], visible=False)
        self.set_skill(triggerIds=[4000], enable=False)
        self.set_skill(triggerIds=[4001], enable=False)
        self.set_onetime_effect(id=1, enable=False, path='BG/Common/ScreenMask/Eff_fadein_1sec.xml')
        self.set_onetime_effect(id=101, enable=False, path='BG/Common/Eff_Com_Vibrate_Short.xml')
        self.set_onetime_effect(id=102, enable=False, path='BG/Common/Eff_Com_Vibrate_Short.xml')
        self.set_onetime_effect(id=103, enable=False, path='BG/Common/Eff_Com_Vibrate_Short.xml')
        self.set_onetime_effect(id=104, enable=False, path='BG/Common/Eff_Com_Vibrate_Short.xml')
        self.set_onetime_effect(id=105, enable=False, path='BG/Common/Eff_Com_Vibrate_Short.xml')
        self.set_onetime_effect(id=106, enable=False, path='BG/Common/Eff_Com_Vibrate_Short.xml')

    def on_tick(self) -> trigger_api.Trigger:
        if self.user_detected(boxIds=[703], jobCode=0):
            return 뒤큐브날리기전(self.ctx)


class 뒤큐브날리기전(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_skill(triggerIds=[4000], enable=True)
        self.create_monster(spawnIds=[104,105,110], animationEffect=False)
        self.set_onetime_effect(id=101, enable=True, path='BG/Common/Eff_Com_Vibrate_Short.xml')

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=500):
            return 뒤큐브날리기(self.ctx)


class 뒤큐브날리기(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_effect(triggerIds=[3001], visible=True)
        self.side_npc_talk(npcId=11004644, illust='SlaveMan3_normal', duration=3000, script='$02000543_BF__MAIN__0$')

    def on_tick(self) -> trigger_api.Trigger:
        if self.user_detected(boxIds=[701], jobCode=0):
            return 게임안내(self.ctx)


class 게임안내(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.select_camera_path(pathIds=[7000], returnView=False)
        self.side_npc_talk(npcId=11004644, illust='SlaveMan3_normal', duration=3000, script='$02000543_BF__MAIN__1$')
        self.lock_my_pc(isLock=True)
        self.set_mesh(triggerIds=[5000,5001], visible=True)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=3000):
            return 게임안내2(self.ctx)


class 게임안내2(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.select_camera_path(pathIds=[7000], returnView=True)
        self.lock_my_pc(isLock=False)
        self.add_balloon_talk(spawnId=104, msg='$02000543_BF__MAIN__2$', duration=3500, delayTick=0)
        self.add_balloon_talk(spawnId=105, msg='$02000543_BF__MAIN__3$', duration=3500, delayTick=500)
        self.create_monster(spawnIds=[107], animationEffect=True)
        self.create_monster(spawnIds=[111], animationEffect=False)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=5000):
            return 카메라리셋(self.ctx)


class 카메라리셋(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.reset_camera(interpolationTime=1)
        self.create_monster(spawnIds=[106], animationEffect=True)
        self.create_monster(spawnIds=[112], animationEffect=False)
        self.side_npc_talk(npcId=11004644, illust='SlaveMan3_normal', duration=4000, script='$02000543_BF__MAIN__4$')

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=5000):
            return 게임설정(self.ctx)


class 게임설정(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.side_npc_talk(npcId=21450036, illust='DesertDragonMagicGreen_normal', duration=4000, script='$02000543_BF__MAIN__5$')
        self.set_onetime_effect(id=101, enable=False, path='BG/Common/Eff_Com_Vibrate_Short.xml')
        self.set_effect(triggerIds=[3002], visible=True)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=3000):
            return 조건체크몬스터스폰1(self.ctx)


class 조건체크몬스터스폰1(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.destroy_monster(spawnIds=[110])
        self.set_event_ui(type=1, arg2='$02000543_BF__MAIN__6$', arg3='3000')
        self.set_onetime_effect(id=104, enable=True, path='BG/Common/Eff_Com_Vibrate_Short.xml')

    def on_tick(self) -> trigger_api.Trigger:
        if self.user_value(key='main', value=4):
            return 조건체크몬스터스폰2(self.ctx)


class 조건체크몬스터스폰2(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=10000):
            return 조건체크몬스터스폰3(self.ctx)


class 조건체크몬스터스폰3(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.create_monster(spawnIds=[108], animationEffect=True)

    def on_tick(self) -> trigger_api.Trigger:
        if self.monster_dead(boxIds=[108]):
            return 단계가기전1_2(self.ctx)


class 단계가기전1_2(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=2000):
            return 단계가기전2_2(self.ctx)


class 단계가기전2_2(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_event_ui(type=1, arg2='$02000543_BF__MAIN__7$', arg3='3000')

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=1000):
            self.set_ai_extra_data(key='phaseSecond', value=1)
            return 단계2(self.ctx)


class 단계2(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_effect(triggerIds=[3000], visible=True)

    def on_tick(self) -> trigger_api.Trigger:
        if self.user_value(key='main', value=5):
            return 단계시작2(self.ctx)


class 단계시작2(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_onetime_effect(id=103, enable=True, path='BG/Common/Eff_Com_Vibrate_Short.xml')

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=10000):
            return 단계조건체크몬스터2(self.ctx)


class 단계조건체크몬스터2(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.create_monster(spawnIds=[109], animationEffect=True)
        self.add_balloon_talk(spawnId=107, msg='$02000543_BF__MAIN__8$', duration=3500, delayTick=500)

    def on_tick(self) -> trigger_api.Trigger:
        if self.monster_dead(boxIds=[109]):
            return 단계시작전1_3(self.ctx)


class 단계시작전1_3(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=2000):
            return 단계시작전2_3(self.ctx)


class 단계시작전2_3(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=1000):
            self.set_ai_extra_data(key='phaseSecond', value=5)
            self.set_ai_extra_data(key='phase', value=5)
            return 단계3(self.ctx)


class 단계3(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_event_ui(type=1, arg2='$02000543_BF__MAIN__9$', arg3='3000')

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=3000):
            return 조건체크몬스터스폰(self.ctx)


class 조건체크몬스터스폰(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.side_npc_talk(npcId=21450036, illust='DesertDragonMagicGreen_normal', duration=4000, script='$02000543_BF__MAIN__10$')

    def on_tick(self) -> trigger_api.Trigger:
        if self.user_value(key='main', value=8):
            return 응접실문열기전몬스터스폰(self.ctx)


class 응접실문열기전몬스터스폰(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.create_monster(spawnIds=[101,102], animationEffect=True)

    def on_tick(self) -> trigger_api.Trigger:
        if self.monster_dead(boxIds=[101,102]):
            return 응접실문대기(self.ctx)


class 응접실문대기(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_ambient_light(primary=[201,38,70], secondary=[0,0,0])
        self.set_onetime_effect(id=106, enable=True, path='BG/Common/Eff_Com_Vibrate_Short.xml')
        self.set_event_ui(type=1, arg2='$02000543_BF__MAIN__11$', arg3='3000')
        self.destroy_monster(spawnIds=[106,107])

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=3000):
            return 응접실문열기1(self.ctx)


class 응접실문열기1(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_effect(triggerIds=[3003], visible=True)
        self.lock_my_pc(isLock=True)
        self.side_npc_talk(npcId=21450036, illust='DesertDragonMagicGreen_normal', duration=3000, script='$02000543_BF__MAIN__12$')

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=3000):
            return 응접실문열기11(self.ctx)


class 응접실문열기11(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_effect(triggerIds=[3000], visible=False)
        self.set_effect(triggerIds=[3002], visible=False)
        self.set_effect(triggerIds=[3004], visible=True)
        self.set_effect(triggerIds=[3005], visible=True)
        self.side_npc_talk(npcId=21450036, illust='DesertDragonMagicGreen_normal', duration=4000, script='$02000543_BF__MAIN__13$')

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=3000):
            return 응접실문열기31(self.ctx)


class 응접실문열기31(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_event_ui(type=1, arg2='$02000543_BF__MAIN__14$', arg3='3000')
        self.destroy_monster(spawnIds=[111,112])
        self.set_effect(triggerIds=[3004], visible=False)
        self.set_effect(triggerIds=[3005], visible=False)
        self.lock_my_pc(isLock=False)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=3000):
            return 응접실문열기4(self.ctx)


class 응접실문열기4(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_onetime_effect(id=102, enable=True, path='BG/Common/Eff_Com_Vibrate_Short.xml')
        self.set_skill(triggerIds=[4001], enable=True)
        self.set_effect(triggerIds=[3003], visible=False)
        self.add_balloon_talk(spawnId=104, msg='$02000543_BF__MAIN__15$', duration=3500)
        self.add_balloon_talk(spawnId=105, msg='$02000543_BF__MAIN__16$', duration=3500)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=4000):
            return 응접실문열고나서처리(self.ctx)


class 응접실문열고나서처리(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.side_npc_talk(npcId=11004644, illust='SlaveMan3_normal', duration=4000, script='$02000543_BF__MAIN__17$')
        self.destroy_monster(spawnIds=[104,105])
        self.enable_spawn_point_pc(spawnId=0, isEnable=False)
        self.enable_spawn_point_pc(spawnId=1, isEnable=True)

    def on_tick(self) -> trigger_api.Trigger:
        if self.user_detected(boxIds=[702], jobCode=0):
            return 보스스폰(self.ctx)


class 보스스폰(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_onetime_effect(id=102, enable=False, path='BG/Common/Eff_Com_Vibrate_Short.xml')
        self.set_onetime_effect(id=103, enable=True, path='BG/Common/Eff_Com_Vibrate_Short.xml')

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=1000):
            return 보스스폰2(self.ctx)


class 보스스폰2(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_onetime_effect(id=103, enable=False, path='BG/Common/Eff_Com_Vibrate_Short.xml')
        self.create_monster(spawnIds=[103], animationEffect=True)

    def on_tick(self) -> trigger_api.Trigger:
        if self.monster_dead(boxIds=[103]):
            return 포탈열기(self.ctx)


class 포탈열기(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_portal(portalId=2, visible=True, enable=True, minimapVisible=True)


initial_state = idle
