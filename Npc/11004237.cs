using Maple2.Model.Enum;
using Maple2.Script.Npc;

/// <summary>
/// 11004237: Allon
/// </summary>
public class _11004237 : NpcScript {
    internal _11004237(INpcScriptContext context) : base(context) {
        Id = 10;
    }

    public override bool Next(int selection = 0) {
        switch (Id) {
            case 0:
                // $script:0809223207010929$ 
                // - Good work, $MyPCName$.
                return true;
            case 10:
                // $script:0809223207010930$ 
                // - Good work, $MyPCName$. I'd better head back to $map:02000001$ now.
                // $script:0809223207010931$ 
                // - I haven't seen his face in some time.
                return true;
            default:
                return true;
        }
    }
}
