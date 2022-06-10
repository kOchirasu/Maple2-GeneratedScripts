using Maple2.Model.Enum;
using Maple2.Script.Npc;

/// <summary>
/// 11001099: Oska
/// </summary>
public class _11001099 : NpcScript {
    internal _11001099(INpcScriptContext context) : base(context) {
        Id = 30;
        // TODO: RandomPick 30
    }

    public override bool Next(int selection = 0) {
        switch (Id) {
            case 0:
                // $script:0831180407003697$ 
                // - Hmm... 
                return true;
            case 30:
                // $script:0831180407003698$ 
                // - This place is $map:52000011$. It channels the power of the Red Lapenta to maintain order among the timelines.
                return true;
            default:
                return true;
        }
    }
}
