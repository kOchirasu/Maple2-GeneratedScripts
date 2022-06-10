using Maple2.Model.Enum;
using Maple2.Script.Npc;

/// <summary>
/// 11000685: Einos
/// </summary>
public class _11000685 : NpcScript {
    internal _11000685(INpcScriptContext context) : base(context) {
        Id = 10;
        // TODO: RandomPick 10
    }

    public override bool Next(int selection = 0) {
        switch (Id) {
            case 0:
                // $script:0831180407002778$ 
                // - How may I help you?
                return true;
            case 10:
                // $script:0831180407002779$ 
                // - $map:02000227$ is the border between the mortal and spirit realms.
                return true;
            default:
                return true;
        }
    }
}
