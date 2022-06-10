using Maple2.Model.Enum;
using Maple2.Script.Npc;

/// <summary>
/// 11004112: Mysterious Bladesman
/// </summary>
public class _11004112 : NpcScript {
    internal _11004112(INpcScriptContext context) : base(context) {
        Id = 10;
    }

    public override bool Next(int selection = 0) {
        switch (Id) {
            case 0:
                // $script:0720125407010467$ 
                // - Focus on the task ahead.
                return true;
            case 10:
                // $script:0720125407010468$ 
                // - If you have something to say to me, say it now.
                return true;
            default:
                return true;
        }
    }
}
