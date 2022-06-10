using Maple2.Model.Enum;
using Maple2.Script.Npc;

/// <summary>
/// 11000548: Leala
/// </summary>
public class _11000548 : NpcScript {
    internal _11000548(INpcScriptContext context) : base(context) {
        Id = 30;
    }

    public override bool Next(int selection = 0) {
        switch (Id) {
            case 0:
                // $script:0831180407002324$ 
                // - What seems to be the problem?
                return true;
            case 30:
                // $script:0831180407002327$ 
                // - The militia will do everything we can to help you. We have to join forces to protect our world.
                return true;
            default:
                return true;
        }
    }
}
