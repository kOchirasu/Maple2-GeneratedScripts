using Maple2.Model.Enum;
using Maple2.Script.Npc;

/// <summary>
/// 11001941: Sophia
/// </summary>
public class _11001941 : NpcScript {
    internal _11001941(INpcScriptContext context) : base(context) {
        Id = 10;
        // TODO: RandomPick 10
    }

    public override bool Next(int selection = 0) {
        switch (Id) {
            case 0:
                // $script:1123165007007487$ 
                // - Can I help you?
                return true;
            case 10:
                // $script:1208184307007523$ 
                // - This season's fashions are so uninspired, don't you think?
                return true;
            default:
                return true;
        }
    }
}
