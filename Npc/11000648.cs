using Maple2.Model.Enum;
using Maple2.Script.Npc;

/// <summary>
/// 11000648: Prisoner 160921
/// </summary>
public class _11000648 : NpcScript {
    internal _11000648(INpcScriptContext context) : base(context) {
        Id = 40;
    }

    public override bool Next(int selection = 0) {
        switch (Id) {
            case 0:
                // $script:0831180407002651$ 
                // - Get me out of here...  
                return true;
            case 40:
                // $script:0831180407002655$ 
                // - I can't wait to get out of here. How much longer?  
                return true;
            default:
                return true;
        }
    }
}
