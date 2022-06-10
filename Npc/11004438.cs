using Maple2.Model.Enum;
using Maple2.Script.Npc;

/// <summary>
/// 11004438: Mason
/// </summary>
public class _11004438 : NpcScript {
    internal _11004438(INpcScriptContext context) : base(context) {
        Id = 10;
        // TODO: RandomPick 10
    }

    public override bool Next(int selection = 0) {
        switch (Id) {
            case 0:
                // $script:1213154907011980$ 
                // - It is time my order stood with the rest of the empire.
                return true;
            case 10:
                // $script:1213154907011981$ 
                // - So many fantastic riddles await us in Kritias... It's exhilarating.
                return true;
            default:
                return true;
        }
    }
}
