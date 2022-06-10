using Maple2.Model.Enum;
using Maple2.Script.Npc;

/// <summary>
/// 11000449: Miran
/// </summary>
public class _11000449 : NpcScript {
    internal _11000449(INpcScriptContext context) : base(context) {
        Id = 30;
    }

    public override bool Next(int selection = 0) {
        switch (Id) {
            case 0:
                // $script:0831180407001878$ 
                // - What is it? 
                return true;
            case 30:
                // $script:0831180407001881$ 
                // - Get out of the way, I can't see $npcName:11000406[gender:0]$! 
                return true;
            default:
                return true;
        }
    }
}
