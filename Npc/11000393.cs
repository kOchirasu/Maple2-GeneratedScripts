using Maple2.Model.Enum;
using Maple2.Script.Npc;

/// <summary>
/// 11000393: Buffett
/// </summary>
public class _11000393 : NpcScript {
    internal _11000393(INpcScriptContext context) : base(context) {
        Id = 40;
        // TODO: RandomPick 40
    }

    public override bool Next(int selection = 0) {
        switch (Id) {
            case 0:
                // $script:0831180407001596$ 
                // - What seems to be the problem?
                return true;
            case 40:
                // $script:0831180407001599$ 
                // - When my manager is angry, he screams at the top of his lungs and throws anything he can get his hands on. No one can stop him. All you can do is avoid him.
                return true;
            default:
                return true;
        }
    }
}
