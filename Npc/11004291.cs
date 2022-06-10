using Maple2.Model.Enum;
using Maple2.Script.Npc;

/// <summary>
/// 11004291: Everton
/// </summary>
public class _11004291 : NpcScript {
    internal _11004291(INpcScriptContext context) : base(context) {
        Id = 10;
    }

    public override bool Next(int selection = 0) {
        switch (Id) {
            case 0:
                // $script:0921211107011344$ 
                // - Say the word, and I'll get it done. 
                return true;
            case 10:
                // $script:0921211107011345$ 
                // - Shall I take your bags? 
                return true;
            default:
                return true;
        }
    }
}
