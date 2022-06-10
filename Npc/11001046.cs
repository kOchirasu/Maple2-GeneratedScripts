using Maple2.Model.Enum;
using Maple2.Script.Npc;

/// <summary>
/// 11001046: Hatar
/// </summary>
public class _11001046 : NpcScript {
    internal _11001046(INpcScriptContext context) : base(context) {
        Id = 40;
        // TODO: RandomPick 40
    }

    public override bool Next(int selection = 0) {
        switch (Id) {
            case 0:
                // $script:0831180407003573$ 
                // - I'm sensing evil energy... The kind that can never be purged... 
                return true;
            case 40:
                // $script:0831180407003577$ 
                // - I came all the way here to clear my head and focus on my training. I don't know how so many people have heard about my lava-reading skill. I would send them away, but I respect their determination to come all the way out here.
                return true;
            default:
                return true;
        }
    }
}
