using Maple2.Model.Enum;
using Maple2.Script.Npc;

/// <summary>
/// 11004118: Royal Watchman
/// </summary>
public class _11004118 : NpcScript {
    internal _11004118(INpcScriptContext context) : base(context) {
        Id = 10;
    }

    public override bool Next(int selection = 0) {
        switch (Id) {
            case 0:
                // $script:0720125407010479$ 
                // - If I see anything unusual, I'll report in right away! 
                return true;
            case 10:
                // $script:0720125407010480$ 
                // - The blast area was pretty big... 
                return true;
            default:
                return true;
        }
    }
}
