using Maple2.Model.Enum;
using Maple2.Script.Npc;

/// <summary>
/// 11004168: Joddy
/// </summary>
public class _11004168 : NpcScript {
    internal _11004168(INpcScriptContext context) : base(context) {
        Id = 10;
        // TODO: RandomPick 10
    }

    public override bool Next(int selection = 0) {
        switch (Id) {
            case 0:
                // $script:0806025707010591$ 
                // - Ah... What should I do?
                return true;
            case 10:
                // $script:0806025707010592$ 
                // - Ohh gee, oh man... I don't know about this royale thing.
                return true;
            default:
                return true;
        }
    }
}
