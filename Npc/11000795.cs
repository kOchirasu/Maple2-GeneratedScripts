using Maple2.Model.Enum;
using Maple2.Script.Npc;

/// <summary>
/// 11000795: Maritel
/// </summary>
public class _11000795 : NpcScript {
    internal _11000795(INpcScriptContext context) : base(context) {
        Id = 10;
    }

    public override bool Next(int selection = 0) {
        switch (Id) {
            case 0:
                // $script:0831180407002960$ 
                // - Welcome to Cathy Mart. 
                return true;
            case 10:
                // $script:0831180407002961$ 
                // - Is there something you're looking for? You can find everything at Cathy Mart. If we don't have it, it doesn't exist! 
                return true;
            default:
                return true;
        }
    }
}
