using Maple2.Model.Enum;
using Maple2.Script.Npc;

/// <summary>
/// 11004091: Lucky Whale
/// </summary>
public class _11004091 : NpcScript {
    internal _11004091(INpcScriptContext context) : base(context) {
        Id = 10;
        // TODO: RandomPick 10
    }

    public override bool Next(int selection = 0) {
        switch (Id) {
            case 0:
                // $script:0622133907010325$ 
                // - <font color="#909090">(This mascot is the unofficial guardian of $map:02000377$.)</font>
                return true;
            case 10:
                // $script:0622133907010326$ 
                // - <font color="#909090">(This mascot is the unofficial guardian of $map:02000377$.)</font>
                // $script:0622133907010327$ 
                // - <font color="#909090">(The local fishermen consider this whale lucky. They say that you'll catch a huge fish if you kiss the whale's cheek before heading out.)</font>
                // $script:0622133907010328$ 
                // - <font color="#909090">(It's also lucky for the villagers. If you have a dream about this whale, buy a lottery ticket the next day and you'll surely win. At least, that's what they tell you.)</font>
                // $script:0622133907010329$ 
                // - <font color="#909090">(Some people assume that this whale's name is Coco, given the name of the island. However, the creator of the whale insists that it isn't true.)</font>
                return true;
            default:
                return true;
        }
    }
}
