using Maple2.Model.Enum;
using Maple2.Script.Npc;

/// <summary>
/// 11004218: Char
/// </summary>
public class _11004218 : NpcScript {
    internal _11004218(INpcScriptContext context) : base(context) {
        Id = 10;
    }

    public override bool Next(int selection = 0) {
        switch (Id) {
            case 0:
                // $script:0806222707010778$ 
                // - What's up?
                return true;
            case 10:
                // $script:0806222707010779$ 
                // - This world is ruled by competition. Only the best win.
                // $script:0806222707010780$ 
                // - If you wanna survive, you've got to win, and there's no right or wrong when it comes to winning. Somebody's got to go, you or them.
                return true;
            default:
                return true;
        }
    }
}
