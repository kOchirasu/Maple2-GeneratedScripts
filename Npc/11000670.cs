using Maple2.Model.Enum;
using Maple2.Script.Npc;

/// <summary>
/// 11000670: Misplaced Book
/// </summary>
public class _11000670 : NpcScript {
    internal _11000670(INpcScriptContext context) : base(context) {
        // TODO: RandomPick 10;20;30
    }

    public override bool Next(int selection = 0) {
        switch (Id) {
            case 0:
                // $script:0831180407002728$ 
                // - <font color="#909090">(One of these books seems out of place.)</font> 
                return true;
            case 10:
                // $script:0831180407002729$ 
                // - No, no! I don't want to go back in there! 
                return true;
            case 20:
                // $script:0831180407002730$ 
                // - Hey! Did you just throw me on the ground?  
                switch (selection) {
                    // $script:0831180407002731$
                    // - How did you end up on the bookshelf?
                    case 0:
                        Id = 0; // TODO: 21 | 22
                        return false;
                }
                return true;
            case 21:
                // $script:0831180407002732$ functionID=1 
                // - A stupid monster brought me back here. Please, you've got to take me with you! 
                return true;
            case 22:
                // $script:0831180407002733$ 
                // - Your bag is full! Make some room for me, will ya? 
                return true;
            case 30:
                // $script:0831180407002734$ 
                // - <font color="#909090">(You always remember to put books back where you found them... right?)</font> 
                return true;
            default:
                return true;
        }
    }
}
