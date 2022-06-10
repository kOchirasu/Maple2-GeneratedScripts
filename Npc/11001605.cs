using Maple2.Model.Enum;
using Maple2.Script.Npc;

/// <summary>
/// 11001605: Rejan
/// </summary>
public class _11001605 : NpcScript {
    internal _11001605(INpcScriptContext context) : base(context) {
        Id = 10;
        // TODO: RandomPick 10
    }

    public override bool Next(int selection = 0) {
        switch (Id) {
            case 0:
                // $script:0504151707006093$ 
                // - Welcome.
                return true;
            case 10:
                // $script:0515180307006142$ 
                // - The sooner this is over with, the sooner I can go back to Calibre Island.
                return true;
            default:
                return true;
        }
    }
}
