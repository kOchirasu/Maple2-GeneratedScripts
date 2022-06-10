using Maple2.Model.Enum;
using Maple2.Script.Npc;

/// <summary>
/// 11000712: Tortie
/// </summary>
public class _11000712 : NpcScript {
    internal _11000712(INpcScriptContext context) : base(context) {
        Id = 30;
    }

    public override bool Next(int selection = 0) {
        switch (Id) {
            case 0:
                // $script:0831180407002868$ 
                // - How may I help you?
                return true;
            case 30:
                // $script:0831180407002871$ 
                // - Dad doesn't want to play with me. $MyPCName$, could you play with me?
                return true;
            default:
                return true;
        }
    }
}
