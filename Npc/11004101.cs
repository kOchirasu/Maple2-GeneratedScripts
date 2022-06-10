using Maple2.Model.Enum;
using Maple2.Script.Npc;

/// <summary>
/// 11004101: NPCNAME_11004101_NAME
/// </summary>
public class _11004101 : NpcScript {
    internal _11004101(INpcScriptContext context) : base(context) {
        Id = 30;
    }

    public override bool Next(int selection = 0) {
        switch (Id) {
            case 0:
                // $script:0705145607010421$ 
                // - SCRIPTNPCNAM_0705145607010421_NAME
                return true;
            case 30:
                // $script:0705145607010423$ 
                // - SCRIPTNPCNAM_0705145607010423_NAME
                return true;
            default:
                return true;
        }
    }
}
