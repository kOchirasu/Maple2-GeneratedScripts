using Maple2.Model.Enum;
using Maple2.Script.Npc;

/// <summary>
/// 11001079: Karte
/// </summary>
public class _11001079 : NpcScript {
    internal _11001079(INpcScriptContext context) : base(context) {
        Id = 30;
        // TODO: RandomPick 30
    }

    public override bool Next(int selection = 0) {
        switch (Id) {
            case 0:
                // $script:0831180407003683$ 
                // - I came here for brawling. Hoo, hoo, woo!
                return true;
            case 30:
                // $script:0831180407003686$ 
                // - Ugh... I know this isn't a vacation, but it's just too hot!
                return true;
            default:
                return true;
        }
    }
}
