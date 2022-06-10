using Maple2.Model.Enum;
using Maple2.Script.Npc;

/// <summary>
/// 11001105: Eve
/// </summary>
public class _11001105 : NpcScript {
    internal _11001105(INpcScriptContext context) : base(context) {
        Id = 40;
    }

    public override bool Next(int selection = 0) {
        switch (Id) {
            case 0:
                // $script:0908154107003710$ 
                // - What brings you to me?
                return true;
            case 40:
                // $script:0908154107003714$ 
                // - If $npcName:11000064[gender:0]$ hadn't come to Katramus to save me, I could've been here with these people for treatment.
                return true;
            default:
                return true;
        }
    }
}
