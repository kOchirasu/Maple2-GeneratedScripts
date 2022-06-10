using Maple2.Model.Enum;
using Maple2.Script.Npc;

/// <summary>
/// 11003824: Strange Claw Marks
/// </summary>
public class _11003824 : NpcScript {
    internal _11003824(INpcScriptContext context) : base(context) {
        Id = 10;
    }

    public override bool Next(int selection = 0) {
        switch (Id) {
            case 0:
                // $script:0116111107009757$ 
                // - <font color="#909090">(There's an odd grouping of large claw marks here.)</font>
                return true;
            case 10:
                // $script:0116111107009758$ 
                // - <font color="#909090">(There's an odd grouping of large claw marks here.)</font>
                // $script:0116111107009759$ 
                // - <font color="#909090">(This must have been left by a $npcName:11003781[gender:0]$.)</font>
                switch (selection) {
                    // $script:0116111107009760$
                    // - (Take a picture.)
                    case 0:
                        Id = 11;
                        return false;
                }
                return true;
            case 11:
                // $script:0116111107009761$ 
                // - <font color="#909090">(This might be a clue. You take a picture of the markings to show them to $npcName:11003536[gender:0]$.)</font>
                return true;
            default:
                return true;
        }
    }
}
