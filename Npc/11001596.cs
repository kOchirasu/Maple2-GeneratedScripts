using Maple2.Model.Enum;
using Maple2.Script.Npc;

/// <summary>
/// 11001596: Landevian
/// </summary>
public class _11001596 : NpcScript {
    internal _11001596(INpcScriptContext context) : base(context) {
        // TODO: RandomPick 10;20
    }

    public override bool Next(int selection = 0) {
        switch (Id) {
            case 0:
                // $script:0504151707006084$ 
                // - Sigh... 
                return true;
            case 10:
                // $script:0515180307006133$ 
                // - This isn't like $npcName:11001229[gender:0]$ at all. Wake up!
                return true;
            case 20:
                // $script:0524142307006222$ 
                // - This isn't like $npcName:11001229[gender:0]$ at all. Wake up!
                return true;
            default:
                return true;
        }
    }
}
