using Maple2.Model.Enum;
using Maple2.Script.Npc;

/// <summary>
/// 11004107: Pemberton
/// </summary>
public class _11004107 : NpcScript {
    internal _11004107(INpcScriptContext context) : base(context) {
        Id = 10;
    }

    public override bool Next(int selection = 0) {
        switch (Id) {
            case 0:
                // $script:0720125407010455$ 
                // - I am dutybound to protect the young mistress.
                return true;
            case 10:
                // $script:0720125407010456$ 
                // - For the lady, I would sacrifice anything.
                return true;
            default:
                return true;
        }
    }
}
