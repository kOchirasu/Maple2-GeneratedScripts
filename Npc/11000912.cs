using Maple2.Model.Enum;
using Maple2.Script.Npc;

/// <summary>
/// 11000912: Shabik
/// </summary>
public class _11000912 : NpcScript {
    internal _11000912(INpcScriptContext context) : base(context) {
        Id = 20;
    }

    public override bool Next(int selection = 0) {
        switch (Id) {
            case 0:
                // $script:0831180407003278$ 
                // - What's wrong?
                return true;
            case 20:
                // $script:0831180407003280$ 
                // - Justice always prevails!
                return true;
            default:
                return true;
        }
    }
}
