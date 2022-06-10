using Maple2.Model.Enum;
using Maple2.Script.Npc;

/// <summary>
/// 11001292: Startz
/// </summary>
public class _11001292 : NpcScript {
    internal _11001292(INpcScriptContext context) : base(context) {
        Id = 10;
    }

    public override bool Next(int selection = 0) {
        switch (Id) {
            case 0:
                // $script:1215203907005006$ 
                // - Cooking requires focus. Understand? 
                return true;
            case 10:
                // $script:1230171207005752$ 
                // - Order now or get a face full of burning oil. Your choice.  
                return true;
            default:
                return true;
        }
    }
}
