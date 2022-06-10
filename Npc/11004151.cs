using Maple2.Model.Enum;
using Maple2.Script.Npc;

/// <summary>
/// 11004151: Lydia
/// </summary>
public class _11004151 : NpcScript {
    internal _11004151(INpcScriptContext context) : base(context) {
        Id = 10;
        // TODO: RandomPick 10
    }

    public override bool Next(int selection = 0) {
        switch (Id) {
            case 0:
                // $script:0806025707010573$ 
                // - How may I help you?
                return true;
            case 10:
                // $script:0806025707010574$ 
                // - $npcName:11004150$, $npcName:11004148$, $npcName:11004149$, and I are here in $map:02000499$ on vacation! Since we all grew up together, we've got some real synergy on the battlefield.
                return true;
            default:
                return true;
        }
    }
}
