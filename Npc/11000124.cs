using Maple2.Model.Enum;
using Maple2.Script.Npc;

/// <summary>
/// 11000124: Copen
/// </summary>
public class _11000124 : NpcScript {
    internal _11000124(INpcScriptContext context) : base(context) {
        Id = 30;
    }

    public override bool Next(int selection = 0) {
        switch (Id) {
            case 0:
                // $script:0831180407000534$ 
                // - What brings you here? 
                return true;
            case 30:
                // $script:0831180407000536$ 
                // - I didn't know this would happen. I thought I would be set once I created the new drug... Then they came after me... Ugh...  
                return true;
            default:
                return true;
        }
    }
}
