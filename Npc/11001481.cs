using Maple2.Model.Enum;
using Maple2.Script.Npc;

/// <summary>
/// 11001481: Dunba
/// </summary>
public class _11001481 : NpcScript {
    internal _11001481(INpcScriptContext context) : base(context) {
        Id = 10;
        // TODO: RandomPick 10
    }

    public override bool Next(int selection = 0) {
        switch (Id) {
            case 0:
                // $script:0106111607005769$ 
                // - Ugh...
                return true;
            case 10:
                // $script:0106111607005770$ 
                // - When $npcName:23000068[gender:0]$ returns... Aww... $npcName:11001472[gender:1]$ has to get better soon...
                return true;
            default:
                return true;
        }
    }
}
