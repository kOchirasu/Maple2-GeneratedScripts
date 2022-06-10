using Maple2.Model.Enum;
using Maple2.Script.Npc;

/// <summary>
/// 11001914: Lennon
/// </summary>
public class _11001914 : NpcScript {
    internal _11001914(INpcScriptContext context) : base(context) {
        Id = 20;
    }

    public override bool Next(int selection = 0) {
        switch (Id) {
            case 0:
                // $script:1116181807007413$ 
                // - Welcome. 
                return true;
            case 20:
                // $script:1116181807007415$ 
                // - Katvan and I will meet again. 
                return true;
            default:
                return true;
        }
    }
}
