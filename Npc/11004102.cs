using Maple2.Model.Enum;
using Maple2.Script.Npc;

/// <summary>
/// 11004102: NPCNAME_11004102_NAME
/// </summary>
public class _11004102 : NpcScript {
    internal _11004102(INpcScriptContext context) : base(context) {
        Id = 30;
    }

    public override bool Next(int selection = 0) {
        switch (Id) {
            case 0:
                // $script:0705145607010425$ 
                // - SCRIPTNPCNAM_0705145607010425_NAME
                return true;
            case 30:
                // $script:0705145607010427$ 
                // - SCRIPTNPCNAM_0705145607010427_NAME
                // $script:0705145607010428$ 
                // - SCRIPTNPCNAM_0705145607010428_NAME
                return true;
            default:
                return true;
        }
    }
}
