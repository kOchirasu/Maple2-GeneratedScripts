using Maple2.Model.Enum;
using Maple2.Script.Npc;

/// <summary>
/// 11004290: Plutino
/// </summary>
public class _11004290 : NpcScript {
    internal _11004290(INpcScriptContext context) : base(context) {
        Id = 10;
        // TODO: RandomPick 10
    }

    public override bool Next(int selection = 0) {
        switch (Id) {
            case 0:
                // $script:0921211107011342$ 
                // - Hello. How can I help you?
                return true;
            case 10:
                // $script:0921211107011343$ 
                // - Welcome to our fine hotel.
                return true;
            default:
                return true;
        }
    }
}
