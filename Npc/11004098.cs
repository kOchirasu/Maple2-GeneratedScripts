using Maple2.Model.Enum;
using Maple2.Script.Npc;

/// <summary>
/// 11004098: Chocolate Waffle Waterfall
/// </summary>
public class _11004098 : NpcScript {
    internal _11004098(INpcScriptContext context) : base(context) {
        Id = 10;
        // TODO: RandomPick 10
    }

    public override bool Next(int selection = 0) {
        switch (Id) {
            case 0:
                // $script:0623132607010349$ 
                // - <font color="#909090">(This chocolate waterfall puts off an overwhelmingly sweet aroma.)</font>
                return true;
            case 10:
                // $script:0623132607010350$ 
                // - <font color="#909090">(This chocolate waterfall puts off an overwhelmingly sweet aroma.)</font>
                // $script:0623132507010346$ 
                // - <font color="#909090">(The rich chocolate of this waterfall is enough to drive some children sugar-crazy.)</font>
                // $script:0623132507010347$ 
                // - <font color="#909090">(The chocolate found in $map:02000257$ is favored by dessert chefs everywhere. Some say it's even Empress $npcName:11001969[gender:1]$'s favorite chocolate.)</font>
                // $script:0623132507010348$ 
                // - <font color="#909090">(In fact, rumor has it the empire's vaults are full of the stuff...)</font>
                return true;
            default:
                return true;
        }
    }
}
