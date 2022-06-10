using Maple2.Model.Enum;
using Maple2.Script.Npc;

/// <summary>
/// 11004530: Reika
/// </summary>
public class _11004530 : NpcScript {
    internal _11004530(INpcScriptContext context) : base(context) {
        // TODO: RandomPick 10;50
    }

    public override bool Next(int selection = 0) {
        switch (Id) {
            case 0:
                // $script:0103163407012522$ 
                // - I see you there.
                return true;
            case 40:
                // $script:0104140207012582$ 
                // - I can't stand the noise here...
                return true;
            case 10:
                // $script:0103163407012523$ 
                // - Can I help you?
                switch (selection) {
                    // $script:0103163407012524$
                    // - I'm just checking in on things.
                    case 0:
                        Id = 20;
                        return false;
                }
                return true;
            case 20:
                // $script:0103163407012525$ 
                // - $npcName:11004437[gender:0]$ sent you, then. As you can see, nothing's changed.
                // $script:0103163407012526$ 
                // - We're still getting shot at by wild robots. We're still dealing with these ridiculous dust clouds. And we're still getting motion sickness when that machine over there sends out tremors...
                // $script:0103163407012527$ 
                // - I miss the forest.
                // $script:0103163407012528$ 
                // - ...
                // $script:0103163407012529$ 
                // - When you get back to the outpost, let them know we need reinforcements to help with the killer machines here.
                switch (selection) {
                    // $script:0103163407012530$
                    // - Will do.
                    case 0:
                        Id = 30;
                        return false;
                }
                return true;
            case 30:
                // $script:0103163407012531$ 
                // - Thanks. You're a life saver!
                return true;
            case 50:
                // $script:0104140207012583$ 
                // - The dust here is unreal... I should have brought a face mask.
                // $script:0104140207012584$ 
                // - I'm going to get a lung disease from my time in this place. Hopefully it's all just in my head...
                return true;
            default:
                return true;
        }
    }
}
