using Maple2.Model.Enum;
using Maple2.Script.Npc;

/// <summary>
/// 11004311: Marianne
/// </summary>
public class _11004311 : NpcScript {
    internal _11004311(INpcScriptContext context) : base(context) {
        Id = 10;
    }

    public override bool Next(int selection = 0) {
        switch (Id) {
            case 0:
                // $script:0921211107011348$ 
                // - I hope I can see papa again soon...
                return true;
            case 10:
                // $script:0921211107011349$ 
                // - You're here! Just like you promised.
                return true;
            default:
                return true;
        }
    }
}
