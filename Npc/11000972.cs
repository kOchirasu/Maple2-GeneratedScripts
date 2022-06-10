using Maple2.Model.Enum;
using Maple2.Script.Npc;

/// <summary>
/// 11000972: Sisel
/// </summary>
public class _11000972 : NpcScript {
    internal _11000972(INpcScriptContext context) : base(context) {
        Id = 20;
    }

    public override bool Next(int selection = 0) {
        switch (Id) {
            case 0:
                // $script:0831180407003364$ 
                // - This situation is more serious than I thought, but I'm not going to back down now! 
                return true;
            case 20:
                // $script:0831180407003366$ 
                // - I'll do anything for the safety and peace of $map:02000076$. I'll fight as long as I can, for the honor of the Green Hoods. 
                return true;
            default:
                return true;
        }
    }
}
