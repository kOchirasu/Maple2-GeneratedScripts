using Maple2.Model.Enum;
using Maple2.Script.Npc;

/// <summary>
/// 11004108: Lanemone
/// </summary>
public class _11004108 : NpcScript {
    internal _11004108(INpcScriptContext context) : base(context) {
        Id = 10;
    }

    public override bool Next(int selection = 0) {
        switch (Id) {
            case 0:
                // $script:0720125407010457$ 
                // - Hah... Well, that opened up a can of worms. 
                return true;
            case 10:
                // $script:0720125407010458$ 
                // - This had better be important. 
                return true;
            default:
                return true;
        }
    }
}
