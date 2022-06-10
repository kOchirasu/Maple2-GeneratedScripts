using Maple2.Model.Enum;
using Maple2.Script.Npc;

/// <summary>
/// 11001300: Allon
/// </summary>
public class _11001300 : NpcScript {
    internal _11001300(INpcScriptContext context) : base(context) {
        Id = 30;
        // TODO: RandomPick 30
    }

    public override bool Next(int selection = 0) {
        switch (Id) {
            case 0:
                // $script:1215203907005014$ 
                // - How may I help you?
                return true;
            case 30:
                // $script:1215203907005017$ 
                // - I command the Royal Knights of Empress $npcName:11000075[gender:1]$. Her safety is our duty.
                return true;
            default:
                return true;
        }
    }
}
