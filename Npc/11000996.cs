using Maple2.Model.Enum;
using Maple2.Script.Npc;

/// <summary>
/// 11000996: Yodano
/// </summary>
public class _11000996 : NpcScript {
    internal _11000996(INpcScriptContext context) : base(context) {
        Id = 30;
    }

    public override bool Next(int selection = 0) {
        switch (Id) {
            case 0:
                // $script:0831180407003421$ 
                // - Speak up. I can't hear you over the alarm. Cluck!
                return true;
            case 30:
                // $script:0831180407003424$ 
                // - Someone, please turn off that alarm clock. Cluck!
                return true;
            default:
                return true;
        }
    }
}
