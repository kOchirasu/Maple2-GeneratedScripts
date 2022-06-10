using Maple2.Model.Enum;
using Maple2.Script.Npc;

/// <summary>
/// 11000447: Injured Guard
/// </summary>
public class _11000447 : NpcScript {
    internal _11000447(INpcScriptContext context) : base(context) {
        Id = 80;
    }

    public override bool Next(int selection = 0) {
        switch (Id) {
            case 0:
                // $script:0831180407001872$ 
                // - Ugh... 
                return true;
            case 80:
                // $script:0831180407001877$ 
                // - Ugh... 
                return true;
            default:
                return true;
        }
    }
}
