using Maple2.Model.Enum;
using Maple2.Script.Npc;

/// <summary>
/// 11003958: Assassin
/// </summary>
public class _11003958 : NpcScript {
    internal _11003958(INpcScriptContext context) : base(context) {
        Id = 20;
        // TODO: RandomPick 20
    }

    public override bool Next(int selection = 0) {
        switch (Id) {
            case 0:
                // $script:0614143707010007$ 
                // - ...What business do you have with me?
                return true;
            case 20:
                // $script:0614143707010008$ 
                // - ...You seem strong.
                return true;
            default:
                return true;
        }
    }
}
