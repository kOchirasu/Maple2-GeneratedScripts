using Maple2.Model.Enum;
using Maple2.Script.Npc;

/// <summary>
/// 11000604: Apollo
/// </summary>
public class _11000604 : NpcScript {
    internal _11000604(INpcScriptContext context) : base(context) {
        Id = 10;
    }

    public override bool Next(int selection = 0) {
        switch (Id) {
            case 0:
                // $script:0831180407002485$ 
                // - ...  
                return true;
            case 10:
                // $script:0831180407002486$ 
                // - Keep it down out there, I'm trying to read! 
                return true;
            default:
                return true;
        }
    }
}
