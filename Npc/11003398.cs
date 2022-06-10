using Maple2.Model.Enum;
using Maple2.Script.Npc;

/// <summary>
/// 11003398: Lance
/// </summary>
public class _11003398 : NpcScript {
    internal _11003398(INpcScriptContext context) : base(context) {
        Id = 10;
    }

    public override bool Next(int selection = 0) {
        switch (Id) {
            case 0:
                // $script:0621181107008565$ 
                // - Ugh... 
                return true;
            case 10:
                // $script:0621181107008566$ 
                // - Is this how I die...? From... training...? 
                return true;
            default:
                return true;
        }
    }
}
