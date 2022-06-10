using Maple2.Model.Enum;
using Maple2.Script.Npc;

/// <summary>
/// 11000534: Modrix
/// </summary>
public class _11000534 : NpcScript {
    internal _11000534(INpcScriptContext context) : base(context) {
        Id = 20;
    }

    public override bool Next(int selection = 0) {
        switch (Id) {
            case 0:
                // $script:0831180407002301$ 
                // - What seems to be the problem? 
                return true;
            case 20:
                // $script:0831180407002303$ 
                // - I handle corpses for a living. There's not much that can rattle me anymore. 
                return true;
            default:
                return true;
        }
    }
}
