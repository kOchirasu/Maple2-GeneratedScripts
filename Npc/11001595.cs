using Maple2.Model.Enum;
using Maple2.Script.Npc;

/// <summary>
/// 11001595: Asimov
/// </summary>
public class _11001595 : NpcScript {
    internal _11001595(INpcScriptContext context) : base(context) {
        Id = 10;
    }

    public override bool Next(int selection = 0) {
        switch (Id) {
            case 0:
                // $script:0504151707006083$ 
                // - How may I help you?
                return true;
            case 10:
                // $script:0515180307006132$ 
                // - $npcName:11001229[gender:0]$'s body may be asleep, but I don't think his mind is. He'll return to us soon. 
                return true;
            default:
                return true;
        }
    }
}
