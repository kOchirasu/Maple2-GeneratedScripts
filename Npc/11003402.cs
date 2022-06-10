using Maple2.Model.Enum;
using Maple2.Script.Npc;

/// <summary>
/// 11003402: Fredrik
/// </summary>
public class _11003402 : NpcScript {
    internal _11003402(INpcScriptContext context) : base(context) {
        Id = 10;
    }

    public override bool Next(int selection = 0) {
        switch (Id) {
            case 0:
                // $script:0621181107008571$ 
                // - This beats the slums, sure, but man... 
                return true;
            case 10:
                // $script:0621181107008572$ 
                // - Listen, I don't really feel like talking. 
                return true;
            default:
                return true;
        }
    }
}
