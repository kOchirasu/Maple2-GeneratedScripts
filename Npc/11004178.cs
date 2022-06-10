using Maple2.Model.Enum;
using Maple2.Script.Npc;

/// <summary>
/// 11004178: Katvan
/// </summary>
public class _11004178 : NpcScript {
    internal _11004178(INpcScriptContext context) : base(context) {
        Id = 10;
    }

    public override bool Next(int selection = 0) {
        switch (Id) {
            case 0:
                // $script:0806025707010618$ 
                // - Do you need something?
                return true;
            case 10:
                // $script:0806025707010619$ 
                // - If we want to win the next match, the two of you need to be more pragmatic.
                return true;
            default:
                return true;
        }
    }
}
