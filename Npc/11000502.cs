using Maple2.Model.Enum;
using Maple2.Script.Npc;

/// <summary>
/// 11000502: Armano
/// </summary>
public class _11000502 : NpcScript {
    internal _11000502(INpcScriptContext context) : base(context) {
        Id = 10;
    }

    public override bool Next(int selection = 0) {
        switch (Id) {
            case 0:
                // $script:0831180407002182$ 
                // - Why did you call me?
                return true;
            case 10:
                // $script:0831180407002183$ 
                // - I want to go home... 
                return true;
            default:
                return true;
        }
    }
}
