using Maple2.Model.Enum;
using Maple2.Script.Npc;

/// <summary>
/// 11000129: Alvin
/// </summary>
public class _11000129 : NpcScript {
    internal _11000129(INpcScriptContext context) : base(context) {
        Id = 40;
    }

    public override bool Next(int selection = 0) {
        switch (Id) {
            case 0:
                // $script:0831180407000552$ 
                // - What seems to be the problem?
                return true;
            case 40:
                // $script:0831180407000555$ 
                // - I took the Royal Road for granted. I've never been on a path so dangerous before. 
                // $script:0831180407000556$ 
                // - And even if you get through this awful forest, there's a treacherous valley to cross. The cliffs of $map:02000051$ are nothing compared to what's ahead! Ahh, I'm never getting out of here alive...
                return true;
            default:
                return true;
        }
    }
}
