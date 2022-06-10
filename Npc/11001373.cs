using Maple2.Model.Enum;
using Maple2.Script.Npc;

/// <summary>
/// 11001373: Sharmobi
/// </summary>
public class _11001373 : NpcScript {
    internal _11001373(INpcScriptContext context) : base(context) {
        Id = 30;
        // TODO: RandomPick 30
    }

    public override bool Next(int selection = 0) {
        switch (Id) {
            case 0:
                // $script:1217144507005348$ 
                // - Wah! You startled me!
                return true;
            case 30:
                // $script:1217144507005351$ 
                // - Sigh... I haven't been back home since I moved to Minar with my husband. I was so looking forward to this trip, and now the train has broken down...
                return true;
            default:
                return true;
        }
    }
}
