using Maple2.Model.Enum;
using Maple2.Script.Npc;

/// <summary>
/// 11004240: Ishura
/// </summary>
public class _11004240 : NpcScript {
    internal _11004240(INpcScriptContext context) : base(context) {
        Id = 10;
    }

    public override bool Next(int selection = 0) {
        switch (Id) {
            case 0:
                // $script:0809223207010940$ 
                // - I still feel out of sorts.
                return true;
            case 10:
                // $script:0809223207010941$ 
                // - I still feel out of sorts.
                // $script:0809223207010942$ 
                // - I am truly in your debt. Thank you. I'm sorry about everything.
                return true;
            default:
                return true;
        }
    }
}
