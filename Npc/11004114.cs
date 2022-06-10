using Maple2.Model.Enum;
using Maple2.Script.Npc;

/// <summary>
/// 11004114: Tinchai
/// </summary>
public class _11004114 : NpcScript {
    internal _11004114(INpcScriptContext context) : base(context) {
        Id = 10;
    }

    public override bool Next(int selection = 0) {
        switch (Id) {
            case 0:
                // $script:0720125407010471$ 
                // - Hmm... Did you need something? 
                return true;
            case 10:
                // $script:0720125407010472$ 
                // - Sounds like you've got an important mission! I'm sure you'll succeed! 
                return true;
            default:
                return true;
        }
    }
}
