using Maple2.Model.Enum;
using Maple2.Script.Npc;

/// <summary>
/// 11001072: Brave Tree Spirit
/// </summary>
public class _11001072 : NpcScript {
    internal _11001072(INpcScriptContext context) : base(context) {
        Id = 30;
        // TODO: RandomPick 30
    }

    public override bool Next(int selection = 0) {
        switch (Id) {
            case 0:
                // $script:0831180407003655$ 
                // - Go away.
                return true;
            case 30:
                // $script:0831180407003658$ 
                // - You're from the outside world, aren't you? What are you going to change here this time?
                return true;
            default:
                return true;
        }
    }
}
