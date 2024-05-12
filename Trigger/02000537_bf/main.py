""" trigger/02000537_bf/main.xml """
import trigger_api


# 심연의 성채
# 플레이어 감지
class idle(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_mesh(triggerIds=[5000], visible=True)
        self.set_mesh(triggerIds=[8900], visible=True)
        self.set_mesh(triggerIds=[8901], visible=True)
        self.set_mesh(triggerIds=[8902], visible=True)
        self.set_mesh(triggerIds=[8903], visible=True)
        self.set_mesh(triggerIds=[8904], visible=True)
        self.set_mesh(triggerIds=[8905], visible=True)
        self.set_effect(triggerIds=[8000], visible=False)
        self.set_effect(triggerIds=[8001], visible=False)
        self.set_skill(triggerIds=[9000], enable=False)
        self.enable_spawn_point_pc(spawnId=0, isEnable=True)
        self.enable_spawn_point_pc(spawnId=1, isEnable=False)
        self.enable_spawn_point_pc(spawnId=2, isEnable=False)
        self.enable_spawn_point_pc(spawnId=3, isEnable=False)
        self.enable_spawn_point_pc(spawnId=4, isEnable=False)
        self.enable_spawn_point_pc(spawnId=5, isEnable=False)
        self.enable_spawn_point_pc(spawnId=6, isEnable=False)
        self.set_portal(portalId=2, visible=False, enable=False, minimapVisible=False)

    def on_tick(self) -> trigger_api.Trigger:
        if self.user_detected(boxIds=[701], jobCode=0):
            return ready(self.ctx)


# 첫번째 발판
class ready(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_event_ui(type=1, arg2='$02000537_BF__MAIN__0$', arg3='3000')
        self.create_monster(spawnIds=[101,1011,1012,1013,1014,1017,1018,1019], animationEffect=False)

    def on_tick(self) -> trigger_api.Trigger:
        if self.monster_dead(boxIds=[101,1011,1012,1013,1014,1017,1018,1019]):
            return 도마뱀스폰1(self.ctx)


class 도마뱀스폰1(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_mesh(triggerIds=[8900], visible=False)
        self.create_monster(spawnIds=[1015,1016], animationEffect=True)

    def on_tick(self) -> trigger_api.Trigger:
        if self.user_detected(boxIds=[702], jobCode=0):
            return 시작702(self.ctx)


class 시작702(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.enable_spawn_point_pc(spawnId=0, isEnable=False)
        self.enable_spawn_point_pc(spawnId=1, isEnable=True)
        self.create_monster(spawnIds=[102,1022,1023,1024,1025], animationEffect=True)
        self.side_npc_talk(npcId=22600006, illust='DesertDragonBigBlue_normal', duration=4000, script='$02000537_BF__MAIN__1$')

    def on_tick(self) -> trigger_api.Trigger:
        if self.monster_dead(boxIds=[102,1022,1023,1024,1025]):
            return 마무리1_702(self.ctx)


class 마무리1_702(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_mesh(triggerIds=[8901], visible=False)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=1500):
            return 마무리2_702(self.ctx)


class 마무리2_702(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.side_npc_talk(npcId=11004643, illust='SlaveWoman3_normal', duration=4000, script='$02000537_BF__MAIN__2$')

    def on_tick(self) -> trigger_api.Trigger:
        if self.user_detected(boxIds=[703], jobCode=0):
            return 시작703(self.ctx)


class 시작703(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.destroy_monster(spawnIds=[1026])
        self.enable_spawn_point_pc(spawnId=1, isEnable=False)
        self.enable_spawn_point_pc(spawnId=2, isEnable=True)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=1000):
            return 진행703(self.ctx)


class 진행703(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_event_ui(type=1, arg2='$02000537_BF__MAIN__3$', arg3='3000')
        self.create_monster(spawnIds=[109], animationEffect=True)
        self.create_monster(spawnIds=[103,1031,1032,1033,1034], animationEffect=True)

    def on_tick(self) -> trigger_api.Trigger:
        if self.monster_dead(boxIds=[103,1031,1032,1033,1034]):
            return 마무리1_703(self.ctx)


class 마무리1_703(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_mesh(triggerIds=[8902], visible=False)
        self.create_monster(spawnIds=[1035], animationEffect=True)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=1500):
            return 마무리2_703(self.ctx)


class 마무리2_703(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.side_npc_talk(npcId=11004644, illust='SlaveMan3_normal', duration=4000, script='$02000537_BF__MAIN__4$')

    def on_tick(self) -> trigger_api.Trigger:
        if self.user_detected(boxIds=[704], jobCode=0):
            return 시작704(self.ctx)


class 시작704(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.enable_spawn_point_pc(spawnId=2, isEnable=False)
        self.enable_spawn_point_pc(spawnId=3, isEnable=True)
        self.create_monster(spawnIds=[104,1041,1042,1043,1044], animationEffect=False)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=3000):
            return 진행704(self.ctx)


class 진행704(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.side_npc_talk(npcId=11004643, illust='SlaveWoman3_normal', duration=4000, script='$02000537_BF__MAIN__5$')

    def on_tick(self) -> trigger_api.Trigger:
        if self.monster_dead(boxIds=[104,1041,1042,1043,1044]):
            return 마무리704(self.ctx)


class 마무리704(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_mesh(triggerIds=[8903], visible=False)
        self.side_npc_talk(npcId=11004643, illust='SlaveWoman3_normal', duration=4000, script='$02000537_BF__MAIN__6$')

    def on_tick(self) -> trigger_api.Trigger:
        if self.user_detected(boxIds=[705], jobCode=0):
            return 시작705(self.ctx)


class 시작705(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.enable_spawn_point_pc(spawnId=3, isEnable=False)
        self.enable_spawn_point_pc(spawnId=4, isEnable=True)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=500):
            return 진행705(self.ctx)


class 진행705(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.create_monster(spawnIds=[105,1051,1052,1053,1054], animationEffect=True)
        self.side_npc_talk(npcId=22600006, illust='DesertDragonBigBlue_normal', duration=4000, script='$02000537_BF__MAIN__7$')

    def on_tick(self) -> trigger_api.Trigger:
        if self.monster_dead(boxIds=[105,1051,1052,1053,1054]):
            return 마무리705(self.ctx)


class 마무리705(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_mesh(triggerIds=[8904], visible=False)
        self.create_monster(spawnIds=[1036], animationEffect=True)

    def on_tick(self) -> trigger_api.Trigger:
        if self.user_detected(boxIds=[708], jobCode=0):
            return 버프걸어주기(self.ctx)


class 버프걸어주기(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.side_npc_talk(npcId=11004644, illust='SlaveMan3_normal', duration=4000, script='$02000537_BF__MAIN__8$')
        self.set_skill(triggerIds=[9000], enable=True)

    def on_tick(self) -> trigger_api.Trigger:
        if self.user_detected(boxIds=[706], jobCode=0):
            return 시작706(self.ctx)


class 시작706(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.side_npc_talk(npcId=11004643, illust='SlaveWoman3_normal', duration=4000, script='$02000537_BF__MAIN__9$')
        self.enable_spawn_point_pc(spawnId=4, isEnable=False)
        self.enable_spawn_point_pc(spawnId=5, isEnable=True)
        self.create_monster(spawnIds=[106,1061,1063,1064,1065], animationEffect=True)

    def on_tick(self) -> trigger_api.Trigger:
        if self.monster_dead(boxIds=[106,1061,1063,1064,1065]):
            return 마무리706(self.ctx)


class 마무리706(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_mesh(triggerIds=[8905], visible=False)
        self.side_npc_talk(npcId=11004644, illust='SlaveMan3_normal', duration=4000, script='$02000537_BF__MAIN__10$')

    def on_tick(self) -> trigger_api.Trigger:
        if self.user_detected(boxIds=[707], jobCode=0):
            return 시작707(self.ctx)


class 시작707(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.enable_spawn_point_pc(spawnId=5, isEnable=False)
        self.enable_spawn_point_pc(spawnId=6, isEnable=True)
        self.create_monster(spawnIds=[108], animationEffect=True)
        self.side_npc_talk(npcId=22600006, illust='DesertDragonBigBlue_normal', duration=4000, script='$02000537_BF__MAIN__11$')

    def on_tick(self) -> trigger_api.Trigger:
        if self.monster_dead(boxIds=[108]):
            return 포털생성전(self.ctx)


class 포털생성전(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.destroy_monster(spawnIds=[109])
        self.create_monster(spawnIds=[1091], animationEffect=True)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=2000):
            return 포털생성전2(self.ctx)


class 포털생성전2(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.destroy_monster(spawnIds=[109])
        self.create_monster(spawnIds=[1091], animationEffect=True)
        self.side_npc_talk(npcId=11004643, illust='SlaveWoman3_normal', duration=4000, script='$02000537_BF__MAIN__12$')

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=2000):
            return 포털생성(self.ctx)


class 포털생성(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_portal(portalId=2, visible=True, enable=True, minimapVisible=True)


initial_state = idle
