""" trigger/52100301_qd/300005_phase_4.xml """
import common


class 대기(common.Trigger):
    def on_enter(self):
        self.set_effect(triggerIds=[200001,200002,200003,200004,200005,200006,200007,200008], visible=False)

    def on_tick(self) -> common.Trigger:
        if self.user_value(key='AI_Phase', value=4):
            return 패이즈_4_시작(self.ctx)


class 패이즈_4_시작(common.Trigger):
    def on_enter(self):
        self.add_buff(boxIds=[1003], skillId=62100169, level=1) # 포탑 기절 이뮨 제거
        self.set_effect(triggerIds=[200011,200012,200013,200014,200015,200016,200017,200018], visible=False) # 페이즈3 포탑 가이드 제거
        self.destroy_monster(spawnIds=[512]) # 포탑 소멸(추후 연출 강화를 위해 사망으로 변경 하자)
        self.destroy_monster(spawnIds=[511])
        self.set_interact_object(triggerIds=[10003122], state=2) # 포탑 제어 장치 제거
        self.set_interact_object(triggerIds=[10003121], state=2)
        self.set_user_value(triggerId=3000041, key='Phase_3_Interect_01', value=0) # 포탑 기능 정지
        self.set_user_value(triggerId=3000042, key='Phase_3_Interect_02', value=0)
        self.side_npc_talk(type='talk', npcId=11004205, illust='ArcaneBlader_unfair', script='$52100301_QD__300005_PHASE_4__0$', duration=3176)

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=6000):
            return 추가대화(self.ctx)


class 추가대화(common.Trigger):
    def on_enter(self):
        self.side_npc_talk(type='talk', npcId=29500101, illust='ArcheonBlack_Angry', script='$52100301_QD__300005_PHASE_4__1$', duration=3176)

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=4000):
            return 추가대화_2(self.ctx)


class 추가대화_2(common.Trigger):
    def on_enter(self):
        self.side_npc_talk(type='talk', npcId=11004205, illust='ArcaneBlader_unfair', script='$52100301_QD__300005_PHASE_4__2$', duration=3176)

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=6000):
            return 엘리베이터_대기(self.ctx)


class 엘리베이터_대기(common.Trigger):
    def on_enter(self):
        self.side_npc_talk(type='talk', npcId=11004205, illust='ArcaneBlader_unfair', script='$52100301_QD__300005_PHASE_4__3$', duration=3176)
        self.set_user_value(key='AI_Phase', value=0)
        self.set_visible_breakable_object(triggerIds=[5351,5352,5353,5354,5355,5356,5357,5358,5359,5360,5361,5362,5363,5364], visible=False) # 좌우 엘리베이터 숨기기(페이즈가 바뀜으로써..)추후 파괴하는걸로 연출을 변경해보자.
        self.set_visible_breakable_object(triggerIds=[5371,5372,5373,5374,5375,5376,5377,5378,5379,5380,5381,5382,5383,5384], visible=False)
        self.set_visible_breakable_object(triggerIds=[5101,5102,5103,5104,5105,5106,5107,5108,5109,5110], visible=True) # 4페이즈 상하 엘리베이터 보이기
        self.set_visible_breakable_object(triggerIds=[5111,5112,5113,5114,5115,5116,5117,5118,5119,5120], visible=True)
        self.set_visible_breakable_object(triggerIds=[5121,5122,5123,5124,5125,5126,5127,5128,5129,5130], visible=True)
        self.set_visible_breakable_object(triggerIds=[5131,5132,5133,5134,5135,5136,5137,5138,5139,5140], visible=True)
        self.set_breakable(triggerIds=[5101,5102,5103,5104,5105,5106,5107,5108,5109,5110], enable=True) # 4페이즈 상하 엘리베이터 동작
        self.set_breakable(triggerIds=[5111,5112,5113,5114,5115,5116,5117,5118,5119,5120], enable=True)
        self.set_breakable(triggerIds=[5121,5122,5123,5124,5125,5126,5127,5128,5129,5130], enable=True)
        self.set_breakable(triggerIds=[5131,5132,5133,5134,5135,5136,5137,5138,5139,5140], enable=True)

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=9000):
            return 엘리베이터_도착(self.ctx)


class 엘리베이터_도착(common.Trigger):
    def on_enter(self):
        self.set_user_value(key='AI_Phase', value=0)
        self.set_visible_breakable_object(triggerIds=[5301,5302,5303,5304,5305,5306,5307,5308,5309,5310,5311,5312,5313,5314,5315,5316,5317,5318,5319,5320,5321,5322,5323,5324,5325,5326,5327,5328,5329,5330,5331,5332,5333,5334,5335,5336,5337,5338,5339,5340], visible=True) # 4페이즈 상하 엘리베이터 보이기
        self.set_user_value(triggerId=3000051, key='Phase_4_Interect_01', value=1) # 폭발물 페이즈로 이동
        self.set_user_value(triggerId=3000052, key='Phase_4_Interect_02', value=1)
        self.set_user_value(triggerId=3000053, key='Phase_4_Interect_03', value=1)
        self.set_user_value(triggerId=3000054, key='Phase_4_Interect_04', value=1)
        self.set_visible_breakable_object(triggerIds=[5101,5102,5103,5104,5105,5106,5107,5108,5109,5110], visible=False) # 4페이즈 상하 엘리베이터 숨기기
        self.set_visible_breakable_object(triggerIds=[5111,5112,5113,5114,5115,5116,5117,5118,5119,5120], visible=False)
        self.set_visible_breakable_object(triggerIds=[5121,5122,5123,5124,5125,5126,5127,5128,5129,5130], visible=False)
        self.set_visible_breakable_object(triggerIds=[5131,5132,5133,5134,5135,5136,5137,5138,5139,5140], visible=False)
        self.set_breakable(triggerIds=[5101,5102,5103,5104,5105,5106,5107,5108,5109,5110], enable=False) # 4페이즈 상하 엘리베이터 멈추기
        self.set_breakable(triggerIds=[5111,5112,5113,5114,5115,5116,5117,5118,5119,5120], enable=False)
        self.set_breakable(triggerIds=[5121,5122,5123,5124,5125,5126,5127,5128,5129,5130], enable=False)
        self.set_breakable(triggerIds=[5131,5132,5133,5134,5135,5136,5137,5138,5139,5140], enable=False)

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=1000):
            return 폭발물제어장치_생성(self.ctx)


class 폭발물제어장치_생성(common.Trigger):
    def on_enter(self):
        self.set_portal(portalId=13, visible=False, enable=False, minimapVisible=False)
        self.set_portal(portalId=14, visible=False, enable=False, minimapVisible=False)
        self.set_portal(portalId=15, visible=False, enable=False, minimapVisible=False)
        self.set_portal(portalId=16, visible=False, enable=False, minimapVisible=False)

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=1500):
            return 길막열기(self.ctx)


class 길막열기(common.Trigger):
    def on_enter(self):
        self.set_event_ui(type=1, arg2='$52100301_QD__300005_PHASE_4__4$', arg3='4000')
        self.set_mesh(triggerIds=[5241,5242,5243,5244], visible=False) # 4페이즈 상하좌우 엘리베이터 길막 열기
        self.set_agent(triggerIds=[1800000,1800001,1800002,1800003,1800004,1800005,1800006,1800007,1800008,1800009,1800010,1800011], visible=False)

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=2000):
            return None # Missing State: 완료


initial_state = 대기
