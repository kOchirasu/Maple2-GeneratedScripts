using Maple2.Model.Enum;
using Maple2.Script.Npc;

/// <summary>
/// 11004082: Frightened Shut-In
/// </summary>
public class _11004082 : NpcScript {
    internal _11004082(INpcScriptContext context) : base(context) {
        Id = 10;
        // TODO: RandomPick 10
    }

    public override bool Next(int selection = 0) {
        switch (Id) {
            case 0:
                // $script:0622133907010273$ 
                // - Sigh... Will I ever get to leave this house again?
                return true;
            case 10:
                // $script:0622133907010274$ 
                // - Sigh... Will I ever get to leave this house again?
                return true;
            default:
                return true;
        }
    }
}
