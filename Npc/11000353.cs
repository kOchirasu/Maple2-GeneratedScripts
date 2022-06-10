using Maple2.Model.Enum;
using Maple2.Script.Npc;

/// <summary>
/// 11000353: Thompson
/// </summary>
public class _11000353 : NpcScript {
    internal _11000353(INpcScriptContext context) : base(context) {
        Id = 30;
        // TODO: RandomPick 30
    }

    public override bool Next(int selection = 0) {
        switch (Id) {
            case 0:
                // $script:0831180407001467$ 
                // - How may I help you?
                return true;
            case 30:
                // $script:0831180407001470$ 
                // - Our fuel needs are growing by the day. I think more excavation sites will be needed soon.
                // $script:0831180407001471$ 
                // - We're pumping oil every day. It's still kind of surprising how much we need to get by.
                return true;
            default:
                return true;
        }
    }
}
