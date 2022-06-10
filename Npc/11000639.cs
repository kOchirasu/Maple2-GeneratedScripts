using Maple2.Model.Enum;
using Maple2.Script.Npc;

/// <summary>
/// 11000639: Prisoner 150121
/// </summary>
public class _11000639 : NpcScript {
    internal _11000639(INpcScriptContext context) : base(context) {
        Id = 40;
    }

    public override bool Next(int selection = 0) {
        switch (Id) {
            case 0:
                // $script:0831180407002604$ 
                // - Get me out of here...  
                return true;
            case 40:
                // $script:0831180407002607$ 
                // - When will I be let out? Is it soon? Please?  
                return true;
            default:
                return true;
        }
    }
}
