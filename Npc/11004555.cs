using Maple2.Model.Enum;
using Maple2.Script.Npc;

/// <summary>
/// 11004555: Tristan
/// </summary>
public class _11004555 : NpcScript {
    internal _11004555(INpcScriptContext context) : base(context) {
        Id = 10;
    }

    public override bool Next(int selection = 0) {
        switch (Id) {
            case 0:
                // $script:0123111007012734$ 
                // - Anything might happen now...
                return true;
            case 10:
                // $script:0123111007012735$ 
                // - Anything might happen now...
                return true;
            default:
                return true;
        }
    }
}
