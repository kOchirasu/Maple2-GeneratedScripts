""" trigger/02010070_bf/main3.xml """
import common


class 대기(common.Trigger):
    def on_enter(self):
        self.set_mesh(triggerIds=[100,101,102,103,104,105,106,107,108,109,110,111,112,113,114,115,116,117,118,119,120,121,122,123,124,125,126,127,128,129,130,131,132,133,134,135,136,137,138,139,140,141,142,143,144,145,146,147,148,149,150,151,152,153,154,155,156,157,158,159,160,161,162,163], visible=False, arg3=0, delay=0, scale=0)
        self.set_mesh(triggerIds=[164,165,166,167,168,169,170,171,172,173,174,175,176,177,178,179,180,181,182,183,184,185,186,187,188,189,190,191,192,193,194,195,196,197,198,199,200,201,202,203,204,205,206,207,208,209,210,211,212,213,214,215,216,217,218,219], visible=False, arg3=0, delay=0, scale=0)
        self.set_mesh(triggerIds=[300,301,302,303,304,305,306,307,308,309,310,311,312,313,314,315,316,317,318,319,320,321,322,323,324,325,326,327,328,329,330,331,332,333,334,335,336,337,338,339,340,341,342,343,344,345,346,347,348,349,350,351,352,353,354,355,356,357,358,359,360,361,362,363], visible=False, arg3=0, delay=0, scale=0)
        self.set_mesh(triggerIds=[400,401,402,403,404,405,406,407,408,409,410,411,412,413,414,415,416,417,418,419,420,421,422,423,424,425,426,427,428], visible=False, arg3=0, delay=0, scale=0)
        self.set_mesh(triggerIds=[430,431,432,433,434,435,436,437,438,439,440,441,442,443,444,445,446,447,448,449,450,451,452,453,454,455,456,457,458,459,460], visible=False, arg3=0, delay=0, scale=0)
        self.set_mesh(triggerIds=[470,471,472,473,474,475,476,477,478,479,480,481], visible=False, arg3=0, delay=0, scale=0)
        self.set_mesh(triggerIds=[490,491,492,493,494,495,496,497,498,499,500,501,502,503,504,505,506,507,508], visible=False, arg3=0, delay=0, scale=0)
        self.set_mesh(triggerIds=[220,221,222,223], visible=False, arg3=0, delay=0, scale=0)
        self.destroy_monster(spawnIds=[3000])
        self.set_portal(portalId=10, visible=False, enable=False, minimapVisible=False)
        self.set_portal(portalId=9, visible=True, enable=True, minimapVisible=False)
        self.set_effect(triggerIds=[9000], visible=False)
        self.set_skill(triggerIds=[9001], enable=False)
        self.set_skill(triggerIds=[9002], enable=False)
        self.set_skill(triggerIds=[9003], enable=False)
        self.set_skill(triggerIds=[9004], enable=False)
        self.set_effect(triggerIds=[95000], visible=False)
        self.set_effect(triggerIds=[95003], visible=False)
        self.set_effect(triggerIds=[95010], visible=False)
        self.set_effect(triggerIds=[95002], visible=False)

    def on_tick(self) -> common.Trigger:
        if self.user_detected(boxIds=[999994]):
            return 대기시간안내01(self.ctx)


class 대기시간안내01(common.Trigger):
    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=1000):
            return 대기시간안내02(self.ctx)


class 대기시간안내02(common.Trigger):
    def on_enter(self):
        self.play_system_sound_in_box(sound='System_ShowGuideSummary_01')
        self.show_guide_summary(entityId=20100703, textId=20100703) # 환상을 만든 미치광이 환영술사 카칼프를 처치하세요.

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=5000):
            return 시작1(self.ctx)


class 시작1(common.Trigger):
    def on_enter(self):
        self.create_monster(spawnIds=[3000], animationEffect=False)

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=3000):
            return 시작2(self.ctx)


class 시작2(common.Trigger):
    def on_enter(self):
        self.hide_guide_summary(entityId=20100703)

    def on_tick(self) -> common.Trigger:
        if self.monster_dead(boxIds=[3000]):
            return 시작3(self.ctx)


class 시작3(common.Trigger):
    def on_enter(self):
        self.set_achievement(triggerId=88321, type='trigger', achieve='kakalfillusion')
        self.set_effect(triggerIds=[9000], visible=True)
        self.play_system_sound_in_box(sound='System_ShowGuideSummary_01')
        self.show_guide_summary(entityId=20100704, textId=20100704) # 사원 가운데 화살표가 있는 곳으로 이동하세요.

    def on_tick(self) -> common.Trigger:
        if self.user_detected(boxIds=[999995]):
            return 시작35(self.ctx)


class 시작35(common.Trigger):
    def on_enter(self):
        self.move_user(mapId=2010070, portalId=11)
        self.set_mesh(triggerIds=[220,221,222,223], visible=True, arg3=0, delay=0, scale=0)

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=1000):
            return 시작4(self.ctx)

    def on_exit(self):
        self.set_mesh(triggerIds=[100,101,102,103,104,105,106,107,108,109,110,111,112,113,114,115,116,117,118,119,120,121,122,123,124,125,126,127,128,129,130,131,132,133,134,135,136,137,138,139,140,141,142,143,144,145,146,147,148,149,150,151,152,153,154,155,156,157,158,159,160,161,162,163], visible=True, arg3=0, delay=0, scale=0)
        self.set_mesh(triggerIds=[164,165,166,167,168,169,170,171,172,173,174,175,176,177,178,179,180,181,182,183,184,185,186,187,188,189,190,191,192,193,194,195,196,197,198,199,200,201,202,203,204,205,206,207,208,209,210,211,212,213,214,215,216,217,218,219], visible=True, arg3=0, delay=0, scale=0)


class 시작4(common.Trigger):
    def on_enter(self):
        self.set_effect(triggerIds=[9000], visible=False)
        self.set_skill(triggerIds=[9001], enable=True)
        self.set_effect(triggerIds=[95002], visible=True)

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=2000):
            return 시작5(self.ctx)


class 시작5(common.Trigger):
    def on_enter(self):
        self.hide_guide_summary(entityId=20100704)
        self.set_skill(triggerIds=[9002], enable=True)
        self.set_mesh(triggerIds=[1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28], visible=False, arg3=0, delay=0, scale=0)
        self.set_mesh(triggerIds=[30,31,32,33,34,35,36,37,38,39,40,41,42,43,44,45,46,47,48,49], visible=False, arg3=0, delay=0, scale=0)
        self.set_mesh(triggerIds=[50,51,52,53,54,55,56,57,58,59,60,61], visible=False, arg3=0, delay=0, scale=0)

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=1000):
            return 시작6(self.ctx)


class 시작6(common.Trigger):
    def on_enter(self):
        self.set_mesh(triggerIds=[300,301,302,303,304,305,306,307,308,309,310,311,312,313,314,315,316,317,318,319,320,321,322,323,324,325,326,327,328,329,330,331,332,333,334,335,336,337,338,339,340,341,342,343,344,345,346,347,348,349,350,351,352,353,354,355,356,357,358,359,360,361,362,363], visible=True, arg3=0, delay=50, scale=0)
        self.set_mesh(triggerIds=[400,401,402,403,404,405,406,407,408,409,410,411,412,413,414,415,416,417,418,419,420,421,422,423,424,425,426,427,428], visible=True, arg3=0, delay=50, scale=0)
        self.set_mesh(triggerIds=[430,431,432,433,434,435,436,437,438,439,440,441,442,443,444,445,446,447,448,449,450,451,452,453,454,455,456,457,458], visible=True, arg3=0, delay=50, scale=0)
        self.set_skill(triggerIds=[9003], enable=True)

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=1000):
            return 시작7(self.ctx)


class 시작7(common.Trigger):
    def on_enter(self):
        self.set_mesh(triggerIds=[460,461,462,463,464,465,466,467,468,469,470,471,472,473,474,475,476,477,478,479,480,481], visible=True, arg3=0, delay=200, scale=0)
        self.set_mesh(triggerIds=[490,491,492,493,494,495,496,497,498,499,500,501,502,503,504,505,506,507,508], visible=True, arg3=0, delay=200, scale=0)
        self.set_effect(triggerIds=[95003], visible=True)
        self.set_skill(triggerIds=[9004], enable=True)

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=2000):
            return 시작8(self.ctx)


class 시작8(common.Trigger):
    def on_enter(self):
        self.set_mesh(triggerIds=[100,101,102,103,104,105,106,107,108,109,110,111,112,113,114,115,116,117,118,119,120,121,122,123,124,125,126,127,128,129,130,131,132,133,134,135,136,137,138,139,140,141,142,143,144,145,146,147,148,149,150,151,152,153,154,155,156,157,158,159,160,161,162,163,164,165,166,167,168,169,170,171,172,173,174,175,176,177,178,179,180,181,182,183,184,185,186,187,188,189,190,191,192,193,194,195,196,197,198,199,200,201,202,203,204,205,206,207,208], visible=False, arg3=0, delay=0, scale=0)
        self.set_mesh(triggerIds=[211,212,213,214,215,216,217,218,219], visible=False, arg3=0, delay=0, scale=0)
        self.set_event_ui(type=1, arg2='$02010070_BF__MAIN__5$', arg3='6000', arg4='0')

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=6000):
            return 종료(self.ctx)


class 종료(common.Trigger):
    def on_enter(self):
        self.set_mesh(triggerIds=[220,221,222,223], visible=False, arg3=0, delay=0, scale=0)
        self.set_portal(portalId=10, visible=True, enable=True, minimapVisible=False)
        self.dungeon_clear()

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=20000):
            return PCGetOut01(self.ctx)


class PCGetOut01(common.Trigger):
    def on_enter(self):
        self.move_user(mapId=0, portalId=0)

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=15000):
            return PCGetOut02(self.ctx)


class PCGetOut02(common.Trigger):
    def on_enter(self):
        self.move_user(mapId=0, portalId=0)

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=15000):
            return PCGetOut03(self.ctx)


class PCGetOut03(common.Trigger):
    def on_enter(self):
        self.move_user(mapId=0, portalId=0)

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=15000):
            return PCGetOut04(self.ctx)


class PCGetOut04(common.Trigger):
    def on_enter(self):
        self.move_user(mapId=0, portalId=0)


initial_state = 대기
