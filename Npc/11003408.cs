using Maple2.Model.Enum;
using Maple2.Script.Npc;

/// <summary>
/// 11003408: Evagor
/// </summary>
public class _11003408 : NpcScript {
    internal _11003408(INpcScriptContext context) : base(context) {
        Id = 10;
    }

    public override bool Next(int selection = 0) {
        switch (Id) {
            case 0:
                // $script:1115100307011843$ 
                // - You should stay put, stranger.
                return true;
            case 10:
                // $script:1115100307011844$ 
                // - You should stay put, stranger.
                return true;
            default:
                return true;
        }
    }
}
