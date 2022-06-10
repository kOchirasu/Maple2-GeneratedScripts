using Maple2.Model.Enum;
using Maple2.Script.Npc;

/// <summary>
/// 11004160: Pemberton
/// </summary>
public class _11004160 : NpcScript {
    internal _11004160(INpcScriptContext context) : base(context) {
        Id = 10;
    }

    public override bool Next(int selection = 0) {
        switch (Id) {
            case 0:
                // $script:0730132107010545$ 
                // - I am dutybound to protect the young mistress. 
                return true;
            case 10:
                // $script:0730132107010546$ 
                // - For the lady, I would sacrifice anything. 
                return true;
            default:
                return true;
        }
    }
}
