using Maple2.Model.Enum;
using Maple2.Script.Npc;

/// <summary>
/// 11001041: Makrasha
/// </summary>
public class _11001041 : NpcScript {
    internal _11001041(INpcScriptContext context) : base(context) {
        Id = 30;
    }

    public override bool Next(int selection = 0) {
        switch (Id) {
            case 0:
                // $script:0831180407003556$ 
                // - How did you find this place?
                return true;
            case 30:
                // $script:0831180407003559$ 
                // - When I close my eyes and listen carefully, I can hear everything... Everything in the entire world.
                return true;
            default:
                return true;
        }
    }
}
