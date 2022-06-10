using Maple2.Model.Enum;
using Maple2.Script.Npc;

/// <summary>
/// 11000490: Soran
/// </summary>
public class _11000490 : NpcScript {
    internal _11000490(INpcScriptContext context) : base(context) {
        Id = 30;
        // TODO: RandomPick 30
    }

    public override bool Next(int selection = 0) {
        switch (Id) {
            case 0:
                // $script:0831180407002146$ 
                // - What is it?
                return true;
            case 30:
                // $script:0831180407002149$ 
                // - Eww, you're ugly! Get out of the way!
                return true;
            default:
                return true;
        }
    }
}
