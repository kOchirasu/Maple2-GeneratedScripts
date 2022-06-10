using Maple2.Model.Enum;
using Maple2.Script.Npc;

/// <summary>
/// 11004262: Small Pond
/// </summary>
public class _11004262 : NpcScript {
    internal _11004262(INpcScriptContext context) : base(context) {
        Id = 10;
        // TODO: RandomPick 10
    }

    public override bool Next(int selection = 0) {
        switch (Id) {
            case 0:
                // $script:0911203207011177$ 
                // - <font color="#909090">(This pleasant little pond holds a prominent position in $npcName:11001350[gender:0]$'s estate.)</font>
                return true;
            case 10:
                // $script:0911203207011178$ 
                // - <font color="#909090">(This pleasant little pond holds a prominent position in $npcName:11001350[gender:0]$'s estate.)</font>
                // $script:0911203207011179$ 
                // - <font color="#909090">(The fish look like golden bladefish, a species unique to the island.)</font>
                // $script:0911203207011180$ 
                // - <font color="#909090">(Their scales shimmer beautifully in the sunlight. The interplay of light brings a sense of peace to your mind...)</font>
                // $script:0911203207011181$ 
                // - <font color="#909090">(Maybe it's time you got some fish of your own.)</font>
                return true;
            default:
                return true;
        }
    }
}
