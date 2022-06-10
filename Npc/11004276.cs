using Maple2.Model.Enum;
using Maple2.Script.Npc;

/// <summary>
/// 11004276: Karkar Snake Statue
/// </summary>
public class _11004276 : NpcScript {
    internal _11004276(INpcScriptContext context) : base(context) {
        Id = 10;
        // TODO: RandomPick 10
    }

    public override bool Next(int selection = 0) {
        switch (Id) {
            case 0:
                // $script:0911203207011271$ 
                // - <font color="#909090">(Snake statues like this one can be found all over Karkar.)</font>
                return true;
            case 10:
                // $script:0911203207011272$ 
                // - <font color="#909090">(Snake statues like this one can be found all over Karkar.)</font>
                // $script:0911203207011273$ 
                // - <font color="#909090">(You've noticed that these seem to be placed wherever poisonous snakes can be found. Perhaps they're a warning for the locals?)</font>
                // $script:0911203207011274$ 
                // - <font color="#909090">(Then again, these statues look pretty old. Wouldn't the snake habitats have moved over time? Better be careful, just in case.)</font>
                return true;
            default:
                return true;
        }
    }
}
