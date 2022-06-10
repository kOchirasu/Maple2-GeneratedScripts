using Maple2.Model.Enum;
using Maple2.Script.Npc;

/// <summary>
/// 11004143: Lian
/// </summary>
public class _11004143 : NpcScript {
    internal _11004143(INpcScriptContext context) : base(context) {
        Id = 10;
    }

    public override bool Next(int selection = 0) {
        switch (Id) {
            case 0:
                // $script:0806025707010557$ 
                // - Hahaha! 
                return true;
            case 10:
                // $script:0806025707010558$ 
                // - $npcName:11001167[gender:0]$ likes to frighten us with scary stories, but now that I know better, I don't believe a word he says! 
                return true;
            default:
                return true;
        }
    }
}
