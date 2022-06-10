using Maple2.Model.Enum;
using Maple2.Script.Npc;

/// <summary>
/// 11004111: Allon
/// </summary>
public class _11004111 : NpcScript {
    internal _11004111(INpcScriptContext context) : base(context) {
        Id = 10;
    }

    public override bool Next(int selection = 0) {
        switch (Id) {
            case 0:
                // $script:0720125407010463$ 
                // - Talk to me whenever you need assistance.
                return true;
            case 10:
                // $script:0720125407010464$ 
                // - Our knights always do their utmost.
                return true;
            default:
                return true;
        }
    }
}
