using Maple2.Model.Enum;
using Maple2.Script.Npc;

/// <summary>
/// 11004201: Tourist
/// </summary>
public class _11004201 : NpcScript {
    internal _11004201(INpcScriptContext context) : base(context) {
        Id = 10;
    }

    public override bool Next(int selection = 0) {
        switch (Id) {
            case 0:
                // $script:0806025707010650$ 
                // - Hello.
                return true;
            case 10:
                // $script:0806025707010651$ 
                // - Out of the way, buddy, you're in my shot.
                return true;
            default:
                return true;
        }
    }
}
