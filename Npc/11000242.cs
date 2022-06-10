using Maple2.Model.Enum;
using Maple2.Script.Npc;

/// <summary>
/// 11000242: Viola
/// </summary>
public class _11000242 : NpcScript {
    internal _11000242(INpcScriptContext context) : base(context) {
        Id = 30;
    }

    public override bool Next(int selection = 0) {
        switch (Id) {
            case 0:
                // $script:0831180407001023$ 
                // - Welcome! Ho, ho, ho. 
                return true;
            case 30:
                // $script:0831180407001026$ 
                // - Did you come alone? Our guests usually arrive as couples. Ho, ho, ho. 
                // $script:0831180407001027$ 
                // - Have a seat. I hope you don't feel out of place. We do get singles up here once in awhile. Sometimes they even find someone to leave with! 
                return true;
            default:
                return true;
        }
    }
}
