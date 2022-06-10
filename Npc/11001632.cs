using Maple2.Model.Enum;
using Maple2.Script.Npc;

/// <summary>
/// 11001632: Eupheria
/// </summary>
public class _11001632 : NpcScript {
    internal _11001632(INpcScriptContext context) : base(context) {
        Id = 10;
        // TODO: RandomPick 10
    }

    public override bool Next(int selection = 0) {
        switch (Id) {
            case 0:
                // $script:0517100407006134$ 
                // - Sniff... 
                return true;
            case 10:
                // $script:0517100407006135$ 
                // - This is all my doing... 
                return true;
            default:
                return true;
        }
    }
}
