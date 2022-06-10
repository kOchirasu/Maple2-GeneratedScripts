using Maple2.Model.Enum;
using Maple2.Script.Npc;

/// <summary>
/// 11001521: Archer
/// </summary>
public class _11001521 : NpcScript {
    internal _11001521(INpcScriptContext context) : base(context) {
        Id = 10;
    }

    public override bool Next(int selection = 0) {
        switch (Id) {
            case 0:
                // $script:0515211707006109$ 
                // - Nice to meet you!
                return true;
            case 10:
                // $script:0515211707006110$ 
                // - I didn't expect $map:02000023$ to be quite this beautiful. When the boss told me the Green Hoods were joining this mission, I didn't know what to think. I've never been so far from home before... But I promise I won't let you down!
                return true;
            default:
                return true;
        }
    }
}
