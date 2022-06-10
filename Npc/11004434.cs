using Maple2.Model.Enum;
using Maple2.Script.Npc;

/// <summary>
/// 11004434: Veliche
/// </summary>
public class _11004434 : NpcScript {
    internal _11004434(INpcScriptContext context) : base(context) {
        Id = 10;
        // TODO: RandomPick 10
    }

    public override bool Next(int selection = 0) {
        switch (Id) {
            case 0:
                // $script:1213154907011972$ 
                // - The future is in our hands.
                return true;
            case 10:
                // $script:1213154907011973$ 
                // - Stay alert. We're in uncharted territory.
                return true;
            default:
                return true;
        }
    }
}
