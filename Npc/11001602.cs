using Maple2.Model.Enum;
using Maple2.Script.Npc;

/// <summary>
/// 11001602: Ruki
/// </summary>
public class _11001602 : NpcScript {
    internal _11001602(INpcScriptContext context) : base(context) {
        Id = 10;
        // TODO: RandomPick 10
    }

    public override bool Next(int selection = 0) {
        switch (Id) {
            case 0:
                // $script:0504151707006090$ 
                // - ...What?
                return true;
            case 10:
                // $script:0515180307006139$ 
                // - Enough with the preamble. It's time for the main event.
                return true;
            default:
                return true;
        }
    }
}
