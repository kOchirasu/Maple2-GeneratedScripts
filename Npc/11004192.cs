using Maple2.Model.Enum;
using Maple2.Script.Npc;

/// <summary>
/// 11004192: Lanemone
/// </summary>
public class _11004192 : NpcScript {
    internal _11004192(INpcScriptContext context) : base(context) {
        Id = 10;
    }

    public override bool Next(int selection = 0) {
        switch (Id) {
            case 0:
                // $script:0813101707010952$ 
                // - Hmm... 
                return true;
            case 10:
                // $script:0813101707010953$ 
                // - Hmmm... This is turning out to be pretty interesting. 
                return true;
            default:
                return true;
        }
    }
}
