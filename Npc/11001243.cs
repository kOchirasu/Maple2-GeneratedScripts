using Maple2.Model.Enum;
using Maple2.Script.Npc;

/// <summary>
/// 11001243: Ishura
/// </summary>
public class _11001243 : NpcScript {
    internal _11001243(INpcScriptContext context) : base(context) {
        Id = 30;
    }

    public override bool Next(int selection = 0) {
        switch (Id) {
            case 0:
                // $script:1203181207004683$ 
                // - What is it? 
                return true;
            case 30:
                // $script:1203181207004686$ 
                // - Now that the draft is in place, we'd better hurry back to the fortress. 
                return true;
            default:
                return true;
        }
    }
}
