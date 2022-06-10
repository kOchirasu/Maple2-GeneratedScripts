using Maple2.Model.Enum;
using Maple2.Script.Npc;

/// <summary>
/// 11000614: Marr
/// </summary>
public class _11000614 : NpcScript {
    internal _11000614(INpcScriptContext context) : base(context) {
        Id = 20;
    }

    public override bool Next(int selection = 0) {
        switch (Id) {
            case 0:
                // $script:0831180407002511$ 
                // - What seems to be the problem? 
                return true;
            case 20:
                // $script:0831180407002513$ 
                // - I can't return to Maple World until I save these people. I'll never be able to forgive myself if I leave them behind. 
                return true;
            default:
                return true;
        }
    }
}
