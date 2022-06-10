using Maple2.Model.Enum;
using Maple2.Script.Npc;

/// <summary>
/// 11001108: Lennon
/// </summary>
public class _11001108 : NpcScript {
    internal _11001108(INpcScriptContext context) : base(context) {
        Id = 30;
    }

    public override bool Next(int selection = 0) {
        switch (Id) {
            case 0:
                // $script:0908154107003723$ 
                // - How did you get here?
                return true;
            case 30:
                // $script:0908154107003726$ 
                // - $npcName:11000614[gender:0]$ and I met in Katramus. I can't believe we were able to meet again here. I'm also glad that his sister is safe!
                return true;
            default:
                return true;
        }
    }
}
