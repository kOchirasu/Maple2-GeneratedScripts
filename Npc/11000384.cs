using Maple2.Model.Enum;
using Maple2.Script.Npc;

/// <summary>
/// 11000384: Johnny
/// </summary>
public class _11000384 : NpcScript {
    internal _11000384(INpcScriptContext context) : base(context) {
        Id = 20;
        // TODO: RandomPick 20
    }

    public override bool Next(int selection = 0) {
        switch (Id) {
            case 0:
                // $script:0831180407001565$ 
                // - Aw, it hurts... 
                return true;
            case 20:
                // $script:0831180407001567$ 
                // - S-stop talking to me... Ughhh... 
                return true;
            default:
                return true;
        }
    }
}
