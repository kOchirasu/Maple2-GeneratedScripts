using Maple2.Model.Enum;
using Maple2.Script.Npc;

/// <summary>
/// 11000849: Hailey
/// </summary>
public class _11000849 : NpcScript {
    internal _11000849(INpcScriptContext context) : base(context) {
        Id = 30;
    }

    public override bool Next(int selection = 0) {
        switch (Id) {
            case 0:
                // $script:0831180407003107$ 
                // - Hello.
                return true;
            case 30:
                // $script:0831180407003110$ 
                // - It's snowing here. How amazing! You understand why, right?
                return true;
            default:
                return true;
        }
    }
}
