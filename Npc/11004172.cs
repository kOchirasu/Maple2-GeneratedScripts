using Maple2.Model.Enum;
using Maple2.Script.Npc;

/// <summary>
/// 11004172: Dunba
/// </summary>
public class _11004172 : NpcScript {
    internal _11004172(INpcScriptContext context) : base(context) {
        Id = 10;
    }

    public override bool Next(int selection = 0) {
        switch (Id) {
            case 0:
                // $script:0806025707010606$ 
                // - Ugh... 
                return true;
            case 10:
                // $script:0806025707010607$ 
                // - Blam, blam! Oh, hey. I'm just practicing my aim. I don't want to let my squad down. 
                return true;
            default:
                return true;
        }
    }
}
