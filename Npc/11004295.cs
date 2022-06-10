using Maple2.Model.Enum;
using Maple2.Script.Npc;

/// <summary>
/// 11004295: Marianne
/// </summary>
public class _11004295 : NpcScript {
    internal _11004295(INpcScriptContext context) : base(context) {
        Id = 10;
    }

    public override bool Next(int selection = 0) {
        switch (Id) {
            case 0:
                // $script:0921211107011346$ 
                // - But, you know...
                return true;
            case 10:
                // $script:0921211107011347$ 
                // - H-hello?
                return true;
            default:
                return true;
        }
    }
}
