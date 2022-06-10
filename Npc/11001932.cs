using Maple2.Model.Enum;
using Maple2.Script.Npc;

/// <summary>
/// 11001932: Apprentice Tochi
/// </summary>
public class _11001932 : NpcScript {
    internal _11001932(INpcScriptContext context) : base(context) {
        Id = 30;
        // TODO: RandomPick 30
    }

    public override bool Next(int selection = 0) {
        switch (Id) {
            case 0:
                // $script:1122150407007455$ 
                // - Can I help you?
                return true;
            case 30:
                // $script:1122214707007475$ 
                // - Handicrafts are so fun that I often lose track of the time. I just wish I had someone to actually give this stuff to... 
                return true;
            default:
                return true;
        }
    }
}
