using Maple2.Model.Enum;
using Maple2.Script.Npc;

/// <summary>
/// 11001600: Char
/// </summary>
public class _11001600 : NpcScript {
    internal _11001600(INpcScriptContext context) : base(context) {
        Id = 10;
        // TODO: RandomPick 10
    }

    public override bool Next(int selection = 0) {
        switch (Id) {
            case 0:
                // $script:0504151707006088$ 
                // - What brings you here?
                return true;
            case 10:
                // $script:0515180307006137$ 
                // - Let's hear them out.
                return true;
            default:
                return true;
        }
    }
}
