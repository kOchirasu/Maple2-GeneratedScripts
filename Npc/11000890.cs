using Maple2.Model.Enum;
using Maple2.Script.Npc;

/// <summary>
/// 11000890: Ringling
/// </summary>
public class _11000890 : NpcScript {
    internal _11000890(INpcScriptContext context) : base(context) {
        Id = 20;
    }

    public override bool Next(int selection = 0) {
        switch (Id) {
            case 0:
                // $script:0831180407003254$ 
                // - What is it? What is it? What is it? There has to be a reason... 
                return true;
            case 20:
                // $script:0831180407003256$ 
                // - What brings you here? 
                return true;
            default:
                return true;
        }
    }
}
