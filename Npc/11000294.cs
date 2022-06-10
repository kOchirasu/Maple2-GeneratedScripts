using Maple2.Model.Enum;
using Maple2.Script.Npc;

/// <summary>
/// 11000294: Papa Frog
/// </summary>
public class _11000294 : NpcScript {
    internal _11000294(INpcScriptContext context) : base(context) {
        Id = 50;
    }

    public override bool Next(int selection = 0) {
        switch (Id) {
            case 0:
                // $script:0831180407001171$ 
                // - May I help you? 
                return true;
            case 50:
                // $script:0831180407001175$ 
                // - Croak, croak, croak. Croaaaaakkk... 
                return true;
            default:
                return true;
        }
    }
}
